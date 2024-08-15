from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import logging
from collections import defaultdict

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# In-memory storage for user points
user_points = defaultdict(int)

# Define the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Tap to Earn", callback_data='earn')],
        [InlineKeyboardButton("Upload", callback_data='upload'), InlineKeyboardButton("Play", web_app=WebAppInfo(url="https://yourdomain.com/game"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Welcome! Choose an option below:', reply_markup=reply_markup)

# Define the button callback
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == 'earn':
        user_id = query.from_user.id
        user_points[user_id] += 1
        await query.edit_message_text(text=f"You earned some points! Your total is now {user_points[user_id]} points. Tap again to earn more.")
    elif query.data == 'upload':
        await query.edit_message_text(text="Upload functionality is not yet implemented.")

# Define the main function
def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's API token
    application = ApplicationBuilder().token("7279460338:AAHVa2jjxzZRHYNdBepiWHrlRomFo5nHKIk").build()

    # Register the start command handler
    application.add_handler(CommandHandler("start", start))

    # Register the button callback handler
    application.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
