from tkinter import *
import math
import requests 
import pandas as pd
import numpy as np
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["stocks"]

mycol.drop()

mycol = mydb["stocks"]


root = Tk()
root.title("Order Book System")
root.configure(background='black')

label1 = Label(root, text="Order book System", fg="white", font="Helvetica 30 bold italic underline",bg='black').place(x=500, y=0)

global flag

flag = 1

def OpenM():
	global flag 
	flag = 1

def CloseM():
	global flag 
	flag = 0

label = Label(root,text="Admin Screen",fg='red',bg='yellow', font = '30')
label.place(x=40,y=50)


button1 = Button(root, text="Open Market",width=11,fg="white",font="Arial 13 bold",bg='red',command=lambda:OpenM())
button1.place(x=150, y=130)

button1 = Button(root, text="Close Market",width=11,fg="white",font="Arial 13 bold",bg='red',command=lambda:CloseM())
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

def Order():
    StockName = df.get()
    OrderType = d1.get()
    Price = v.get()
    Quantity = v2.get()
    print(StockName)
    print(OrderType)
    print(Price)
    print(Quantity)
    mydict = { "StockName": StockName, "OrderType": OrderType, "Price": Price, "Quantity": Quantity}
    mycol.insert_one(mydict)


l0 = Label(root,text="Customer Screen",fg='red',bg='yellow', font = '30')
l0.place(x=1100,y=50)

if(flag==0):
    label = Label(root,text="Market's closed",fg='red',bg='yellow', font = '30')
    label.place(x=1100,y=100)
else:
    l1 = Label(root,text="Search a Stock",fg='white',bg='red', font = '30')
    l1.place(x=1100,y=100)

    options = ['DBS', 'AAPL', 'GOOGL', 'FB', 'BARC']
    df = StringVar()
    df.set("Select a Stock")
    drop = OptionMenu(root ,df, *options )
    drop.config(bg='antique white')
    drop.place(x=1100,y='130')

    l2 = Label(root,text="Order Type",fg='white',bg='red', font = '30')
    l2.place(x=1100,y=200)

    o1 = ['Limit', 'Market']
    d1 = StringVar()
    d2 = OptionMenu( root ,d1, *o1 )
    d2.config(bg='antique white')
    d2.place(x='1100',y=230)

    l2 = Label(root, text="Price (if market order)", bg='red',fg="white", font="times 15")
    l2.place(x=1100, y=280)

    v= Entry(root, width =20,borderwidth=2, bg='antique white')
    v.place(x=1100,y=310)

    Price = str(v.get())

    l3 = Label(root, text="Quantity", bg='red',fg="white", font="times 15")
    l3.place(x=1100, y=340)
    v2= Entry(root, width =20,borderwidth=2, bg='antique white')
    v2.place(x=1100,y=370)

    Quantity = str(v2.get())

    button1 = Button(root, text="Place Order",width=22,fg="white",font="times 15 bold",bg='red', command=lambda:Order()).place(x=1100,y=440)

#------------------------------- // Backend //----------------------------------------------#

#---------------------------------------------------------------------------------------------------

root.geometry('1400x600')
root.mainloop()