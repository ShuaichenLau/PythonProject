import socket
import threading

import wx

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8888
CLOSE_SIGNAL = "__SERVER_CLOSED__"


class ClientFrame(wx.Frame):
    def __init__(self, username):
        super().__init__(None, wx.ID_ANY, f'{username}的客户端界面', size=(450, 580))
        self.username = username
        self.client_socket = None
        self.is_connected = False
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        # 1. 顶部操作区
        self.btn_conn = wx.Button(panel, label='连接')
        self.btn_leave = wx.Button(panel, label='离开')
        self.btn_leave.Disable()

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        top_sizer.Add(self.btn_conn, 1, wx.EXPAND | wx.ALL, 2)
        top_sizer.Add(self.btn_leave, 1, wx.EXPAND | wx.ALL, 2)

        # 2. 聊天记录展示区（只读多行）
        self.text_chat = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)

        # 3. 消息输入区（多行）
        self.text_input = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        # 4. 底部发送与重置
        self.btn_reset = wx.Button(panel, label='重置')
        self.btn_send = wx.Button(panel, label='发送')
        self.btn_send.Disable()

        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        bottom_sizer.Add(self.btn_reset, 1, wx.EXPAND | wx.ALL, 2)
        bottom_sizer.Add(self.btn_send, 1, wx.EXPAND | wx.ALL, 2)

        # 整体主布局
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(top_sizer, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.text_chat, 3, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.text_input, 1, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(bottom_sizer, 0, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(main_sizer)

        # 绑定按钮事件
        self.btn_conn.Bind(wx.EVT_BUTTON, self.OnConnect)
        self.btn_leave.Bind(wx.EVT_BUTTON, self.OnLeave)
        self.btn_reset.Bind(wx.EVT_BUTTON, self.OnReset)
        self.btn_send.Bind(wx.EVT_BUTTON, self.OnSend)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def AppendMsg(self, msg):
        """向聊天记录框追加消息"""
        wx.CallAfter(self.text_chat.AppendText, msg + "\n--------------------------------\n")

    def OnConnect(self, event):
        """点击【连接】进入聊天室"""
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((SERVER_HOST, SERVER_PORT))

            # 第一时间把用户名发送给服务器注册
            self.client_socket.sendall(self.username.encode('utf-8'))
            self.is_connected = True

            # 按钮状态切换
            self.btn_conn.Disable()
            self.btn_leave.Enable()
            self.btn_send.Enable()

            # 开启子线程监听接收服务端推送的消息（防止阻塞界面）
            t = threading.Thread(target=self.ReceiveMsg, daemon=True)
            t.start()
        except Exception as e:
            wx.MessageBox(f"无法连接到服务器: {e}", "连接失败", wx.OK | wx.ICON_ERROR)

    def ReceiveMsg(self):
        """后台持续接收服务器广播的消息"""
        while self.is_connected:
            try:
                data = self.client_socket.recv(4096)
                if not data:
                    break

                raw_text = data.decode('utf-8')

                # 检查是否包含服务器强制关闭信号
                if CLOSE_SIGNAL in raw_text:
                    clean_msg = raw_text.replace(CLOSE_SIGNAL, "").strip()
                    if clean_msg:
                        self.AppendMsg(clean_msg)
                    # 断开连接但【不关闭客户端窗口】
                    self.HandleDisconnection()
                    break
                else:
                    self.AppendMsg(raw_text)
            except Exception:
                break

        self.HandleDisconnection()

    def HandleDisconnection(self):
        """处理断开连接后的控件状态还原（在主线程安全运行）"""
        self.is_connected = False
        try:
            if self.client_socket:
                self.client_socket.close()
        except:
            pass

        def update_ui():
            self.btn_conn.Enable()
            self.btn_leave.Disable()
            self.btn_send.Disable()

        wx.CallAfter(update_ui)

    def OnSend(self, event):
        """点击【发送】发送消息"""
        msg = self.text_input.GetValue().strip()
        if not msg:
            return

        if self.is_connected and self.client_socket:
            try:
                self.client_socket.sendall(msg.encode('utf-8'))
                self.text_input.Clear()
            except Exception as e:
                wx.MessageBox(f"消息发送失败: {e}", "错误", wx.OK | wx.ICON_ERROR)

    def OnReset(self, event):
        """点击【重置】清空输入框"""
        self.text_input.Clear()

    def OnLeave(self, event):
        """点击【离开】主动退出聊天室"""
        if self.is_connected and self.client_socket:
            try:
                self.client_socket.sendall("__LEAVE__".encode('utf-8'))
            except:
                pass
        self.HandleDisconnection()

    def OnCloseWindow(self, event):
        """窗口被右上角 X 关闭时触发"""
        self.OnLeave(None)
        self.Destroy()


# ==========================================
# 客户端启动逻辑：启动前先输入姓名
# ==========================================
if __name__ == '__main__':
    app = wx.App()

    # 弹出对话框让用户输入用户名
    dlg = wx.TextEntryDialog(None, "请输入你的名字加入聊天室:", "用户登录", "李四")
    if dlg.ShowModal() == wx.ID_OK:
        name = dlg.GetValue().strip()
        dlg.Destroy()
        if name:
            frame = ClientFrame(name)
            frame.Center()
            frame.Show()
            app.MainLoop()
        else:
            wx.MessageBox("用户名不能为空！", "提示")
    else:
        dlg.Destroy()