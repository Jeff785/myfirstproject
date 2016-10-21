import pigpio
import DHT22
import csv
import datetime
from flask import Flask, render_template
from time import sleep, time, strftime
from datetime import datetime

#GPIO.setmode(GPIO.BCM)
pi = pigpio.pi()
dht22 = DHT22.sensor(pi,4)
dht22.trigger()
sleeptime = 30


def readDHT22():
    dht22.trigger()
    humidity = '%.2f' % (dht22.humidity())
    temp = '%.2f' % (dht22.temperature())
    return(humidity, temperature)

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
       'title' : 'Office Sensor Readings',
       'time' : timeString
       }
    return render_template('main.html', **templateData)
@app.route("/sensor_reads/")
def sensor_reads():
#    while True :
        sleep(sleeptime)        
        humidity, temperature = readDHT22()
        localtime = now.strftime("%m-%d-%Y %H:%M")
        sensor_dht22 = ["localtime", "humidity", "temperature"]
#        sleep(sleeptime)
        templateData = {
            'title' : 'Office conditons ar Hicks Place',
            'Current date and time is ' : localtime,
            'Humidity is' : humidity,
            'Temperature is' : temperature
            }
        return render_template('sensor_reads.html', **templateData)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
