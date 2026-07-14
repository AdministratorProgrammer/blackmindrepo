from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.CYAN}  ____  {Fore.RED}_      {Fore.YELLOW}   _     {Fore.GREEN} ____  {Fore.BLUE}_  __ {Fore.MAGENTA}___  {Fore.WHITE}_   _ {Fore.CYAN}____  
{Fore.CYAN} |  _ \\ {Fore.RED}| |     {Fore.YELLOW} / \\   {Fore.GREEN}/ ___|{Fore.BLUE}| |/ /{Fore.MAGENTA}|_ _|{Fore.WHITE}| \\ | |{Fore.CYAN}|  _ \\ 
{Fore.CYAN} | |_) |{Fore.RED}| |     {Fore.YELLOW}/ _ \\ {Fore.GREEN}| |    {Fore.BLUE}| ' / {Fore.MAGENTA} | | {Fore.WHITE}|  \\| |{Fore.CYAN}| | | |
{Fore.CYAN} |  _ < {Fore.RED}| |___  {Fore.YELLOW}/ ___ \\{Fore.GREEN}| |___ {Fore.BLUE}| . \\ {Fore.MAGENTA} | | {Fore.WHITE}| |\\  |{Fore.CYAN}| |_| |
{Fore.CYAN} |_| \\_\\{Fore.RED}|_____|{Fore.YELLOW}/_/   \\_\\{Fore.GREEN}\\____|{Fore.BLUE}|_|\\_\\{Fore.MAGENTA}|___|{Fore.WHITE}|_| \\_|{Fore.CYAN}|____/ 
{Fore.MAGENTA}                                           by lxnd
"""

if __name__ == "__main__":
    print(BANNER)
    print(f"{Style.BRIGHT}{Fore.YELLOW} • BlackMind Tools v1.0 •{Style.RESET_ALL}")
