from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import CallbackContext

import db
from main import reasons


def new(update: Update, context: CallbackContext):
    s = db.Session()
    u = s.query(db.User).get(update["_effective_user"]["id"])
    if not u or not all([u.first_name, u.last_name, u.birth_date, u.birth_city, u.address]):
        context.bot.send_message(chat_id=update.effective_chat.id, text="You have no data saved !",
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚙️ Set data",
                                                                                          callback_data="data")],
                                                                    [InlineKeyboardButton("🏘 Home", callback_data="home")]
                                                                    ]))
    else:
        if update.effective_chat.id not in reasons:
            reasons[update.effective_chat.id] = {}
        if update["_effective_user"]["id"] not in reasons[update.effective_chat.id]:
            reasons[update.effective_chat.id][update["_effective_user"]["id"]] = []

        last_line = [InlineKeyboardButton("🏘 Home", callback_data="home")]
        if len(reasons[update.effective_chat.id][update["_effective_user"]["id"]]) != 0:
            last_line.append(InlineKeyboardButton("✅ Send", callback_data="create"))

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Select your reasons\n`" +
                                      "`, `".join(reasons[update.effective_chat.id][update["_effective_user"]["id"]]) +
                                 "`",
                                 parse_mode=ParseMode.MARKDOWN_V2,
                                 reply_markup=InlineKeyboardMarkup([
                                     [InlineKeyboardButton("💼 Work", callback_data="reason_work"),
                                      InlineKeyboardButton("🛒 Shopping", callback_data="reason_shopping")],
                                     [InlineKeyboardButton("💊 Health", callback_data="reason_health"),
                                      InlineKeyboardButton("👨‍👩‍👧‍👦 Family", callback_data="reason_family")],
                                     [InlineKeyboardButton("♿️ Handicap", callback_data="reason_handicap"),
                                      InlineKeyboardButton("🚴‍♀️🐕 Sport/animal", callback_data="reason_sport_animal")],
                                     [InlineKeyboardButton("⚖️ Injunction", callback_data="reason_injunction"),
                                      InlineKeyboardButton("📜 Missions", callback_data="reason_missions")],
                                     [InlineKeyboardButton("👶 Children", callback_data="reason_children")],
                                     last_line]))

