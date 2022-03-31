import sys

from Primitives.ArmMirror import ArmMirror
from Primitives.Dance import Dance
from Primitives.ReplayPrimitive import ReplayPrimitive

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')
import time
from threading import Thread
from tkinter import *
from KoalbyHumanoid.robot import Robot

# Start Script
print("Start User Interface")
b1, b2, b3, b4, b5, b6, b7, b8, b9, b10 = Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button()  # create Buttons
robot = Robot()
dance = Dance()
replay = ReplayPrimitive(robot.motors)
armMirror = ArmMirror(robot.motors[0:3], robot.motors[4:7])  # Arm Mirror created with left and right arm motor groups


# Add primitives to robot primitive list
# robot.primitives.append(dance)
# robot.primitives.append(armMirror)
# robot.primitives.append(replay)

def init():
    for prim in robot.primitives:
        prim.notActive()
    robot.primitives.clear()
    robot.initialize()


def shutdown():
    for prim in robot.primitives:
        prim.notActive()
    robot.primitives.clear()
    robot.shutdown()


# Primitive Manager Thread
def primitiveUpdateMeth():
    print("Primitive Manager Thread Started")
    while True:
        if dance.isActive or armMirror.isActive or replay.isActive:
            robot.PrimitiveManagerUpdate()


# Start Primitive Manager Thread
primitiveUpdateT = Thread(target=primitiveUpdateMeth)
primitiveUpdateT.start()


# Dance Thread
def danceMeth():
    print("Dancing Thread Started")
    while True:
        if dance.isActive:
            robot.poseTimeMillis = 1000
            dance.armDance()
            time.sleep(1)


def danceSetup():
    if dance.isActive:
        robot.removePrimitive(dance)
        dance.isActive = False
        b3.config(bg="red")
    else:
        robot.addPrimitive(dance)
        dance.isActive = True
        b3.config(bg="green")


# Start Dance Thread
danceT = Thread(target=danceMeth)
danceT.start()


# Arm Mirror Thread
def armMirrorMeth():
    print("Arm Mirror Thread Started")
    while True:
        if armMirror.isActive:
            armMirror.armMirror()


def armMirrorSetup():
    if armMirror.isActive:
        robot.removePrimitive(armMirror)
        armMirror.isActive = False
        b4.config(bg="red")
    else:
        robot.addPrimitive(armMirror)
        armMirror.isActive = True
        b4.config(bg="green")


# Start Arm Mirror Thread
armMirrorT = Thread(target=armMirrorMeth)
armMirrorT.start()


# Replay Thread
def replayMeth():
    print("Replay Thread Started")
    while True:
        if replay.isActive:
            replay.playMotion()


def replaySetup(posTime, posDelay, filename):
    replay.poseTime = posTime + 0.005
    replay.poseDelay = posDelay
    robot.poseTimeMillis = int((replay.poseTime - 0.005) * 1000)
    replay.replayFilename = filename

    if replay.isActive:
        robot.removePrimitive(replay)
        replay.isActive = False
        b5.config(bg="red")
        b6.config(bg="red")
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        b10.config(bg="red")

    else:
        robot.addPrimitive(replay)
        replay.isActive = True


# Clap 0.2 0.1, Dab 0.1 0, Macerena 0.5 0.2, Shake 0.2 0 , Extend 0.5 0, Wave 0.3 0
def clap():
    replaySetup(0.5, 0.5, "clapCycle")
    b5.config(bg="green")


def dab():
    replaySetup(0.3, 0.5, "dab")
    b6.config(bg="green")


def macarena():
    replaySetup(0.5, 1, "macarena")
    b7.config(bg="green")


def shake():
    replaySetup(0.2, 0.5, "shakeRightHand")
    b10.config(bg="green")


def extend():
    replaySetup(0.5, 0.5, "extendRightArm")
    b9.config(bg="green")


def wave():
    replaySetup(0.3, 0.5, "wave")
    b8.config(bg="green")


# Start Replay Thread
replayT = Thread(target=replayMeth)
replayT.start()


# User Interface

def UI():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10
    window = Tk()
    window.geometry("800x500")

    # Make the buttons
    b1 = Button(window, text="Initialize", command=init, activeforeground="black", activebackground="pink", padx=25, pady=25)
    b2 = Button(window, text="Shutdown", command=shutdown, activeforeground="black", activebackground="pink", padx=25, pady=25)
    b3 = Button(window, text="Dance Toggle", command=danceSetup, activeforeground="black", activebackground="pink", padx=25, pady=25)
    b4 = Button(window, text="Mirror Toggle", command=armMirrorSetup, activeforeground="black", activebackground="pink", padx=25, pady=25)

    # Clap 0.2 0.1, Dab 0.1 0, Macerena 0.5 0.2, Shake 0.2 0 , Extend 0.5 0, Wave 0.3 0
    b5 = Button(window, text="Clap Toggle", command=clap, activeforeground="black", activebackground="pink", padx=25, pady=25)
    b6 = Button(window, text="Dab Toggle", command=dab, activeforeground="black", activebackground="pink", padx=25, pady=25)
    b7 = Button(window, text="Macarena Toggle", command=macarena, activeforeground="black", activebackground="pink", padx=25, pady=25)
    b8 = Button(window, text="Wave Toggle", command=wave, activeforeground="black", activebackground="pink", padx=25, pady=25)
    b9 = Button(window, text="Extend Toggle", command=extend, activeforeground="black", activebackground="pink", padx=25, pady=25)
    b10 = Button(window, text="Shake Toggle", command=shake, activeforeground="black", activebackground="pink", padx=25, pady=25)

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


# Start UI Thread
UIThread = Thread(target=UI)
UIThread.start()

while True:
    pass
