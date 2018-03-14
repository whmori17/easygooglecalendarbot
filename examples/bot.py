from classes.CalendarBot import CalendarBot

file = open('token', 'r')
token = file.read(file)

calendarBot = CalendarBot(token)
calendarBot.run()