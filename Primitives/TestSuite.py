from KoalbyHumanoid.motor import Motor

"""A simple test suite to check pi -> arduino communication and motor control"""

motor = Motor(0x01, -140)

print(motor.getPosition())
motor.setPositionPos(-90)
print(motor.getPosition())
