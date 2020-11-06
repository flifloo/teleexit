from commands.start import start_handler
from main import updater


updater.dispatcher.add_handler(start_handler)
