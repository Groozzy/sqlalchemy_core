import asyncio

from .queries import core

# asyncio.run(core.print_version_sync())

core.drop_tables()
core.create_tables()
core.insert_authors()
core.insert_categories()
core.insert_posts()

# print(core.select_posts_by_category(2))

# core.delete_post_by_id(2)
# print(core.select_all_data())

print(core.count_posts_by_category(3))
