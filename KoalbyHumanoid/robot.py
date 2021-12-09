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
from Kinematics.CopiedIK import IKChain
import config



class Robot(object):

    def __init__(self):
        self.r_shoulder_x = Motor(0x01, [0, 100])  # This is made up. Change later
        self.motors = self.motorsInit()
        self.l_arm = self.motorGroupIniti(0)
        self.r_arm = self.motorGroupIniti(1)
        self.torso = self.motorGroupIniti(2)

        # Change these later
        self.l_arm_chain = IKChain.from_poppy_creature(self, motors=self.torso + self.l_arm, passiv=self.torso,
                                                       tip=[0, 0.18, 0])
        self.r_arm_chain = IKChain.from_poppy_creature(self, motors=self.torso + self.r_arm, passiv=self.torso,
                                                       tip=[0, 0.18, 0], reversed_motors=[self.r_shoulder_x])


    def shutdown(self):
        """sends command to the arduino to shutdown all motors on the entire robot and turn their LEDs red"""
        cmdArr = [100]
        ArduinoSerial.send_command(cmdArr)

    def motorsInit(self):
        motors = list()
        for motorConfig in config.motors:
            motor = Motor(motorConfig[0], motorConfig[1])
            motors.append(motor)
        return motors

    def motorGroupIniti(self, groupNumber):
        group = list()
        for motorConfig in config.Motorgroup[groupNumber]:
            motor = Motor(motorConfig[0], motorConfig[1])
            group.append(motor)
        return group
