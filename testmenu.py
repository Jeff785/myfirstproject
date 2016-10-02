#!/usr/bin/python3
import RPi.GPIO as GPIO
import time




#GPIO.setmode(GPIO.BCM)
#GPIO.setup(variablename,GPIO.IN)
#GPIO.input(pin#, True)
#GPIO.output(pin#, False)

# Print statement asking for what you want to do.
# Create new , Modify Existing , or Open existing file for Road Commmander config
#
# Make this into an actual module for creating new module configruation?
# Select type of module, LC, HC, SO, SM (M), BT
# module position number, id number between 1 to 32 inclusive per module type
# define number of inputs, channel 1 thru 8
# define polarity of input, H/L -side
# define position id of the target module
# define the output channel on target for control
# define type of action for the outptu channel - momentary or latching
# number of outputs, channel 1 thru 4
#

print(" Select from the following module types:")
print(" Low Current = L, High Current = H, Slide-out = S, System Monitor = M, Blue tooth = B, Exit program = X")
selection = input()
y = selection
print("You selected module type: ", y)
# Determines branching and atributes for the module type
if y == "L" :
	Module_type = "Low Current"
        print("Enter the position number, range between 1 and 32: ")
        t = input()
        idnum_s = t
	id = int(idnum_s)
	if id in range (1, 32) : {
		idnum.append(id\n)	# Opportunity to test for duplicate id number assignments
		print("Used position numbers: ",idnum)
		Module_id = id
		}
	Module_name = input("Enter distinct module name, 6 characters max: ")
	print(Module_type\n, id\n, "Module name is ",Module_name)
	m = "No"
		while m == "No" or "no" : # To continue inputting channel input assignments
	chinput_num_s = input("Enter channel input assignment: ")
	chinput = int(chinput_num_s)
		if chinput in range (1,8): {
#			chinput_num_s = input("Enter channel input assignment: ")
			chinput_num = int(chinput_num_s)
			chinput.append(chinput_num)
			print("Configured Input Channels: ",chinput) # test for duplicate input channel assignments
#
# 	polarity is H/L -side, idpositiontarget is targeted module Id position number,
#	outputchanneltarget is output channel number, outputtarget-type is latching or momentary]
#
			input_type(self, polarity, idpositiontarget, outputchanneltarget, outputtarget_type) :
			print("Done with configuring input channels?")
			m = input("Enter Yes or No")
#				While m == "No" or "no" :
		continue 	# if m = Yes, then branches out of while loop
			}
	print(module_type\n, id\n, Module_name\n, chinput)	# Prints last ch inpt number, may require chinput()?
	m = "no"
		while m == "No" or "no" :
	choutput_num_s = input("Enter channel input assignment: ")
	choutput = int(choutput_num_s)
			if choutput in range (1,4): {
#				choutput_num_s = input("Enter channel input assignment: ")
				choutput_num = int(choutput_num_s)
				choutput.append(choutput_num)
				print("Configured Output Channels: ",choutput)
				print("Done with configuring output channels?")
				m = input("Enter Yes or No")
		continue	# if m = Yes, then branches out of while loop
			}
	print(module_type\n, id\n, Module_name\n, chinput\n, choutput)

# check to see if looping is correct and how would you see the entire configuration thus far fro input and output
		# end of If-Elif-Else loop for module class configuration of the Low Current Module

#	Begin If-Elif_Else loop for module class configuration of the High Current Module
#	elif y == "H" : {
#		Module_type = "High Current"

#	}
#	elif y == "S" : {
#		Module_type = "Slide-out"

#	}
#	elif y == "M" : {
#		Module_type = "System Monitor"

#	}
#	elif y == "B" : {
#		Module_type = "Blue tooth"

#	}
else:
	y == "X" :
	print("That's all folks")
	module_end :

def input_type(self, polarity, idpositiontarget, outputchanneltarget, outputtarget_type) :
		pass
#				self.polarity

		print("Done with configuring input channels?")
		m = input("Enter Yes or No")
		return(polarity, idpositiontarget, outputchanneltarget, outputtarget_type)

# End point for first set of If-elseif-else
def module_end() :
	return
