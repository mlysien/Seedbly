import json
from json import JSONDecodeError
from termcolor import colored
from loader import settings

SETTINGS_FILE_PATH = 'settings.json'

def as_settings(dct) -> settings.Settings:
    """Loads settings from local file and parse to ``Settings`` entity."""
    return settings.Settings(dct['engine'], dct['stencil'], dct['size'], dct['connection-string'])

def load_settings() -> settings.Settings:
    """Loads settings from local file and parse to ``Settings`` entity."""
    try:
        with open(SETTINGS_FILE_PATH, 'r', encoding='utf-8') as json_file:
            loaded_settings = json.load(json_file, object_hook=as_settings)

        print(colored('\u2713', 'green'), colored('Settings loaded successful!', 'white'))

        return loaded_settings

    except FileNotFoundError:
        print(colored(f'File "{SETTINGS_FILE_PATH}" not found!', 'red'))
        return settings.Settings('', '', 0, '')

    except JSONDecodeError:
        print(colored('Settings file has invalid structure!', 'red'))
        return settings.Settings('', '', 0, '')
