from telegram import Update
from telegram.ext import CallbackContext

from main import reasons


def create(update: Update, context: CallbackContext):
    del reasons[update.effective_chat.id][update["_effective_user"]["id"]]

