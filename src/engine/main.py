from termcolor import colored
from engine.core import DatabaseEngine
from engine.drivers.postgresql import create_postgresql_schema
from engine.drivers.sqlite import create_sqlite_schema
from engine.drivers.mssql import create_mssql_schema

def __load_schema_script(engine, schema):
    """
    Loads schema script for specified engine and schema
    :param engine: Database engine
    :param schema: Database schema
    :return: Script file content
    """
    script_path = f'./schemas/{schema}/scripts/{schema}.schema.{engine}.sql'

    with open(script_path, encoding='utf-8') as script:
        return script.read()


def setup_engine(engine_params: dict[str, str]):
    """
    Setups engine.
    """
    script = __load_schema_script(engine_params['engine'], engine_params['schema'])

    if engine_params['engine'] == DatabaseEngine.SQLITE.value:
        create_sqlite_schema(engine_params['database'], script)

    if engine_params['engine'] == DatabaseEngine.MSSQL.value:
        create_mssql_schema(engine_params, script)

    if engine_params['engine'] == DatabaseEngine.POSTGRESQL.value:
        create_postgresql_schema(engine_params, script)

    print(colored('\u2713', 'green'), colored('Engine setup successful!', 'white'))
