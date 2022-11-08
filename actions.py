from telegram.ext import CallbackContext
from message import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram import ReplyKeyboardRemove
from telegram.utils.request import Request

words_check_application = ("заявку", "заявка", "заявки", "анкета", "анкеты", "анкету", "тест", "тесты", "теста", "обучение", "обучения", "форма", "форму", "волонтер", "волонтером", "волонтеры", "волонтерство")
words_check_video = ["видео", "отбор", "выбор"]
words_check_recommendation = ["рекомендации", "волонтерская книжка", "волонтерская книга", "книга волонтера", "волонтерские книжки", "рекомендация", "благодарность", "благодарности"]
words_check_medical = ["медицинская книжка", "медицинские книжки", "справка",  "справки", "комиссия", "комиссии", "страховка", "страховки", "страховку", "ограничение", "ограничения"]
words_check_schedule = ["график", "сезон", "срок", "сроки", "сезонов", "графики"]
words_check_electr_connect = ["электричество", "связь", "электричесвто", "зарядить", "заряжать", "интернет", "инет"]
words_check_preparing = ["подготовка", "что взять с собой", "вещи", "вещей", "одежда", "одежду", "одежда", "снаряжение", "погода", "путешествие", "путешествия"]
words_check_health = ["здоровье", "пцр", "аптечка", "здоровье", "прививки", "ковид", "ковид-19"]
words_check_food = ["продукты", "питание", "питания", "кормить", "кушать", "продукты", "продуктами", "пайок"]
words_check_living = ["проживание", "отель", "условие", "условия", "домик", "дом", "палатка", "туалет", "баня", "душ", "стирка", "стирать", "мыть", "мыться", "купаться", "гостиница"]
words_check_signing = ["договор", "соглашение", "договора", "соглaшения"]
words_check_departure = ["отлет", "отлёт", "отправка", "как добраться", "как добираться", "дата вылета", "дату вылета", "вертолет"]
words_check_waiting_departure = ["ожидание", "предоставляет", "предоставит", "остановиться", "остановка"]
words_check_area_work = ["территория", "работа", "работу", "работать", "работы", "выходные"]
words_check_report = ["отзыв", "отзыв", "отчет", "офис", "возвращение", "возвращении"]
words_check_kardon = ["кoрдон"]


CALLBACK_BUTTON1_LEFT = "callback_button1_left"
CALLBACK_BUTTON1_RIGHT = "callback_button1_right"
CALLBACK_BUTTON2_LEFT = "callback_button2_left"
CALLBACK_BUTTON2_RIGHT = "callback_button2_right"
CALLBACK_BUTTON3_LEFT = "callback_button3_left"
CALLBACK_BUTTON3_RIGHT = "callback_button3_right"
CALLBACK_BUTTON4_LEFT = "callback_button4_left"
CALLBACK_BUTTON_HIDE_KEYBOARD = "callback_button9_hide"

CALLBACK_BUTTON1 = "callback_button1"
CALLBACK_BUTTON2 = "callback_button2"
CALLBACK_BUTTON3 = "callback_button3"
CALLBACK_BUTTON4 = "callback_button4"
CALLBACK_BUTTON5 = "callback_button5"
CALLBACK_BUTTON6= "callback_button6"
CALLBACK_BUTTON_HELP1 = "callback_button_help1"
CALLBACK_BUTTON_HELP2 = "callback_button_help2"
CALLBACK_BUTTON_HELP3= "callback_button_help3"



TITLES = {
    CALLBACK_BUTTON1_LEFT: "Мини-отель АМТО",
    CALLBACK_BUTTON1_RIGHT: "Вила Хостел",
    CALLBACK_BUTTON2_LEFT: "Хостел Камчатский Стиль",
    CALLBACK_BUTTON2_RIGHT: "Гостиница Арт Отель",
    CALLBACK_BUTTON3_LEFT: "Yu Hotel",
    CALLBACK_BUTTON3_RIGHT: "Forest Hotel",
    CALLBACK_BUTTON4_LEFT: "Аэро Отель",
    CALLBACK_BUTTON_HIDE_KEYBOARD: "Спрячь клавиатуру",
}

