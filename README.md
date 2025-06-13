# DDS
# Веб-сервис для управления движением денежных средств (ДДС)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-4.0-brightgreen.svg)](https://www.djangoproject.com/)

## 🛠 Установка зависимостей

```bash
# Клонирование репозитория
git clone https://github.com/ваш-username/название-репозитория.git
cd название-репозитория

# Создание виртуального окружения
python -m venv venv  # Windows/Linux
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt
```

## 🗃 Настройка базы данных

SQLite (по умолчанию)
```bash
python manage.py migrate
```

## 🚀 Запуск веб-сервиса

```bash
python manage.py runserver
```

## 🌐 Доступные URL

Основное приложение: http://127.0.0.1:8000
Админ-панель: http://127.0.0.1:8000/admin
API документация: http://127.0.0.1:8000/api/docs/
