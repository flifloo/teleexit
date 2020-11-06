from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters

from main import messages
from message.edit import edit


def message(update: Update, context: CallbackContext):
    if update.effective_chat.id in messages:
        if update["_effective_user"]["id"] in messages[update.effective_chat.id]:
            data = messages[update.effective_chat.id][update["_effective_user"]["id"]]
            if data.startswith("edit_"):
                edit(update, context, data)


message_handler = MessageHandler(Filters.text, message)
