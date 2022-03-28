import time

from KoalbyHumanoid.robot import Robot
from threading import Thread

from Primitives.ArmMirror import ArmMirror

robot = Robot()
#robot.shutdown()
# robot.arduino_serial.send_command('1,')
armFollow = ArmMirror() #TODO: insert arm groups
robot.primitives.append(armFollow)


def update():
    while True:
        robot.PrimitiveManagerUpdate()


def arm_Follow():
    while True:
        armFollow.armMirror()
        time.sleep(1)


t1 = Thread(target=update)
t2 = Thread(target=arm_Follow)
t1.start()
t2.start()

while True:
    pass
