import os
from tkinter import *

from tkinter import messagebox

from sample_data import student

import os

dir="frame"
if os.path.exists(dir):
    j=0;
else:
    os.mkdir(dir)


for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))


def del_sc1():
    sc1.destroy()
def err_screen():
    global sc1
    sc1 = Tk()
    sc1.geometry('200x80')
    sc1.title('Warning!!')
    sc1.configure(background='snow')
    Label(sc1,text='Enrollment & Name required!!!',fg='#f5427e',bg='white',font=('times', 16, ' bold ')).pack()
    Button(sc1,text='OK',command=del_sc1,fg="black"  ,bg="#42bcf5"  ,width=9  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold ')).place(x=90,y= 50)
def clear():
    txt.delete(first=0, last=22)


def training():
    a=txt.get()

    if (a==""):
        messagebox.showinfo(title="Alert", message="Enter Your Email")

    else:
        s1=student;
        s1.name=a
        import main

root = Tk()
w=780
h=500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("FIRE DETECTION")
root.configure(background='#a3a4d4')
message = Label(root, text="FIRE DETECTION",fg="#FFF",bg='#a3a4d4', width=35,height=3, font=('times', 30, 'italic bold '))
message.place(x=2, y=20)

lbl = Label(root, text="EMAIL ID", width=20, height=2, fg="#FFF",bg='#a3a4d4', font=('times', 15, ' bold '))
lbl.place(x=30, y=200)
#
# lbl2 = Label(root, text="PASSWORD", width=20, fg="black",  height=2, font=('times', 15, ' bold '))
# lbl2.place(x=30, y=275)

txt = Entry(root, validate="key", width=20, font=('times', 25, ' bold '))
txt.place(x=300, y=200)

# txt2 = Entry(root, width=20, font=('times', 25, ' bold '))
# txt2.place(x=300, y=275)

compare_dataset = Button(root, text="START",width=28  ,height=1,fg="#FFF",bg="#004080",command=training, activebackground = "orange",activeforeground="white" ,font=('times', 15, ' bold '))
compare_dataset.place(x=300, y=350)

root.mainloop()
