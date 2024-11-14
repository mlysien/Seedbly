import os
from termcolor import colored
from settings import provide_settings

def welcome_banner():
    """
    Displays welcome banner.
    """
    print(colored('Welcome in Seedbly - a tool for create database schemas\n', 'light_cyan'))

def clear_console():
    """
    Clears console depends on operating system.
    """
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':

    #clear console
    clear_console()

    # display welcome banner
    welcome_banner()

    # provide settings
    settings = provide_settings()

    print(colored('\u2713', 'green'), colored('Settings provided successful!', 'white'))
