# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:25:29 2022

@author: riyam
"""

from tkinter import*

root=Tk()
root.title("My Calculator")
root.geometry("600x410")

def b_click(number):
    global  val
    val=val+str(number)
    myVal.set(val)
    
def b_clear():
    global val
    val=""
    myVal.set("")
    
def b_equal():
    global val
    rslt=str(eval(val))           # evaluate the value or calculation
    myVal.set(rslt)
    
val=""
myVal=StringVar()

e1=Entry(root,textvariable=myVal,font=('Simple',45,'bold'),width=17,justify="right",bg="skyblue")  #bd=30
e1.grid(row=0,columnspan=4)
b7=Button(root,text="7",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click(7))
b7.grid(row=1,column=0)
b8=Button(root,text="8",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click(8))
b8.grid(row=1,column=1)
b9=Button(root,text="9",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click(9))
b9.grid(row=1,column=2)
b_add=Button(root,text="+",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click('+'))
b_add.grid(row=1,column=3)

b4=Button(root,text="4",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click(4))
b4.grid(row=2,column=0)
b5=Button(root,text="5",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click(5))
b5.grid(row=2,column=1)
b6=Button(root,text="6",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click(6))
b6.grid(row=2,column=2)
b_sub=Button(root,text="-",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click('-'))
b_sub.grid(row=2,column=3)

b1=Button(root,text="1",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click(1))
b1.grid(row=3,column=0)
b2=Button(root,text="2",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click(2))
b2.grid(row=3,column=1)
b3=Button(root,text="3",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click(3))
b3.grid(row=3,column=2)
b_mul=Button(root,text="*",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click('*'))
b_mul.grid(row=3,column=3)

b_clear=Button(root,text="C",font=('Simple',14,'bold'),width=12,height=3,command=b_clear)
b_clear.grid(row=4,column=0)
b0=Button(root,text="0",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click(0))
b0.grid(row=4,column=1)
b_equal=Button(root,text="=",font=('Simple',14,'bold'),width=12,height=3,command=b_equal)
b_equal.grid(row=4,column=2)
b_div=Button(root,text="/",font=('Simple',14,'bold'),width=12,height=3,command=lambda:b_click('/'))
b_div.grid(row=4,column=3)

root.mainloop()