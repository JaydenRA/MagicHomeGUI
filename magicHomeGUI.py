from magichomeAPI import *
from tkinter import *

#AssignIP
def Start():
	x = IP_entry.get()
	controller1 = MagicHomeApi(x,0)
	connected_label.place(x=570,y=130)
	return controller1

#Command def
def On():
	Start().turn_on()
def Off():
	Start().turn_off()
def Activate():
	R = RValue.get()
	G = GValue.get()
	B = BValue.get()
	W = WValue.get()
	Start().update_device(R,G,B,W)

#TK Config
screen = Tk()
screen.geometry('1200x500')
screen.title('Magic Home')
heading = Label(text = 'Magic Home GUI\nGithub: @JaydenRA', bg = 'grey', fg = 'black', width = '500', height = '3')
heading.pack()

#IP Config
x = StringVar()
IP_entry = Entry(textvariable = x)
IP_entry.place(x=540,y=80)
IP_label = Label(text = 'IP')
IP_label.place(x=595,y=55)
IP_save = Button(screen, text = 'Confirm', width = '6', height = '1', command = Start)
IP_save.place(x=575,y=100)
connected_label = Label(text = 'Connected.')

#Command call
On = Button(screen, text = 'On', width = '20', height = '5', command = On)
On.place(x=900,y=125)
Off = Button(screen, text = 'Off', width = '20', height = '5', command = Off)
Off.place(x=150,y=125)
Activate = Button(screen, text = 'Activate\nRGBW', width = '50', height = '5', command = Activate)
Activate.place(x=400,y=350)

#Colour
RValue = IntVar()
GValue = IntVar()
BValue = IntVar()
WValue = IntVar()

R_entry = Entry(textvariable = RValue)
G_entry = Entry(textvariable = GValue)
B_entry = Entry(textvariable = BValue)
W_entry = Entry(textvariable = WValue)

R_label = Label(screen,text='R')
R_label.config(font=("Courier", 44))
G_label = Label(screen,text='G')
G_label.config(font=("Courier", 44))
B_label = Label(screen,text='B')
B_label.config(font=("Courier", 44))
W_label = Label(screen,text='W')
W_label.config(font=("Courier", 44))

R_entry.place(x=80,y=300)
R_label.place(x=120,y=230)
G_entry.place(x=380,y=300)
G_label.place(x=420,y=230)
B_entry.place(x=680,y=300)
B_label.place(x=720,y=230)
W_entry.place(x=980,y=300)
W_label.place(x=1020,y=230)

#run tk
screen.mainloop()