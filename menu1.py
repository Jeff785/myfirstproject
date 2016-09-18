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

class Module :
	if selection == "C" :
		print("You selected Create New Module")
		def Module_create :
	elif selection == "M" :
		print("You selected Modify Existing")
		def Module_modify :
	elif selection == "O" :
		print("You selected Open Existing")
		def Module_open :
	else selection == "X" :
		print("Exiting program")
		def Module_End :

	def Module_create() :
		print("You selected Create New Module")
		return
	def Module_modify() :
		print("You selected Modify Existing")
		return
	def Module_open() :
		print("You selected Open Existing")
		return
	def Module_End() :
		print("Exiting program")
		break

