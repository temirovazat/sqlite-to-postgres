from db.postgres import PostgresSettings
from db.sqlite import SQLiteSettings

SQLITE_PARAMS = SQLiteSettings(_env_file='.env').dict()

POSTGRES_PARAMS = PostgresSettings(_env_file='.env').dict()

RECORDS_SIZE = 100
