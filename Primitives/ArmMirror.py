import csv
import KoalbyPrimitive
import time


class ArmMirror(KoalbyPrimitive.Primitive):

    def __init__(self, leftArmGroup, rightArmGroup):
        super().__init__()  # inheritance
        self.motorPositionsDict = {}
        if str(input('Which arm would you like to control?:')) == 'left':  # set controller arm and follower arm
            self.masterArm = leftArmGroup
            self.followerArm = rightArmGroup
        else:
            self.masterArm = rightArmGroup
            self.followerArm = leftArmGroup
        for motor in self.masterArm:  # set desired controller arm to be compliant for manual control
            motor.compliantOnOff(1)

    def armMirror(self):
        masterPositions = list()
        for motor in self.masterArm:  # log motor positions of controller arm
            masterPositions.append(motor.getPosition)
        for motor in self.followerArm:  # set motors in follower arm to positions of controller arm
            self.motorPositionsDict[motor.motorID] = masterPositions[0]  # add motor pos to motor dict sent to robot
            masterPositions.pop(0)
