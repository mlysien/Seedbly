import os
from termcolor import colored

from engine.main import setup_engine
from settings import provide_settings, provide_connection_params


def welcome_banner():
    """
    Displays welcome banner.
    """
    print(colored('Welcome in Seedbly - a tool for create database scripts\n', 'light_cyan'))

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

    # provide connection params
    params = provide_connection_params(settings['engine'])

    # merge two dictionaries and setup Seedbly engine
    setup_engine(settings | params)

    print(colored('\u2713', 'green'), colored('All tasks were executed successful!', 'white'))
