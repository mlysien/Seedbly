import sqlite3

def create_sqlite_schema(database_name, schema_script):
    """
    Creating database schema based on passed schema parameter.
    :param database_name: name of database.
    :param schema_script: schema script.
    :return:
    """
    db = sqlite3.connect(database_name)
    cursor = db.cursor()
    cursor.executescript(schema_script)
    db.commit()
    db.close()
