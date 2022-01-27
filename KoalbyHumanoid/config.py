#!/usr/bin/env python3
'''
Motor 1 - Herkulex, Right Forearm
Motor 2 - Herkulex, Right Upper Arm
Motor 3 - Herkulex, Right Arm Connector
Motor F - Herkulex, Right Shoulder

Motor B - Herkulex, Left Forearm
Motor A - Herkulex, Right Upper Arm
Motor 6 - Herkulex, Right Arm Connector
Motor 7 - Herkulex, Right Shoulder

Motor 11 - Herkulex, Torso Double Rotation Backside
Motor 12 - Herkulex, Torso Double Rotation Frontside
Motor 13 - Herkluex, Abdomen
'''


'''Array of all motors for Koalby.'''
motors = [
    [0x0F, [0, 0], 'Herk', 'r_shoulder_y'],
    [0x03, [0, 0], 'Herk', 'r_shoulder_x'],
    [0x02, [0, 0], 'Herk', 'r_arm_z'],
    [0x01, [0,0], 'Herk', 'r_elbow_y'],

    [0x07, [0,0], 'Herk', 'l_shoulder_y'],
    [0x06, [0,0], 'Herk', 'l_shoulder_x'],
    [0x0A, [0,0], 'Herk', 'l_arm_z'],
    [0x0B, [0, 0], 'Herk', 'l_elbow_y'],

    [0x11, [0,0], 'Herk', 'bust_x'],
    [0x12, [0,0], 'Herk', 'bust_y'],
    [0x13, [0,0], 'Herk', 'abs_z']

]

''' Array of all motor groups for Koalby.'''
motorGroups = [
    ['Right Arm', motors[0:4]],
    ['Left Arm', motors[4:8]],
    ['Chest', motors[8:11]],
]




