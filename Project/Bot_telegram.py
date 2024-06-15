import telebot
import datetime

API_TOKEN = '7027295784:AAH4PYMknrBUq45HakpSxefGmMhZ1Tc6CH0'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    date = message.date
    date_string = datetime.datetime.fromtimestamp(date).strftime('%H:%M:%S %d-%m-%y')
    chatid = message.from_user.id
    bot.reply_to(message, '''
first name = {}
last name = {}                      
username = {}              
date = {}                 
chatid = {}   
'''.format(first_name, last_name, username, date_string, str(chatid)))

@bot.message_handler(commands=['kabar'])
def kabar(message):
    bot.reply_to(message, 'Bagaimana kabarmu hari ini??')

print('Bot is Running')
bot.polling()