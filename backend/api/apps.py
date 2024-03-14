"""Вернуть путь к корневому каталогу KOS."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Вернуть путь к корневому каталогу KOS."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
