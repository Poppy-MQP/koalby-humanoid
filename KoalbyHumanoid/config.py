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
    # Right Arm
    [0x0F, [0, 0], 'Herk', 'r_shoulder_y'],
    [0x03, [0, 0], 'Herk', 'r_shoulder_x'],
    [0x02, [0, 0], 'Herk', 'r_arm_z'],
    [0x01, [0,0], 'Herk', 'r_elbow_y'],

    # Left Arm
    [0x07, [0,0], 'Herk', 'l_shoulder_y'],
    [0x06, [0,0], 'Herk', 'l_shoulder_x'],
    [0x0A, [0,0], 'Herk', 'l_arm_z'],
    [0x0B, [0, 0], 'Herk', 'l_elbow_y'],

    # Torso
    [0x12, [0, 0], 'Herk', 'abs_y'],
    [0x11, [0, 0], 'Herk', 'abs_x'],
    [0x13, [0,0], 'Herk', 'abs_z'],
    [0x12, [0,0], 'Herk', 'bust_y'],
    [0x11, [0,0], 'Herk', 'bust_x'],

    # Right Leg
    [0x14, [0,0], 'Herk', 'r_hip_x'],
    [0x15, [0,0], 'Herk', 'r_hip_z'],
    [0x14, [0,0], 'Herk', 'r_hip_y'],
    [0x15, [0,0], 'Herk', 'r_knee_y'],
    [0x15, [0,0], 'Herk', 'r_ankle_y'],

    # Left Leg
    [0x14, [0,0], 'Herk', 'l_hip_x'],
    [0x15, [0,0], 'Herk', 'l_hip_z'],
    [0x14, [0,0], 'Herk', 'l_hip_y'],
    [0x15, [0,0], 'Herk', 'l_knee_y'],
    [0x15, [0,0], 'Herk', 'l_ankle_y'],

    # Head
    [0x14, [0, 0], 'Herk', 'head_z'],
    [0x15, [0, 0], 'Herk', 'head_y']
]

''' Array of all motor groups for Koalby.'''
motorGroups = [
    ['r_arm', motors[0:4]],
    ['l_arm', motors[4:8]],
    ['torso', motors[8:13]],
    ['r_leg', motors[13:18]],
    ['l_leg', motors[18:23]],
    ['head', motors[23:25]]
]




