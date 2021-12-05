from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler, updater, \
    CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from actions import *
from textProceed import *


def handlers_setup(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, fromHandlerToFunction))
    dp.add_handler(CallbackQueryHandler(callback=keyboard_callback_handler))
    #dp.add_handler(MessageHandler(Filters.voice, fromHandlerToFunction))
    return dp