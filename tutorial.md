## Project setup

```shell
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python -m venv .venv
source .venv/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django==3.2.18
pip install djangorestframework

# Set up a new project
django-admin startproject config .  # Note the trailing '.' character

python manage.py startapp users
python maange.py startapp todos
```

```python
# config/settings.py

INSTALLED_APPS = [
    'todos',
    'users',

    'rest_framework',
    ...
]
```

```python
# config/urls.py

from django.urls import path, include
from todos.views import hello_rest_api, api_root
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', hello_rest_api, name='hello_rest_api'),
    path('', api_root),
    path('todos/', include('todos.urls'))
]
```

```python
# todos/urls.py
from django.urls import path
from .views import TodoList, TodoDetail
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'todos'
urlpatterns = format_suffix_patterns([
    path('', TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo-detail'),,
])
```

```python
# todos/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Todo(models.Model):
    content = models.CharField(_(""), max_length=255)
```

```python
# todos/serializers.py

from rest_framework import serializers
from .models import *
from django.utils.translation import gettext_lazy as _


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # The source argument controls which attribute is used to populate a field
    class Meta:
        model = Todo
        fields = ['url', 'id','content',] ## hyperlinkedModelSerializer 사용시 'url', 'id' 포함
        extra_kwargs = {'url': {'view_name': 'todos:todo-detail'}} ## !! app_name 을 사용하려면 반드시 설정 !!
```

```python
# todos/views.py
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import mixins, generics, permissions, renderers, status

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def hello_rest_api(request):
    data = {'message': 'Hello, REST API!'}
    return Response(data)

# root endpoint
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def api_root(request, format=None):
    return Response({
        # use REST framework's reverse function in order to return fully-qualified URLs
        # URL patterns are identified by convenience names, declared in ./urls.py
        'todos': reverse('todos:todo-list', request=request, format=format)
    })

class TodoList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    List all Todos, or create a new Todo.

    The base class provides the core functionality,
    the mixin classes provide the .list() and .create() actions.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("request", request)
        return self.create(request, *args, **kwargs)

    # set owner field as request.user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    """
    Retrieve, update or delete a todo.

    the GenericAPIView class provide the core functionality,
    mixins provide the .retrieve(), .update() and .destroy()
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

```shell
# sync your database
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin

# runserver
python manage.py runserver

# test server in terminal windows
pip install httpie

http http://127.0.0.1:8000/todos/
http POST http://127.0.0.1:8000/todos/ content="print(123)"

```
