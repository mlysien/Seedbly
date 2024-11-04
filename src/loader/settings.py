<<<<<<< Updated upstream
﻿class Settings:
    """Contains application settings."""
=======
﻿"""
Contains entity represents application settings.
"""

class Settings:
    """Represents application settings."""

>>>>>>> Stashed changes
    def __init__(self, engine, stencil, size, connection_string):
        self.engine = engine
        self.stencil = stencil
        self.size = size
        self.connection_string = connection_string
