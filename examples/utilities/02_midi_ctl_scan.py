#!/usr/bin/env python
# encoding: utf-8
"""
Scan for Midi controller numbers. Launch this script from a terminal.

"""
from pyo import *
import time
import sys

if sys.version_info[0] < 3:
    input = raw_input    # if Python 2.x use a raw_input instead of an input

pm_list_devices()  # Prints a list of all devices found by Portmidi.

num = eval(input("Enter your Midi interface number: "))

ins = pm_get_input_devices()
print(f"selected ---> {ins[0][num]}\n")

s = Server(duplex=0)
s.setMidiInputDevice(num)  # open num device
s.boot().start()

print("Play with your Midi controllers...")

def pp(x):
    pass
    # print("controller number =", x)

scan = CtlScan(pp, True)   # Scan the Midi controller’s number in input.

again = "y"
while again == "y":
    time.sleep(10)
    scan.stop()
    again = input("Do you want to continue ? (y/n) : ")
    if again == "y":
        print("Continue...")
        scan.play()

s.stop()
time.sleep(1)
exit()
