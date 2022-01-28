import KoalbyPrimitive
from KoalbyHumanoid import motor


class ArmMirror(KoalbyPrimitive):

    def __init__(self, readMotors, writeMotors):
        self.readMotors = readMotors
        self.writeMotors = writeMotors

    def update(self):
        positions = []
        for motor in self.readMotors:
            pos = motor.getPosition()
            positions.append(pos)
        for motor in self.writeMotors:
            motor.setPositionPos(positions[0])
            positions.remove(positions[0])
