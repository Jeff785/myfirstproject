import pigpio
import DHT22
import csv
import datetime
from flask import Flask, render_template
from time import sleep, time, strftime
#from datetime import datetime

#GPIO.setmode(GPIO.BCM)
pi = pigpio.pi()
dht22 = DHT22.sensor(pi,4)
dht22.trigger()
sleeptime = 30

def write_data_reads(t1):
    with open("gpiodata.txt",'a') as out_file:
        sep = '\n'
        t = str(t1)
        out_file.write(t + sep)
        out_file.close()
    return
    
def readDHT22():
    dht22.trigger()
    humidity = '%.2f' % (dht22.humidity())
    temperature = '%.2f' % (dht22.temperature())
    return(humidity, temperature)
# function call to read dHT22 sensor format

refresh = True # allows for updating the sensor_reads page on web at a reasonable interval

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M") # format str style output
    templateData = {
        'title' : 'Office conditions ar Hicks Place',
        'time' : timeString
        }
    return render_template('main.html', **templateData)

# this template pushes content to the URL / webpage using Flask
# requires generation of web pages as html in templates directory
# import files must be locatable by the main python program

@app.route("/sensor_reads/")
def data_task():
    humidity, temperature = readDHT22()
    now = datetime.datetime.now() # an instance then defined with method
    localtime = now.strftime("%m-%d-%Y %H:%M") # provides format for time and date
    t1 = localtime, humidity, temperature # create a list of variables
    write_data_reads(t1) # function for recording data sensor reads
    templateData = {
        'title' : 'Interior conditons @ Hicks Place',
        'time' : localtime,
        'humidity' : humidity,
        'temperature' : temperature
        }
    return render_template('sensor_reads.html', **templateData)
    sleep(sleeptime)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
