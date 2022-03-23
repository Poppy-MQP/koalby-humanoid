import sys

from Primitives.ArmMirror import ArmMirror

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')
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
armMirror = ArmMirror()
robot.primitives.append(dance)
robot.primitives.append(armMirror)

# Global Boolean to stop all threads
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
    while True:
        dance.armDance()
        time.sleep(1)
        global stopThread
        if stopThread:
            break;

#Arm Mirror Thread
def armMirror():
    while True:
        armMirror.armMirror()
        global stopThread
        if stopThread:
            break;


def init():
    robot.initialize()


def shut():
    robot.shutdown()
    global stopThread
    stopThread = True


primitiveThread = Thread(target=update)
primitiveThread.start()

danceThread = Thread(target=dance)
armMirrorThread = Thread(target=armMirror)

# User Interface

# Make the buttons
b1 = Button(window, text="Initialize", command=init, activeforeground="red", activebackground="pink", padx=25, pady=25)
b2 = Button(window, text="Shutdown", command=shut, activeforeground="green", activebackground="pink", padx=25, pady=25)
b3 = Button(window, text="Dance", command=danceThread.start, activeforeground="yellow", activebackground="pink", padx=25, pady=25)
b4 = Button(window, text="ArmMirror", command=armMirrorThread.start, activeforeground="blue", activebackground="pink", padx=25, pady=25)

# Set button locations
b1.place(x=0, y=0)
b2.place(x=150, y=0)
b3.place(x=300, y=0)
b4.place(x=450, y=0)

# loop window
window.mainloop()
