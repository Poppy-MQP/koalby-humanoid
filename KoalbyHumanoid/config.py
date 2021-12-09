#!/usr/bin/env python3
from array import *
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

motors = [
    [0x01, 'Herk', 'Right Forearm'],
    [0x02, 'Herk', 'Right Upper Shoulder'],
    [0x03, 'Herk', 'Right Arm Connector'],
    [0x0F, 'Herk', 'Right Shoulder'],

    [0x0B, 'Herk', 'Left Forearm'],
    [0x0A, 'Herk', 'Left Upper Shoulder'],
    [0x06, 'Herk', 'Left Arm Connector'],
    [0x07, 'Herk', 'Left Shoulder'],

    [0x11, 'Herk', 'Torso Double Rotation Back'],
    [0x12, 'Herk', 'Torso Double Rotation Front'],
    [0x13, 'Herk', 'Abdomen']

]


motorGroups = [
    ['Right Arm', motors[0:4]],
    ['Left Arm', motors[4:8]],
    ['Chest', motors[8:11]],
]


