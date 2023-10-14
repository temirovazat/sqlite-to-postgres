## SQLite to PostgreSQL

[![python](https://img.shields.io/static/v1?label=python&message=3.8%20|%203.9%20|%203.10&color=informational)](https://github.com/temirovazat/sqlite-to-postgres/actions/workflows/main.yml)
[![dockerfile](https://img.shields.io/static/v1?label=dockerfile&message=published&color=2CB3E8)](https://hub.docker.com/r/temirovazat/sqlite_to_postgres)
[![lint](https://img.shields.io/static/v1?label=lint&message=flake8%20|%20mypy&color=brightgreen)](https://github.com/temirovazat/sqlite-to-postgres/actions/workflows/main.yml)
[![code style](https://img.shields.io/static/v1?label=code%20style&message=WPS&color=orange)](https://wemake-python-styleguide.readthedocs.io/en/latest/)
[![tests](https://img.shields.io/static/v1?label=tests&message=%E2%9C%94%2010%20|%20%E2%9C%98%200&color=critical)](https://github.com/temirovazat/sqlite-to-postgres/actions/workflows/main.yml)

### **Description**

_The goal of this project is to implement a script in [Python](https://www.python.org) to migrate data from [SQLite](https://sqlite.org) to [PostgreSQL](https://www.postgresql.org). The data includes information about movies, people, and genres. The code utilizes data classes, context managers for establishing and closing connections, and handles read and write errors. [Pytest](https://pytest.org) is used to check data integrity between tables in both databases._

### **Technologies**

```Python``` ```SQLite``` ```PostgreSQL``` ```PyTest``` ```Pydantic``` ```Docker```

### **How to Run the Project:**

Clone the repository and navigate to the `/infra` directory:

```
git clone https://github.com/temirovazat/sqlite-to-postgres.git
```
```
cd sqlite-to-postgres/infra/
```

Create a `.env` file and add project settings:

```
nano .env
```
```
# PostgreSQL
POSTGRES_DB=cinemax_database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# SQLite
SQLITE_PATH=/opt/sqilte_to_postgres/db.sqlite
```

Deploy and run the project in containers:

```
docker-compose up
```

Along with PostgreSQL, the associated admin panel [pgAdmin](https://www.pgadmin.org) is launched at:

```
http://127.0.0.1:5050
```