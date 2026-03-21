from bot.loader import bot
from telebot import types


@bot.message_handler()
def newword_handler(message: types.Message):
   # bot.send_message('Yangi so`z')
   if message