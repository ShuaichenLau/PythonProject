import wx

class MyServerFrame(wx.Frame):
    def __init__(self):
        super.__init__(None,100,'服务器窗口',wx.DefaultPosition,(500,580))
        pl=wx.Panel(parent=self)

if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None,100,'Hello World')
    frame.Show()
    app.MainLoop()
