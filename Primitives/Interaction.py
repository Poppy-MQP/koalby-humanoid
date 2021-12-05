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