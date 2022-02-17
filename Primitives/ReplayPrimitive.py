import KoalbyPrimitive
import time


class ReplayPrimitive(KoalbyPrimitive.Primitive):

    def __init__(self, Motors):
        super().__init__()  # inheritance

        self.Motors = Motors
        self.recordedPoses = list()
        self.continueSelect = 0
        self.poseNum = int(input("Input number of poses desired:"))
        self.poseFrequency = float(input("Select pose time:"))
        self.motorPositionsDict = {}

    def playMotion(self):
        for poseMotorPositionsDict in self.recordedPoses:  # for each pose in the list of recorded poses
            for motorID in poseMotorPositionsDict:  # for each motor on the robot for that pose
                motorID.setPositionPos(poseMotorPositionsDict[
                                           motorID])  # set the motor's position to the recorded position at that time step
            time.sleep(self.poseFrequency)

    def recordMotion(self):
        for poseIndex in range(self.poseNum):
            self.continueSelect = int(input("prompt"))
            while self.continueSelect != 0:
                for m in self.Motors:  # for each motor in Motors list
                    self.motorPositionsDict[m.motorID].append(m.getPosition())  # add the motor ID as key and motor position as value
                self.recordedPoses.append(self.motorPositionsDict)  # add dictionary of current robot pose to list of recorded poses
            self.continueSelect = 0
            print(self.recordedPoses)
            time.sleep(0.01)
