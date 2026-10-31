"""聊天室通信协议（服务端与客户端共用，不依赖 wxPython）

为什么需要这个模块
------------------
TCP 是「字节流」而不是「消息流」：如果直接 sendall("张三")、sendall("你好")，
接收方一次 recv 可能只拿到 "张"，也可能把两条拼在一起变成 "张三你好"。
所以这里补一层「分帧」：

    每条消息 = 一行 JSON + b'\\n' 结尾

* JSON 会把文本里的换行转义成 \\n 这两个字符，所以多行聊天内容也不会破坏分帧；
* 接收方按 \\n 切开，就一定能一条一条拿到完整的消息。

消息格式
--------
    {"type": "chat", "text": "你好"}

各种 type 的含义见下方常量说明。
"""

import datetime
import json
import socket

# ---------------------------------------------------------------- 连接参数
DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8888
ENCODING = 'utf-8'
BUFFER_SIZE = 4096

# ---------------------------------------------------------------- 消息类型
# 客户端 -> 服务端
JOIN = 'join'         # 加入聊天室，字段 name  ：昵称
CHAT = 'chat'         # 发送聊天内容，字段 text：聊天文本
LEAVE = 'leave'       # 主动离开聊天室
# 服务端 -> 客户端
NOTICE = 'notice'     # 服务器通知（欢迎/离开/聊天转发），字段 text：要显示的文本
CLOSED = 'closed'     # 服务器即将关闭，客户端收到后应断开连接


def make_message(message_type, **fields):
    """构造一条消息字典，例如 make_message(CHAT, text='你好')"""
    return {'type': message_type, **fields}


def encode_message(message):
    """把消息字典编码成可以直接 sendall 的字节串（末尾带换行）"""
    return (json.dumps(message, ensure_ascii=False) + '\n').encode(ENCODING)


def send_message(sock, message):
    """发送一条消息，失败时抛出 OSError（由调用方决定如何处理）"""
    sock.sendall(encode_message(message))


class MessageReader:
    """从 socket 里按「一条一条消息」读取的读取器。

    用法（只在一个接收线程里循环调用，不保证线程安全）：

        reader = MessageReader(sock)
        while True:
            message = reader.recv()
            if message is None:      # 对端已关闭连接
                break
            print(message['type'])
    """

    def __init__(self, sock):
        self._sock = sock
        self._buffer = b''          # 还没凑够一整行的残留字节

    def recv(self):
        """阻塞读取下一条消息：返回 dict；连接断开时返回 None"""
        while True:
            line = self._read_line()
            if line is None:
                return None
            if not line:
                continue            # 忽略空行
            try:
                message = json.loads(line)
            except json.JSONDecodeError:
                continue            # 忽略坏数据，不因为一行非法内容断开连接
            if isinstance(message, dict) and 'type' in message:
                return message

    def _read_line(self):
        """从缓冲区 / socket 里取出下一行文本；连接断开返回 None"""
        while b'\n' not in self._buffer:
            try:
                chunk = self._sock.recv(BUFFER_SIZE)
            except OSError:
                return None         # socket 已关闭 / 连接被重置
            if not chunk:           # 对端正常关闭
                return None
            self._buffer += chunk
        line, _, self._buffer = self._buffer.partition(b'\n')
        return line.decode(ENCODING, errors='replace').strip()


def now_str():
    """当前时间的显示文本，服务端日志与客户端界面共用同一种格式"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def close_quietly(sock):
    """关闭 socket，忽略关闭过程中的任何异常"""
    if sock is None:
        return
    try:
        sock.close()
    except OSError:
        pass


def shutdown_write(sock):
    """只关闭「写方向」：已发出的数据仍能送达对方，对方会读到 EOF"""
    try:
        sock.shutdown(socket.SHUT_WR)
    except OSError:
        pass
