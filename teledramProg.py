import telegram
import random
import message
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler, updater

token = '5056349584:AAEmz0Stk_CrOHyAEA8jeYij2E36qOf3aR4'
updater = Updater(token=token)


words_check_application = ("заявку", "заявка", "заявки", "анкета", "анкеты", "анкету", "тест", "тесты", "теста", "обучение", "обучения", "форма", "форму", "волонтер", "волонтером", "волонтеры", "волонтерство")
words_check_video = ("видео")


def start(update, context):
    update.message.reply_text(message.msg['WelcomeMessage'])
    #get_question(message)

def get_question(update, context):
    answer = update.message.text
    if any(word in answer.lower() for word in words_check_application):
        update.message.reply_text(message.msg['StartApplication'])
        update.message.reply_text(message.msg['FirstStepApplication'])
        update.message.reply_text(message.msg['SecondStepApplication'])

def get_information_about_video(update, context):
    answer = update.message.text
    if any(word in answer.lower() for word in words_check_video):
        update.message.reply_text(message.msg['InformationVideo'])


if __name__ == "__main__":
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, get_question))
    dp.add_handler(MessageHandler(Filters.text, get_information_about_video))
    updater.start_polling()
