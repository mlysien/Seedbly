import psycopg2
from psycopg2 import sql

def create_postgresql_schema(connection_parameters: dict[str, str], schema_query):
    """
    Creating database schema based on schema query.
    :param connection_parameters: connection parameters.
    :param schema_query: schema query.
    :return:
    """
    try:
        conn = psycopg2.connect(**connection_parameters)
        conn.autocommit = True
        cursor = conn.cursor()

        # Define the schema creation SQL command
        create_schema_query = sql.SQL(schema_query).format(
            schema_name=sql.Identifier(connection_parameters['database'])
        )

        # Execute the SQL command
        cursor.execute(create_schema_query)

        print("Schema created successfully!")

    except psycopg2.DatabaseError as error:
        print(f"Error: {error}")

    finally:
        if conn:
            cursor.close()
            conn.close()
