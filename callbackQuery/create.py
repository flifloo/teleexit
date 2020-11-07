from datetime import datetime
from io import BytesIO
from re import compile

from PyPDF2 import PdfFileReader, PdfFileWriter
from qrcode import make
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

import db
from main import reasons

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
address_re = compile(r"^(.*),? ([0-9]{5}) ([a-zA-Z]+(?:[\s-][a-zA-Z]+)*)$")


def create(update: Update, context: CallbackContext):
    reason = reasons[update.effective_chat.id][update["_effective_user"]["id"]]
    del reasons[update.effective_chat.id][update["_effective_user"]["id"]]
    date = datetime.now()
    s = db.Session()
    u = s.query(db.User).get(update["_effective_user"]["id"])
    s.close()
    first_name = u.first_name
    last_name = u.last_name
    birth_date = u.birth_date
    birth_city = u.birth_city
    address = address_re.fullmatch(u.address).groups()

    img = make(f"Cree le: {date.strftime('%d/%m/%Y a %Hh%M')};\n"
               f"Nom: {first_name};\n"
               f"Prenom: {last_name};\n"
               f"Naissance: {birth_date} a "
               f"{birth_city};\n"
               f"Adresse: {address[0]} {address[1]} {address[2]};\n"
               f"Sortie: {date.strftime('%d/%m/%Y a %Hh%M')}\n"
               f"Motifs: {', '.join(map(lambda r: local[r], reason))};")
    photo = BytesIO()
    photo.name = "QRCode.jpeg"
    img.save(photo, "JPEG")
    photo.seek(0)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)

    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 11)
    can.drawString(119, 696, f"{first_name} {last_name}")
    can.drawString(119, 674, birth_date.strftime("%d/%m/%Y"))
    can.drawString(297, 674, birth_city)
    can.drawString(133, 652, f"{address[0]} {address[1]} {address[2]}")
    can.setFontSize(18)
    for r in reason:
        y = 0
        if r == "work":
            y = 578
        elif r == "shopping":
            y = 533
        elif r == "health":
            y = 477
        elif r == "family":
            y = 435
        elif r == "handicap":
            y = 396
        elif r == "sport_animal":
            y = 358
        elif r == "injunction":
            y = 295
        elif r == "missions":
            y = 255
        elif r == "children":
            y = 211
        can.drawString(78, y, "x")
    can.setFontSize(11)
    can.drawString(105, 177, address[2])
    can.drawString(91, 153, date.strftime("%d/%m/%Y"))
    can.drawString(264, 153, date.strftime("%Hh%M"))
    existing_pdf = PdfFileReader(open("certificate.pdf", "rb"))
    photo.seek(0)
    can.drawImage(ImageReader(photo), existing_pdf.getPage(0).mediaBox[2] - 156, 100, 92, 92)
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    output_stream = BytesIO()
    output_stream.name = "Exit certificate.pdf"
    output.write(output_stream)
    output_stream.seek(0)
    context.bot.send_document(chat_id=update.effective_chat.id, document=output_stream,
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏘 Home", callback_data="home")],
                                                                 [InlineKeyboardButton("📝 New", callback_data="new")]]))
