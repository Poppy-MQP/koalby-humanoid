import csv
import KoalbyPrimitive
import time


class ReplayPrimitive(KoalbyPrimitive.Primitive):

    def __init__(self, leftArmGroup, rightArmGroup):
        super().__init__()  # inheritance
        self.motorPositionsDict = {}
        if str(input('Which arm would you like to control?:')) == 'left':
            self.masterArm = leftArmGroup
            self.followerArm = rightArmGroup
        else:
            self.masterArm = rightArmGroup
            self.followerArm = leftArmGroup
        for motor in self.masterArm:
            motor.compliantOnOff(1)

    def armMirror(self):
        masterPositions = list()
        for motor in self.masterArm:
            masterPositions.append(motor.getPosition)
        for rightMotor in self.followerArm:
            self.motorPositionsDict[rightMotor.motorID] = masterPositions[0]
            masterPositions.pop[0]