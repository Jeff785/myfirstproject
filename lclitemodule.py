""" Module is intended to test the following aspects of the attached module
Module address for uniqueness, no repeats by variable idnum and will set a variable once the number
or address is verified.

  """


#!/usr/bin/python3

## Initialize variables
##

lc1 = False
lc2 = False
lc3 = False
lc4 = False
lc5 = False

# Beginning of construct for object group
class lcmodule:

	def address(self):
		if self.idnum == 1 :	# test to see if address entered is valid within range and acceptable
			print("good idnum", self.idnum)
			lc1 = True	#set a flag for assignment of idnumbers in LC class
		elif self.idnum == 2 :
			print("good idnum", self.idnum)
			lc2 = True
		elif self.idnum == 3 :
			print("good idnum", self.idnum)
			lc3 = True
		elif self.idnum == 4 :
			print("good idnum", self.idnum)
			lc4 = True	
		elif self.idnum > 4 :
			print("Out of range idnum", self.idnum)
			lc5 = True	
			self.idnum = "invalid range"	# test to see if idnum is invalid

	def logicalbuttonpressed(self):
		if self.logicalbuttonpressed == "On" : {
			print(" the app button has been pressed", mylcmodule.logicalbuttonpressed)
			}
				self.logicalbuttonpressed = "Off"
				
	def physicalchanneloutput(self):
		if self.physicalchanneloutput == range(1,2,3,4): {
			print("Physical channel output is", mylcmodule.physicalchanneloutput)
			}
				self.physicalchanneloutput = "Off"

	def physicalchanneloutputstate(self) :
		if self.physicalchanneloutputstate == "On"
			self.physicalchanneloutputstate = "Off"
				
	def logicalchannelinput(self) : {
		if self.logicalchannelinput == 1 :{
			print(" logical channel input is valid", mylcmodule.logicalchannelinput)
			}
				self.logicalchannelinput = "Invalid channel assignment"

mylcmodule = lcmodule()
mylcmodule.idnum = 1
mylcmodule.logicalbuttonpressed = "On"
mylcmodule.logicalchannelinput = 1
mylcmodule.physicalchanneloutput = 1

# test execution of module
print("my lc module address is", mylcmodule.idnum)
print("a logical channel is ", mylcmodule.logicalbuttonpressed)
print("my logical channel input is ", mylcmodule.logicalchannelinput)
print("my physical channel output address is", mylcmodule.pyhsicalchanneloutput)
print("my physical channel output is",mylcmodule.physicalchanneloutputstate)
print("Let's change the state of the output")
print
mylcmodule.physicalchanneloutputstate()
mylcmodule.logicalbuttonpressed()
mylcmodule.address() # Trips the value to a new setting for address
print("my physical output channel is", mylcmodule.physcalchanneloutputstate)
print("my lc module address is", mylcmodule.idnum)
print("a logical channel is ", mylcmodule.logicalbuttonpressed)
