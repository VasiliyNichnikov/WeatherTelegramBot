from telegram.ext import CallbackContext
from telegram import Location
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup


class Start:
    def __init__(self):
        self.__button_location: KeyboardButton = KeyboardButton("Отправить локацию", request_location=True)
        self.__keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup([[self.__button_location]], resize_keyboard=True,
                                                                   one_time_keyboard=True)

    def execute(self, update: Update, context: CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Мне нужна ваша локация.",
                                 reply_markup=self.__keyboard)
