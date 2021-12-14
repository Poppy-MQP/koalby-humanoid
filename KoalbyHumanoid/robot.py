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
        self.arduino_serial = ArduinoSerial.ArduinoSerial()
        self.arduino_serial.send_command('1')

        self.motors = self.motorsInit()
        self.l_arm = self.motorGroupsInit(0)
        self.r_arm = self.motorGroupsInit(1)
        self.torso = self.motorGroupsInit(2)

        # Change these later
        self.l_arm_chain = IKChain.from_poppy_creature(self, motors=self.torso + self.l_arm, passiv=self.torso,
                                                       tip=[0, 0.18, 0])
        self.r_arm_chain = IKChain.from_poppy_creature(self, motors=self.torso + self.r_arm, passiv=self.torso,
                                                       tip=[0, 0.18, 0])

    def shutdown(self):
        """sends command to the arduino to shutdown all motors on the entire robot and turn their LEDs red"""
        cmdArr = [100]
        self.arduino_serial.send_command(cmdArr)

    def motorsInit(self):
        motors = list()
        for motorConfig in config.motors:
            motor = Motor(motorConfig[0], motorConfig[1], self.arduino_serial)
            motors.append(motor)
        return motors

    def motorGroupsInit(self, groupNumber):
        group = list()
        for motorConfig in config.motorGroups[groupNumber]:
            motor = Motor(motorConfig[0], motorConfig[1], self.arduino_serial)
            group.append(motor)
        return group
