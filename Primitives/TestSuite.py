
import sys, os

from Primitives.Idle import Dance2

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')
import time

import ArduinoSerial
from KoalbyHumanoid.motor import Motor
from KoalbyHumanoid.robot import Robot
import Dance

"""A simple test suite to check pi -> arduino communication and motor control"""

'''
NEXT STEPS:
'''

robot = Robot()

robot.primitives.append(Dance)
Dance.isActive = True
robot.primitives.append(Dance2)
Dance2.isActive = True
for i in range(0,2):
    robot.PrimitiveManagerUpdate()
    i=i+1


# # Ian Code. Temporary putting here
# def arm_follow_test():
#     koalby = Robot()
#     for m in koalby.motors:
#         m.goto_position(0, 2)
#
#     # Left arm is compliant, right arm is active
#     for m in koalby.l_arm:
#         m.compliant = False
#
#     for m in koalby.r_arm:
#         m.compliant = False
#
#     # The torso itself must not be compliant
#     for m in koalby.torso:
#         m.compliant = False
#
#     target_delta = 3
#     try:
#         while True:
#             follow_hand(koalby, target_delta)
#             time.sleep(10)
#
#     # Close properly the object when finished
#     except KeyboardInterrupt:
#         koalby.close()
#
#
# def follow_hand(koalby, delta):
#     """Tell the right hand to follow the left hand"""
#     right_arm_position = koalby.l_arm_chain.end_effector + delta
#     koalby.r_arm_chain.goto(right_arm_position, 0.5, wait=True)

