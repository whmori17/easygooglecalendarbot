#GoogleTelegramBot - Requisiti

##Introduzione
GoogleCalendarBot è un telegram bot sviluppato in Python che utilizza le Api Google di Calendar

##Obiettivi
CalendarBot si propone di offrire agli utenti una facile interfaccia, via chatbot, per ottenere informazioni relative alla propria agenda personale, in modo semplice, rapido e veloce.

###Come
Mediante l’uso di semplici domande e comandi

##Funzionalità
L’iterazione col bot permette di reperire le informazioni sui seguenti eventi:
* Giornalieri
* Data specifica
* Settimana corrente
* Mese corrente
* Mese specifico
* Periodo specifico

Il bot permette anche di:
* Creare eventi
* Scaricare il csv degli eventi di un periodo specifico
* Scaricare l’ics di un evento specifico
* Scaricare l’ics di ‘n’ eventi specifici

##Nomi funzioni
* description - Description of the bot
* fromtoevents - Get events between from to dates
* todayevents - Get today events
* lastnevents - Get the last n events
* newevent - Create a new event
* icsofevent - Get the ics file of a event
* csvevents - Get the csv files of last events