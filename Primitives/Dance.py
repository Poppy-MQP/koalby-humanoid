"""
Dance Primitive

    DanceToBeat()
        cause robot to move rythmically in response to a beats per minute (BPM) input
"""
import random
import threading
import time

from KoalbyHumanoid.config import motors
from Primitives import KoalbyPrimitive


class Dance(KoalbyPrimitive.Primitive):

    def __init__(self):
        super().__init__()  # inheritance
        self.motorPositionsDict = {}
        self.isActive = True

    def robotdance(self):
        if self.isActive:
            self.timer(1)
        else:
            pass

    def armDance(self):
        self.motorPositionsDict = {}  # Clear the dictionary
        for index in range(0, 4):  # Set depth to run in config file (0-4 is right arm motors)
            motorID = motors[index][0]  # Get motor ID
            motorPos = random.randrange(0, 100, 25)  # Generate random positons between 0 and 100
            self.motorPositionsDict[motorID] = motorPos  # add position to dictionary

    def timer(self, duration):
        timer = threading.Timer(duration,self.armDance())
        timer.start()  # after 'duration' seconds, 'removePrimitive' will be called
