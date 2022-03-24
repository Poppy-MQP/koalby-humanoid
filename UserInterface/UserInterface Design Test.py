import sys
from threading import Thread

from KoalbyHumanoid.robot import Robot
from Primitives.Dance import Dance

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')
from tkinter import *

window = Tk()
window.geometry("500x500")
robot = Robot()
dance = Dance()
stopThread = False

def update():
    while True:
        global stopThread
        if not stopThread:
            pass
            #print("Update")

# Dance Thread
def dance():
    while True:
        global stopThread
        if not stopThread:
            print("Dance")

#Arm Mirror Thread
def armMirror():
    while True:
        global stopThread
        if not stopThread:
            print("Mirror")


def init():
    robot.initialize()
    print("Init")
    pass


def shut():
    robot.shutdown()
    print("Shutdown")
    pass



danceThread = Thread(target=dance)
armMirrorThread = Thread(target=armMirror)

def stopAll():
    global stopThread
    stopThread = True
    danceThread.join()
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
window.mainloop()
