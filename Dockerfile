
FROM python:3.11-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./
COPY app ./app
COPY scripts ./scripts
COPY alembic ./alembic
COPY alembic.ini .


RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction

EXPOSE 8000


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]