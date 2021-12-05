from actions import *
from AudioRecognition import *


def fromHandlerToFunction(update, context):
    if (update.message.text != None):
        message = update.message.text
        message = message.lower()
    # if (update.message.voice != None):
    # message = audio_message(update.message.voice)
    # print(audio_message(update.message.voice))
    # message = message.lower()
    textProceed(message, update, context)


def textProceed(message, update, context):
    get_question(message, update)
    get_information_about_video(message, update, context)
    get_information_about_recommendation(message, update)
    get_information_about_medical_test(message, update)
    get_information_about_signing(message, update, context)
    get_information_about_departure(message, update)
    get_information_about_area_work(message, update)
    get_information_about_connection_electricity(message, update, context)
    get_information_about_food(message, update, context)
    get_information_about_health(message, update, context)
    get_information_about_living(message, update, context)
    get_information_about_preparing_trip(message, update, context)
    get_information_about_report(message, update, context)
    get_information_about_waiting_departure(message, update)
    get_information_about_schedule(message, update)