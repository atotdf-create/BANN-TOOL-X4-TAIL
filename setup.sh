#!/bin/bash

# tdftech Telegram Bot Setup Script for Termux

# --- Colors for better output ---
GREEN=\'\033[0;32m\'
YELLOW=\'\033[0;33m\'
RED=\'\033[0;31m\'
CYAN=\'\033[0;36m\'
NC=\'\033[0m\' # No Color

echo -e "${CYAN}tdftech Telegram Bot Setup${NC}"
echo -e "${CYAN}--------------------------${NC}"

# --- 1. Update and Upgrade Termux Packages ---
echo -e "${YELLOW}[*] Updating and upgrading Termux packages...${NC}"
pkg update -y && pkg upgrade -y

# --- 2. Install Python and Git ---
echo -e "${YELLOW}[*] Installing Python and Git...${NC}"
pkg install python -y
pkg install git -y

# --- 3. Navigate to the bot directory ---
echo -e "${YELLOW}[*] Navigating to bot directory...${NC}"
# Assuming the script is run from the root of the cloned repository
cd "$(dirname "$0")" || exit

# --- 4. Install Python dependencies ---
echo -e "${YELLOW}[*] Installing Python dependencies...${NC}"
pip install -r requirements.txt

# --- 5. Configure Bot Token and AI API Key ---
echo -e "\n${YELLOW}[*] Configuration:${NC}"
echo -e "${GREEN}Please obtain your Telegram Bot Token from BotFather on Telegram.${NC}"
read -p "Enter your Telegram Bot Token: " TELEGRAM_BOT_TOKEN_INPUT

echo -e "${GREEN}If you plan to use AI features, obtain an AI API Key (e.g., OpenAI, Gemini). (Optional)${NC}"
read -p "Enter your AI API Key (leave blank if not using AI): " AI_API_KEY_INPUT

# Update config.py with provided tokens
if [ -n "$TELEGRAM_BOT_TOKEN_INPUT" ]; then
    sed -i "s|TELEGRAM_BOT_TOKEN = os.getenv(\"TELEGRAM_BOT_TOKEN\", \"YOUR_BOT_TOKEN_HERE\")|TELEGRAM_BOT_TOKEN = \"$TELEGRAM_BOT_TOKEN_INPUT\"|" config.py
    echo -e "${GREEN}[+] Telegram Bot Token updated in config.py${NC}"
else
    echo -e "${RED}[!] Telegram Bot Token not provided. Please edit config.py manually.${NC}"
fi

if [ -n "$AI_API_KEY_INPUT" ]; then
    sed -i "s|AI_API_KEY = os.getenv(\"AI_API_KEY\", \"YOUR_AI_API_KEY_HERE\")|AI_API_KEY = \"$AI_API_KEY_INPUT\"|" config.py
    echo -e "${GREEN}[+] AI API Key updated in config.py${NC}"
else
    echo -e "${YELLOW}[-] AI API Key not provided. AI features will be limited or require manual configuration.${NC}"
fi

# --- 6. Make the bot executable ---
chmod +x bot.py
chmod +x tdftech.py

echo -e "\n${GREEN}[+] Setup complete!${NC}"
echo -e "${CYAN}To run your tdftech Telegram Bot, execute:${NC}"
echo -e "${CYAN}python bot.py${NC}"
echo -e "\n${YELLOW}Remember to keep your bot token secure!${NC}"
