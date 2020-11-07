from telegram import Update
from telegram.ext import CallbackContext, CallbackQueryHandler

from callbackQuery.create import create
from callbackQuery.data import data
from callbackQuery.edit import edit
from callbackQuery.new import new
from callbackQuery.reason import reason
from commands.start import start


def callback_query(update: Update, context: CallbackContext):
    if update.callback_query.data == "home":
        start(update, context)
    elif update.callback_query.data == "new":
        new(update, context)
    elif update.callback_query.data == "data":
        data(update, context)
    elif update.callback_query.data == "create":
        create(update, context)
    elif update.callback_query.data.startswith("edit_"):
        edit(update, context)
    elif update.callback_query.data.startswith("reason_"):
        reason(update, context)


callback_query_handler = CallbackQueryHandler(callback_query)
