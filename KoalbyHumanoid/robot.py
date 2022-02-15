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
from collections import defaultdict


class Robot(object):

    def __init__(self):
        self.primitives = []
        self.primitiveMotorDict = {}
        #self.motors = [Motor(7,2,0), Motor(16,2,0)]
        #self.motors = self.motorsInit()
    """
        self.arduino_serial = ArduinoSerial.ArduinoSerial()
        self.arduino_serial.send_command('1')

        

       
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

    def updateMotors(self):
        '''
        Take the primitiveMotorDict and send the motor values to the robot
        '''
        for key,value in self.primitiveMotorDict.items():
            for motor in self.motors:
                if str(motor.motorID) == str(key):
                    motor.setPositionPos(self.primitiveMotorDict[key])


    def PrimitiveManagerUpdate(self):
        '''
        Take list of active primitives which will come from UI
        Look at motor Dict from primitives.
        All primitive update functions need to have a dict of motor IDs and setPositions
        '''

        # If there is only 1 primitive in active list, return primitive's dictionary
        if len(self.primitives) == 1:
            print("TRUE")
            return self.primitives[0].getMotorDict()

        #
        primitiveDicts = []
        for primitive in self.primitives:
            print("Get Dictionary")
            print(primitive.getMotorDict())
            primitiveDicts.append(primitive.getMotorDict())  # Add primitive dictionary to primitiveDicts

        # create new dictionary with 1 key value and a list of motor positions
        mergedDict = defaultdict(list) # Create a default list dictionary empty.
        for dict in primitiveDicts:
            for key, value in dict.items():
                mergedDict[key].append(value)

        # for each key average motor positions and return key value with the average value
        for key, value in mergedDict.items():
            finalMotorValue = 0
            for motorValue in mergedDict[key]:
                finalMotorValue = motorValue + finalMotorValue
            self.primitiveMotorDict[key] = finalMotorValue/len(mergedDict[key]) # average values

        print("Final")
        print(self.primitiveMotorDict)

        self.updateMotors() # send new dict to motors

        return self.primitiveMotorDict
