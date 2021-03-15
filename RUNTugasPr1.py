import wx
import TUGASPR1

# buat instance app
app = wx.App()

# buat instance frame
frame = TUGASPR1.MyFrame1(parent = None)
# nampilkan framenya
frame.Show()

# jalankan aplikasinya
app.MainLoop()