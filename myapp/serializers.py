from rest_framework import serializers
from . import models


class TaskManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskManager
        fields = '__all__'