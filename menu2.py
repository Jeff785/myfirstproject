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


	def Module_create(self,module_type):
		y = "Low Current = L ",Slide-out =S ", "High Current = H ", "System Monitor = M ", "Blue tooth = B "
		selection_s = input("Select Module type: ")
		selection = str(selection_s)
		if selection == "L" :
			print("You want to create a low Current module")
			class Module_create_type :
		elif selection == "S" :
			print("You want to create a slide-out module")
			class Module_modify_type :
		elif selection == "H" :
			print("You want to create a high current module")
			class Module_open_type :
		elif selection == "M" :
			print("You want to create a system Monitor module")
			class Module_open_type :
		elif selection == "B" :
			print("You want to create a blue tooth module")
			class Module_open_type :
		else selection == "X" :
			print("Exiting Create New Module section of program")
			class Module_End :
	
def Module_create_type(self,module_type, position_num,module_name)
	
	return (module_type,position_num,module_name)
	
def Module_modify_type(self,module_type,position_num,module_config)

	return(module_type,position_num,module_config)

def Module_open(self,)
	
def Module_End(self) :
	print("G'Day Mate")
	return "G'Day Mate"


