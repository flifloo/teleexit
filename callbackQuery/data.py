from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext

import db


def data(update: Update, context: CallbackContext):
    s = db.Session()
    u = s.query(db.User).get(update["_effective_user"]["id"])
    if not u:
        u = db.User(update["_effective_user"]["id"])
        s.add(u)
        s.commit()
    s.close()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"*Firstname*: `{u.first_name}`\n"
                                  f"*Lastname*: `{u.last_name}`\n"
                                  f"*Birth date*: `{u.birth_date}`\n"
                                  f"*Birth city*: `{u.birth_city}`\n"
                                  f"*Address*: `{u.address}`\n\n"
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
                                                                [InlineKeyboardButton("🏘 Home",
                                                                                      callback_data="home")]]))
