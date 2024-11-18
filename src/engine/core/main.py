from enum import Enum

class DatabaseSchemaSizes(Enum):
    """
    Represents database schema sizes.
    """
    SMALL = 'Small'
    MEDIUM = 'Medium'
    BIG = 'Big'

class DatabaseSchemas(Enum):
    """
    Represents database scripts.
    """
    BLOG = 'Blog'
    LIBRARY = 'Library'
    UNIVERSITY = 'University'

class DatabaseEngine(Enum):
    """
    Represents database engines.
    """
    SQLITE = 'SQLite'
    MSSQL = 'MS-SQL'
    POSTGRESQL = 'PostgreSQL'
