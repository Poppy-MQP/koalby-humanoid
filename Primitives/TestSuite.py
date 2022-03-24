import sys, os
import time
from threading import Thread

from Primitives.Dance import Dance

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')

from KoalbyHumanoid.robot import Robot
from threading import Thread

robot = Robot()
dance2 = Dance()
robot.primitives.append(dance2)


def update():
    while True:
        robot.PrimitiveManagerUpdate()


def dance():
    while True:
        dance2.armDance()
        time.sleep(1)


t1 = Thread(target=update)
t2 = Thread(target=dance)
t1.start()
t2.start()


while True:
    pass
