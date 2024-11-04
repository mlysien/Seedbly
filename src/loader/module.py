import json
from loader import *
from json import JSONDecodeError

from termcolor import colored
<<<<<<< Updated upstream
=======

from loader import settings
>>>>>>> Stashed changes

settings_file_path = 'settings.json'

<<<<<<< Updated upstream
def as_settings(dct):
    return Settings(dct['engine'], dct['stencil'], dct['size'], dct['connection-string'])
=======

def as_settings(dct) -> settings.Settings:
    """Loads settings from local file and parse to ``Settings`` entity."""
    return settings.Settings(dct['engine'], dct['stencil'], dct['size'], dct['connection-string'])
>>>>>>> Stashed changes


def load_settings() -> settings.Settings:
    """Loads settings from local file and parse to ``Settings`` entity."""
    try:
        json_file = open(settings_file_path, mode="r")
        loaded_settings = json.load(json_file, object_hook=as_settings)

        print(colored('\u2713', 'green'), colored('Settings loaded successful!', 'white'))

        return loaded_settings

    except FileNotFoundError:
<<<<<<< Updated upstream
        print(colored(f'File "{settings_file_path}" not found!', 'red'))

    except JSONDecodeError:
        print(colored(f'Settings file has invalid structure!', 'red'))
=======
        print(colored(f'File "{SETTINGS_FILE_PATH}" not found!', 'red'))
        return settings.Settings('', '', 1, '')

    except JSONDecodeError:
        print(colored('Settings file has invalid structure!', 'red'))
        return settings.Settings('', '', 1, '')
>>>>>>> Stashed changes
