from json import load

from telegram.ext import Updater

config = load(open("config.json"))
updater = Updater(token=config["bot_token"], use_context=True)

import commands
import callbackQuery
import message
