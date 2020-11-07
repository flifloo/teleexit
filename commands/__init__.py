from commands.cancel import cancel_handler
from commands.start import start_handler
from main import updater


updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(cancel_handler)
