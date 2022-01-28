"""
To be used for robot instantiation.
Possible functionalities:
    - call robot URDF body layout file and call kinematic and IK methods
    - set up config file and motor groupings
    - handle sensor layout set up
    - handle full robot-wide commands such as "shutdown"
"""
import ArduinoSerial
from KoalbyHumanoid.motor import Motor
from Kinematics.IK import IKChain
import KoalbyHumanoid.config as config


class Robot(object):

    def __init__(self):
        #self.arduino_serial = [] # Fake assignment for testing without robot.
        # If it reaches 'AttributeError: 'list' object has no attribute 'send_command'' Then test on robot
        self.arduino_serial = ArduinoSerial.ArduinoSerial()
        self.arduino_serial.send_command('1')  # This initializes the robot with all the initial motor positions

        self.motors = self.motorsInit()
        self.motorGroupsInit()

        # Change the tip later if needed
        self.l_arm_chain = IKChain.from_poppy_creature(self, motors=self.torso + self.l_arm, passiv=self.torso,
                                                       tip=[0, 0.18, 0])
        self.r_arm_chain = IKChain.from_poppy_creature(self, motors=self.torso + self.r_arm, passiv=self.torso,
                                                       tip=[0, 0.18, 0])
        self.l_leg_chain = IKChain.from_poppy_creature(self, motors=self.torso + self.l_leg, passiv=self.torso,
                                                       tip=[0, 0.18, 0])
        self.r_leg_chain = IKChain.from_poppy_creature(self, motors=self.torso + self.r_leg, passiv=self.torso,
                                                       tip=[0, 0.18, 0])

    def shutdown(self):
        """sends command to the arduino to shutdown all motors on the entire robot and turn their LEDs red"""
        cmdArr = [100]
        self.arduino_serial.send_command(cmdArr)

    def motorsInit(self):
        motors = list()
        for motorConfig in config.motors:
            motor = Motor(motorConfig[0], motorConfig[1], motorConfig[3], self.arduino_serial)
            setattr(Robot, motorConfig[3], motor)
            motors.append(motor)
        return motors

    def motorGroupsInit(self):
        i = 0
        for row in config.motorGroups:
            group = list()
            for row2 in row[1]:
                motor = Motor(row2[0], row2[1], row2[3], self.arduino_serial)
                group.append(motor)
            setattr(Robot, config.motorGroups[i][0], group)
            i += 1
