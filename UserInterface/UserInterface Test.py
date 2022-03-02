from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry("500x500")


def fun():
    messagebox.showinfo("Hello", "Red Button clicked")


b1 = Button(top, text="Red", command=fun, activeforeground="red", activebackground="pink",padx=50, pady=50)

b2 = Button(top, text="Blue", activeforeground="blue", activebackground="pink",padx=50, pady=50)

b3 = Button(top, text="Green", activeforeground="green", activebackground="pink", padx=50,pady=50)

b4 = Button(top, text="Yellow", activeforeground="yellow", activebackground="pink", padx=50, pady=50)

b1.pack(side=LEFT)

b2.pack(side=RIGHT)

b3.pack(side=TOP)

b4.pack(side=BOTTOM)

top.mainloop()