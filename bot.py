import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from config import TELEGRAM_BOT_TOKEN
from utils.ui import print_banner, log_info, log_error
from handlers.ai import ask, autotype
from handlers.scan import scan

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Welcome to the <b>tdftech</b> Powerful Telegram Bot. "
        "Use /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "<b>Available Commands:</b>\n"
        "/start - Welcome message\n"
        "/help - Show this help message\n"
        "/ask &lt;query&gt; - Ask the AI a question\n"
        "/autotype &lt;message&gt; - Simulate typing for a message\n"
        "/scan &lt;target&gt; - Perform a secure scan (demo)\n"
    )
    await update.message.reply_html(help_text)

def main():
    print_banner()
    
    if TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        log_error("Please set your TELEGRAM_BOT_TOKEN in config.py or as an environment variable.")
        # We don't return here so that the user can see the banner and the error message in Termux.
        # In production, you'd exit.
    
    log_info("Initializing bot...")
    
    try:
        application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
        
        application.add_handler(CommandHandler('start', start))
        application.add_handler(CommandHandler('help', help_command))
        application.add_handler(CommandHandler('ask', ask))
        application.add_handler(CommandHandler('autotype', autotype))
        application.add_handler(CommandHandler('scan', scan))
        
        log_info("Bot is running. Press Ctrl+C to stop.")
        application.run_polling()
    except Exception as e:
        log_error(f"Failed to start bot: {e}")

if __name__ == '__main__':
    main()
