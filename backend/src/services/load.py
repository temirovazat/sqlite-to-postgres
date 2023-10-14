from typing import Dict, List

from psycopg2.extensions import connection as _connection
from psycopg2.extras import register_uuid
from pydantic.dataclasses import dataclass

from services.base import Config
from models.film_work import Filmwork
from models.genre import Genre, GenreFilmwork
from models.person import Person, PersonFilmwork


@dataclass(config=Config)
class PostgresLoader(object):
    """Class for executing PostgreSQL queries."""

    conn: _connection

    DATABASE = [
        ('person', Person),
        ('genre', Genre),
        ('film_work', Filmwork),
        ('genre_film_work', GenreFilmwork),
        ('person_film_work', PersonFilmwork),
    ]

    def __post_init__(self):
        """Upon initialization, create a database cursor object for database operations."""
        self.curs = self.conn.cursor()

    def get_columns(self, table: str) -> List[str]:
        """Retrieve the columns of a database table.

        Args:
            table: The table name.

        Returns:
            List[str]: A list of column names for the table.
        """
        query = """SELECT column_name from information_schema.columns
                WHERE table_name = '{table}' ORDER BY ordinal_position;"""
        self.curs.execute(query.format(table=table))
        return [row[0] for row in self.curs.fetchall()]

    def get_query_data(self, table: str, cnt_columns: int) -> Dict[str, str]:
        """Retrieve parameters for preparing an insert query into a table.

        Args:
            table: The table name.
            cnt_columns: The number of columns in the table.

        Returns:
            Dict[str, str]: Query parameters.
        """
        params = ['${0}'.format(param) for param in range(1, cnt_columns + 1)]
        return {
            'table': table,
            'statement': '{0}_insert'.format(table),
            'params': ', '.join(params),
        }

    def get_insert_query(self, statement: str, columns: List[str]) -> str:
        """Get an insert query for adding data to a table.

        Args:
            statement: The name of the prepared statement.
            columns: The column names of the table.

        Returns:
            str: The insert data query.
        """
        args = ['%({0})s'.format(name) for name in columns]
        query = 'EXECUTE {statement} ({args});'
        return query.format(statement=statement, args=', '.join(args))

    def prepare_insert(self, table: str) -> str:
        """Perform preparation for inserting data into a table.

        Args:
            table: The table name.

        Returns:
            str: The data insertion query.
        """
        register_uuid()
        columns = self.get_columns(table)
        data = self.get_query_data(table, len(columns))
        query = """PREPARE {statement} AS
            INSERT INTO {table} VALUES({params})
            ON CONFLICT (id) DO NOTHING;"""
        self.curs.execute(query.format(**data))
        return self.get_insert_query(data['statement'], columns)
