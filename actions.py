from message import *
from AudioRecognition import *

words_check_application = ["заявку", "заявка", "заявки", "анкета", "анкеты", "анкету", "тест", "тесты", "теста", "обучение", "обучения", "форма", "форму", "волонтер", "волонтером", "волонтеры", "волонтерство"]
words_check_video = ["видео"]
words_check_recommendation = ["рекомендации"]
words_check_medical = ["страховка"]


def start(update, context):
    update.message.reply_text(msg['WelcomeMessage'])


def get_question(message, update):
    if any(word in message.split() for word in words_check_application):
        update.message.reply_text(msg['StartApplication'])
        update.message.reply_text(msg['FirstStepApplication'])
        update.message.reply_text(msg['SecondStepApplication'])


def get_question(audio_link, update):
    if any(word in audio_message(audio_link).split() for word in words_check_application):
        update.message.reply_text(msg['StartApplication'])
        update.message.reply_text(msg['FirstStepApplication'])
        update.message.reply_text(msg['SecondStepApplication'])

def get_information_about_video(message, update):
    if any(word in message.split() for word in words_check_video):
        update.message.reply_text(msg['InformationVideo'])


def get_information_about_recommendation(message, update):
    if any(word in message.split() for word in words_check_recommendation):
        update.message.reply_text(msg['InformationRecommendation'])


def get_information_about_medical_test(message, update):
    if any(word in message.split() for word in words_check_medical):
        update.message.reply_text(msg['MedInformation'])

def get_information_about_medical_test(message, update):
    if any(word in message.split() for word in words_check_medical):
        update.message.reply_text(msg['MedInformation'])


def get_information_about_medical_test(message, update):
    if any(word in message.split() for word in words_check_medical):
        update.message.reply_text(msg['MedInformation'])