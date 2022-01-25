import time

import ArduinoSerial
from KoalbyHumanoid.motor import Motor
from KoalbyHumanoid.robot import Robot
import Primitives.Interaction as Interaction

"""A simple test suite to check pi -> arduino communication and motor control"""

'''
NEXT STEPS:
'''


Interaction.arm_follow_test()
'''
robot = Robot()
motor = Motor(4, [-3, 140], "dummy_name", robot.arduino_serial)

time.sleep(3)
print(motor.getPosition())
motor.setPositionPos(50)
time.sleep(3)
print(motor.getPosition())'''


