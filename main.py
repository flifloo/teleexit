import logging

from bot import updater


local = {"first_name": "Firstname",
         "last_name": "Lastname",
         "birth_date": "Birth date",
         "birth_city": "Birth city",
         "address": "Address"}
database = {}
messages = {}
reasons = {}

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

updater.start_polling()
