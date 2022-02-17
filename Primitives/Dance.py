"""
Dance Primitive

    DanceToBeat()
        cause robot to move rythmically in response to a beats per minute (BPM) input
"""
import time

from Primitives import KoalbyPrimitive


class Dance(KoalbyPrimitive.Primitive):

    def __init__(self):
        super().__init__() # inheritance
        self.motorPositionsDict = {7: 5,
                                   0: 10,
                                   1: 15,
                                   2: 20}
