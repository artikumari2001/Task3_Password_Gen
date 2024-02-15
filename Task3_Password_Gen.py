from tkinter import *
import string
import random

win = Tk()
win.title("Password Generator")
win.geometry("450x350+0+0")
win.resizable(False,False)

ico=PhotoImage(file = 'password-512.png')
win.iconphoto(False,ico)

#functionality



inputval=StringVar()
outputval=StringVar()
outputval.set("")

s1=string.ascii_uppercase
s2=string.ascii_lowercase
s3=string.digits
s4=string.punctuation

s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

def reset(event):
    inputval.set("")
    outputval.set("")

def generate(event):
    len=int(inputval.get())
    if len<7 or len>15:
        raise ValueError("Password length is not in range")
    else:
        try:
            random.shuffle(s)
            outputval.set("".join(s[0:len]))
        except Exception as e:
            outputval.set("Error occured due to "+e)
    output_field.update()


#gui

title = Label(win,text="PASSWORD GENERATOR",font=("times new roman",20,"bold"),
              width=30,relief=GROOVE,bg="red",fg="white")
title.pack(side=TOP,fill=X)

lbl1 = Label(win,text="Enter size of password :",fg="black",
             font=("times new roman",14))
lbl1.place(x=10,y=70)

input_field = Entry(win,textvariable=inputval,font=("audela",15),borderwidth=2,
                    relief=RIDGE)
input_field.place(x=200,y=70)

btn1=Button(win,text="GENERATE",font=("times new roman",10,"bold"),width=15,height=2,
            relief=RAISED,fg="white",bg="green")
btn1.place(x=75,y=140)
btn1.bind("<Button-1>",generate)
btn2=Button(win,text="RESET",font=("times new roman",10,"bold"),width=18,height=2,
            relief=RAISED,fg="white",bg="green")
btn2.place(x=230,y=140)
btn2.bind("<Button-1>",reset)

output_field=Entry(win,textvariable=outputval,font=("times new roman",25,"bold"),bg="white",fg="black",
                   relief=SOLID,state='readonly',borderwidth=4)
output_field.place(x=50,y=230)

note=Label(win,text="Note :- Password length should be in range of 6 to 15",
           font=("times new roman",10,"italic bold"),fg="brown")
note.place(x=10,y=300)


win.mainloop()