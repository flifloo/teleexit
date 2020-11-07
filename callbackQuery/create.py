from datetime import datetime
from io import BytesIO

from qrcode import make
from telegram import Update
from telegram.ext import CallbackContext

from main import reasons, database


local = {
    "work": "travail",
    "shopping": "achats",
    "health": "sante",
    "family": "famille",
    "handicap": "handicap",
    "sport_animal": "sport_animaux",
    "injunction": "convocation",
    "missions": "missions",
    "children": "enfants"
}


def create(update: Update, context: CallbackContext):
    reason = map(lambda r: local[r], reasons[update.effective_chat.id][update["_effective_user"]["id"]])
    del reasons[update.effective_chat.id][update["_effective_user"]["id"]]
    date = datetime.now().strftime('%d/%m/%Y a %Hh%M')

    img = make(f"Cree le: {date};\n"
               f"Nom: {database[update['_effective_user']['id']]['last_name']};\n"
               f"Prenom: {database[update['_effective_user']['id']]['first_name']};\n"
               f"Naissance: {database[update['_effective_user']['id']]['birth_date']} a "
               f"{database[update['_effective_user']['id']]['birth_city']};\n"
               f"Adresse: {database[update['_effective_user']['id']]['address']};\n"
               f"Sortie: {date}\n"
               f"Motifs: {', '.join(reason)};")
    photo = BytesIO()
    photo.name = "QRCode.jpeg"
    img.save(photo, "JPEG")
    photo.seek(0)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)

