from telegram.ext import Dispatcher, Updater, CommandHandler, MessageHandler, Filters
from commands.start import Start
from commands.location import Location
from config import TOKEN


def run() -> None:
    updater: Updater = Updater(token=TOKEN)
    dispatcher: Dispatcher = updater.dispatcher

    # start: Start = Start()
    # location: Location = Location()
    #
    # start_handler: CommandHandler = CommandHandler("start", start.execute)
    # location_handler: MessageHandler = MessageHandler(Filters.location, location.execute)
    # dispatcher.add_handler(start_handler)
    # dispatcher.add_handler(location_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    print("Run")
    run()
