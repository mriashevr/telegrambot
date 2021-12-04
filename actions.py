import message


def start(update, context):
    update.message.reply_text(message.msg['WelcomeMessage'])


def get_question(update, context):
    update.message.reply_text(message.msg['StartApplication'])
    update.message.reply_text(message.msg['FirstStepApplication'])
    update.message.reply_text(message.msg['SecondStepApplication'])


def get_information_about_video(update, context):
    update.message.reply_text(message.msg['InformationVideo'])