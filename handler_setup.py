from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler, updater
from actions import *


def handlers_setup(dp):
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.regex(r'(заявк[а-я])') | Filters.regex(r'(анкет[а-я])'), get_question))
    dp.add_handler(MessageHandler(Filters.regex(r'(виде[а-я])'), get_information_about_video))
    return dp