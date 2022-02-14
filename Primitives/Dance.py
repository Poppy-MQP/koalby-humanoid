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
        self.motorPositionsDict = {0x07: 5,
                                   0x10: 10,
                                   0x11: 15,
                                   0x12: 20}
