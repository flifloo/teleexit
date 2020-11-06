from main import updater
from message.main import message_handler


updater.dispatcher.add_handler(message_handler)
