"""
Dance Primitive

    DanceToBeat()
        cause robot to move rythmically in response to a beats per minute (BPM) input
"""
import random
import time

from KoalbyHumanoid.config import motors
from Primitives import KoalbyPrimitive


class Dance(KoalbyPrimitive.Primitive):

    def __init__(self):
        super().__init__()  # inheritance
        self.motorPositionsDict = {}

    def armDance(self):
        self.motorPositionsDict = {} # Clear the dictionary
        for index in range(0,4): # Set depth to run in config file (0-4 is right arm motors)
            motorID = motors[index][0] # Get motor ID
            motorPos = random.randint(0, 100) # Generate random positons between 0 and 100
            self.motorPositionsDict[motorID] = motorPos # add position to dictionary
