from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

from main import database


def new(update: Update, context: CallbackContext):
    if update['_effective_user']['id'] not in database or not all(database[update['_effective_user']['id']].values()):
        context.bot.send_message(chat_id=update.effective_chat.id, text="You have no data saved !",
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Set data",
                                                                                          callback_data="data")],
                                                                    [InlineKeyboardButton("Home", callback_data="home")]
                                                                    ]))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Select your reasons")

