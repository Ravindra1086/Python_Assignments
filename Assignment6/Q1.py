import os
from tkinter import *

window = Tk()

window.geometry('350x400')
#Input box
e = Entry(window,width= 40,borderwidth=5)
e.place(x=0,y=0)

def click(i):
    result = e.get()
    e.delete(0,END)
    # print(f"you clicked {i}!!")    
    e.insert(0,str(result)+str(i))




#buttons
b= Button(window,width=10,text='1',command=lambda:click(1))
b.place(x=00,y=30)

b= Button(window,width=10,text='2',command=lambda:click(2))
b.place(x=85,y=30)

b= Button(window,width=10,text='3',command=lambda:click(3))
b.place(x=170,y=30)

b= Button(window,width=10,text='4',command=lambda:click(4))
b.place(x=0,y=60)

b= Button(window,width=10,text='5',command=lambda:click(5))
b.place(x=85,y=60)

b= Button(window,width=10,text='6',command=lambda:click(6))
b.place(x=170,y=60)

b= Button(window,width=10,text='7',command=lambda:click(7))
b.place(x=0,y=90)

b= Button(window,width=10,text='8',command=lambda:click(8))
b.place(x=85,y=90)

b= Button(window,width=10,text='9',command=lambda:click(9))
b.place(x=170,y=90)

b= Button(window,width=10,text='0',command=lambda:click(0))
b.place(x=0,y=120)


def add():    
    n1 = e.get()
    #print(n1)
    if n1 !="" :
        global math
        math = "addition"
        global i
        i = float(n1)
        e.delete(0,END)
    
    # print(f"you clicked {i}!!")    
    #e.insert(0,result + i)

b= Button(window,width=10,text='+',command=add)
b.place(x=85,y=120)

def sub():    
    n1 = e.get()
    if n1 !="" :
        global math
        math = "subtraction"
        global i
        i = float(n1)
        e.delete(0,END)    

b= Button(window,width=10,text='-',command=sub)
b.place(x=170,y=120)

def mul():    
    n1 = e.get()    
    if n1 !="" :
        global math
        math = "multiplication"
        global i
        i = float(n1)
        e.delete(0,END)    

b= Button(window,width=10,text='*',command=mul)
b.place(x=0,y=150)


def div():    
    n1 = e.get()
    if n1 !="" :
        global math
        math = "division"
        global i
        i = float(n1)
        e.delete(0,END)

b= Button(window,width=10,text='/',command=div)
b.place(x=85,y=150)

def equal():    
    n2 = e.get()
    e.delete(0,END)
    if math =="addition":
        e.insert(0,i+ float(n2))
    if math =="subtraction":
        e.insert(0,i- float(n2))
    if math =="multiplication":
        e.insert(0,i * float(n2))
    if math =="division":
        if(n2!="cannot divide by 0"):
            if float(n2) == 0.0 :
                e.insert(0,"cannot divide by 0")    
            else:
                e.insert(0,i/ float(n2))
        else:
              e.insert(0,"")    

b= Button(window,width=10,text='=',command=equal)
b.place(x=170,y=150)

def clear():    
    e.delete(0,END)

b= Button(window,width=10,text='Clear',command=clear)
b.place(x=0,y=180)

window.mainloop()    



