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


def send_command(command):
    ser = initialize_buffer()
    ser.write(str.encode(command))


def read_command():
    ser = initialize_buffer()
#    ser2 = serial.Serial('/dev/tty.usbmodem14201', 115200, timeout=1)
    line = ser.readline().decode('utf-8').rstrip()
 #   line2 = ser2.readline().decode('utf-8').rstrip()
    return line


def initialize_buffer():
    ser = serial.Serial('/dev/tty.usbserial-1410', 115200, timeout=1)
    ser.reset_input_buffer()
    return ser
