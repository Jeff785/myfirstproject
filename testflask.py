from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%m-%d-%Y %H:%M")
    templateData = {
       'title' : 'Office Sensor Readings',
       'time' : timeString
       }
    return render_template('main.html', **templateData)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
