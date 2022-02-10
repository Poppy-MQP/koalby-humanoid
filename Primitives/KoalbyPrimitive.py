#
# 3 dicts - motors, sensors, externals
# need to be dicts of key and list of values
# get primitive attach primitive to robot add itself to robot primitive list
# also a remove primitive function
# timing method
import threading
from KoalbyHumanoid import config


class Primitive:

    def __init__(self, motorPositionsDict, sensors, isActive):
        self.motorPositionsDict = motorPositionsDict #list
        self.sensors = sensors #list
        self.isActive = isActive #boolean

    def timer(self, duration):
        timer = threading.Timer(duration, self.removeCommand)
        timer.start()  # after 'duration' seconds, 'removePrimitive' will be called

    def getCommand(self):
        return self.motorPositionsDict[0]

    def removeCommand(self):
        del self.motorPositionsDict[0]
