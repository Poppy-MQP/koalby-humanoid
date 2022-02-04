import KoalbyPrimitive


class ArmMirror(KoalbyPrimitive.Primitive):

    def __init__(self, readMotors, writeMotors):
        self.readMotors = readMotors
        self.writeMotors = writeMotors

''' This function is wrong but idea is right
    def update(self):
        positions = []
        motorPosDict = {}
        
        for motor in self.readMotors:
            pos = motor.getPosition()
            positions.append(pos)
            
        for motor in self.writeMotors:
            motorPosDict[motor.motorID] = positions[0]
            positions.pop(0)

        return motorPosDict
'''
