"""
To be used for robot instantiation.
Possible functionalities:
    - call robot URDF body layout file and call kinematic and IK methods
    - set up config file and motor groupings
    - handle sensor layout set up
    - handle full robot-wide commands such as "shutdown"
"""
import ArduinoSerial


class Robot(object):

    def __init__(self):
        pass

    def shutdown(self):
        """sends command to the arduino to shutdown all motors on the entire robot and turn their LEDs red"""
        cmdArr = [100]
        ArduinoSerial.send_command(cmdArr)
