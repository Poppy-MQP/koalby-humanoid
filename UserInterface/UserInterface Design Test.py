from tkinter import *

global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10
window = Tk()
window.geometry("800x500")

# Make the buttons
b1 = Button(window, text="Initialize", bg="red", activeforeground="black", activebackground="green", padx=25, pady=25)
b2 = Button(window, text="Shutdown", bg="red", activeforeground="black", activebackground="green", padx=25, pady=25)
b3 = Button(window, text="Dance Toggle", bg="red", activeforeground="black", activebackground="green", padx=25, pady=25)
b4 = Button(window, text="Mirror Toggle", bg="red", activeforeground="black", activebackground="green", padx=25, pady=25)

# Clap 0.2 0.1, Dab 0.1 0, Macerena 0.5 0.2, Shake 0.2 0 , Extend 0.5 0, Wave 0.3 0
b5 = Button(window, text="Clap Toggle", bg="red", activeforeground="black", activebackground="green", padx=25, pady=25)
b6 = Button(window, text="Dab Toggle", bg="red", activeforeground="black", activebackground="green", padx=25, pady=25)
b7 = Button(window, text="Macarena Toggle", bg="red", activeforeground="black", activebackground="green", padx=20, pady=25)
b8 = Button(window, text="Wave Toggle", bg="red", activeforeground="black", activebackground="green", padx=25, pady=25)
b9 = Button(window, text="Extend Toggle", bg="red", activeforeground="black", activebackground="green", padx=25, pady=25)
b10 = Button(window, text="Shake Toggle", bg="red", activeforeground="black", activebackground="green", padx=25, pady=25)

# Set button locations
b1.place(x=0, y=0)
b2.place(x=0, y=80)
b3.place(x=150, y=0)
b4.place(x=150, y=80)
b5.place(x=300, y=0)
b6.place(x=300, y=80)
b7.place(x=450, y=0)
b8.place(x=450, y=80)
b9.place(x=600, y=0)
b10.place(x=600, y=80)

while True:
    window.update()
    window.update_idletasks()
