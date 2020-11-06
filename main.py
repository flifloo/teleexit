import logging
from json import load

from telegram.ext import CommandHandler
from telegram.ext import Updater


updater = Updater(token=load(open("config.json"))["bot_token"], use_context=True)

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler("start", start)
updater.dispatcher.add_handler(start_handler)

updater.start_polling()
