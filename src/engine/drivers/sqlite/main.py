import sqlite3

def create_sqlite_schema(database_name, schema):
    """
    Creating database schema based on passed schema parameter.
    :param database_name: name of database.
    :param schema: content of schema.
    :return:
    """
    db = sqlite3.connect(database_name)
    cursor = db.cursor()
    cursor.execute(schema)
    db.commit()
    db.close()
