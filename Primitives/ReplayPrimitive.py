import KoalbyPrimitive
import time


class ArmMirror(KoalbyPrimitive.Primitive):

    def __init__(self, Motors):
        self.Motors = Motors
        self.recordedPoses = list()
        self.continueSelect = 0
        self.poseNum = 10
        self.poseFrequency = 0.001

    def recordMotion(self):
        poseMotorPositionsDict = {}  # create temporary dictionary of robot's current pose at time step 't'
        # TODO: make poseNum user input
        for poseIndex in range(self.poseNum):
            # TODO: make continueSelect user input
            while self.continueSelect != 0:
                for m in self.Motors:  # for each motor in Motors list
                    poseMotorPositionsDict[m.motorID].append(m.getPosition())  # add the motor ID as key and motor position as value
                self.recordedPoses.append(poseMotorPositionsDict)  # add dictionary of current robot pose to list of recorded poses
            self.continueSelect = 0

    def playMotion(self):
        # TODO: change poseFrequency to be a selectable value
        for poseMotorPositionsDict in self.recordedPoses:  # for each pose in the list of recorded poses
            for motorID in poseMotorPositionsDict:  # for each motor on the robot for that pose
                motorID.setPositionPos()  # set the motor's position to te recorded position at that time step
            time.sleep(self.poseFrequency)

