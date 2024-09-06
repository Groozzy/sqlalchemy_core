from datetime import date

from sqlalchemy import select

from database import sync_engine, Session
from tables import Author, Category, DeclarativeBase, Post


def create_tables() -> None:
    DeclarativeBase.metadata.create_all(sync_engine)


def create_session() -> Session:
    return Session()


def insert_authors() -> None:
    with create_session() as session:
        authors = (
            Author(name='Василий', surname='Васильев', email='vasya@gmail.com'),
            Author(name='Николай', surname='Николаев', email='kolya@mail.ru'),
            Author(name='Ольга', surname='Форточкина', email='olya@yandex.ru'),
        )
        session.add_all(authors)
        session.commit()


def insert_categories() -> None:
    with create_session() as session:
        categories = (
            Category(name='Путешествия'),
            Category(name='Литература'),
            Category(name='Музыка'),
        )
        session.add_all(categories)
        session.commit()


def insert_posts() -> None:
    with create_session() as session:
        posts = (
            Post(
                author_email='vasya@gmail.com',
                category_id=1,
                title='10 лайфхаков для перелётов',
                text='Сегодня мы рассмотрим...',
                published=date(2020, 1, 1),
            ),
            Post(
                author_email='kolya@mail.ru',
                category_id=2,
                title='Топ 3 книг по финансам',
                text='Сегодня мы рассмотрим...',
                published=date(2023, 12, 7),
            ),
            Post(
                author_email='olya@yandex.ru',
                category_id=2,
                title='О чём книга "Приключения Тома Сойера"',
                text='Сегодня мы рассмотрим...',
                published=date(2022, 6, 9),
            ),
        )
        session.add_all(posts)
        session.commit()


def get_posts_authors() -> list:
    with create_session() as session:
        return [post.author for post in session.query(Post).all()]


def select_posts_by_category(category_id: int) -> list:
    with create_session() as session:
        return session.query(Post).filter_by(category_id=category_id).all()


def delete_post_by_id(post_id: int) -> None:
    with create_session() as session:
        session.query(Post).filter_by(id=post_id).delete()
        session.commit()


def select_all_data() -> list:
    with create_session() as session:
        return session.query(Post, Category, Author).all()
        # statement = (
        #         select(Post.title, Category.name, Author.surname)
        #         .join(Category, Post.category_id == Category.id)
        #         .join(Author, Post.author_email == Author.email)
        #     )
        # return session.execute(statement).fetchall()


def count_posts_by_category(category_id: int) -> int:
    with create_session() as session:
        return session.query(Post).filter_by(category_id=category_id).count()
