from sqlalchemy import (
    MetaData,
    Column, Table,
    Date, ForeignKey, Integer, String, Text,
)

metadata_obj = MetaData()

authors = Table(
    'authors',
    metadata_obj,
    Column('name', String(255)),
    Column('surname', String(255)),
    Column('email', String(255), primary_key=True),
)

categories = Table(
    'categories',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), unique=True, nullable=False),
)

posts = Table(
    'posts',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('author_email', ForeignKey('authors.email'), nullable=False),
    Column('category_id', ForeignKey('categories.id'), nullable=False),
    Column('title', String(255)),
    Column('text', Text),
    Column('published', Date),
)
