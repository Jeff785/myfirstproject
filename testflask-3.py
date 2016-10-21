import pigpio
import DHT22
import csv
import datetime
from flask import Flask, render_template
from time import sleep, time, strftime
#from datetime import datetime

#GPIO.setmode(GPIO.BCM)
#pi = pigpio.pi()
#dht22 = DHT22.sensor(pi,4)
#dht22.trigger()
#sleeptime = 30

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'Office conditions ar Hicks Place',
        'time' : timeString
        }
    return render_template('main.html', **templateData)
    
@app.route("/sensor_reads/")
def task():
"""
def readDHT22():
    dht22.trigger()
    humidity = '%.2f' % (dht22.humidity())
    temperature = '%.2f' % (dht22.temperature())
    return(humidity, temperature)
    sleep(sleeptime)
"""
#    humidity, temperature = readDHT22()
     localtime = now.strftime("%m-%d-%Y %H:%M")
#    sensor_dht22 = ["localtime", "humidity", "temperature"]
     temperature = 18.3
     humidity = 54
     templateData = {
        'title' : 'Interior Office conditons @ Hicks Place',
        'time' : localtime,
        'humidity' : humidity,
        'temperature' : temperature
        }
     return render_template('sensor_reads.html', **templateData)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
