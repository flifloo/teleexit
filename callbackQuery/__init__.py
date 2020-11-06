from callbackQuery.main import callback_query_handler
from main import updater


updater.dispatcher.add_handler(callback_query_handler)
