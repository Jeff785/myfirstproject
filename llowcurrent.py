#!/user/bin/python3
import RPi.GPIO as GPIO
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

GPIO.setmode()
GPIO.setup(chout1, GPIO.OUT)
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
					N)

z_s = input("Setup of new module 'Y' or 'N' :,")
	if z_s == "Y" :
			module_type = input("Select type of Module, 'L' for low current, 'B' for Bluetooth, 'S' for Slide-out, 'H' for High Current, 'M' for System Monitor")
				if module_type == "L" : {
					print("LC module selected") 
					module_name = input("Enter name of module: ")
					}
				elif module_type == "S" : {
					print("Slide-out module selected")
					module_name = input("Enter name of module: ")
					}
				elif module_type == "B" : {
					print("bluetooth module selected")
					module_name = input("Enter name of module: ")
					}
				elif module_type == "H" : {
					print("Hig current module selected")
					module_name = input("Enter name of module: ")
					}
				elif module_type == "M" : {
					print("System Monitor module selected")
					module_name = input("Enter name of module: ")
					}
				else module_type == '' : 
				
				