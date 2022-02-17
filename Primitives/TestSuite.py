import sys, os
import time
from threading import Thread



from Primitives.Dance import Dance

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')

from KoalbyHumanoid.robot import Robot
from threading import Thread

"""A simple test suite to check pi -> arduino communication and motor control"""

'''
NEXT STEPS:
'''

robot = Robot()
dance = Dance()
robot.primitives.append(dance)

def Update():
    while True:
        robot.PrimitiveManagerUpdate()

def Dance():
    while True:
        dance.armDance()
        time.sleep(1)

t1 = Thread(target=Update)
t2 = Thread(target=Dance)
t1.start()
t2.start()

while True:
    pass
