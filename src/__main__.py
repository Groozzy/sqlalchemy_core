import asyncio

# from .queries import core
from .queries import orm

# SQLAlchemy Core ======================================================

# asyncio.run(core.print_version_sync())

# core.drop_tables()
# core.create_tables()
# core.insert_authors()
# core.insert_categories()
# core.insert_posts()

# print(core.select_posts_by_category(2))

# core.delete_post_by_id(2)
# print(core.select_all_data())

# print(core.count_posts_by_category(3))


# SQLAlchemy ORM =======================================================

# orm.create_tables()

# orm.insert_authors()
# orm.insert_categories()
# orm.insert_posts()

print(orm.get_posts_authors())
print(orm.select_posts_by_category(2))

orm.delete_post_by_id(2)
print(orm.select_posts_by_category(2))

print(orm.select_all_data())

print(orm.count_posts_by_category(1))
