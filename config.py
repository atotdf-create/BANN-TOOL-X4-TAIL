import os

# Bot Configuration
# In a real scenario, you should use environment variables for sensitive information.
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
AI_API_KEY = os.getenv("AI_API_KEY", "YOUR_AI_API_KEY_HERE")

# Other settings
AUTOTYPE_SPEED = 0.05  # Seconds per character
