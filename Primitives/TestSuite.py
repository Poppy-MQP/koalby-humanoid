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
        m.goto_position(0, 2)

    # Left arm is compliant, right arm is active
    for m in koalby.l_arm:
        m.compliant = False

    for m in koalby.r_arm:
        m.compliant = False

    # The torso itself must not be compliant
    for m in koalby.torso:
        m.compliant = False

    target_delta = 3
    try:
        while True:
            follow_hand(koalby, target_delta)
            time.sleep(10)

    # Close properly the object when finished
    except KeyboardInterrupt:
        koalby.close()


def follow_hand(koalby, delta):
    """Tell the right hand to follow the left hand"""
    right_arm_position = koalby.l_arm_chain.end_effector + delta
    koalby.r_arm_chain.goto(right_arm_position, 0.5, wait=True)
