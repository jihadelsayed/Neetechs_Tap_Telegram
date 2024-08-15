from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import blockchain

# Define the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    args = context.args

    if len(args) != 1:
        await update.message.reply_text('Usage: /start <your_ethereum_address>')
        return

    ethereum_address = args[0]

    if not blockchain.is_user_authenticated(ethereum_address):
        await update.message.reply_text('Please authenticate first by using /authenticate <your_ethereum_address>.')
        return

    keyboard = [
        [InlineKeyboardButton("Tap to Earn", callback_data='earn')],
        [InlineKeyboardButton("Upload", callback_data='upload'), InlineKeyboardButton("Play", callback_data='play')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Welcome! Choose an option below:', reply_markup=reply_markup)
