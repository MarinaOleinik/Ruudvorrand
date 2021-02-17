from tkinter import *
from math import *
def lahenda():    
    if (a.get()!=""and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
        else:
            t="Корней нет"
        vastus.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        elif b.get()=="":
            b.configure(bg="red")
        elif c.get()=="":
            c.configure(bg="red")


aken=Tk()
aken.geometry("600x200")
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
#btn.bind("<Button-1>",lahenda)

aken.mainloop()
