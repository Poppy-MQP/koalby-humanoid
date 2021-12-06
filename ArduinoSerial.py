#!/usr/bin/env python3
import serial

'''
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
'''

class ArduinoSerial:

    def __init__(self):


    def send_command(self, command):
        ser = self.initialze_buffer()
        ser.write(b"Hello from Raspberry Pi!\n")

    def read_command(self):
        ser = self.initialze_buffer()
        line = ser.readline().decode('utf-8').rstrip()
        print(line)

    def initialze_buffer(self):
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.reset_input_buffer()
        return ser




