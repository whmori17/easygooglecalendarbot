from telegram.ext import Updater, CommandHandler

Updater.start_webhook(
    listen='0.0.0.0',
    port=8443,
    url_path='/easygooglecalendarbot/bot.py',
    key='private.key',
    cert='cert.pem',
    webhook_url='https://18.188.71.226:443/easygooglecalendarbot/example.py'
)