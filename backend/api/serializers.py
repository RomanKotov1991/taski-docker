"""Вернуть путь к корневому каталогу KOS."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Вернуть путь к корневому каталогу KOS."""

    class Meta:
        """Вернуть путь к корневому каталогу KOS."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
