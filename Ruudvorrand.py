from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
flag=True
text=""
def lahenda():    
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            flag=True
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            flag=True
        else:
            t="Корней нет"
            flag=False
        vastus.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return flag,D,t
def graafik():
    global flag,text
    flag,D,t=lahenda()
    if flag==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)#min max step
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    vastus.configure(text=f"D={D}\n{t}\n{text}")
aken=Tk()
aken.geometry("620x200")
aken.title("Квадратные уравнения")
lbl=Label(aken,text="Решение квадратного уравнения",font="Calibri 26", fg="green",bg="lightblue")
lbl.pack()
vastus=Label(aken,text="Решение", height=4,width=60,bg="yellow")
vastus.pack(side=BOTTOM)
a=Entry(aken,font="Calibri 26", fg="green",bg="lightblue",width=3)
a.pack(side=LEFT)#,padx=10,pady=10
x2=Label(aken,text="x**2+",font="Calibri 26", fg="green", padx=10)
x2.pack(side=LEFT)
b=Entry(aken,font="Calibri 26", fg="green",bg="lightblue",width=3)
b.pack(side=LEFT)
x=Label(aken,text="x+",font="Calibri 26", fg="green")
x.pack(side=LEFT)
c=Entry(aken,font="Calibri 26", fg="green",bg="lightblue",width=3)
c.pack(side=LEFT)
y=Label(aken,text="=0",font="Calibri 26", fg="green")
y.pack(side=LEFT)

btn=Button(aken,text="Решить", font="Calibri 26",bg="green",command=lahenda)
btn.pack(side=LEFT)
btn_g=Button(aken,text="График", font="Calibri 26",bg="green",command=graafik)
btn_g.pack(side=LEFT)
#btn.bind("<Button-1>",lahenda)

aken.mainloop()
