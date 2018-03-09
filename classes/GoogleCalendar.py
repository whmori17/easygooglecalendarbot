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
        self.events = {}

    def getLastNEvents(self, n):
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        message = f"Getting the upcoming {n} events"
        print(message)
        eventsResult = self.service.events().list(
            calendarId='primary', timeMin=now, maxResults=n, singleEvents=True,
            orderBy='startTime').execute()
        self.events = eventsResult.get('items', [])

    def printEvents(self):
        if not self.events:
            print('No upcoming events found.')
        for event in self.events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])