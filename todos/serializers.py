from rest_framework import serializers
from .models import *
from django.utils.translation import gettext_lazy as _


class TodoSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=255)
    due_date = serializers.DateTimeField(allow_null=True, required=False)
    # status = serializers.CharField(
    #     max_length=4,
    #     choices=Todo.Status.choices,
    #     default=Todo.Status.TODO,
    # )

    def create(self, validated_data):
        """
        Create and return a new `Todo` instance, given the validated data.
        """
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Todo` instance, given the validated data.
        """
        instance.content = validated_data.get('content', instance.content)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        # instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


# Test Code
"""
from todos.models import *
from todos.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# create new instance

todo = Todo(content="나의 할일")
todo.save()

# serialize

serializer = TodoSerializer(todo)
serializer.data
# {'content': '나의 할일', 'due_date': None}

content = JSONRenderer().render(serializer.data)
content
# b'{"content":"\xeb\x82\x98\xec\x9d\x98 \xed\x95\xa0\xec\x9d\xbc","due_date":null}'

# deserialize

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

serializer = TodoSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('content', '나의 할일'), ('due_date', None)])
serializer.save()
# <Todo: Todo object (3)>


# serialize queryset
serializer = TodoSerializer(Todo.objects.all(), many=True)
serializer.data
"""
