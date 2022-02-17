import sys, os
from datetime import time
from threading import Thread

from Primitives.ReplayPrimitive import ReplayPrimitive

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')

from KoalbyHumanoid.robot import Robot

"""A simple test suite to check pi -> arduino communication and motor control"""

'''
NEXT STEPS:
'''

robot = Robot()
replay = ReplayPrimitive(robot.motors)
replay.recordMotion()
robot.primitives.append(replay)


def Play():
    while True:
        replay.playMotion()

def Update():
    while True:
        robot.PrimitiveManagerUpdate()

t1 = Thread(target=Update)
t2 = Thread(target=Play)
t1.start()
t2.start()

while True:
    pass

