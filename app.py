# Project       : Red Alpha Assistant Bot
# Author        : Mindula Dilthushan
# Email         : minduladilthushan1@gmail.com
# Crate Date    : 22/04/09
# Update Date   : 22/04/10

# import ---------------------------------------------------------------------------------

from api import api as keys
from telegram.ext import *
import alpha_bot as alpha

print("Welcome to Alpha Telegram Bot")
print("Alpha bot started...!")

def start(update, context):
    update.message.reply_text("Type something! I can help you")

def help(update, context):
        update.message.reply_text("If you need help? what you need to know ?")

def handle(update, context):
    handle_text = str(update.message.text).lower()
    handle_response = alpha.bot_messages(handle_text)

    update.message.reply_text(handle_response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():

    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    dispatcher.add_handler(MessageHandler(Filters.text, handle))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()