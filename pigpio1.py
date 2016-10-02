#!/user/bin/python3
import RPi.GPIO as GPIO
from RPi.GPIO import LED, Button
import time

chout1 = 2
chout2 = 3
chout3 = 4
chout4 = 5
chin1 = 6
chin2 = 7
chin3 = 8
chin4 = 8
standalone = 9
interlock = 10

GPIO.setmode(GPIO.BCM)  # set board to Broadcom
GPIO.setup(chout1, GPIO.OUT)    #Sets up input and Output channel assignments
GPIO.setup(chout2 GPIO.OUT)
GPIO.setup(chout3, GPIO.OUT)
GPIO.setup(chout4, GPIO.OUT)
GPIO.setup(chin1, GPIO.IN)
GPIO.setup(chin2, GPIO.IN)
GPIO.setup(chin3, GPIO.IN)
GPIO.setup(chin4, GPIO.IN)
#GPIO.setup(chin5, GPIO.IN)
#GPIO.setup(chin6, GPIO.IN)
#GPIO.setup(chin7, GPIO.IN)
#GPIO.setup(chin8, GPIO.IN)
GPIO.setup(standalone, GPIO.IN)
GPIO.setup(interlock, GPIO.Imodule_name = input("Enter name of module: ")

# Control to turn ON output channel
# GPIO.output(channel number, state) 1 is On, 0 is Off
# GPIO.input(channel number, state)

button = chin1
led = chout1

button.when_pressed = led.on
button.when_released = led.off

while True:
button.wait_for_press()
led.toggle()
