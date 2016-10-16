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

#creates the CSV write object

def readDHT22():
    dht22.trigger()
    humidity = '%.2f' % (dht22.humidity())
    temp = '%.2f' % (dht22.temperature())
    return(humidity, temp)

def write_data_reads(t1):
        with open("gpiodata.txt", 'a') as out_file:
                sep = '\n'
                t1 = str(t1)
                out_file.write(t1 + sep)
                out_file.close()
        return

def write_data_log(t):
        with open("gpiodata.csv", 'a') as out_file:
                sep = '\n'
                localtime = str(datetime.now())
                t = localtime, temperature, humidity
                t = str(t)
                out_file.write(t + sep)
                out_file.close()
        return

end_prog = ""

while True :
        humidity, temperature = readDHT22()
        localtime = str(datetime.now())
        t = temperature, humidity
        t1 = localtime, temperature, humidity
        write_data_reads(t1)
        write_data_log(t)
        print("humidity is: " + humidity + "%")
        print("Temperature is: " + temperature + "C")
        print("Local date and time is: ", localtime)
        sleep(sleeptime)
        if end_prog == "q" :
                end_prog = input("Type q to quit")
                break
print("Closing files")
