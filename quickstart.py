
from __future__ import print_function

import datetime

from classes.GoogleCalendar import GoogleCalendar
from classes.MyClient import MyClient


def main():

    myClient = MyClient('client_secret.json', 'example')
    googleCalendar = GoogleCalendar(myClient)

    # googleCalendar.getLastNEvents(10)
    # googleCalendar.printEvents()

    # dt = datetime.datetime

    # dateFrom = dt.today().isoformat() + 'Z' #today
    # dateTo = (dt.today() + datetime.timedelta(1)).isoformat() + 'Z' #domani
    dateFrom = '2018-02-01'
    dateTo = '2018-03-10'
    print(dateFrom, dateTo)

    googleCalendar.getEventsFromDateToDate(dateFrom, dateTo)
    googleCalendar.printEvents()

if __name__ == '__main__':
    main()