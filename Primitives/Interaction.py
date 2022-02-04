import time
import KoalbyHumanoid.robot as robot
"""
Interaction Primitive:
*** may break up into multiple primitives ***

    ArmMirror()
        allows user to move left arm such that the right arm copies the left arm motion

    ManualArmControlHold()
        allows user to move arms to positions and robot will then hold arm at those positions
        can then move arm again and robot will become compliant to do so

    ManualArmControlCopy()
        allows user to make a motion with the arms, the robot will then copy this motion in a loop until stopped
        example: user moves arm in a waving pattern, robot will then loop this wave until told to stop
"""

def ArmMirror():
    koalby = robot.Robot()
    for m in koalby.r_arm:
        m.torqueOnOff(0)

    try:
        while True:
            r_arm_angles = koalby.r_arm_chain.joints_position()
            print("Right arm: ",r_arm_angles)
            for m, pos in list(zip(koalby.l_arm_chain.motors, r_arm_angles)):
                m.setPositionTime(pos, 0.5)
            time.sleep(1)

    # Close properly the object when finished
    except KeyboardInterrupt:
        koalby.close()

# Ian Code. Temporary putting here
def arm_follow_test():
    koalby = robot.Robot()

    # Left arm is compliant, right arm is active
    '''for m in koalby.l_arm:
        m.torqueOnOff(1)'''

    for m in koalby.r_arm:
        m.torqueOnOff(0)

    # The torso itself must not be compliant
    '''for m in koalby.torso:
        m.torqueOnOff(1)'''

    target_delta = [0, 0.1, 0]
    try:
        while True:
            follow_hand(koalby, target_delta)
            time.sleep(1)

    # Close properly the object when finished
    except KeyboardInterrupt:
        koalby.close()


def follow_hand(koalby, delta):
    """Tell the left hand to follow the right hand"""
    left_arm_position = koalby.r_arm_chain.position() + delta
    koalby.l_arm_chain.goto(left_arm_position, 0.5, 0.5, wait=True)
