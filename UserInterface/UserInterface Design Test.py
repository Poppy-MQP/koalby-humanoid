from tkinter import *

window = Tk()
window.geometry("800x500")
b1,b2,b3,b4,b5,b6,b7,b8,b9,b10 = Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button(),Button()

i = False
# Make the buttons
def init():
    pass


def setup():
    global i
    if i:
        i  = False
        b1.config(bg="red")
    else:
        i  = True
        b1.config(bg="green")

def buttons():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10
    b1 = Button(window, text="Initialize", command=setup, activeforeground="black", activebackground="pink", padx=25, pady=25)

    # Set button locations
    b1.place(x=0, y=0)
    while True:
        window.update()
        window.update_idletasks()