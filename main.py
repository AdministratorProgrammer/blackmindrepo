from colorama import Fore, Style, init
from core import banner
init(autoreset=True)

banner.glitch_banner("BLACKMIND")
print(f"{Style.BRIGHT}{Fore.YELLOW} • BlackMind Repository v1.0 • {Style.RESET_ALL}")