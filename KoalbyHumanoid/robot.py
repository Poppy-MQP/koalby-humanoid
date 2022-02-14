"""
To be used for robot instantiation.
Possible functionalities:
    - call robot URDF body layout file and call kinematic and IK methods
    - set up config file and motor groupingsx
    - handle sensor layout set up
    - handle full robot-wide commands such as "shutdown"
"""
import sys, os

import self as self

from Primitives.KoalbyPrimitive import Primitive
from Primitives import Dance

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')
import ArduinoSerial
from KoalbyHumanoid.motor import Motor
from Kinematics.CopiedIK import IKChain
import KoalbyHumanoid.config as config


class Robot(object):

    def __init__(self):
        self.primitives = []

    """
        self.arduino_serial = ArduinoSerial.ArduinoSerial()
        self.arduino_serial.send_command('1')

        self.motorPositionsDict = {}

        self.motors = self.motorsInit()
        self.l_arm = self.motorGroupsInit(0)
        self.r_arm = self.motorGroupsInit(1)
        self.torso = self.motorGroupsInit(2)

        # Change these later
        # Currently commented out to allow for motor testing without errors
        self.l_arm_chain = IKChain.from_poppy_creature(self, motors=self.torso + self.l_arm, passiv=self.torso,
                                                       tip=[0, 0.18, 0])
        self.r_arm_chain = IKChain.from_poppy_creature(self, motors=self.torso + self.r_arm, passiv=self.torso,
                                                       tip=[0, 0.18, 0])
    """

    def shutdown(self):
        """sends command to the arduino to shutdown all motors on the entire robot and turn their LEDs red"""
        cmdArr = [100]

        self.arduino_serial.send_command(cmdArr)

    def motorsInit(self):
        motors = list()
        for motorConfig in config.motors:
            motor = Motor(motorConfig[0], motorConfig[1], self.arduino_serial)
            motors.append(motor)
        return motors

    def motorGroupsInit(self, groupNumber):
        group = list()
        for motorConfig in config.motorGroups[groupNumber]:
            motor = Motor(motorConfig[0], motorConfig[1], self.arduino_serial)
            group.append(motor)
        return group

    def PrimitiveManagerUpdate(self):
        '''
        Take list of active primitives which will come from UI
        Look at motor commands from primitives.
        All primitive update functions need to return a dict of motor IDs and setPositions
        '''

        # From user interface

        motorPositionsNew = []
        for primitive in self.primitives:
            print("Get")
            print(primitive.getCommand()) # Get motor position and id
            motorPositionsNew.append(primitive.getCommand()) # add id to new motor positions list.
            primitive.removeCommand() # remote command from the primitive motor dictionary
            # primitive.timer(0.00001) #will remove the command after timer ends

        print("New")
        print(motorPositionsNew)
        if len(motorPositionsNew) == 1:
            return motorPositionsNew # if there is only 1 motor command in the list of primitives it will only return the 1st one


        finalMotorPositions = []
        for m1 in range(0, len(motorPositionsNew)): #for every motor command in motor positions new
            for m2 in range(m1 + 1, len(motorPositionsNew)): # for every next motor command in motor positions new
                if motorPositionsNew[m1][0] == motorPositionsNew[m2][0]: # if the  motor m1 and next motor m2 are the same id
                    m3 = [motorPositionsNew[m1][0], int((motorPositionsNew[m1][1] + motorPositionsNew[m2][1]) / 2)] # average the motor command and create new command
                    finalMotorPositions.append(m3) #add m3 to new list of motor positions
                else:
                    finalMotorPositions.append(motorPositionsNew[m1]) # add m1 to the new list of motor positions (not modified)

        print("Final")
        print(finalMotorPositions)
        return finalMotorPositions



'''
        for motor in range(0, len(duplicates)):
            for motorNext in range(motor+1, len(duplicates)):
                if duplicates[motor] == duplicates[motorNext]:
'''
