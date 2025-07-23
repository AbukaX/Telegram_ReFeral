import os

# Порт из переменной окружения
bind = f"0.0.0.0:{os.environ.get('PORT', 5000)}"

# Количество воркеров
workers = 1

# Тип воркера
worker_class = "sync"

# Таймауты
timeout = 120
keepalive = 5

# Логирование
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Для корректной работы в контейнере
preload_app = True
