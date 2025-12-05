# FastAPI Template

Чистый темплейт для FastAPI проектов с PostgreSQL.

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
```

## Быстрый старт

1. Скопируйте `.env.example` в `.env`
2. Настройте переменные окружения
3. Запустите проект:

```bash
docker-compose up --build
```

## Разработка

Раскомментируйте примеры кода в файлах для начала разработки:
- `models/example.py` - пример модели
- `schemas/example.py` - пример схем
- `services/example_service.py` - пример сервиса
- `routers/example.py` - пример роутера

Не забудьте подключить роутер в `main.py`!
