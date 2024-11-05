"""
Seedbly engine
Version: 0.0.1
"""
from engine.core.main import DatabaseEngine
from engine.drivers.sqlite import create_sqlite_schema

def setup_engine(engine: DatabaseEngine):
    """
    Setup engine.
    :param engine:
    :return:
    """
    if engine == DatabaseEngine.SQLITE:
        create_sqlite_schema('', '')
