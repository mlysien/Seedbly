import json

from loader import *

settings_file_path = 'settings.json'


def as_settings(dct):
    return Settings(dct['engine'], dct['stencil'], dct['size'], dct['connection-string'])


def load_settings() -> Settings:
    """Loads settings from local file and parse to ``Settings`` entity."""
    json_file = open(settings_file_path, mode="r")
    return json.load(json_file, object_hook=as_settings)
