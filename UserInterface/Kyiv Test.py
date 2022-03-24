

# import kivy module
import kivy
kivy.require("1.9.1")
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button


import sys, os
import time
from threading import Thread

from Primitives.Dance import Dance

sys.path.insert(0, '/home/pi/Documents/koalby-humanoid')

from KoalbyHumanoid.robot import Robot
from threading import Thread

robot = Robot()
dance2 = Dance()
robot.primitives.append(dance2)


def update():
    while True:
        robot.PrimitiveManagerUpdate()


def dance():
    while True:
        dance2.armDance()
        time.sleep(1)


t1 = Thread(target=update)
t2 = Thread(target=dance)
t1.start()


# class in which we are creating the button
class ButtonApp(App):

    def build(self):
        # use a (r, g, b, a) tuple
        btn = Button(text="Push Me !",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(300, 250))

        # bind() use to bind the button to function callback
        btn.bind(on_press=self.callback)
        return btn

    # callback function tells when button pressed
    def callback(self, event):
        dance()


# creating the object root for ButtonApp() class
root = ButtonApp()
root.run()