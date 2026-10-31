"""聊天室客户端界面（wxPython）

本文件只负责界面与线程切换，网络逻辑在 chat_client.py。

操作方式：
    * 点【连接】进入聊天室；
    * 输入框里按【回车】直接发送，按 Shift+回车 才是换行；
    * 点【离开】退出聊天室（窗口保留，可再次连接）。

注意：网络层的回调运行在子线程，直接操作 wx 控件会崩溃，
所以统一用 wx.CallAfter 把动作丢回主线程执行。
"""

import wx

from chat_client import ChatClient

SEPARATOR = '-' * 40


class ClientFrame(wx.Frame):
    def __init__(self, username):
        super().__init__(None, wx.ID_ANY, f'{username}的客户端界面', size=(450, 580))
        self._closing = False               # 窗口正在关闭时不再更新界面
        self._client = ChatClient(
            username,
            on_message=self._on_remote_message,
            on_disconnected=self._on_remote_disconnected,
            on_error=self._on_remote_message,
        )
        self._build_ui()

    # ================================================== 界面搭建
    def _build_ui(self):
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

        # 3. 消息输入区（多行：回车发送，Shift+回车 换行）
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

        # 事件绑定
        self.btn_conn.Bind(wx.EVT_BUTTON, self._on_connect)
        self.btn_leave.Bind(wx.EVT_BUTTON, self._on_leave)
        self.btn_reset.Bind(wx.EVT_BUTTON, self._on_reset)
        self.btn_send.Bind(wx.EVT_BUTTON, self._on_send)
        self.text_input.Bind(wx.EVT_KEY_DOWN, self._on_input_key_down)
        self.Bind(wx.EVT_CLOSE, self._on_close)

    # ================================================== 网络层回调（子线程）
    def _on_remote_message(self, text):
        """ChatClient 推来一条要显示的内容"""
        if self._closing:
            return
        wx.CallAfter(self._show_message, text)

    def _on_remote_disconnected(self):
        """ChatClient 通知连接已断开：还原按钮状态，但不关闭窗口"""
        if self._closing:
            return
        wx.CallAfter(self._restore_ui_after_disconnect)

    # ================================================== 主线程更新界面
    # 这几个方法都由 wx.CallAfter 调度，窗口可能已经销毁，故忽略 RuntimeError
    def _show_message(self, text):
        try:
            self.text_chat.AppendText(f'{text}\n{SEPARATOR}\n')
        except RuntimeError:
            pass

    def _restore_ui_after_disconnect(self):
        """断开后：可以重新连接，不能再发送"""
        try:
            self.btn_conn.Enable()
            self.btn_leave.Disable()
            self.btn_send.Disable()
        except RuntimeError:
            pass

    # ================================================== 按钮事件
    def _on_connect(self, event):
        """点击【连接】进入聊天室"""
        try:
            self._client.connect()
        except OSError as exc:
            wx.MessageBox(f'无法连接到服务器: {exc}', '连接失败',
                          wx.OK | wx.ICON_ERROR)
            return

        self.btn_conn.Disable()
        self.btn_leave.Enable()
        self.btn_send.Enable()
        self._show_message(f'已连接到 {self._client.host}:{self._client.port}')

    def _on_send(self, event):
        """点击【发送】：把输入框内容发给服务器"""
        self._send_current_input()

    def _on_input_key_down(self, event):
        """输入框里按【回车】= 发送；Shift+回车 = 普通换行"""
        is_enter = event.GetKeyCode() in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER)
        if is_enter and not event.ShiftDown():
            self._send_current_input()
            return          # 不再 Skip：不交给输入框处理，回车就不会变成换行
        event.Skip()        # 其它按键（包括 Shift+回车）交给输入框自己处理

    def _send_current_input(self):
        """取出输入框内容并发送，发送成功才清空输入框"""
        text = self.text_input.GetValue().strip()
        if not text:
            return
        if not self._client.connected:
            self._show_message('提示: 请先点击【连接】进入聊天室')
            return
        if self._client.send_chat(text):
            self.text_input.Clear()

    def _on_reset(self, event):
        """点击【重置】：清空输入框"""
        self.text_input.Clear()

    def _on_leave(self, event):
        """点击【离开】：主动退出聊天室（窗口保留，可再次连接）"""
        self._client.disconnect()
        self._show_message('已离开聊天室')

    def _on_close(self, event):
        """右上角 X：断开连接并关闭窗口"""
        self._closing = True                # 后续网络回调不再碰控件
        self._client.disconnect()
        self.Destroy()


def ask_username():
    """启动前弹窗输入昵称；用户取消或输入为空时返回 None"""
    dialog = wx.TextEntryDialog(None, '请输入你的名字加入聊天室:', '用户登录', '李四')
    try:
        if dialog.ShowModal() != wx.ID_OK:
            return None
        return dialog.GetValue().strip() or None
    finally:
        dialog.Destroy()


def main():
    app = wx.App()
    username = ask_username()
    if not username:
        wx.MessageBox('用户名不能为空！', '提示')
        return

    frame = ClientFrame(username)
    frame.Center()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
