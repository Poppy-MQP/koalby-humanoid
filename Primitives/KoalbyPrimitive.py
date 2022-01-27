#
# 3 dicts - motors, sensors, externals
# need to be dicts of key and list of values
# get primitive attach primitive to robot add itself to robot primitive list
# also a remove primitive function
# timing method
import threading


class Primitive:

    def __init__(self):
        motors = {}
        sensors = {}

        pass

    def attachPrimitive(self):
        pass

    def removePrimitive(self):
        pass

    def timer(self):
        timer = threading.Timer(60.0, self.callback)
        timer.start()  # after 60 seconds, 'callback' will be called

    def callback(self):
        pass