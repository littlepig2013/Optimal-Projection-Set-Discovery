from optimal_projections_discovery_engine import *
import wx
import numpy as np
import matplotlib.pyplot as plt

class Mywin(wx.Frame):
	def __init__(self, parent, title, discovery):
		super(Mywin, self).__init__(parent, title=title, size=(400,650))
		self.discovery = discovery

		panel = wx.Panel(self)
		vbox=wx.BoxSizer(wx.VERTICAL)

		#Radiobox for data set choice
		setlist=['Wisconsin Diagnostic Breast Cancer','Wine','Yeast']
		self.rbox=wx.RadioBox(panel, label='Data Set', choices=setlist,majorDimension=1,style=wx.RA_SPECIFY_COLS)
		vbox.Add(self.rbox)
		self.rbox.Bind(wx.EVT_RADIOBOX, self.radio)

		#Text for discription of data set
		hbox5=wx.BoxSizer(wx.HORIZONTAL)
		self.t5=wx.TextCtrl(panel, size=(400,250),style=wx.TE_MULTILINE)
		self.t5.AppendText("Title: Wisconsin Diagnostic Breast Cancer (WDBC)\n")
		self.t5.AppendText("\n")
		self.t5.AppendText("Number of instances: 569 \n")
		self.t5.AppendText("\n")
		self.t5.AppendText("Number of attributes: 32\n")
		self.t5.AppendText("    ID, diagnosis, 30 real-valued input features\n")
		self.t5.AppendText("\n")
		self.t5.AppendText("Class distribution:\n")
		self.t5.AppendText("    357 benign\n")
		self.t5.AppendText("    212 malignant\n")
		self.t5.AppendText("\n")
		hbox5.Add(self.t5,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox5)

		#Input for noise
		hbox1=wx.BoxSizer(wx.HORIZONTAL)
		l1=wx.StaticText(panel, -1, "Noise:")
		hbox1.Add(l1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)

		self.t1=wx.TextCtrl(panel)
		self.t1.AppendText('0.2')
		hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox1)

		#Input for step size
		hbox2=wx.BoxSizer(wx.HORIZONTAL)
		l2=wx.StaticText(panel, -1, "Step size:")
		hbox2.Add(l2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)

		self.t2=wx.TextCtrl(panel)
		self.t2.AppendText('1.0')
		hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox2)

		#Input for convergence
		hbox3=wx.BoxSizer(wx.HORIZONTAL)
		l3=wx.StaticText(panel, -1, "Convergence")
		hbox3.Add(l3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)

		self.t3=wx.TextCtrl(panel)
		self.t3.AppendText('0.1')
		hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox3)

		#Output for result
		hbox6=wx.BoxSizer(wx.HORIZONTAL)
		l6=wx.StaticText(panel, -1, "Result:")
		hbox6.Add(l6,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)

		self.t6=wx.TextCtrl(panel)
		hbox6.Add(self.t6,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox6)

		#Buttons
		hbox4=wx.BoxSizer(wx.HORIZONTAL)
		b1=wx.Button(panel, label="Start")
		b2=wx.Button(panel, label="Close")
		b3=wx.Button(panel, label="Next")
		hbox4.Add(b1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		hbox4.Add(b3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		hbox4.Add(b2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox4)

		#Binding events
		self.Bind(wx.EVT_BUTTON,self.start,b1)
		self.Bind(wx.EVT_BUTTON,self.close,b2)
		self.Bind(wx.EVT_BUTTON,self.next,b3)

		#Author information
		hbox7=wx.BoxSizer(wx.HORIZONTAL)
		l7=wx.StaticText(panel, -1, "Zhu Zichen")
		hbox7.Add(l7,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)

		t7=wx.StaticText(panel, -1, "3030049220")
		hbox7.Add(t7,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
		vbox.Add(hbox7)

		hbox8=wx.BoxSizer(wx.HORIZONTAL)
		l8=wx.StaticText(panel, -1, "Wen Jing")
		hbox8.Add(l8,1,wx.EXPAND|wx.ALIGN_RIGHT|wx.ALL,5)

		t8=wx.StaticText(panel, -1, "3030048903")
		hbox8.Add(t8,1,wx.EXPAND|wx.ALIGN_RIGHT|wx.ALL,5)
		vbox.Add(hbox8)

		hbox9=wx.BoxSizer(wx.HORIZONTAL)
		l9=wx.StaticText(panel, -1, "Presented for 2017 Fall COMP8035 @HKU")
		hbox9.Add(l9,1,wx.EXPAND|wx.ALIGN_RIGHT|wx.ALL,5)

		vbox.Add(hbox9)

		#Display
		panel.SetSizer(vbox)
		self.Center()
		self.Show()

	#Radiobox event
	def radio(self, event):
		self.t6.Clear()
		self.t5.Clear()
		s=self.rbox.GetSelection()
		if s==0:
			self.t5.AppendText("Title: Wisconsin Diagnostic Breast Cancer (WDBC)\n")
			self.t5.AppendText("\n")
			self.t5.AppendText("Number of instances: 569 \n")
			self.t5.AppendText("\n")
			self.t5.AppendText("Number of attributes: 32\n")
			self.t5.AppendText("    ID, diagnosis, 30 real-valued input features\n")
			self.t5.AppendText("\n")
			self.t5.AppendText("Class distribution:\n")
			self.t5.AppendText("    357 benign\n")
			self.t5.AppendText("    212 malignant\n")
			self.t5.AppendText("\n")
		elif s==1:
			self.t5.AppendText("Title: Wine recognition data\n")
			self.t5.AppendText("\n")
			self.t5.AppendText("Number of Instances: 178\n")
			self.t5.AppendText("\n")
			self.t5.AppendText("Number of Attributes:13\n")
			self.t5.AppendText("\n")
			self.t5.AppendText("Class distribution:\n")
			self.t5.AppendText("    Class 1 59\n")
			self.t5.AppendText("    Class 2 71\n")
			self.t5.AppendText("    Class 3 48\n")
			self.t5.AppendText("\n")

		elif s==2:
			self.t5.AppendText("Title: Protein Localization Sites\n")
			self.t5.AppendText("\n")
			self.t5.AppendText("Number of Instances:  1484 for the Yeast dataset.\n")
			self.t5.AppendText("\n")
			self.t5.AppendText("Number of Attributes: 9\n")
			self.t5.AppendText("    8 predictive, 1 name\n")
			self.t5.AppendText("\n")
			self.t5.AppendText("Class Distribution:\n")
			self.t5.AppendText("    463  CYT (cytosolic or cytoskeletal)\n")
			self.t5.AppendText("    429  NUC (nuclear)\n")
			self.t5.AppendText("    244  MIT (mitochondrial)\n")
			self.t5.AppendText("    163  ME3 (membrane protein, no N-terminal signal)\n")
			self.t5.AppendText("     51   ME2 (membrane protein, uncleaved signal)\n")
			self.t5.AppendText("     44   ME1 (membrane protein, cleaved signal)\n")
			self.t5.AppendText("     37   EXC (extracellular)\n")
			self.t5.AppendText("     30   VAC (vacuolar)\n")
			self.t5.AppendText("     20   POX (peroxisomal)\n")
			self.t5.AppendText("      5    ERL (endoplasmic reticulum lumen)\n")
			self.t5.AppendText("\n")

	#Button event
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
		print('a')

		plist=self.discovery(data,arg1,arg2,arg3)
		print('b')
		c=1
		num=len(plist)
		self.t6.Clear()
		self.t6.AppendText(str(num))
		for item in plist:
			X=item
			fig1=plt.figure("Projection"+str(c))
			c=c+1
			plt.plot(X[:,0],X[:,1],'o')
			plt.show()

		c=1
		fig2=plt.figure("All projections")
		for item in plist:
			X=item
			if len(plist)==1:
				ax=fig2.add_subplot(110+c)
			elif len(plist)==2:
				ax=fig2.add_subplot(120+c)
			elif len(plist)<5:
				ax=fig2.add_subplot(220+c)
			elif len(plist)<7:
				ax=fig2.add_subplot(230+c)
			elif len(plist)<10:
				ax=fig2.add_subplot(330+c)
			elif len(plist)<13:
				ax=fig2.add_subplot(340+c)
			plt.plot(X[:,0],X[:,1],'o')
			ax.set_title('Projection'+str(c))
			c=c+1
		fig2.tight_layout()
		plt.show()


	def next(self, event):
		plt.close()

	#Exit
	def close(self, event):
		wx.Exit()

app=wx.App()
Mywin(None, "Optimal Sets of Projections of High-Dimentional Data", optimal_projections_discovery)
app.MainLoop()
