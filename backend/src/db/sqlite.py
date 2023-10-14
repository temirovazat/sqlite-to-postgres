import sqlite3
from contextlib import contextmanager
from typing import Iterator

from pydantic import BaseSettings, Field


@contextmanager
def get_sqlite(db_path: str) -> Iterator[sqlite3.Connection]:
    """
    Context manager function for connecting to a SQLite database.

    Args:
        db_path: Path to the database file

    Yields:
        sqlite3.Connection: Connection to the database
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()


class SQLiteSettings(BaseSettings):
    """Class for validating SQLite connection settings."""

    db_path: str = Field(env='sqlite_path', default='../../infra/data/db.sqlite')
