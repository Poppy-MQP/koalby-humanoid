import sys

from Primitives.ArmMirror import ArmMirror
from Primitives.Dance import Dance

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')
import time
from threading import Thread
from tkinter import *
from tkinter import messagebox
from KoalbyHumanoid.robot import Robot




robot = Robot()
dance = Dance()
armMirror = ArmMirror(robot.motors[0:3], robot.motors[4:7])
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
def dancing():
    while True:
        dance.armDance()
        time.sleep(1)
        global stopThread
        if stopThread:
            break;

#Arm Mirror Thread
def armMirrorMeth():
    while True:
        armMirror.armMirror()
        global stopThread
        if stopThread:
            break;


def init():
    robot.initialize()
    time.sleep(2)


def shut():
    robot.shutdown()
    global stopThread
    stopThread = True


primitiveThread = Thread(target=update)
primitiveThread.start()
danceThread = Thread(target=dancing)
armMirrorThread = Thread(target=armMirrorMeth)

def stopAll():
    global stopThread
    stopThread = True

window = Tk()
window.geometry("500x500")

# User Interface

# Make the buttons
b0 = Button(window, text="Stop All Threads", command=stopAll, activeforeground="red", activebackground="pink", padx=50, pady=25)
b1 = Button(window, text="Initialize", command=init, activeforeground="red", activebackground="pink", padx=25, pady=25)
b2 = Button(window, text="Shutdown", command=shut, activeforeground="green", activebackground="pink", padx=25, pady=25)
b3 = Button(window, text="Dance", command=danceThread.start, activeforeground="yellow", activebackground="pink", padx=25, pady=25)
b4 = Button(window, text="ArmMirror", command=armMirrorThread.start, activeforeground="blue", activebackground="pink", padx=25, pady=25)

# Set button locations
b0.place(x=175,y=425)
b1.place(x=0, y=0)
b2.place(x=150, y=0)
b3.place(x=300, y=0)
b4.place(x=0, y=150)
#b5.place(x=150, y=150)

# loop window
time.sleep(1)
window.mainloop()