TITLES2 = {
    CALLBACK_BUTTON1: "Озерный",
    CALLBACK_BUTTON2: "Травяной",
    CALLBACK_BUTTON3: "Долина гейзеров",
    CALLBACK_BUTTON4: "Узон",
    CALLBACK_BUTTON5: "Исторки и аэродром",
    CALLBACK_BUTTON6: "Кроноки и семячик",
    CALLBACK_BUTTON_HELP1: "Инфраструктурный",
    CALLBACK_BUTTON_HELP2: "Добровольческий",
    CALLBACK_BUTTON_HELP3: "Назад"
}


def start(update, context):
    context.bot.send_sticker(update.message.chat.id, "CAACAgIAAxkBAAEDajdhrCSVfZtOU31ctyyYvJ49I-_RtQACLxcAAvztYUmgOtyGwX__ziIE")
    update.message.reply_text(msg['WelcomeMessage'])


def get_question(message, update):
    if any(word.split() in message.split() for word in words_check_application):
        update.message.reply_text(msg['StartApplication'])
        update.message.reply_text(msg['FirstStepApplication'])
        update.message.reply_text(msg['SecondStepApplication'])


def get_information_about_video(message, update, context):
    if any(word in message.split() for word in words_check_video):
        context.bot.send_sticker(update.message.chat.id, "CAACAgIAAxkBAAEDajthrCTs0tEh8SbI4wJgHzBVXXFvTAAC5xIAAjknYUlgm2AzjcYoqiIE")
        update.message.reply_text(msg['InformationVideo'])


def get_information_about_recommendation(message, update):
    if any(word in message.split() for word in words_check_recommendation):
        update.message.reply_text(msg['InformationRecommendation'])


def get_information_about_medical_test(message, update):
    if any(word in message.split() for word in words_check_medical):
        update.message.reply_text(msg['MedInformation'])


def get_information_about_schedule(message, update):
    if any(word in message.split() for word in words_check_schedule):
        update.message.reply_text(msg['InformationSchedule'])


def get_information_about_preparing_trip(message, update, context):
    if any(word in message.split() for word in words_check_preparing):
        context.bot.send_sticker(update.message.chat.id, "CAACAgIAAxkBAAEDakFhrCUe8XvuibbWE7zGjg_faW0OWwACRhQAAoU3YUkjhCn-2V-G7SIE")
        update.message.reply_text(msg['InformationPreparingTrip'])


def get_information_about_connection_electricity(message, update, context):
    if any(word in message.split() for word in words_check_electr_connect):
        context.bot.send_sticker(update.message.chat.id, "CAACAgIAAxkBAAEDakNhrCUuHqfB1zJsMfNHiJ5bLEahIAAClhUAAk53YUm9T-aoPpHA7yIE")
        update.message.reply_text(msg['InformationPreparingTrip'])


def get_information_about_health(message, update, context):
    if any(word in message.split() for word in words_check_health):
        context.bot.send_sticker(update.message.chat.id, "CAACAgIAAxkBAAEDakVhrCU_2XQ5eGZn6TfRrb8niNJffAAChBYAAp9aYEkRjG_q1EdfHiIE")
        update.message.reply_text(msg['InformationHealth'])


def get_information_about_food(message, update, context):
    if any(word in message.split() for word in words_check_food):
        context.bot.send_sticker(update.message.chat.id, "CAACAgIAAxkBAAEDaj9hrCUOx3GtsQjE9e0nW7u-Y8e1bgACVhgAAjyrYUkYWKaWteg3FCIE")
        update.message.reply_text(msg['InformationFood'])


def get_information_about_living(message, update, context):
    if any(word in message.split() for word in words_check_living):
        context.bot.send_sticker(update.message.chat.id, "CAACAgIAAxkBAAEDajlhrCTWGsw7nUcLYicPsfsFgNTvuAACxBUAAnhjYUkz8IPUX_8NmCIE")
        update.message.reply_text(msg['InformationLiving'],
        reply_markup = get_base_inline_keyboard())


