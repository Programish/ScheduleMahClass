import colorama
from colorama import Fore, Style, init

init(autoreset=True)

#ScheduleMahClass    
def Start():
    print()
    print(Fore.RED + Style.BRIGHT + '   _____     ', end='') 
    print(Fore.GREEN + '      ______')
    print(Fore.YELLOW + Style.BRIGHT + '  / ___/____', end='')
    print(Fore.MAGENTA + Style.BRIGHT + ' ___  / ____/')
    print(Fore.WHITE + Style.BRIGHT + '  \__ \/ __ ', end='')
    print(Fore.CYAN + Style.BRIGHT + '`__ \/ /     ')
    print(Fore.RED + Style.BRIGHT + ' ___/ / / /', end='') 
    print(Fore.GREEN + ' / / / /___   ') 
    print(Fore.YELLOW + Style.BRIGHT + '/____/_/ /_', end='')
    print(Fore.MAGENTA + Style.BRIGHT + '/ /_/\____/')

#EndOfDay
def End():
    print()
    print(Fore.RED + Style.BRIGHT + '    ______   ', end='') 
    print(Fore.GREEN + '   ____ ')
    print(Fore.YELLOW + Style.BRIGHT + '   / ____/___', end='')
    print(Fore.MAGENTA + Style.BRIGHT + '  / __ \\')
    print(Fore.WHITE + Style.BRIGHT + '  / __/ / __ \\', end='')
    print(Fore.CYAN + Style.BRIGHT + '/ / / /')
    print(Fore.RED + Style.BRIGHT + ' / /___/ /_/', end='') 
    print(Fore.GREEN + ' / /_/ / ') 
    print(Fore.YELLOW + Style.BRIGHT + '/_____/\____', end='')
    print(Fore.MAGENTA + Style.BRIGHT + '/_____/')
