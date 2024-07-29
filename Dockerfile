<<<<<<< HEAD
# Используем базовый образ Python
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем poetry
RUN pip install poetry

# Копируем зависимости в контейнер
COPY poetry.lock pyproject.toml /app/

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-root

# Копируем код приложения в контейнер
COPY . /app/

# Команда для запуска приложения при старте контейнера
=======
# Используем базовый образ Python
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем poetry
RUN pip install poetry

# Копируем зависимости в контейнер
COPY poetry.lock pyproject.toml /app/

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-root

# Копируем код приложения в контейнер
COPY . /app/

# Команда для запуска приложения при старте контейнера
>>>>>>> b06ae89223852ac8726da1a522d7e09db2c8c7e7
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]