import json
from loader import *
from json import JSONDecodeError
from termcolor import colored

settings_file_path = 'settings.json'

def as_settings(dct):
    return Settings(dct['engine'], dct['stencil'], dct['size'], dct['connection-string'])


def load_settings() -> Settings:
    """Loads settings from local file and parse to ``Settings`` entity."""
    try:
        json_file = open(settings_file_path, mode="r")
        loaded_settings = json.load(json_file, object_hook=as_settings)

        print(colored('\u2713', 'green'), colored('Settings loaded successful!', 'white'))

        return loaded_settings

    except FileNotFoundError:
        print(colored(f'File "{settings_file_path}" not found!', 'red'))

    except JSONDecodeError:
        print(colored(f'Settings file has invalid structure!', 'red'))
