import re
from datetime import datetime

from telegram import Update, ParseMode
from telegram.ext import CallbackContext

import db
from callbackQuery.create import address_re
from callbackQuery.data import data
from main import local, messages

rex = {
    "first_name": re.compile(r"^([a-zA-Z]| )+$"),
    "last_name": re.compile(r"^([a-zA-Z]| )+$"),
    "birth_date": re.compile(r"^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$"),
    "birth_city": re.compile(r"^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$"),
    "address": address_re
}

examples = {
    "first_name": "Camille",
    "last_name": "Dupont",
    "birth_date": "01/01/1970",
    "birth_city": "Paris",
    "address": "999 avenue de France, 75001 Paris"
}


def check_date(date) -> bool:
    try:
        datetime.strptime(date, "%d/%m/%Y")
    except:
        return False
    else:
        return True


def edit(update: Update, context: CallbackContext, data_edit: str):
    name = data_edit.replace("edit_", "")
    if not rex[name].fullmatch(update.message.text) or\
            (name == "birth_date" and not check_date(update.message.text)):
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invalid value for `{local[name]}` \!\n"
                                                                        f"*Example*: `{examples[name]}`",
                                 parse_mode=ParseMode.MARKDOWN_V2)
    else:
        s = db.Session()
        u = s.query(db.User).get(update["_effective_user"]["id"])
        del messages[update.effective_chat.id][update["_effective_user"]["id"]]
        if name == "birth_date":
            setattr(u, name, datetime.strptime(update.message.text, "%d/%m/%Y").date())
        else:
            setattr(u, name, update.message.text)
        s.add(u)
        s.commit()
        s.close()
        data(update, context)
