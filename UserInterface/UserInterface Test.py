import sys

from Primitives.ArmMirror import ArmMirror
from Primitives.Dance import Dance

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')
import time
from threading import Thread
from tkinter import *
from KoalbyHumanoid.robot import Robot

print("Start User Interface")
robot = Robot()
dance = Dance()

# armMirror = ArmMirror(robot.motors[0:3], robot.motors[4:7])
robot.primitives.append(dance)
# robot.primitives.append(armMirror)

# Global Boolean to stop all threads
runAll = True
danceFlag = False


# Initialize Method
def initMeth():
    print("Init")
    robot.initialize()


# Shutdown Method
def shutMeth():
    print("Shutdown")
    robot.shutdown()


# Primitive Manager Thread
def primitiveUpdateMeth():
    global runAll
    print("Primitive Manager Started")
    while True:
        if runAll:
            robot.PrimitiveManagerUpdate()

updateT = Thread(target=primitiveUpdateMeth)
updateT.start()


# Dance Thread
def danceMeth():
    print("Dancing Thread Started")
    global danceFlag
    while True:
        if runAll and danceFlag:
            dance.armDance()
            time.sleep(1)

def startDanceMeth():

    global danceFlag,runAll
    danceFlag = True
    runAll = True
def stopDanceMeth():

    global danceFlag,runAll
    danceFlag = False
    runAll = False

danceT = Thread(target=danceMeth)
danceT.start()

def armMirrorMeth():
    pass

armMirrorT = Thread(target=armMirrorMeth)


# User Interface

def uiupdate():
    window = Tk()
    window.geometry("1500x1080")

    # Make the buttons
    #b0 = Button(window, text="Stop All Threads and Shutdown", command=stop, activeforeground="red", activebackground="pink", padx=50, pady=25)
    b1 = Button(window, text="Initialize", command=initMeth, activeforeground="red", activebackground="pink", padx=25, pady=25)
    b2 = Button(window, text="Shutdown", command=shutMeth, activeforeground="green", activebackground="pink", padx=25, pady=25)
    b3 = Button(window, text="Start Dance", command=startDanceMeth, activeforeground="yellow", activebackground="pink", padx=25, pady=25)
    b4 = Button(window, text="ArmMirror", command=armMirrorT.start, activeforeground="blue", activebackground="pink", padx=25, pady=25)
    b5 = Button(window, text="Stop Dance", command=stopDanceMeth, activeforeground="blue", activebackground="pink", padx=25, pady=25)

    # Set button locations
    #b0.place(x=175, y=425)
    b1.place(x=0, y=0)
    b2.place(x=150, y=0)
    b3.place(x=300, y=0)
    b4.place(x=0, y=150)
    b5.place(x=150, y=150)

    while True:
        window.update()
        window.update_idletasks()


UIThread = Thread(target=uiupdate)
UIThread.start()

while True:
    pass

'''
# Arm Mirror Thread
def armMirrorMeth():
    print("ArmMirror")
    while True:
        armMirror.armMirror()
        global stopThread
        if stopThread:
            break;





armMirrorThread = Thread(target=armMirrorMeth)


def stopAll():
    global stopThread
    stopThread = True






while True:

'''
