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
    BLOG = 'blog'

class DatabaseEngine(Enum):
    """
    Represents database engines.
    """
    SQLITE = 'sqlite'
