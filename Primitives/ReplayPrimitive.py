import KoalbyPrimitive


class ArmMirror(KoalbyPrimitive.Primitive):

    def __init__(self, readMotors, writeMotors):
        self.readMotors = readMotors
        self.writeMotors = writeMotors
        self.recordedPoses = list()

    def recordMotion(self):
        poseMotorPositionsDict = {}  # create temporary dictionary of robot's current pose at time step 't'
        # TODO: set up predefined frequency of recording
        for m in self.readMotors:  # for each motor in readMotors list
            poseMotorPositionsDict[m.motorID].append(m.getPosition())  # add the motor ID as key and motor position as value
        self.recordedPoses.append(poseMotorPositionsDict)  # add dictionary of current robot pose to list of recorded poses

    def playMotion(self):
        # TODO: set up predefined frequency of recording
        for poseMotorPositionsDict in self.recordedPoses:  # for each pose in the list of recorded poses
            for motorID in poseMotorPositionsDict:  # for each motor on the robot for that pose
                motorID.setPositionPos()  # set the motor's position to te recorded position at that time step

