from tkinter import *
import math
import requests 
import pandas as pd
import numpy as np

root = Tk()
root.title(" DBS Order Book System")
root.configure(background='black')

label1 = Label(root, text="Order book System", fg="white", font="Helvetica 30 bold italic underline",bg='black').place(x=500, y=0)

button1 = Button(root, text="Customer Screen",width=20,height='2',fg="white",font="times 13 bold",bg='red', command=lambda:Customer()).place(x=1400,y=50)


flag = 1

def OpenM():
	flag = 1

def Closem():
	flag = 0

label = Label(root,text="Admin Screen",fg='red',bg='yellow', font = '30')
label.place(x=40,y=50)


button1 = Button(root, text="Open Market",width=11,fg="white",font="Arial 13 bold",bg='red',command=lambda:OpenM())
button1.place(x=150, y=130)

button1 = Button(root, text="Close Market",width=11,fg="white",font="Arial 13 bold",bg='red',command=lambda:OpenM())
button1.place(x=330, y=130)

l1 = Label(root,text="Select a Stock",fg='white',bg='red', font = '30')
l1.place(x=150,y=230)

options = ['DBS', 'AAPL', 'GOOGL', 'FB', 'BARC']
df = StringVar(root)
df.set("Select a Stock")
drop = OptionMenu( root ,df, *options )
drop.config(bg='antique white')
drop.place(x='150',y=265)


v= Entry(root, width =20,borderwidth=2, bg='antique white')
v.place(x=400,y=240)
Str = str(v.get())

v2= Entry(root, width =20,borderwidth=2, bg='antique white')
v2.place(x=580,y=240)
Str = str(v2.get())

l1 = Label(root,text="Show Orders",fg='white',bg='blue', font = '30')
l1.place(x=750,y=230)


l1 = Label(root,text="Execution Qty",fg='white',bg='red', font = '30')
l1.place(x=150,y=450)

v3= Entry(root, width =20,borderwidth=2, bg='antique white')
v3.place(x=150,y=490)
Str = str(v3.get())

l1 = Label(root,text="Execution Price",fg='white',bg='red', font = '30')
l1.place(x=350,y=450)

v3= Entry(root, width =20,borderwidth=2, bg='antique white')
v3.place(x=350,y=490)
Str = str(v3.get())

l1 = Label(root,text="Execute Orders",fg='white',bg='blue', font = '30')
l1.place(x=750,y=490)


#-------------------------------// Customer Screen //----------------------------------------------

def Customer():
    nwin=Toplevel()
    nwin.configure(background='black')

    l0 = Label(nwin,text="Customer Screen",fg='red',bg='yellow', font = '30')
    l0.place(x=40,y=10)

    if(flag==0):
        label = Label(nwin,text="Market's closed",fg='red',bg='yellow', font = '30')
        label.place(x=40,y=60)
    else:

        l1 = Label(nwin,text="Search a Stock",fg='white',bg='red', font = '30')
        l1.place(x=40,y=60)

        options = ['DBS', 'AAPL', 'GOOGL', 'FB', 'BARC']
        df = StringVar(nwin)
        df.set("Select a Stock")
        drop = OptionMenu( nwin ,df, *options )
        drop.config(bg='antique white')
        drop.place(x='40',y='100')

        l2 = Label(nwin,text="Order Type",fg='white',bg='red', font = '30')
        l2.place(x=40,y=160)

        o1 = ['Limit', 'Market']
        d1 = StringVar(nwin)
        d1.set("Select Market Type")
        drop = OptionMenu( nwin ,d1, *o1 )
        drop.config(bg='antique white')
        drop.place(x='40',y='190')

        l2 = Label(nwin, text="Price (if market order)", bg='red',fg="white", font="times 15")
        l2.place(x=40, y=240)
        v= Entry(nwin, width =20,borderwidth=2, bg='antique white')
        v.place(x=40,y=270)

        l3 = Label(nwin, text="Quantity", bg='red',fg="white", font="times 15")
        l3.place(x=40, y=320)
        v2= Entry(nwin, width =20,borderwidth=2, bg='antique white')
        v2.place(x=40,y=350)

        button1 = Button(nwin, text="Place Order",width=22,fg="white",font="times 15 bold",bg='red', command=lambda:Order()).place(x=40,y=400)


    nwin.geometry('500x600')


#---------------------------------------------------------------------------------------------------




#------------------------------- // Backend //----------------------------------------------#



root.state('zoomed')
root.mainloop()