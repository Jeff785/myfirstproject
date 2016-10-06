""" 
Remembe to run sudo pigpiod before launching program
"""
import pigpio
import DHT22
from time import sleep

#initiate GPIO
pi = pigpio.pi()
dht22 =DHT22.sensor(pi, 4)
dht22.trigger()
sleeptime = 300

def readDHT22():
	dht22.trigger()
	humidity = '%.2f' % (dht22.humidity())
	temp = '%.2f' % (dht22.temperature())
	return(humidity, temp)

while True :
	humidity, temperature = readDHT22()
	print("humidity is: " + humidity + "%")
	print("Temperature is: " + temperature + "C")
	sleep(sleeptime)
