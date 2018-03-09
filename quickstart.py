
from __future__ import print_function

from classes.GoogleCalendar import GoogleCalendar
from classes.MyClient import MyClient


def main():

    myClient = MyClient('client_secret.json', 'example')
    googleCalendar = GoogleCalendar(myClient)

    googleCalendar.getLastNEvents(10)
    googleCalendar.printEvents()

if __name__ == '__main__':
    main()