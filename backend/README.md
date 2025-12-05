# FastAPI Template

Чистый темплейт для FastAPI проектов с PostgreSQL и Alembic.

## Структура проекта

```
app/
├── configs/         # Конфигурации (БД, настройки)
├── models/          # SQLAlchemy модели
├── routers/         # FastAPI роутеры
├── schemas/         # Pydantic схемы
├── services/        # Бизнес-логика
├── utils/           # Утилиты
└── main.py          # Точка входа
alembic/             # Миграции БД
```

## Быстрый старт

1. Скопируйте `.env.example` в `.env`
2. Настройте переменные окружения
3. Запустите проект:

```bash
docker-compose up --build
```

## Миграции БД

```bash
# Создать миграцию
alembic revision --autogenerate -m "Initial migration"

# Применить миграции
alembic upgrade head

# Откатить миграцию
alembic downgrade -1
```

## Разработка

Раскомментируйте примеры кода в файлах для начала разработки:
- `models/example.py` - пример модели
- `schemas/example.py` - пример схем
- `services/example_service.py` - пример сервиса
- `routers/example.py` - пример роутера

Не забудьте подключить роутер в `main.py`!
