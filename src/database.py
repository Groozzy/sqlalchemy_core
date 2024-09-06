from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings


settings = Settings(_env_file='.env')

sync_engine = create_engine(
    settings.DB_URL,
    echo=True,
    pool_size=5,
    max_overflow=5,
)

async_engine = create_async_engine(
    settings.DB_URL,
    echo=True,
    pool_size=5,
    max_overflow=5
)

Session = sessionmaker(bind=sync_engine)
