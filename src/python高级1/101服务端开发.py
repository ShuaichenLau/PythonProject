import datetime
import socket
import threading

import wx

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8888
CLOSE_SIGNAL = "__SERVER_CLOSED__"  # 服务器关闭的特殊协议标记


class ServerFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, '老肖的服务器界面', size=(450, 580))
        self.InitUI()

        # 服务端网络相关变量
        self.server_socket = None
        self.is_running = False
        # 客户端连接列表：存储字典 [{'socket': client_sock, 'name': client_name}, ...]
        self.clients = []
        self.lock = threading.Lock()  # 线程锁，防止并发修改 clients

    def InitUI(self):
        panel = wx.Panel(self)

        # 顶部按钮
        self.btn_start = wx.Button(panel, label='启动')
        self.btn_save = wx.Button(panel, label='聊天记录保存')
        self.btn_stop = wx.Button(panel, label='停止')

        self.btn_save.Disable()
        self.btn_stop.Disable()

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        top_sizer.Add(self.btn_start, 1, wx.EXPAND | wx.ALL, 2)
        top_sizer.Add(self.btn_save, 2, wx.EXPAND | wx.ALL, 2)
        top_sizer.Add(self.btn_stop, 1, wx.EXPAND | wx.ALL, 2)

        # 聊天记录显示区域（多行只读）
        self.text_chat = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(top_sizer, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.text_chat, 1, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(main_sizer)

        # 绑定事件
        self.btn_start.Bind(wx.EVT_BUTTON, self.OnStart)
        self.btn_save.Bind(wx.EVT_BUTTON, self.OnSave)
        self.btn_stop.Bind(wx.EVT_BUTTON, self.OnStop)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def AppendMsg(self, msg):
        """向聊天记录文本框追加消息（线程安全）"""
        wx.CallAfter(self.text_chat.AppendText, msg + "\n--------------------------------\n")

    def Broadcast(self, message):
        """向所有在线客户端广播消息"""
        self.AppendMsg(message)  # 服务器自身记录
        with self.lock:
            for client in self.clients[:]:
                try:
                    client['socket'].sendall(message.encode('utf-8'))
                except Exception:
                    self.clients.remove(client)

    def OnStart(self, event):
        """点击【启动】：开启 Socket 服务"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((SERVER_HOST, SERVER_PORT))
            self.server_socket.listen(50)
            self.is_running = True

            # 开启子线程监听客户端连接（防止阻塞 UI 界面）
            t = threading.Thread(target=self.AcceptClients, daemon=True)
            t.start()

            self.btn_start.Disable()
            self.btn_save.Enable()
            self.btn_stop.Enable()

            self.AppendMsg(f"服务器通知: 聊天室服务已启动 [{SERVER_HOST}:{SERVER_PORT}]")
        except Exception as e:
            wx.MessageBox(f"启动失败: {e}", "错误", wx.OK | wx.ICON_ERROR)

    def AcceptClients(self):
        """循环接收客户端连接"""
        while self.is_running:
            try:
                client_sock, addr = self.server_socket.accept()
                # 客户端连入后，第一条消息必须是其“用户姓名”
                client_name = client_sock.recv(1024).decode('utf-8').strip()
                if not client_name:
                    client_sock.close()
                    continue

                client_info = {'socket': client_sock, 'name': client_name}
                with self.lock:
                    self.clients.append(client_info)

                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                join_msg = f"服务器通知: 欢迎{client_name}进入聊天室!\n时间: {now_time}"
                self.Broadcast(join_msg)

                # 为该客户端开启独立线程监听其发送的消息
                t = threading.Thread(target=self.HandleClientMsg, args=(client_info,), daemon=True)
                t.start()
            except Exception:
                break

    def HandleClientMsg(self, client_info):
        """接收单个客户端消息的子线程"""
        client_sock = client_info['socket']
        client_name = client_info['name']

        while self.is_running:
            try:
                data = client_sock.recv(4096)
                if not data:
                    break  # 客户端断开连接

                msg = data.decode('utf-8').strip()
                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if msg == "__LEAVE__":  # 客户端点击“离开”发出的协议指令
                    break
                else:
                    # 普通聊天消息广播
                    chat_msg = f"{client_name} : {msg}\n\n时间: {now_time}"
                    self.Broadcast(chat_msg)
            except Exception:
                break

        # 客户端离开/断开处理
        with self.lock:
            if client_info in self.clients:
                self.clients.remove(client_info)
        try:
            client_sock.close()
        except:
            pass

        if self.is_running:
            now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            leave_msg = f"服务器通知: {client_name}离开聊天室!\n时间: {now_time}"
            self.Broadcast(leave_msg)

    def OnSave(self, event):
        """点击【聊天记录保存】：将文本保存到本地文件"""
        content = self.text_chat.GetValue()
        if not content.strip():
            wx.MessageBox("暂无聊天记录可保存", "提示", wx.OK | wx.ICON_INFORMATION)
            return

        file_path = f"chat_record_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        wx.MessageBox(f"聊天记录已成功保存到: {file_path}", "保存成功", wx.OK | wx.ICON_INFORMATION)

    def OnStop(self, event):
        """
        点击【停止】：
        1. 广播服务即将关闭通知
        2. 发送特定标记 CLOSE_SIGNAL 让客户端安全断开
        3. 关闭所有连接并关闭服务器窗口
        """
        self.is_running = False
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        stop_notice = f"服务器通知: 服务器已停止服务，聊天室关闭!\n时间: {now_time}"

        # 1. 广播通知 & 发送关闭标记
        with self.lock:
            for client in self.clients:
                try:
                    # 先发通知内容
                    client['socket'].sendall(stop_notice.encode('utf-8'))
                    # 紧接着发送服务关闭确认标识
                    client['socket'].sendall(CLOSE_SIGNAL.encode('utf-8'))
                    client['socket'].close()
                except:
                    pass
            self.clients.clear()

        # 2. 关闭服务端主监听 Socket
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass

        # 3. 销毁并关闭服务器窗口
        self.Destroy()

    def OnCloseWindow(self, event):
        if self.is_running:
            self.OnStop(None)
        else:
            self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = ServerFrame()
    frame.Center()
    frame.Show()
    app.MainLoop()