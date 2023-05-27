from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(
        many=True, view_name='todos:todo-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'todos']
        extra_kwargs = {'url': {'view_name': 'users:user-detail'}}
