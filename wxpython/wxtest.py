import wx


app = wx.App()
win = wx.Frame(None, title='Redis查询', size=(410, 335))  # 新建窗口对象
bkg = wx.Panel(win)

search_btn = wx.Button(bkg, label='Search')
del_btn = wx.Button(bkg, label='Del')
file_name = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(file_name, proportion=1, flag=wx.EXPAND)
hbox.Add(search_btn, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(del_btn, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND |wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
bkg.SetSizer(vbox)



win.Show()
app.MainLoop()