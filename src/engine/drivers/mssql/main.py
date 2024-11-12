from pyodbc import connect
from termcolor import colored


def create_mssql_schema(connection_parameters: dict[str, str], mssql_script):
    """
    Creates MSSQL Server database schema
    :param connection_parameters: Collection of connection parameters
    :param mssql_script: MSSQL schema generator script
    """
    driver = 'SQL Server'
    server = connection_parameters['server']
    port = connection_parameters['port']
    database = connection_parameters['database']
    username = connection_parameters['username']
    password = connection_parameters['password']

    connection_string = (f'DRIVER={driver};'
                         f'SERVER={server},{port};'
                         f'DATABASE={database};'
                         f'UID={username};'
                         f'PWD={password}')

    connection = connect(connection_string)

    cursor = connection.cursor()
    cursor.execute(mssql_script)
    connection.commit()

    print(colored('\u2713', 'green'), colored('MSSQL schema created successfully!', 'white'))
