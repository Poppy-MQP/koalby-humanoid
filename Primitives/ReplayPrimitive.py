import csv
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
        with open(str("Input saved file name to play back:")) as f:
            csvRecordedPoses = [{k: int(v) for k, v in row.items()}
                                for row in csv.DictReader(f, skipinitialspace=True)]
        for poseMotorPositionsDict in csvRecordedPoses:  # for each pose in the list of recorded poses
            self.motorPositionsDict = poseMotorPositionsDict
            print("Play")
            print(self.motorPositionsDict)
            time.sleep(self.poseFrequency)

    def recordMotion(self):
        for m in self.Motors:
            m.compliantOnOff(1)

        for poseIndex in range(self.poseNum):
            poseMotorPositionsDict = {}
            self.continueSelect = int(input("prompt"))
            if self.continueSelect != 0:
                for m in self.Motors:  # for each motor in Motors list
                    poseMotorPositionsDict[m.motorID] = m.getPosition()  # add the motor ID as key and motor position as value
                self.recordedPoses.append(poseMotorPositionsDict)  # add dictionary of current robot pose to list of recorded poses
            self.continueSelect = 0
            time.sleep(0.01)
        motorIDHeaders = self.recordedPoses[0].keys()
        motionFile = open(str(input("Input saved file name:")), "w")
        dict_writer = csv.DictWriter(motionFile, motorIDHeaders)
        dict_writer.writeheader()
        dict_writer.writerows(self.recordedPoses)
        motionFile.close()
        for m in self.Motors:
            m.compliantOnOff(0)
