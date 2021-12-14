import ArduinoSerial
#import config

"""The Motor class hold all information for an abstract motor on the physical robot. It is used to interface with the
arduino which directly controls the motors"""


class Motor(object):

    def __init__(self, _motorID, angleLimit):
        self.motorID = _motorID
        self.angle_limit = angleLimit
        self.present_position = self.getPosition()

    def getPosition(self):
        """reads the motor's current position from the arduino and returns the value in degrees"""
        idArr = [1, self.motorID]
        ArduinoSerial.send_command(','.join(map(str,idArr)))
        print("here")
        currentPosition = ArduinoSerial.read_command()
        return currentPosition

    def setPositionPos(self, position):
        """sends a desired motor position to the arduino"""
        idPosArr = [2, self.motorID, position]

        ArduinoSerial.send_command(','.join(map(str,idPosArr)))
        print(ArduinoSerial.read_command())

    def setPositionTime(self, position, time):
        """sends a desired motor position to the arduino <to be executed in a set amount of time?>"""
        idPosTimeArr = [3, self.motorID, position, time]
        ArduinoSerial.send_command(','.join(map(str, idPosTimeArr)))

    def torqueOnOff(self, toggle):
        """turns the torque of a motor on or off based on a 1 or 0 input and sends this to the arduino"""
        idBoolArr = [5, self.motorID, toggle]
        ArduinoSerial.send_command(idBoolArr)
