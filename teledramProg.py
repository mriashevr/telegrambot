import os

import telegram
import random
import message
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler, updater
import handler_setup

words_check_application = ("заявку", "заявка", "заявки", "анкета", "анкеты", "анкету", "тест", "тесты", "теста", "обучение", "обучения", "форма", "форму", "волонтер", "волонтером", "волонтеры", "волонтерство")
words_check_video = ("видео")


if __name__ == "__main__":
    updater = Updater(os.environ.get('TELEGRAM-TOKEN'))
    dp = updater.dispatcher
    handler_setup.handlers_setup(dp)
    updater.start_polling()
