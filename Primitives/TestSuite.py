import time
from KoalbyHumanoid.motor import Motor
from KoalbyHumanoid.robot import Robot

"""A simple test suite to check pi -> arduino communication and motor control"""

motor = Motor(0x01, -140)

print(motor.getPosition())
motor.setPositionPos(-90)
print(motor.getPosition())


# Ian Code. Temporary putting here
def arm_follow_test():
    koalby = Robot()
    for m in koalby.motors:
        m.setPositionTime(0, 2)
        # m.goto_position(0, 2)

    # Left arm is compliant, right arm is active
    for m in koalby.l_arm:
        m.torqueOnOff(0)

    for m in koalby.r_arm:
        m.torqueOnOff(1)

    # The torso itself must not be compliant
    for m in koalby.torso:
        m.torqueOnOff(1)

    target_delta = [0, 0.2, 0]
    try:
        while True:
            follow_hand(koalby, target_delta)
            time.sleep(10)

    # Close properly the object when finished
    except KeyboardInterrupt:
        koalby.close()


def follow_hand(koalby, delta):
    """Tell the left hand to follow the right hand"""
    left_arm_position = koalby.r_arm_chain.end_effector + delta
    koalby.l_arm_chain.goto(left_arm_position, 0.5, wait=True)

