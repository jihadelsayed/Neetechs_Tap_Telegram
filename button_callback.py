from telegram import Update
from telegram.ext import ContextTypes
from collections import defaultdict
import database as db
import blockchain

# In-memory storage for user points
user_points = defaultdict(int)

# Define the button callback
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user_id = query.from_user.id

    # if not db.is_user_authenticated(user_id):
    #     await query.answer()
    #     await query.edit_message_text(text='Please authenticate first by using /authenticate <your_code>.')
    #     return

    # blockchain authentication
    args = context.args

    if len(args) != 1:
        await update.message.reply_text('Usage: /start <your_ethereum_address>')
        return

    ethereum_address = args[0]

    if not blockchain.is_user_authenticated(ethereum_address):
        await query.answer()
        await query.edit_message_text(text='Please authenticate first by using /authenticate <your_ethereum_address>.')
        return
    

    await query.answer()

    if query.data == 'earn':
        user_points[user_id] += 1
        await query.edit_message_text(text=f"You earned some points! Your total is now {user_points[user_id]} points. Tap again to earn more.")
    elif query.data == 'upload':
        await query.edit_message_text(text="Upload functionality is not yet implemented.")
    elif query.data == 'play':
        await query.edit_message_text(text="Play functionality is not yet implemented. This will open a new window or view.")
