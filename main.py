
import telebot

bot = telebot.TeleBot("5698088306:AAEvKMetal9oAzISOHqt4MYbn13A5tpfdhU")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()