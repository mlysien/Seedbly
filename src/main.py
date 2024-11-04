from loader import load_settings

if __name__ == '__main__':

    # load settings
    settings = load_settings()

    print(f'Settings loaded {settings.engine}')
