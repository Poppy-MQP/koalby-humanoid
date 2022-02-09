"""
Dance Primitive

    DanceToBeat()
        cause robot to move rythmically in response to a beats per minute (BPM) input
"""
from Primitives.KoalbyPrimitive import Primitive

motorPositionDict = [
    [0x07, 25],
    [0x05, 50],
    [0x04, 60],
    [0x03, 10],
    [0x02, 20],
    [0x01, 152],
    [0x11, 125],
    [0x12, 123],
    [0x13, 12],
    [0x07, 213],
]


sensors = [
    #list of sensor commands

]
Dance = Primitive(motorPositionDict,sensors ,False)
