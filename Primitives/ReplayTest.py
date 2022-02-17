import sys, os

from Primitives.Dance import Dance
from Primitives.Idle import Idle
from Primitives.ReplayPrimitive import ReplayPrimitive

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')
import time

import ArduinoSerial
from KoalbyHumanoid.motor import Motor
from KoalbyHumanoid.robot import Robot
import Primitives.Interaction as Interaction

"""A simple test suite to check pi -> arduino communication and motor control"""

'''
NEXT STEPS:
'''

robot = Robot()
replay = ReplayPrimitive(robot.motors)
replay.recordMotion()
robot.primitives.append(replay)
replay.playMotion()
while 1:
    robot.PrimitiveManagerUpdate()
