from django.contrib.auth.models import User
from rest_framework import serializers
from todos.models import *
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'todos']
