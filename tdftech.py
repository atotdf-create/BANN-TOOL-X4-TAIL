import os
import sys
import subprocess
import time
from utils.ui import Colors, WATERMARK, print_banner, log_info, log_error, log_warning

def clear_screen():
    os.system("clear")

def display_main_menu():
    clear_screen()
    print_banner()
    print(f"\n{WATERMARK} {Colors.BOLD}Main Menu:{Colors.END}")
    print(f"  {Colors.GREEN}1.{Colors.END} {Colors.CYAN}Setup Bot (Install dependencies & Configure){Colors.END}")
    print(f"  {Colors.GREEN}2.{Colors.END} {Colors.CYAN}Start Telegram Bot{Colors.END}")
    print(f"  {Colors.GREEN}3.{Colors.END} {Colors.CYAN}Run Mock AI Query (via bot command){Colors.END}")
    print(f"  {Colors.GREEN}4.{Colors.END} {Colors.CYAN}Run Mock Autotype (via bot command){Colors.END}")
    print(f"  {Colors.GREEN}5.{Colors.END} {Colors.CYAN}Run Mock Scan (via bot command){Colors.END}")
    print(f"  {Colors.RED}0.{Colors.END} {Colors.YELLOW}Exit{Colors.END}")
    print(f"\n{WATERMARK} {Colors.BOLD}Enter your choice:{Colors.END} ", end="")

def run_setup():
    log_info("Starting setup script...")
    try:
        subprocess.run(["bash", "setup.sh"], check=True)
        log_info("Setup script finished.")
    except subprocess.CalledProcessError as e:
        log_error(f"Setup script failed: {e}")
    input(f"\n{WATERMARK} {Colors.YELLOW}Press Enter to return to main menu...{Colors.END}")

def start_bot():
    log_info("Starting Telegram Bot. Press Ctrl+C to stop the bot and return to the menu.")
    try:
        # This will block until the bot is stopped with Ctrl+C
        subprocess.run(["python", "bot.py"], check=False) # check=False because Ctrl+C is a normal exit
    except KeyboardInterrupt:
        log_info("Bot stopped by user.")
    except Exception as e:
        log_error(f"Error starting bot: {e}")
    input(f"\n{WATERMARK} {Colors.YELLOW}Press Enter to return to main menu...{Colors.END}")

def run_bot_command(command_name, prompt_message):
    log_warning("This function is for demonstration. You need to run the bot first and send commands via Telegram.")
    log_info(f"Simulating command: /{command_name}")
    user_input = input(f"{WATERMARK} {Colors.GREEN}{prompt_message}{Colors.END} ")
    log_info(f"Command /{command_name} with input: \"{user_input}\" would be sent to the bot.")
    log_warning("Please start the bot (Option 2) and send this command directly in Telegram.")
    input(f"\n{WATERMARK} {Colors.YELLOW}Press Enter to return to main menu...{Colors.END}")

def main():
    while True:
        display_main_menu()
        choice = input()

        if choice == "1":
            run_setup()
        elif choice == "2":
            start_bot()
        elif choice == "3":
            run_bot_command("ask", "Enter your AI query: ")
        elif choice == "4":
            run_bot_command("autotype", "Enter message for autotype: ")
        elif choice == "5":
            run_bot_command("scan", "Enter target for scan: ")
        elif choice == "0":
            log_info("Exiting tdftech All-in-One Tool. Goodbye!")
            sys.exit(0)
        else:
            log_error("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
