from optimal_projections_discovery_engine import *
import wx

class Mywin(wx.Frame):
	def __init__(self, parent, title, discovery):
		super(Mywin, self).__init__(parent, title=title, size=(300,500))
		self.discovery = discovery

		panel = wx.Panel(self)
		vbox=wx.BoxSizer(wx.VERTICAL)

		setlist=['Wisconsin Diagnostic Breast Cancer','Wine','Yeast']

		self.rbox=wx.RadioBox(panel, label='Data Set', choices=setlist,majorDimension=1,style=wx.RA_SPECIFY_COLS)
		vbox.Add(self.rbox)
		self.rbox.Bind(wx.EVT_RADIOBOX, self.radio)

		hbox5=wx.BoxSizer(wx.HORIZONTAL)

		self.t5=wx.TextCtrl(panel, size=(300,100),style=wx.TE_MULTILINE)
		self.t5.AppendText("A")
		hbox5.Add(self.t5,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox5)


		hbox1=wx.BoxSizer(wx.HORIZONTAL)
		l1=wx.StaticText(panel, -1, "Noise")
		hbox1.Add(l1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)

		self.t1=wx.TextCtrl(panel)
		self.t1.AppendText('0.2')
		hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox1)

		hbox2=wx.BoxSizer(wx.HORIZONTAL)
		l2=wx.StaticText(panel, -1, "Step size")
		hbox2.Add(l2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)

		self.t2=wx.TextCtrl(panel)
		self.t2.AppendText('1.0')
		hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox2)

		hbox3=wx.BoxSizer(wx.HORIZONTAL)
		l3=wx.StaticText(panel, -1, "Convergence")
		hbox3.Add(l3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)

		self.t3=wx.TextCtrl(panel)
		self.t3.AppendText('0.1')
		hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox3)

		hbox4=wx.BoxSizer(wx.HORIZONTAL)
		b1=wx.Button(panel, label="Start")
		b2=wx.Button(panel, label="Close")
		hbox4.Add(b1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		hbox4.Add(b2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox4)

		self.Bind(wx.EVT_BUTTON,self.start,b1)
		self.Bind(wx.EVT_BUTTON,self.close,b2)

		panel.SetSizer(vbox)
		self.Center()
		self.Show()

	def radio(self, event):
		self.t5.Clear()
		s=self.rbox.GetSelection()
		if s==0:
			self.t5.AppendText("A")
		elif s==1:
			self.t5.AppendText("B")
		elif s==2:
			self.t5.AppendText("C")


	def start(self, event):
		arg1=float(self.t1.GetValue())
		arg2=float(self.t2.GetValue())
		arg3=float(self.t3.GetValue())
		s=self.rbox.GetSelection()
		if s==0:
			data='wdbc'
		elif s==1:
			data='wine'
		elif s==2:
			data='yeast'

		plist=self.discovery(data,arg1,arg2,arg3)


	def close(self, event):
		wx.Exit()

app=wx.App()
Mywin(None, "Optimal Sets of Projections of High-Dimentional Data", optimal_projections_discovery)
app.MainLoop()
