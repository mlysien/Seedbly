from termcolor import colored
from loader import load_settings

if __name__ == '__main__':
    # load settings
    settings = load_settings()

    print(colored('\u2713', 'green'), colored('Settings loaded successful!', 'white'))
    