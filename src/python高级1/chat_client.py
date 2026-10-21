"""聊天室客户端核心逻辑（纯网络层，不依赖 wxPython）

界面层只需要关心三个回调：
    on_message(text)    服务器推来一条内容，需要显示
    on_disconnected()   连接已断开（服务器关闭 / 网络异常 / 自己点了离开）
    on_error(text)      可选：需要提示给用户的错误

用法
----
    client = ChatClient('张三', on_message=print)
    client.connect()              # 连不上会抛 OSError
    client.send_chat('你好')       # 返回是否发送成功
    client.disconnect()           # 离开聊天室
"""

import socket
import threading

import chat_protocol as proto


class ChatClient:
    def __init__(self, username, host=proto.DEFAULT_HOST, port=proto.DEFAULT_PORT,
                 on_message=None, on_disconnected=None, on_error=None):
        self.username = username
        self.host = host
        self.port = port

        self._on_message = on_message if on_message else (lambda text: None)
        self._on_disconnected = on_disconnected if on_disconnected else (lambda: None)
        self._on_error = on_error if on_error else (lambda text: None)

        self._socket = None
        self._running = False
        self._disconnect_reported = False   # 保证 on_disconnected 只回调一次

    # ================================================== 供界面层调用
    @property
    def connected(self):
        return self._running and self._socket is not None

    def connect(self):
        """连接服务器并登记昵称；失败会抛 OSError，由界面层弹窗提示"""
        if self.connected:
            return

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.host, self.port))
            # 第一条消息登记昵称，服务端据此识别
            proto.send_message(sock, proto.make_message(proto.JOIN, name=self.username))
        except OSError:
            proto.close_quietly(sock)
            raise

        self._socket = sock
        self._running = True
        self._disconnect_reported = False
        threading.Thread(
            target=self._receive_loop, args=(sock,), name='chat-receive', daemon=True
        ).start()

    def send_chat(self, text):
        """发送一条聊天消息；返回是否发送成功"""
        if not self.connected:
            return False
        try:
            proto.send_message(self._socket, proto.make_message(proto.CHAT, text=text))
            return True
        except OSError as exc:
            self._on_error(f'消息发送失败: {exc}')
            self._running = False
            proto.close_quietly(self._socket)
            self._socket = None
            self._report_disconnected()
            return False

    def disconnect(self, notify_server=True):
        """主动离开聊天室（点「离开」或关闭窗口时调用），可重复调用"""
        sock = self._socket
        if sock is not None and notify_server and self._running:
            try:
                proto.send_message(sock, proto.make_message(proto.LEAVE))
            except OSError:
                pass

        self._running = False
        self._socket = None
        proto.close_quietly(sock)
        self._report_disconnected()

    # ================================================== 接收线程
    def _receive_loop(self, sock):
        """后台持续接收服务器推送的通知，直到断开"""
        reader = proto.MessageReader(sock)
        while self._running:
            message = reader.recv()
            if message is None:             # 服务器关闭了连接
                break

            message_type = message.get('type')
            if message_type == proto.NOTICE:
                self._on_message(str(message.get('text', '')))
            elif message_type == proto.CLOSED:
                break                       # 服务器要关闭，直接断开

        self._running = False
        if self._socket is sock:            # 避免和 disconnect() 重复关闭
            self._socket = None
        proto.close_quietly(sock)
        self._report_disconnected()

    def _report_disconnected(self):
        """统一通知界面：连接已断开（只通知一次）"""
        if self._disconnect_reported:
            return
        self._disconnect_reported = True
        self._on_disconnected()
