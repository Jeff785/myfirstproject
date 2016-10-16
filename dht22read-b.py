""" 
Remembe to run sudo pigpiod before launching program
"""
import pigpio
import DHT22
import csv
from time import sleep, time, strftime
from datetime import datetime

#initiate GPIO
pi = pigpio.pi()
dht22 =DHT22.sensor(pi, 4)
dht22.trigger()
sleeptime = 30   #300

#opens files for data generated from pi
data_file = open('data_file.csv', 'a')
mywriter = csv.writer(data_file)
#creates the CSV write object

def readDHT22():
	dht22.trigger()
	humidity = '%.2f' % (dht22.humidity())
	temp = '%.2f' % (dht22.temperature())
	return(humidity, temp)

while True :
	humidity, temperature = readDHT22()
	localtime = str(datetime.now())
	data_file = open('new_notes.txt', 'a')
	print("humidity is: " + humidity + "%")
	data_file = mywriter.writerow(humidity)
	print("Temperature is: " + temperature + "C")
	data_file = mywriter.writerow(temperature)
	print("Local date and time is: ", localtime)
	data_file = mywriter.writerow(localtime)
#	print >> data_file, ([humidity\ttemperature\tlocaltime\n])
	sleep(sleeptime)
mew_notes.close()
