from __future__ import with_statement

import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool, sql

from alembic import context


sys.path = ["", ".."] + sys.path[1:]

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None

from src.schemas import DBSchemas  # noqa: E402
from src.config.db import target_metadata  # noqa: E402
from src.config import settings  # noqa: E402

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url():
    user = settings.postgres.USER
    password = settings.postgres.PASS
    host = settings.postgres.HOST
    port = settings.postgres.PORT
    db = settings.postgres.DB
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return url


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url", None)
    if not url:
        url = get_url()

    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    if not config.get_main_option("sqlalchemy.url", None):
        configuration["sqlalchemy.url"] = get_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            include_schemas=True,
        )

        for schema in DBSchemas:
            connection.execute(sql.text(f"CREATE SCHEMA IF NOT EXISTS {schema.value}"))

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
