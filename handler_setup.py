from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler, updater
from actions import *
from textProceed import *


def handlers_setup(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, fromHandlerToFunction))
    return dp