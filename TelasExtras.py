import wx

class CadastrosWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size = (500,300))
        self.Show()