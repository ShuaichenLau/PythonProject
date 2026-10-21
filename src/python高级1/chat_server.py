"""聊天室服务端核心逻辑（纯网络层，不依赖 wxPython）

职责划分
--------
* ChatServer 只负责：监听端口、管理客户端列表、转发消息。
* 要显示在服务器界面上的内容，通过 on_log 回调交给界面层，
  界面层再用 wx.CallAfter 切回主线程去改控件。

线程模型
--------
    1 个 accept 线程      : 循环接收新连接
    每个客户端 1 个线程    : 循环读取该客户端发来的消息
    共享的 _clients 列表   : 用 _lock 保护

用法
----
    server = ChatServer(on_log=print)
    server.start()     # 端口被占用等情况会抛 OSError
    ...
    server.stop()      # 通知所有客户端并断开连接
"""

import socket
import threading
from dataclasses import dataclass

import chat_protocol as proto


@dataclass
class ClientSession:
    """一个已登记（发过昵称）的客户端连接"""
    name: str
    sock: socket.socket
    address: tuple


class ChatServer:
    def __init__(self, host=proto.DEFAULT_HOST, port=proto.DEFAULT_PORT, on_log=None):
        self.host = host
        self.port = port
        self._on_log = on_log if on_log else (lambda text: None)

        self._server_socket = None
        self._clients = []                  # [ClientSession, ...]
        self._lock = threading.Lock()       # 保护 _clients
        self._running = False

    # ================================================== 供界面层调用
    @property
    def running(self):
        return self._running

    @property
    def client_count(self):
        with self._lock:
            return len(self._clients)

    def start(self):
        """开始监听；失败（如端口被占用）会抛 OSError，由界面层提示用户"""
        if self._running:
            return

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            server_socket.bind((self.host, self.port))
            server_socket.listen(50)
        except OSError:
            proto.close_quietly(server_socket)
            raise

        self._server_socket = server_socket
        self._running = True
        threading.Thread(
            target=self._accept_loop, name='chat-accept', daemon=True
        ).start()

        self._log(f'服务器通知: 聊天室服务已启动 [{self.host}:{self.port}]')

    def stop(self, notice='服务器通知: 服务器已停止服务，聊天室关闭！'):
        """广播关闭通知 -> 断开所有客户端 -> 关闭监听端口。可重复调用"""
        if not self._running:
            return

        self._running = False           # 先停标志位，让各子线程不再接新消息
        if notice:
            self._broadcast(notice, closing=True)
        if self._server_socket:
            proto.close_quietly(self._server_socket)
            self._server_socket = None

    # ================================================== 网络层内部实现
    def _log(self, text):
        """把一条记录交给界面回调（调用方可能来自子线程）"""
        self._on_log(text)

    def _broadcast(self, text, closing=False):
        """给所有在线客户端推送一条通知，同时记录到服务器界面。

        closing=True 时，先发通知，再补一条 CLOSED，然后关闭写方向，
        让客户端能读完内容后自行断开。
        """
        line = f'[{proto.now_str()}] {text}'
        self._log(line)

        with self._lock:
            sessions = list(self._clients)
            if closing:
                self._clients.clear()       # 列表已清空，后续线程只做收尾

        for session in sessions:
            self._send(session, proto.make_message(proto.NOTICE, text=line))
            if closing:
                self._send(session, proto.make_message(proto.CLOSED))
                proto.shutdown_write(session.sock)

    @staticmethod
    def _send(session, message):
        """给单个客户端发消息；发不出去就忽略（对应线程会负责清理）"""
        try:
            proto.send_message(session.sock, message)
        except OSError:
            pass

    def _accept_loop(self):
        """accept 线程：循环接收新连接，每个连接再开一个子线程服务它"""
        while self._running:
            try:
                client_socket, address = self._server_socket.accept()
            except OSError:
                break                       # 监听 socket 已关闭
            threading.Thread(
                target=self._serve_client,
                args=(client_socket, address),
                name=f'chat-client-{address[1]}',
                daemon=True,
            ).start()

    def _serve_client(self, client_socket, address):
        """单个客户端的完整生命周期：登记昵称 -> 循环收消息 -> 清理"""
        reader = proto.MessageReader(client_socket)
        session = self._register(client_socket, address, reader)
        if session is None:
            proto.close_quietly(client_socket)
            return

        try:
            self._broadcast(f'服务器通知: 欢迎 {session.name} 进入聊天室!')
            self._receive_from_client(session, reader)
        finally:
            self._unregister(session)
            if self._running:           # 服务器整体关闭时不必再广播离开
                self._broadcast(f'服务器通知: {session.name} 离开聊天室!')

    def _register(self, client_socket, address, reader):
        """客户端连入后的第一条消息必须是 JOIN（带昵称），否则断开"""
        first = reader.recv()
        if not first or first.get('type') != proto.JOIN:
            self._log('服务器通知: 有客户端未按协议登记昵称，已断开')
            return None

        name = str(first.get('name', '')).strip() or f'游客{address[1]}'
        session = ClientSession(name=name, sock=client_socket, address=address)
        with self._lock:
            self._clients.append(session)
        return session

    def _unregister(self, session):
        """从在线列表移除并关闭 socket"""
        with self._lock:
            if session in self._clients:
                self._clients.remove(session)
        proto.close_quietly(session.sock)

    def _receive_from_client(self, session, reader):
        """读取该客户端发来的消息，直到它离开或断开"""
        while self._running:
            message = reader.recv()
            if message is None:             # 客户端断开连接
                return

            message_type = message.get('type')
            if message_type == proto.LEAVE:  # 客户端点了「离开」
                return
            if message_type == proto.CHAT:
                text = str(message.get('text', '')).strip()
                if text:
                    self._broadcast(f'{session.name}: {text}')
