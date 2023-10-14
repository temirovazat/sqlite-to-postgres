import sqlite3
from typing import Dict, Iterator, List

from pydantic.dataclasses import dataclass

from services.base import Config, LoadDataError, LoadTableError
from core.logger import logger


@dataclass(config=Config)
class SQLiteExtractor(object):
    """Class for executing SQLite queries."""

    conn: sqlite3.Connection

    def __post_init__(self):
        """Upon initialization, create a cursor object for working with the database."""
        self.curs = self.conn.cursor()

    def get_columns(self, table: str, cls_fields: Dict) -> str:
        """Retrieve the columns of a table that exist in the data class fields.

        Args:
            table: Table name.
            cls_fields: Data class fields.

        Returns:
            str: Comma-separated column names of the table.
        """
        query = 'PRAGMA table_info({table});'
        self.curs.execute(query.format(table=table))
        columns = [column['name'] for column in self.curs.fetchall()]
        return ', '.join(name for name in columns if name in cls_fields)

    def select_table(self, table: str, cls_fields: Dict):
        """Retrieve a database table.

        Args:
            table: Table name.
            cls_fields: Data class fields.

        Raises:
            LoadTableError: Error when loading the table.
        """
        query = 'SELECT {columns} FROM {table};'
        try:
            self.curs.execute(
                query.format(
                    table=table,
                    columns=self.get_columns(table, cls_fields),
                ),
            )
        except sqlite3.OperationalError as error:
            message = str(error)
            if message == 'no such table: {0}'.format(table):
                logger.error('Table {0} not found!')
            elif message == 'near "FROM": syntax error':
                logger.error(
                    'Table {0} has no fields {1}!'.format(table, *cls_fields),
                )
            raise LoadTableError(error)

    def get_object(self, row: sqlite3.Row, db_class: type) -> Dict:
        """Convert a table row into a data class object.

        Args:
            row: Table row.
            db_class: Data class.

        Raises:
            LoadDataError: Error when loading data.

        Returns:
            Dict: Data class object as a dictionary.
        """
        try:
            obj = db_class(**row)
        except TypeError as error:
            required_field = str(error).split()[-1]
            logger.error(
                'The required field {0} is missing in the row!'.format(required_field),
            )
            raise LoadDataError(error)
        return obj.__dict__

    def load_records(self, db_class: type, size: int) -> Iterator[List[Dict]]:
        """Load data in batches of the specified `size`.

        Args:
            db_class: Data class.
            size: Batch size.

        Yields:
            Iterator[List[Dict]]: Iterator with lists of database objects.
        """
        logger.info('Loading table {0}'.format(db_class.__name__))
        while data := self.curs.fetchmany(size):
            yield [self.get_object(row, db_class) for row in data]
        logger.info('Data loaded successfully!')
