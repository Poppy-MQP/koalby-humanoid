import KoalbyPrimitive
import time


class ReplayPrimitive(KoalbyPrimitive.Primitive):

    def __init__(self, Motors):
        super().__init__()  # inheritance

        self.Motors = Motors
        self.recordedPoses = list()
        self.continueSelect = 0
        self.poseNum = 10
        self.poseFrequency = 0.001

        self.motorPositionsDict = {}

    def recordMotion(self):
        self.motorPositionsDict = {}  # create temporary dictionary of robot's current pose at time step 't'
        # TODO: make poseNum user input
        for poseIndex in range(self.poseNum):
            # TODO: make continueSelect user input
            self.continueSelect = 0
            while self.continueSelect < 10:
                for m in self.Motors:  # for each motor in Motors list
                    self.motorPositionsDict[m.motorID].append(m.getPosition())  # add the motor ID as key and motor position as value
                self.recordedPoses.append(self.motorPositionsDict)  # add dictionary of current robot pose to list of recorded poses
            self.continueSelect = self.continueSelect + 1
            print(self.recordedPoses)
            time.sleep(0.01)

    def playMotion(self):
        # TODO: change poseFrequency to be a selectable value
        for poseMotorPositionsDict in self.recordedPoses:  # for each pose in the list of recorded poses
            for motorID in poseMotorPositionsDict:  # for each motor on the robot for that pose
                motorID.setPositionPos(poseMotorPositionsDict[
                                           motorID])  # set the motor's position to the recorded position at that time step
            time.sleep(self.poseFrequency)
