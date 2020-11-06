from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, CommandHandler


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to TeleExit",
                             reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Create a new certificate",
                                                                                      callback_data="new")],
                                                                [InlineKeyboardButton("Manage saved data",
                                                                                      callback_data="data")]
                                                                ]))


start_handler = CommandHandler("start", start)
