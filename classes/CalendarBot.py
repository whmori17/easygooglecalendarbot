from pprint import pprint

import os
import telepot
from telepot.loop import MessageLoop


class CalendarBot:

    def __init__(self):
        file = open(os.getcwd() + '/token', 'r')
        self.token = file.read()
        self.bot = telepot.Bot(self.token)

    def run(self):
        MessageLoop(self.bot, self.handle).run_as_thread()

    def handle(self, message):
        methodName = message['text'].replace('/','')
        chatId = message['chat']['id']
        try:
            getattr(self, methodName)(chatId)
        except AttributeError:
            raise NotImplementedError(
                f"Class {self.__class__.__name__} does not implement {methodName}")

    def fromtoevents(self, id):
        self.bot.sendMessage(id, f"fromtoevents{id}")
    def todayevents(self, id):
        self.bot.sendMessage(id, 'todayevents')
    def lastnevents(self, id):
        self.bot.sendMessage(id, 'lastnevents')
    def newevent(self, id):
        self.bot.sendMessage(id, 'newevent')
    def icsofevent(self, id):
        self.bot.sendMessage(id, 'icsofevent')
    def csvevents(self, id):
        self.bot.sendMessage(id, 'csvevents')
