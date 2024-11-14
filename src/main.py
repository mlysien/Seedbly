import inquirer
import loader

if __name__ == '__main__':
    setup = [
        inquirer.List(
            name='engine',
            carousel= True,
            message="What database engine you want to use?",
            choices=['SQLite', 'MS-SQL', 'PostgreSQL']
        ),
        inquirer.List(
            name='schema',
            carousel=True,
            message="What database schema you want to generate?",
            choices=['Blog', 'Library', 'University']
        ),
        inquirer.List(
            name='size',
            carousel=True,
            message="What size of database you want to generate?",
            choices=['Small', 'Medium', 'Big']
        )
    ]

    # get setup parameters
    parameters = inquirer.prompt(setup)

    # load settings
    settings = loader.load_settings()
