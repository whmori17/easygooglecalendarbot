from flask import Flask
from classes.CalendarBot import CalendarBot

calendarBot = CalendarBot()
calendarBot.run()
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/fromtoevents')
def getFromToEvents():
    calendarBot.fromtoevents()
    return 'ok'

@app.route('/todayevents')
def getTodayEvents():
    calendarBot.todayevents()

@app.route('/lastnevents')
def getLastEvents():
    calendarBot.lastnevents()

@app.route('/newevent')
def getNewEvent():
    calendarBot.newevent()

@app.route('/icsofevent')
def getIcsOfEvent():
    calendarBot.icsofevent()

@app.route('/csvevents')
def getCsvEvents():
    calendarBot.csvevents()

if __name__ == "__main__":
    app.run(host = '0.0.0.0')