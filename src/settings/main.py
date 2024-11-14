import inquirer
from engine import DatabaseEngine
from engine.core.main import DatabaseSchemas

def provide_settings():
    """
    Displays interactive menu for provide required settings.
    """
    setup = [
        inquirer.List(
            name='engine',
            carousel= True,
            message="What database engine you want to use?",
            choices=[e.value for e in DatabaseEngine]
        ),
        inquirer.List(
            name='schema',
            carousel=True,
            message="What database schema you want to generate?",
            choices=[e.value for e in DatabaseSchemas]
        ),
        inquirer.List(
            name='size',
            carousel=True,
            message="What size of database you want to generate?",
            choices=['Small', 'Medium', 'Big']
        )
    ]

    # return setup parameters
    return inquirer.prompt(setup)
