# auth_module
Простой модуль аутентификации для онлайн-образовательной платформы.

## Функционал
- Регистрация (`POST /auth/register`)
- Вход и выдача JWT (`POST /auth/login`)

## Технологии
- Python 3.10, Flask, SQLAlchemy, Bcrypt, PyJWT

## Запуск
1. `pip install -r requirements.txt`
2. Установить переменные окружения:
   - `SECRET_KEY`
   - `DATABASE_URL`
3. `export FLASK_APP=app.py`
4. `flask run`
