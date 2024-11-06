import sqlite3

def create_sqlite_schema(database_name, schema_script_path):
    """
    Creating database schema based on passed schema parameter.
    :param database_name: name of database.
    :param schema_script_path: path of schema.
    :return:
    """
    with open(schema_script_path, 'r', encoding='utf-8') as schema_script:
        db = sqlite3.connect(database_name)
        cursor = db.cursor()
        cursor.executescript(schema_script.read())
        db.commit()
        db.close()
