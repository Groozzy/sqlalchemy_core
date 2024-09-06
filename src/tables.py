from sqlalchemy import (
    MetaData,
    Column, Table,
    Date, ForeignKey, Integer, String, Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import registry

mapper_registry = registry()

# Declarative

DeclarativeBase = declarative_base()


class Author(DeclarativeBase):
    __tablename__ = 'authors'
    name = Column(String(255))
    surname = Column(String(255))
    email = Column(String(255), primary_key=True)
    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f'<Author(name={self.name}, surname={self.surname})>'


class Category(DeclarativeBase):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    posts = relationship("Post", back_populates="category")

    def __repr__(self):
        return f'<Category(name={self.name})>'


class Post(DeclarativeBase):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    text = Column(Text)
    published = Column(Date)
    author_email = Column(String(255), ForeignKey('authors.email'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    author = relationship(Author, lazy='select')
    category = relationship(Category, lazy='select')

    def __repr__(self):
        return f'<Post(id={self.id}, category={self.category})>'


# Imperative

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
