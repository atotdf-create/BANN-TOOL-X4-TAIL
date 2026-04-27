import asyncio
from telegram import Update, constants
from telegram.ext import ContextTypes
from config import AI_API_KEY, AUTOTYPE_SPEED

# This is a mock AI function. In a real scenario, you'd call OpenAI or Gemini API.
async def get_ai_response(query):
    # Simulated AI logic
    await asyncio.sleep(1) # Simulate network delay
    return f"AI Response to '{query}': This is a powerful AI response generated for tdftech."

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = ' '.join(context.args)
    if not query:
        await update.message.reply_text("Please provide a query. Usage: /ask <your question>")
        return

    # Show typing status
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=constants.ChatAction.TYPING)
    
    response = await get_ai_response(query)
    
    # Simulate autotyping for the response
    await autotype_message(update, context, response)

async def autotype(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = ' '.join(context.args)
    if not message_text:
        await update.message.reply_text("Please provide a message. Usage: /autotype <message>")
        return
    
    await autotype_message(update, context, message_text)

async def autotype_message(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str):
    """Helper function to simulate autotyping in Telegram."""
    chat_id = update.effective_chat.id
    
    # We can't actually 'autotype' in the sense of showing character by character in the message bubble 
    # as it's being sent, but we can simulate the 'typing...' status and then send the message.
    # For a more advanced 'autotype' effect, we could send an empty message and edit it repeatedly, 
    # but that's often rate-limited by Telegram.
    
    # Method 1: Typing status + Send
    await context.bot.send_chat_action(chat_id=chat_id, action=constants.ChatAction.TYPING)
    
    # Calculate delay based on text length
    delay = min(len(text) * AUTOTYPE_SPEED, 5) # Cap at 5 seconds
    await asyncio.sleep(delay)
    
    await update.message.reply_text(text)
