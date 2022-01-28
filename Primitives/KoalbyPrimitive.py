#
# 3 dicts - motors, sensors, externals
# need to be dicts of key and list of values
# get primitive attach primitive to robot add itself to robot primitive list
# also a remove primitive function
# timing method
import threading
from KoalbyHumanoid import config

class Primitive:

    def __init__(self):
        motors = []
        sensors = []

    def attachPrimitive(self):
        pass

    def removePrimitive(self):
        pass

    def timer(self, duration):
        timer = threading.Timer(duration, self.removePrimitive)
        timer.start()  # after 60 seconds, 'removePrimitive' will be called

