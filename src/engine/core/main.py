from enum import Enum

class DatabaseEngine(Enum):
    """
    Represents database engines.
    """
    SQLITE = 1
    MSSQL = 2
    POSTGRESQL = 3
