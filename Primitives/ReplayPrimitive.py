import KoalbyPrimitive
import time


class ReplayPrimitive(KoalbyPrimitive.Primitive):

    def __init__(self, motors):
        super().__init__()  # inheritance

        self.Motors = motors
        self.recordedPoses = list()
        self.continueSelect = 0
        self.poseNum = int(input("Input number of poses desired:"))
        self.poseFrequency = float(input("Select pose time:"))
        self.motorPositionsDict = {}

    def playMotion(self):
        for m in self.Motors:
            m.compliantOnOff(0)
        for poseMotorPositionsDict in self.recordedPoses:  # for each pose in the list of recorded poses
            self.motorPositionsDict = poseMotorPositionsDict
            time.sleep(self.poseFrequency)

    def recordMotion(self):
        poseMotorPositionsDict = {}
        for m in self.Motors:
            m.compliantOnOff(1)
        for poseIndex in range(self.poseNum):
            self.continueSelect = int(input("prompt"))
            if self.continueSelect != 0:
                for m in self.Motors:  # for each motor in Motors list
                    poseMotorPositionsDict[m.motorID] = (m.getPosition())  # add the motor ID as key and motor position as value
                self.recordedPoses.append(poseMotorPositionsDict)  # add dictionary of current robot pose to list of recorded poses
            self.continueSelect = 0
            print(self.recordedPoses)
            time.sleep(0.01)
