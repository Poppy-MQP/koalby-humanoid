"""
Dance Primitive

    DanceToBeat()
        cause robot to move rythmically in response to a beats per minute (BPM) input
"""
import time

from Primitives import KoalbyPrimitive


class Idle(KoalbyPrimitive.Primitive):

    def __init__(self):
        super().__init__()  # inheritance
        self.motorPositionsDict = {3: 50,
                                   2: 50,
                                   1: 50,
                                   0: 50}

    def changePos(self):
        self.motorPositionsDict = {3: 0,
                                   2: 0,
                                   1: 0,
                                   0: 0}

