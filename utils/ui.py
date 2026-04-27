import sys

# ANSI Escape Codes for Colors
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

WATERMARK = f"{Colors.BOLD}{Colors.CYAN}[ tdftech ]{Colors.END}"

def print_banner():
    banner = f"""
{Colors.MAGENTA}╔══════════════════════════════════════════════════════╗
║ {Colors.CYAN}  _____  _____  ______ _______ ______ _____ _    _  {Colors.MAGENTA} ║
║ {Colors.CYAN} |_   _||  __ \|  ____|__   __|  ____/ ____| |  | | {Colors.MAGENTA} ║
║ {Colors.CYAN}   | |  | |  | | |__     | |  | |__ | |    | |__| | {Colors.MAGENTA} ║
║ {Colors.CYAN}   | |  | |  | |  __|    | |  |  __|| |    |  __  | {Colors.MAGENTA} ║
║ {Colors.CYAN}  _| |_ | |__| | |       | |  | |___| |____| |  | | {Colors.MAGENTA} ║
║ {Colors.CYAN} |_____||_____/|_|       |_|  |______\_____|_|  |_| {Colors.MAGENTA} ║
║                                                      ║
║ {Colors.YELLOW}         Powerful Telegram Bot Framework             {Colors.MAGENTA} ║
║ {Colors.GREEN}              Developed by tdftech                   {Colors.MAGENTA} ║
╚══════════════════════════════════════════════════════╝{Colors.END}
"""
    print(banner)

def log_info(message):
    print(f"{WATERMARK} {Colors.GREEN}[INFO]{Colors.END} {message}")

def log_error(message):
    print(f"{WATERMARK} {Colors.RED}[ERROR]{Colors.END} {message}")

def log_warning(message):
    print(f"{WATERMARK} {Colors.YELLOW}[WARNING]{Colors.END} {message}")
