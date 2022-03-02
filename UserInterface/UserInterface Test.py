import time
from threading import Thread
from tkinter import *
from tkinter import messagebox
from KoalbyHumanoid.robot import Robot

from Primitives.Dance import Dance

window = Tk()
window.geometry("500x500")

robot = Robot()
dance = Dance()

# Global to stop all threads
stopThread = False


# Primitive Manager Thread
def update():
    while True:
        robot.PrimitiveManagerUpdate()
        global stopThread
        if stopThread:
            break;


# Dance Thread
def dance():
    robot.primitives.append(dance)
    while True:
        dance.armDance()
        time.sleep(1)
        global stopThread
        if stopThread:
            break;


# Setup the threads
t1 = Thread(target=update)
t2 = Thread(target=dance)


def stopAllThreads():
    global stopThread
    stopThread = True


# Functions for the buttons
def thread1Start():
    t1.start()


def thread1Start():
    t2.start()


# Make the buttons
b1 = Button(window, text="Shutdown", command=robot.shutdown(), activeforeground="red", activebackground="pink", padx=50,
            pady=50)
b2 = Button(window, text="PrimitiveManager", command=thread1Start(), activeforeground="blue", activebackground="pink",
            padx=50, pady=50)
b3 = Button(window, text="Dance", command=thread1Start(), activeforeground="green", activebackground="pink", padx=50,
            pady=50)
b4 = Button(window, text="StopAll", activeforeground="yellow", activebackground="pink", padx=50, pady=50)
b5 = Button(window, text="", activeforeground="yellow", activebackground="pink", padx=50, pady=50)

# Set button locations
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)
b5.pack(side=LEFT)

# loop window
window.mainloop()
