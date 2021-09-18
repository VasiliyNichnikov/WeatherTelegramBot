from telegram.ext import CallbackContext
from telegram import Update


class Location:
    def __init__(self):
        pass

    def execute(self, update: Update, context: CallbackContext) -> None:
        user = update.message.from_user
        user_location = update.message.location
        print("Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)