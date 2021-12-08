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
    ser.write(command + "\n").encode('utf-8')


def read_command():
    ser = initialize_buffer()
    line = ser.readline().decode('utf-8').rstrip()
    return line


def initialize_buffer():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    return ser
