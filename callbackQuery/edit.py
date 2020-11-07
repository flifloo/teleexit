from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from main import messages, local


def edit(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Send the new value for `{local[update.callback_query.data.replace('edit_', '')]}`",
                             parse_mode=ParseMode.MARKDOWN_V2)
    if update.effective_chat.id not in messages:
        messages[update.effective_chat.id] = {}

    messages[update.effective_chat.id][update["_effective_user"]["id"]] = update.callback_query.data

