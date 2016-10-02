#/usr/bin/python3
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt  # plotting routine for python3
from time import sleep, strftime, time # this sets up delay, obtain current date and time for the information to CSV file
from subprocess import check_output
from re import findall # obtains the float value using regular expressions


# check temperature of Raspberry Pi
temp = check_output(["vcgencmd", "measure_temp"])
temp = temp.decode("UTF-8") # type of format to keyboard  .\d+ is one significant digit
temp = findall("\d+.\d+", temp) # searches for the number \d and by adding + puts the numbers together and . decimal equivalent
temp = temp[0]  # obtain the oth element in this list which means the first number in the list
temp = float(temp)   # converts the string to a floating point type variable

# written as a function call to Pi vcgencmd
# setup for plot function call
plt.ion()
x = []
y = []

""" 
Three fucnction calls for entire program
obtaining temperature information get_temp()
writing temperature information into a CSV file
graphing the temperature results against time of readings
"""

def get_temp():
    temp = check_output(["vcgencmd", "measure_temp"]).decode("UTF-8")
    temp = float(findall("\d+.\d+", temp)[0])
    return(temp)

"""
 creates a log file, cpu_temp, calls the function get_temp, 
 writes the retrieved data into two placeholders separated by a commain 
 in the described format with the second piece of informationn writted as a string
 last is the delay between capturing readings with sleep method
 """
def write_temp(temp):
    with open("cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))
       
def graph(temp):
    y.append(temp) # Y-axis is the temperature reading
    x.append(time()) # X-axis is the time of temperature reading
    plt.clf() # clears the plot area
    plt.scatter(x,y) # defines the plot as a scatter line type
    plt.plot(x,y) # begins the plot routine when data is retrieved
    plt.draw() # actually draws the graph
        
while True:
    temp = get_temp()
    write_temp(temp)
    graph(temp)
    sleep(10)

        
