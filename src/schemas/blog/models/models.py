"""
Contains all entities of blog scripts.
"""

from datetime import datetime

class User:
    """
    Represents User entity.
    """
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
        self.joined_at = datetime.now()
        self.posts = []
        self.comments = []

class Post:
    """
    Represents Post entity.
    """
    def __init__(self, author: User, title: str, content: str, category: 'Category'):
        self.author = author
        self.title = title
        self.content = content
        self.category = category
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.comments = []
        self.tags = []
        self.likes = 0

class Category:
    """
    Represents Category entity.
    """
    def __init__(self, name: str):
        self.name = name
        self.posts = []

class Comment:
    """
    Represents Comment entity.
    """
    def __init__(self, author: User, content: str, post: Post):
        self.author = author
        self.content = content
        self.post = post
        self.created_at = datetime.now()

class Tag:
    """
    Represents Tag entity.
    """
    def __init__(self, name: str):
        self.name = name
        self.posts = []

class Like:
    """
    Represents Like entity.
    """
    def __init__(self, user: User, post: Post):
        self.user = user
        self.post = post
        self.liked_at = datetime.now()
