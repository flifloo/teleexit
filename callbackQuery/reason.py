from telegram import Update
from telegram.ext import CallbackContext

from callbackQuery.new import new
from main import reasons


def reason(update: Update, context: CallbackContext):
    data = update.callback_query.data.replace("reason_", "")
    if data in reasons[update.effective_chat.id][update["_effective_user"]["id"]]:
        del reasons[update.effective_chat.id][update["_effective_user"]["id"]]\
        [reasons[update.effective_chat.id][update["_effective_user"]["id"]].index(data)]
    else:
        reasons[update.effective_chat.id][update["_effective_user"]["id"]].append(data)
    new(update, context)

