from message import *

words_check_application = ("заявку", "заявка", "заявки", "анкета", "анкеты", "анкету", "тест", "тесты", "теста", "обучение", "обучения", "форма", "форму", "волонтер", "волонтером", "волонтеры", "волонтерство")
words_check_video = ("видео")

def start(update, context):
    update.message.reply_text(msg['WelcomeMessage'])


def get_question(message, update):
    if any(word in message for word in words_check_application):
        update.message.reply_text(msg['StartApplication'])
        update.message.reply_text(msg['FirstStepApplication'])
        update.message.reply_text(msg['SecondStepApplication'])


def get_information_about_video(message, update):
    if any(word in message for word in words_check_video):
        update.message.reply_text(msg['InformationVideo'])


def get_information_about_recommendation(message, update):
    # add if
    update.message.reply_text(msg['InformationVideo'])