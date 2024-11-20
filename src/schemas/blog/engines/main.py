import random
import sqlite3
import time
import uuid
from faker import Faker

from engine.core import DatabaseSchemaSizes


def generate_sqlite_blog_database(database, script, size):
    """
    Generates SQLite blog database based on script
    :param database: Name of database
    :param script: Script for create database
    :param size: Size of database data to generate
    """
    # create sqlite schema
    connection = sqlite3.connect(f'{database}.db')
    cursor = connection.cursor()
    cursor.executescript(script)
    connection.commit()

    # prepare size
    size_params = __get_data_size_params(size)

    # generate data
    __generate_data(connection, size_params)


def __get_data_size_params(size):
    """
    Returns database data size parameters by selected size
    :param size: Selected database data size
    """
    if size == DatabaseSchemaSizes.SMALL.value:
        return {
            'num_users': 500,
            'num_categories': 50,
            'num_posts': 1000,
            'num_comments': 800,
            'num_tags': 50,
            'num_likes': 6000
        }

    if size == DatabaseSchemaSizes.MEDIUM.value:
        return {
            'num_users': 50000,
            'num_categories': 500,
            'num_posts': 10000,
            'num_comments': 8000,
            'num_tags': 500,
            'num_likes': 60000
        }

    if size == DatabaseSchemaSizes.BIG.value:
        return {
            'num_users': 1000000,
            'num_categories': 10000,
            'num_posts': 1000000,
            'num_comments': 1100000,
            'num_tags': 5000,
            'num_likes': 1000000
        }

    return {}


def __generate_data(connection, params):
    """
    Generates database data
    :param connection: Connection to database
    :param params: Database data parameters
    """
    # generate Users
    __generate_users(connection, params['num_users'])

    # generate Categories
    __generate_categories(connection, params['num_categories'])

    # generate Posts
    __generate_posts(connection, params['num_posts'])

    # generate Comments
    __generate_comments(connection, params['num_comments'])

    # generate Tags
    __generate_tags(connection, params['num_tags'])

    # generate PostTags
    __generate_post_tags(connection)

    # generate Likes
    __generate_likes(connection, params['num_likes'])


def __generate_users(connection, num_users):
    """
    Generates users
    """
    faker = Faker()

    cursor = connection.cursor()
    start_time = time.time()

    print(f'💣 Generating {num_users} rows for "User" table...')

    emails = [
        f'{faker.user_name()}{uuid.uuid4().hex[:6].upper()}@{faker.domain_name()}'
        for _ in range(num_users)
    ]

    for email in emails:
        cursor.execute("INSERT INTO [User] (username, email, password, joined_at) "
                       "VALUES (?, ?, ?, ?)",
                       (faker.name(), email, faker.password(), faker.date_time_this_decade()))

    connection.commit()

    print(f"💥 Done in {time.time() - start_time:.2f} seconds.")

def __generate_categories(connection, num_categories):
    """
    Generates categories
    """
    faker = Faker()
    cursor = connection.cursor()
    start_time = time.time()

    print(f'💣 Generating {num_categories} rows for "Category" table...')

    categories = [
        f'{faker.word().lower()}-{uuid.uuid4().hex[:6].upper()}'
        for _ in range(num_categories)
    ]

    for cat in categories:
        cursor.execute("INSERT INTO Category (name) VALUES (?)", (cat,))

    connection.commit()

    print(f"💥 Done in {time.time() - start_time:.2f} seconds.")

def __generate_posts(connection, num_posts):
    """
    Generates posts
    """
    faker = Faker()
    cursor = connection.cursor()
    start_time = time.time()
    user_ids = [row[0] for row in cursor.execute("SELECT id FROM [User]").fetchall()]
    category_ids = [row[0] for row in cursor.execute("SELECT id FROM Category").fetchall()]

    print(f'💣 Generating {num_posts} rows for "Post" table...')

    for _ in range(num_posts):
        author_id = random.choice(user_ids)
        category_id = random.choice(category_ids) if category_ids else None
        cursor.execute("INSERT INTO Post (author_id, title, content, category_id, "
                       "created_at, updated_at, likes) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (author_id, faker.sentence(), faker.text(), category_id, faker.date_time_this_decade(),
             faker.date_time_this_decade(), random.randint(0, 100)))

    connection.commit()

    print(f"💥 Done in {time.time() - start_time:.2f} seconds.")


def __generate_comments(connection, num_comments):
    """
    Generates comments
    """
    faker = Faker()
    cursor = connection.cursor()
    start_time = time.time()
    user_ids = [row[0] for row in cursor.execute("SELECT id FROM [User]").fetchall()]
    post_ids = [row[0] for row in cursor.execute("SELECT id FROM Post").fetchall()]

    print(f'💣 Generating {num_comments} rows for "Comment" table...')

    for _ in range(num_comments):
        author_id = random.choice(user_ids)
        post_id = random.choice(post_ids)
        cursor.execute("INSERT INTO Comment (author_id, post_id, content, created_at) "
                       "VALUES (?, ?, ?, ?)",
                       (author_id, post_id, faker.text(), faker.date_time_this_decade()))

    connection.commit()

    print(f"💥 Done in {time.time() - start_time:.2f} seconds.")


def __generate_tags(connection, num_tags):
    """
    Generates tags
    """
    faker = Faker()
    cursor = connection.cursor()
    start_time = time.time()

    print(f'💣 Generating {num_tags} rows for "Tag" table...')

    tags = [f'#{faker.word().upper()}{uuid.uuid4().hex[:6].upper()}'
            for _ in range(num_tags)]

    for tag in tags:
        cursor.execute("INSERT INTO Tag (name) VALUES (?)", (f'#{tag}',))

    connection.commit()

    print(f"💥 Done in {time.time() - start_time:.2f} seconds.")

def __generate_post_tags(connection):
    """
    Links posts with tags
    """
    cursor = connection.cursor()
    start_time = time.time()
    post_ids = [row[0] for row in cursor.execute("SELECT id FROM Post").fetchall()]
    tag_ids = [row[0] for row in cursor.execute("SELECT id FROM Tag").fetchall()]

    print('💣 Linking posts with tags...')

    for post_id in post_ids:
        tags_for_post = random.sample(tag_ids, k=random.randint(1, min(len(tag_ids), 3)))
        for tag_id in tags_for_post:
            cursor.execute("INSERT INTO PostTag (post_id, tag_id) VALUES (?, ?)", (post_id, tag_id))

    connection.commit()

    print(f"💥 Done in {time.time() - start_time:.2f} seconds.")

def __generate_likes(connection, num_likes):
    """
    Generates likes:
    """
    faker = Faker()
    cursor = connection.cursor()
    likes_set = set()
    start_time = time.time()
    post_ids = [row[0] for row in cursor.execute("SELECT id FROM Post").fetchall()]
    user_ids = [row[0] for row in cursor.execute("SELECT id FROM [User]").fetchall()]

    print(f'💣 Generating {num_likes} rows for "Like" table...')

    for _ in range(num_likes):
        user_id = random.choice(user_ids)
        post_id = random.choice(post_ids)
        if (user_id, post_id) not in likes_set:
            likes_set.add((user_id, post_id))
            cursor.execute("INSERT INTO [Like] (user_id, post_id, liked_at) VALUES (?, ?, ?)",
                           (user_id, post_id, faker.date_time_this_decade()))

    connection.commit()

    print(f"💥 Done in {time.time() - start_time:.2f} seconds.")
