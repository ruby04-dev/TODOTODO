from rest_framework import serializers
from .models import *
from django.utils.translation import gettext_lazy as _


"""
HyperlinkedModelSerializer has the following differences from ModelSerializer:

It does not include the id field by default.
It includes a url field, using HyperlinkedIdentityField.
-> 'url', 'id' 를 Meta 클래스의 fields 리스트에 추가해야함

Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.

Because we've included format suffixed URLs such as '.json', 
we also need to indicate on the highlight field 
that any format suffixed hyperlinks it returns should use the '.html' suffix.
"""


class TodoSerializer(serializers.HyperlinkedModelSerializer):

    # The source argument controls which attribute is used to populate a field
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='todos:todo-highlight', format='html')

    class Meta:
        model = Todo
        fields = ['url', 'id', 'highlight',
                  'content', 'due_date', 'status', 'owner',]
        extra_kwargs = {'url': {'view_name': 'todos:todo-detail'}}

    """
    An automatically determined set of fields.
    Simple default implementations for the create() and update() methods.

    # TodoSerializer():
    # id = IntegerField(label='ID', read_only=True)
    # content = CharField(max_length=255)
    # due_date = DateTimeField(allow_null=True, required=False)
    # status = ChoiceField(choices=[('None', 'Pending'), ('1', 'To do'), ('2', 'In pregress'), ('3', 'Completed')], required=False)
    """


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


# inspect serializer
serializer = TodoSerializer()
print(repr(serializer))
"""
