<<<<<<< HEAD

# Medical Analytics API

Этот проект — аналитический сервис для медицинских изделий. Он собирает данные о продажах, проводит исследовательский анализ (EDA) и предоставляет API для получения аналитики и предсказаний.

## Технологии

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic (миграции)
- JWT (аутентификация)
- Docker / docker-compose
- pandas, matplotlib, seaborn (EDA)
- pytest (тесты)

## Возможности

- Регистрация и аутентификация пользователей (JWT)
- CRUD для товаров и пользователей
- Генерация данных о продажах медицинских изделий
- Аналитические эндпоинты:
  - `/analytics/summary` — общая статистика
  - `/analytics/category_revenue` — выручка по категориям
  - `/analytics/top_products` — топ товаров
- Alembic-миграции для управления схемой БД

## Запуск локально

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/ShadowLynxTrail/DataAnalyst_FastAPI.git
   cd DataAnalyst_FastAPI
2. Установи зависимости:  
    ```bash
    poetry install
3. Запусти: 
    ```bash
    uvicorn app.main:app --reload 

## Эндпоинты
- `POST /auth/register`
- `POST /auth/login`
- `GET /analytics/summary`

## Автор
ShadowLynxTrail

