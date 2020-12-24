from tkinter import *
import tkinter
top=Tk()
Checkvar1=IntVar()
Checkvar2=IntVar()
C1=Checkbutton(top,text="male",
               variable=Checkvar1,
               onvalue=1,
               offvalue=0)
C2=Checkbutton(top,text="female",
               variable=Checkvar2,
               onvalue=1,
               offvalue=0)
C1.pack()
C2.pack()

def gender():
    gen=""
    ref={1:"male", 2:"female"}
    if Checkvar1.get==1:
        gen=gen+"MALE"
    elif Checkvar2.get==2:
        gen=gen+"female"
Button(top,text=gender,command=gender,bitmap="info",width=15).pack(anchor=CENTER)
top.mainloop()