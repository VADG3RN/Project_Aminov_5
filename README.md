# Project_Aminov_5

Django-приложение для управления книгами (JSON/PostgreSQL, AJAX).

## Запуск в Docker Desktop

1. Установи Docker Desktop и запусти.
2. Клонируй: `git clone https://github.com/VADG3RN/Project_Aminov_5`
3. Создай `.env` в корне.
4. В терминале проекта: `docker compose up --build`
5. Миграции: `docker compose exec web python manage.py makemigrations` и `docker compose exec web python manage.py migrate`
6. Создай superuser: `docker compose exec web python manage.py createsuperuser`
7. Перенеси данные: `python migrate_data.py` (локально, host='localhost'). Или внутри: `docker compose exec web python migrate_data.py` (host='db').
8. Открой: http://localhost:8000/myapp3/add/
9. Останови: `docker compose down`.

## Миграция данных

1. Запусти Docker (БД готова).
2. Запусти `python migrate_data.py` (host='localhost' для локального, 'db' для внутри).
3. Скрипт читает `db.sqlite3` и вставляет в PostgreSQL.
4. Проверь в PostgreSQL: `docker compose exec db psql -U books_user -d books_db -c "SELECT * FROM myapp3_book;"`

## Функционал

- Выбор сохранения (JSON/PostgreSQL).
- Проверка дубликатов.
- Выбор источника просмотра.
- AJAX-поиск, редактирование, удаление.
- Bootstrap.

## Требования

- .dockerignore: игнорирует venv, sqlite.
- Секреты в .env (в .gitignore).
- Volumes: для БД и статики.

GitHub: https://github.com/VADG3RN/Project_Aminov_5
