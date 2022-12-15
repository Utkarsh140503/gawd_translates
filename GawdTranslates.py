from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('2084329551:AAHRgI2CV3Ls3yVoq-VfcMbL5uSrrdacpRA',use_context = True )

def start(updater,context):
 updater.message.reply_text("Hi there!\nThis is the Gawd Translator.\nI am not that old and I am still learning so I only know English to other languages translation.\nPlease bear with me. I'll get stronger soon :) ")
 

def echo(updater,context):
 
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='hi') 
 updater.message.reply_text(translation.text)

 
dp=updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()