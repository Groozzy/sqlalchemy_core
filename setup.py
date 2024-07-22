from setuptools import setup, find_packages


setup(
    name='database',
    version='1.0.0',
    description='',
    packages=find_packages(),
    install_requires=[
        'alembic==1.13.1',
        'pydantic==1.10.8',
        'python-dotenv==1.0.1',
        'psycopg==3.1.19',
        'SQLAlchemy==2.0.31',
    ],
)
