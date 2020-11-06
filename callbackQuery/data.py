from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext

from main import database


def data(update: Update, context: CallbackContext):
    if update["_effective_user"]["id"] not in database:
        database[update["_effective_user"]["id"]] = {"first_name": None,
                                                     "last_name": None,
                                                     "birth_date": None,
                                                     "birth_city": None,
                                                     "address": None}
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"*Firstname*: `{database[update['_effective_user']['id']]['first_name']}`\n"
                                  f"*Lastname*: `{database[update['_effective_user']['id']]['last_name']}`\n"
                                  f"*Birth date*: `{database[update['_effective_user']['id']]['birth_date']}`\n"
                                  f"*Birth city*: `{database[update['_effective_user']['id']]['birth_city']}`\n"
                                  f"*Address*: `{database[update['_effective_user']['id']]['address']}`\n\n"
                                  f"Choose the data you want to edit",
                             parse_mode=ParseMode.MARKDOWN_V2,
                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Firstname",
                                                                                      callback_data="edit_first_name"),
                                                                 InlineKeyboardButton("Lastname",
                                                                                      callback_data="edit_last_name")],
                                                                [InlineKeyboardButton("Birth date",
                                                                                      callback_data="edit_birth_date"),
                                                                 InlineKeyboardButton("Birth city",
                                                                                      callback_data="edit_birth_city")],
                                                                [InlineKeyboardButton("Address",
                                                                                      callback_data="edit_address")],
                                                                [InlineKeyboardButton("Home",
                                                                                      callback_data="home")]]))
