from tkinter import *
from datetime import datetime
from time import strftime


w=Tk()
w.geometry('825x200')
w.minsize(825,200)
w.title("Digital Clock")


a=datetime.today().strftime('%A')
b=(a.upper())
c=(b[0:3]) 


f1=Frame(w,width=825, height=250,bg='#0e1013')
f1.pack(expand=True)

def time():
    a=strftime("%I : %M : %S %p")
    l1.config(text=a)
    l1.after(1000,time)

l1=Label(f1, font=('Century Gothic',60),bg='#0e1013',foreground='#d3d3d3')

l1.place(x=275,y=35)
time()

l2=Label(f1, font=('Century Gothic',60),bg='#0e1013',foreground='#d3d3d3')
l2.config(text=c+" |")
l2.place(x=65,y=35)


def labels():
    l3=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='DAY')
    l3.place(x=112,y=130)

    l4=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='HOURS')
    l4.place(x=295,y=130)

    l5=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='MINUTES')
    l5.place(x=435,y=130)

    l3=Label(f1, font=('Century Gothic',8),bg='#0e1013',fg='#7f7f7f',text='SECONDS')
    l3.place(x=435+145+5,y=130)

labels()

w.mainloop()

