### **How to Run Tests:**

Clone the repository and navigate to the `/tests` directory:
```
git clone https://github.com/temirovazat/sqlite-to-postgres.git
```
```
cd sqlite-to-postgres/tests/
```

Create a .env file and add test settings:
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

Deploy and run the tests in containers:
```
docker-compose up --build
```