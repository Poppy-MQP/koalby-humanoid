"""
Dance Primitive

    DanceToBeat()
        cause robot to move rythmically in response to a beats per minute (BPM) input
"""
import time

from Primitives.KoalbyPrimitive import Primitive

motorPositionDict = [
    [0x07, 50],
    [0x05, 100],
    [0x04, 120],
    [0x03, 20],
    [0x02, 40],
    [0x01, 0],
    [0x11, 15],
    [0x12, 13],
    [0x13, 14],
    [0x07, 243],
]

sensors = [
    # list of sensor commands

]
Dance2 = Primitive(motorPositionDict, 0, False)


def getCommand():
    return Dance2.getCommand()


def timer(time):
    return Dance2.timer(time)


def removeCommand():
    Dance2.removeCommand()
