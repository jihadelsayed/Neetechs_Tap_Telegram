# pip install python-telegram-bot web3

from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from button_callback import button

from command.authentication_command import authenticate_blockchain_command
from command.start_command import start
from command.help_command import help_command
import os

import logging
import database as db

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

token = os.getenv("TELEGRAM_BOT_TOKEN")

def main() -> None:
    # Initialize the database
    db.init_db()

    # Replace 'YOUR_TOKEN' with your bot's API token 
    application = ApplicationBuilder().token(token).build()

    # Register the start command handler
    application.add_handler(CommandHandler("start", start))

    # Register the authenticate command handler
    application.add_handler(CommandHandler("authenticate", authenticate_blockchain_command))
    # Register the help command handler
    application.add_handler(CommandHandler("help", help_command))
    # Register the button callback handler
    application.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