def get_information_about_signing(message, update, context):
    if any(word in message.split() for word in words_check_signing):
        context.bot.send_sticker(update.message.chat.id, "CAACAgIAAxkBAAEDakdhrCVNdGJ-yVsVYVoToYO6WJGyCwAC2BIAAqJcaEkEZIBxqkmC6CIE")
        update.message.reply_text(msg['InformationSigning'])


def get_information_about_departure(message, update):
    if any(word in message.split() for word in words_check_departure):
        update.message.reply_text(msg['InformationDeparture'])


def get_information_about_waiting_departure(message, update):
    if any(word in message.split() for word in words_check_waiting_departure):
        update.message.reply_text(msg['InformationWaiting'])


def get_information_about_area_work(message, update):
    if any(word in message.split() for word in words_check_area_work):
        update.message.reply_text(msg['InformationArea'])


def get_information_about_report(message, update, context):
    if any(word in message.split() for word in words_check_report):
        context.bot.send_sticker(update.message.chat.id, "CAACAgIAAxkBAAEDaklhrCVkUgkR2o8GCBAn0e89S1pEEgACyRUAArMaYEnoQcLjKVyRpSIE")
        update.message.reply_text(msg['InformationReport'])

def get_information_about_kardon(message, update):
    if any(word in message.split() for word in words_check_kardon):
        update.message.reply_text(msg['InformationKardon'],
        reply_markup = get_base_inline_keyboard2())


