import inquirer

from engine.core import DatabaseEngine, DatabaseSchemas, DatabaseSchemaSizes


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
            choices=[e.value for e in DatabaseSchemaSizes]
        )
    ]

    # return setup parameters
    return inquirer.prompt(setup)

def provide_connection_params(engine):
    """
    Displays interactive menu for provide required settings.
    """

    if engine == DatabaseEngine.SQLITE.value:
        setup = [
            inquirer.Text("database", message="Enter SQLite database name", default="local"),
        ]

        # return connection parameters for sqlite
        return inquirer.prompt(setup)

    return -1
