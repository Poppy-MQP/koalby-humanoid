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
    [3, [0, 0], 'Herk', 'r_shoulder_y'],
    [2, [0, 0], 'Herk', 'r_shoulder_x'],
    [1, [0, 0], 'Herk', 'r_arm_z'],
    [0, [0,0], 'Herk', 'r_elbow_y'],

    # Left Arm
    [7, [0,0], 'Herk', 'l_shoulder_y'],
    [6, [0,0], 'Herk', 'l_shoulder_x'],
    [5, [0,0], 'Herk', 'l_arm_z'],
    [4, [0, 0], 'Herk', 'l_elbow_y'],

    # Torso
    [21, [0, 0], 'Dyn', 'abs_y'],
    [22, [0, 0], 'Dyn', 'abs_x'],
    [10, [0,0], 'Herk', 'abs_z'],
    [9, [0,0], 'Herk', 'bust_y'],
    [8, [0,0], 'Herk', 'bust_x'],

    # Right Leg
    [16, [0,0], 'Herk', 'r_hip_x'],
    [17, [0,0], 'Herk', 'r_hip_z'],
    [18, [0,0], 'Herk', 'r_hip_y'],
    [19, [0,0], 'Dyn', 'r_knee_y'],
    [20, [0,0], 'Herk', 'r_ankle_y'],

    # Left Leg
    [11, [0,0], 'Herk', 'l_hip_x'],
    [12, [0,0], 'Herk', 'l_hip_z'],
    [13, [0,0], 'Dyn', 'l_hip_y'],
    [14, [0,0], 'Herk', 'l_knee_y'],
    [15, [0,0], 'Herk', 'l_ankle_y'],

    # Head
    [23, [0, 0], 'Dyn', 'head_z'],
    [24, [0, 0], 'Dyn', 'head_y']
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