def get_base_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_LEFT], callback_data=CALLBACK_BUTTON1_LEFT),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_RIGHT], callback_data=CALLBACK_BUTTON1_RIGHT),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_LEFT], callback_data=CALLBACK_BUTTON2_LEFT),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_RIGHT], callback_data=CALLBACK_BUTTON2_RIGHT),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_LEFT], callback_data=CALLBACK_BUTTON3_LEFT),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_RIGHT], callback_data=CALLBACK_BUTTON3_RIGHT),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_LEFT], callback_data=CALLBACK_BUTTON4_LEFT),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_HIDE_KEYBOARD], callback_data=CALLBACK_BUTTON_HIDE_KEYBOARD),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard2():
    keyboard = [
        [
            InlineKeyboardButton(TITLES2[CALLBACK_BUTTON1], callback_data=CALLBACK_BUTTON1),
        ],
        [
            InlineKeyboardButton(TITLES2[CALLBACK_BUTTON2], callback_data=CALLBACK_BUTTON2),
        ],
        [
            InlineKeyboardButton(TITLES2[CALLBACK_BUTTON3], callback_data=CALLBACK_BUTTON3),
        ],
        [
            InlineKeyboardButton(TITLES2[CALLBACK_BUTTON4], callback_data=CALLBACK_BUTTON4),
        ],
        [
            InlineKeyboardButton(TITLES2[CALLBACK_BUTTON5], callback_data=CALLBACK_BUTTON5),
        ],
        [
            InlineKeyboardButton(TITLES2[CALLBACK_BUTTON6], callback_data=CALLBACK_BUTTON6),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_base_inline_keyboard2for2():
    keyboard = [
        [
            InlineKeyboardButton(TITLES2[CALLBACK_BUTTON_HELP1], callback_data=CALLBACK_BUTTON_HELP1),
            InlineKeyboardButton(TITLES2[CALLBACK_BUTTON_HELP2], callback_data=CALLBACK_BUTTON_HELP2),
        ],
        [
            InlineKeyboardButton(TITLES2[CALLBACK_BUTTON_HELP3], callback_data=CALLBACK_BUTTON_HELP3),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def keyboard_callback_handler(update, context: CallbackContext):
        query = update.callback_query
        data = query.data
        chat_id = update.effective_message.chat_id
        current_text = update.effective_message.text
        if data == CALLBACK_BUTTON1_LEFT:
            query.edit_message_text(
                text=current_text,
                parse_mode=ParseMode.MARKDOWN,
            )
            context.bot.send_message(
                chat_id=chat_id,
                text="Мини-отель АМТО ул. Ленина, 32, Елизово, Камчатский край, 684300, 8 (924) 585-35-35, стоимость от 1500 рублей".format(data),
                reply_markup=get_base_inline_keyboard(),
            )
        if data == CALLBACK_BUTTON1_RIGHT:
            query.edit_message_text(
                text=current_text,
                parse_mode=ParseMode.MARKDOWN,
            )
            context.bot.send_message(
                chat_id=chat_id,
                text="Вила Хостел, Уральская ул., дом 2, Камчатский край, 684007, 8 (963) 833-22-32, стоимость от 2000 рублей".format(data),
                reply_markup=get_base_inline_keyboard(),
            )
        if data == CALLBACK_BUTTON2_LEFT:
            query.edit_message_text(
                text=current_text,
                parse_mode=ParseMode.MARKDOWN,
            )
            context.bot.send_message(
                chat_id=chat_id,
                text="Хостел Камчатский Стиль, ул. Беринга, 26, Елизово, Камчатский край, 684000•8 (951) 290-67-42, стоимость от 3000 рублей".format(data),
                reply_markup=get_base_inline_keyboard(),
            )
        if data == CALLBACK_BUTTON2_RIGHT:
            query.edit_message_text(
                text=current_text,
                parse_mode=ParseMode.MARKDOWN,
            )
            context.bot.send_message(
                chat_id=chat_id,
                text="Гостиница Арт Отель ул. Виталия Кручины, 3, Елизово, Камчатский край, 684000, 8 (415) 317-14-43, стоимость от 6500 рублей".format(data),
                reply_markup=get_base_inline_keyboard(),
            )
        if data == CALLBACK_BUTTON3_LEFT:
            query.edit_message_text(
                text=current_text,
                parse_mode=ParseMode.MARKDOWN,
            )
            context.bot.send_message(
                chat_id=chat_id,
                text="Yu Hotel, ул. Виталия Кручины, д. 38 А, Камчатский край, 684000 8 (914) 021-27-27, стоимость от 8000 рублей".format(data),
                reply_markup=get_base_inline_keyboard(),
            )
        if data == CALLBACK_BUTTON3_RIGHT:
            query.edit_message_text(
                text=current_text,
                parse_mode=ParseMode.MARKDOWN,
            )
            context.bot.send_message(
                chat_id=chat_id,
                text="Forest Hotel, Геофизическая ул., 9а, 3-й этаж, Елизово, Камчатский край, 684000•8 (924) 698-55-55, стоимость от 3000 рублей".format(data),
                reply_markup=get_base_inline_keyboard(),
            )
        if data == CALLBACK_BUTTON4_LEFT:
            query.edit_message_text(
                text=current_text,
                parse_mode=ParseMode.MARKDOWN,
            )
            context.bot.send_message(
                chat_id=chat_id,
                text="Аэро Отель ул. Магистральная, 44В, Елизово, Камчатский край, 684010•8 (963) 833-44-00, стоимость от 4500 рублей".format(data),
                reply_markup=get_base_inline_keyboard(),
            )
        if data == CALLBACK_BUTTON_HIDE_KEYBOARD:
            query.edit_message_text(
                text=current_text,
                parse_mode=ParseMode.MARKDOWN,
            )
            context.bot.send_message(
                chat_id=chat_id,
            )


def keyboard_callback2_handler(update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text
    if data == CALLBACK_BUTTON1:
        # query.edit_message_text(
        #     text=current_text,
        #     parse_mode=ParseMode.MARKDOWN,
        # )
        context.bot.send_message(
            chat_id=chat_id,
            text=current_text,
            reply_markup=get_base_inline_keyboard2for2(),
        )
    if data == CALLBACK_BUTTON_HELP1:
        # query.edit_message_text(
        #     text=current_text,
        #     parse_mode=ParseMode.MARKDOWN,
        # )
        context.bot.send_message(
            chat_id=chat_id,
            text=current_text,
            reply_markup=get_base_inline_keyboard2for2(),
        )