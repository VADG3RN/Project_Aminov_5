import sqlite3
import psycopg2

# SQLite
sqlite_conn = sqlite3.connect('db.sqlite3')
sqlite_cursor = sqlite_conn.cursor()

# PostgreSQL
pg_conn = psycopg2.connect(
    dbname='books_db',
    user='books_user',
    password='books_password',
    host='db',  # запуск вне Docker - 'localhost'; внутри — 'db'
    port='5432'
)
pg_cursor = pg_conn.cursor()

# Перенос таблицы myapp3_book
sqlite_cursor.execute("SELECT author, title, genre, pages, year, created FROM myapp3_book")
rows = sqlite_cursor.fetchall()

for row in rows:
    pg_cursor.execute(
        "INSERT INTO myapp3_book (author, title, genre, pages, year, created) VALUES (%s, %s, %s, %s, %s, %s)",
        row
    )

pg_conn.commit()

pg_cursor.close()
pg_conn.close()
sqlite_cursor.close()
sqlite_conn.close()

print("Данные перенесены!")