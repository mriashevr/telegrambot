from actions import *


def fromHandlerToFunction(update, context):
    message = update.message.text
    message = message.lower()
    textProceed(message, update)


def textProceed(message, update):
    get_question(message, update)
    get_information_about_video(message, update)