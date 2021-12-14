import time

import ArduinoSerial
from KoalbyHumanoid.motor import Motor
from KoalbyHumanoid.robot import Robot

"""A simple test suite to check pi -> arduino communication and motor control"""

'''
NEXT STEPS:
Move arduino_serial init from motor class to robot class.
Pass arduino serial from robot into motor as param.
Refactor command enums on arduino to avoid using 0 for init cmd and to allow for future additons to command list
'''

motor = Motor(0, [-3, 140])
time.sleep(10)
print(motor.getPosition())
motor.setPositionPos(50)
print(motor.getPosition())


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

