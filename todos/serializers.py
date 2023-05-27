from rest_framework import serializers
from .models import *


class TodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    publication_date = serializers.DateField()

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
