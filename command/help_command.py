from telegram import Update
from telegram.ext import ContextTypes

# Define the help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "Welcome to @Neetechs_bot! Here are the available commands and how to use them:\n\n"
        "/start <your_ethereum_address> - Start the bot and verify your Ethereum address.\n"
        "/authenticate <your_ethereum_address> - Authenticate your Ethereum address to use the bot.\n"
        "/help - Display this help message.\n\n"
        "Features:\n"
        "- Tap to Earn Points: Use the 'Tap to Earn' button to accumulate points.\n"
        "- Upload Content: (Coming Soon) Upload your favorite photos, videos, or documents.\n"
        "- Play Games: (Coming Soon) Play exciting games directly within the bot.\n"
        "- Leaderboards: (Coming Soon) Compete with others and climb the leaderboards.\n"
        "- Rewards and Badges: (Coming Soon) Unlock rewards and badges for your achievements.\n\n"
        "Stay tuned for more exciting features!"
    )
    await update.message.reply_text(help_text)
