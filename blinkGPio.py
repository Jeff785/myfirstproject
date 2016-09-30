#!?usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # denotes I/O channel number, not physical pin
GPIO.setup(2, GPIO.IN)
GPIO.setup(6, GPIO.OUT)


GPIO.output(6,0) # outputs may be set to ON or OFF
GPIO.input(2) # input are read as logical values 

test = GPIO.input(2)

while test == True:
    GPIO.output(6,1)
    sleep(2)
    GPIO.output(6,0)
    sleep(2)
    test = GPIO.input(2)
    print("inside IF loop and executing")

GPIO.output(6,0)
print("Exiting porgram")
GPIO.cleanup()

