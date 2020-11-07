from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, CommandHandler

from main import messages


def cancel(update: Update, context: CallbackContext):
    if update.effective_chat.id in messages and\
            update["_effective_user"]["id"] in messages[update.effective_chat.id]:
        del messages[update.effective_chat.id][update["_effective_user"]["id"]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Action canceled",
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏘 Home",
                                                                                          callback_data="home")]]))


cancel_handler = CommandHandler("cancel", cancel)
