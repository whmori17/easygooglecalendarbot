import datetime

import httplib2
from apiclient import discovery

from classes.Authentication import Authentication


class GoogleCalendar:

    def __init__(self, myClient):
        self.auth = Authentication()
        self.credentials = self.auth.getCredentials(myClient)
        self.http = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http=self.http)
        self.maxEvents = 1000
        self.dt = datetime.datetime

    def getLastNEvents(self, n):
        return self.extractNEventsByPeriod(n)

    def getEventsFromDateToDate(self, dateFrom, dateTo):
        return self.extractNEventsByPeriod(self.maxEvents, dateFrom, dateTo)

    def extractNEventsByPeriod(self, n=1000, dateFrom=None, dateTo=None):
        dateFrom = self.cleanStringDate(dateFrom)
        dateTo = self.cleanStringDate(dateTo)

        message = self.getCorrectMessage(dateFrom, dateTo, n)
        print(message)

        eventsResult = self.service.events().list(
            calendarId='primary', timeMin=dateFrom, timeMax=dateTo, maxResults=n, singleEvents=True,
            orderBy='startTime').execute()
        return eventsResult.get('items', [])

    def getCorrectMessage(self, dateFrom, dateTo, n):
        message = ''
        if n != 1000:
            message += f"Getting the upcoming {n} events"
        else:
            message += f"Getting the upcoming events"
        if dateFrom != None and dateTo != None:
            message += f" between {dateFrom} and {dateTo}"

        return message

    def cleanStringDate(self, date):
        if type(date) is str:
            date = self.dt.strptime(date, '%Y-%m-%d').isoformat() + 'Z'
        return date

    def printEvents(self, events):
        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])