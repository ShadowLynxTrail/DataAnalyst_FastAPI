
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

## ML-модель

Для предсказания количества продаж используется модель RandomForestRegressor, обученная на исторических данных. Модель сохранена в `app/ml_models/`.


Пример запроса:
```json
  {
  "date": "2023-01-01",
  "category": "Расходные материалы",
  "region": "Москва",
  "product_name": "Шприцы 5 мл",
  "price": 15.0
  }
 
 ```
  ##Запуск локально
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
- `POST /predict/sales` (требует авторизацию)

## Автор
ShadowLynxTrail

