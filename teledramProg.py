import telegram
import os
import random
import message
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler, updater
import handler_setup

if __name__ == "__main__":
    updater = Updater(os.environ.get('TELEGRAM-TOKEN'))
    dp = updater.dispatcher
    handler_setup.handlers_setup(dp)
    updater.start_polling()
