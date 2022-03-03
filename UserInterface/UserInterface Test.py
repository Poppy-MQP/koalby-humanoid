import sys
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
robot.primitives.append(dance)

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
    while True:
        dance.armDance()
        time.sleep(1)
        global stopThread
        if stopThread:
            break;

def init():
    robot.initialize()
    print("init")

def shut():
    robot.shutdown()
    print("shutdwon")

# Make the buttons
b1 = Button(window, text="Initialize", command=init, activeforeground="red", activebackground="pink", padx=25, pady=25)
b2 = Button(window, text="Shutdown", command=shut, activeforeground="green", activebackground="pink", padx=25, pady=25)
b3 = Button(window, text="Dance", activeforeground="yellow", activebackground="pink", padx=25, pady=25)

# Set button locations
b1.place(x=0, y=0)
b2.place(x=150, y=0)
b3.place(x=300, y=0)



# loop window
window.mainloop()

