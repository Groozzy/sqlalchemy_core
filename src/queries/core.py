from datetime import date

from sqlalchemy import func, insert, select, text

from database import async_engine, sync_engine
from tables import authors, categories, metadata_obj, posts


def print_version_sync():
    with sync_engine.connect() as conn:
        result = conn.execute(text("SELECT VERSION()"))
        print(f'{result.first()=}')


async def print_version_async():
    async with (async_engine.connect() as conn):
        res = await conn.execute(text("SELECT VERSION()"))
        print(f'{res.first()=}')


def create_tables():
    metadata_obj.create_all(sync_engine)


def drop_tables():
    metadata_obj.drop_all(sync_engine)


def insert_authors():
    with sync_engine.connect() as conn:
        statement = insert(authors).values(
            [
                {
                    'name': 'Василий',
                    'surname': 'Васильев',
                    'email': 'vasya@gmail.com',
                },
                {
                    'name': 'Николай',
                    'surname': 'Николаев',
                    'email': 'kolya@mail.ru',
                },
                {
                    'name': 'Ольга',
                    'surname': 'Форточкина',
                    'email': 'olya@yandex.ru',
                },
            ]
        )
        conn.execute(statement)
        conn.commit()


def insert_categories():
    with sync_engine.connect() as conn:
        statement = insert(categories).values(
            [
                {
                    'name': 'Путешествия',
                },
                {
                    'name': 'Литература',
                },
                {
                    'name': 'Музыка',
                }
            ]
        )
        conn.execute(statement)
        conn.commit()


def insert_posts():
    with sync_engine.connect() as conn:
        # statement = f"""
        # INSERT INTO posts (author_email, category_id, title, text, published)
        # VALUES (
        #     'vasya@gmail.com',
        #     '1',
        #     '10 лайфхаков для перелётов',
        #     'Сегодня мы рассмотрим...',
        #     {date(2020, 1, 1)}
        # );
        # """
        # conn.execute(text(statement))
        statement = insert(posts).values(
            [
                {
                    'author_email': 'vasya@gmail.com',
                    'category_id': 1,
                    'title': '10 лайфхаков для перелётов',
                    'text': 'Сегодня мы рассмотрим...',
                    'published': date(2020, 1, 1),
                },
                {
                    'author_email': 'kolya@mail.ru',
                    'category_id': 2,
                    'title': 'Топ 3 книг по финансам',
                    'text': 'Сегодня мы рассмотрим...',
                    'published': date(2023, 12, 7),
                },
                {
                    'author_email': 'olya@yandex.ru',
                    'category_id': 2,
                    'title': 'О чём книга "Приключения Тома Сойера"',
                    'text': 'Сегодня мы рассмотрим...',
                    'published': date(2022, 6, 9),
                },
            ]
        )
        conn.execute(statement)
        conn.commit()


def select_posts_by_category(category_id):
    with sync_engine.connect() as conn:
        statement = select(posts).where(posts.c.category_id == category_id)
        return conn.execute(statement).fetchall()


def select_all_data():
    with sync_engine.connect() as conn:
        statement = (
            select(posts.c.title, categories.c.name, authors.c.surname)
            .join(categories, posts.c.category_id == categories.c.id)
            .join(authors, posts.c.author_email == authors.c.email)
        )
        return conn.execute(statement).fetchall()


def delete_post_by_id(post_id):
    with sync_engine.connect() as conn:
        statement = posts.delete().where(posts.c.id == post_id)
        conn.execute(statement)
        conn.commit()


def count_posts_by_category(category_id):
    with sync_engine.connect() as conn:
        statement = (
            select(func.count("*")).where(posts.c.category_id == category_id)
        )
        return conn.execute(statement).scalar()
