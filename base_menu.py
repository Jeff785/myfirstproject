#!/usr/bin/python3
import RPi.GPIO as GPIO
import time




#GPIO.setmode(GPIO.BCM)
#GPIO.setup(variablename,GPIO.IN)
#GPIO.input(pin#, True)
#GPIO.output(pin#, False)

selection = input("What do you want to do?"\n)
t = "Create New = C", "Modify Existing = M", "Open Existing = O"
print(" Please input selection: \n", t)
