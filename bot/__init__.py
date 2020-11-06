from json import load

from telegram.ext import Updater


updater = Updater(token=load(open("config.json"))["bot_token"], use_context=True)

import commands
import callbackQuery
import message
