"""聊天室服务端界面（wxPython）

本文件只负责三件事：
    1. 摆放控件；
    2. 把按钮点击翻译成 ChatServer 的方法调用；
    3. 把 ChatServer 的回调（来自子线程）用 wx.CallAfter 切回主线程再改控件。

真正的网络逻辑在 chat_server.py，通信协议在 chat_protocol.py。
"""

import datetime

import wx

from chat_server import ChatServer

SEPARATOR = '-' * 40


class ServerFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, '老肖的服务器界面', size=(450, 580))
        # on_log 可能被子线程调用，_append_message 内部会切回主线程
        self._server = ChatServer(on_log=self._append_message)
        self._build_ui()

    # ================================================== 界面搭建
    def _build_ui(self):
        panel = wx.Panel(self)

        # 顶部按钮区
        self.btn_start = wx.Button(panel, label='启动')
        self.btn_save = wx.Button(panel, label='聊天记录保存')
        self.btn_stop = wx.Button(panel, label='停止')
        self.btn_save.Disable()             # 未启动时不可用
        self.btn_stop.Disable()

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        top_sizer.Add(self.btn_start, 1, wx.EXPAND | wx.ALL, 2)
        top_sizer.Add(self.btn_save, 2, wx.EXPAND | wx.ALL, 2)
        top_sizer.Add(self.btn_stop, 1, wx.EXPAND | wx.ALL, 2)

        # 聊天记录显示区（多行只读）
        self.text_chat = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(top_sizer, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.text_chat, 1, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(main_sizer)

        # 事件绑定
        self.btn_start.Bind(wx.EVT_BUTTON, self._on_start)
        self.btn_save.Bind(wx.EVT_BUTTON, self._on_save)
        self.btn_stop.Bind(wx.EVT_BUTTON, self._on_stop)
        self.Bind(wx.EVT_CLOSE, self._on_close)

    # ================================================== 网络层回调
    def _append_message(self, text):
        """ChatServer 的 on_log 回调（可能运行在子线程）"""
        wx.CallAfter(self._show_record, text)

    def _show_record(self, text):
        """真正往文本框里追加内容（主线程）

        CallAfter 排队的一瞬间窗口可能已经被销毁，此时控件已不存在，
        捕获 RuntimeError 直接忽略即可。
        """
        try:
            self.text_chat.AppendText(f'{text}\n{SEPARATOR}\n')
        except RuntimeError:
            pass

    # ================================================== 按钮事件
    def _on_start(self, event):
        """点击【启动】：开启聊天室服务"""
        try:
            self._server.start()
        except OSError as exc:
            wx.MessageBox(f'启动失败: {exc}', '错误', wx.OK | wx.ICON_ERROR)
            return

        self.btn_start.Disable()
        self.btn_save.Enable()
        self.btn_stop.Enable()

    def _on_save(self, event):
        """点击【聊天记录保存】：把文本框内容存成本地文件"""
        content = self.text_chat.GetValue()
        if not content.strip():
            wx.MessageBox('暂无聊天记录可保存', '提示', wx.OK | wx.ICON_INFORMATION)
            return

        file_path = f"chat_record_{datetime.datetime.now():%Y%m%d_%H%M%S}.txt"
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        wx.MessageBox(f'聊天记录已成功保存到: {file_path}', '保存成功',
                      wx.OK | wx.ICON_INFORMATION)

    def _on_stop(self, event):
        """点击【停止】：通知客户端并关闭服务，然后关闭窗口"""
        self._server.stop()                 # 内部会广播关闭通知并断开所有客户端
        self.Destroy()

    def _on_close(self, event):
        """右上角 X：先确保服务已停止，再销毁窗口"""
        self._server.stop()                 # 未启动时什么也不做
        self.Destroy()


def main():
    app = wx.App()
    frame = ServerFrame()
    frame.Center()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
