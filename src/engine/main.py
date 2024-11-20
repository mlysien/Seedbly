from termcolor import colored
from engine.core import DatabaseEngine
from schemas.blog.engines.main import generate_sqlite_blog_database


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
        generate_sqlite_blog_database(engine_params['database'], script, engine_params['size'])


    print(colored('\u2713', 'green'), colored('Engine setup successful!', 'white'))
