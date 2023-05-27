from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import *
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics


"""
Django REST Framework에서 뷰는 HTTP 요청을 처리하고 HTTP 응답을 반환하는 역할을 담당합니다.
뷰는 종종 시리얼라이저를 사용하여 클라이언트가 이해할 수 있는 형식으로 데이터를 반환합니다.
Django REST Framework는 APIView, GenericAPIView, ViewSet과 같은 여러 내장 뷰를 제공하여 
일반적인 작업을 처리하여 API 구축을 용이하게 합니다.
"""
"""
 If we send malformed json, or if a request is made with a method that the view doesn't handle, 
 then we'll end up with a 500 "server error" response. Still, this'll do for now.
"""
"""
http http://127.0.0.1:8000/Todos/ Accept:application/json  # Request JSON
http http://127.0.0.1:8000/Todos/ Accept:text/html         # Request HTML
http http://127.0.0.1:8000/Todos.json  # JSON suffix
http http://127.0.0.1:8000/Todos.api   # Browsable API suffix

# control the format of the request that we send, using the Content-Type header

# POST using form data
http --form POST http://127.0.0.1:8000/Todos/ code="print(123)"

# POST using JSON
http --json POST http://127.0.0.1:8000/Todos/ code="print(456)"

# If you add a --debug switch to the http requests above, you will be able to see the request type in request headers.



"""


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message': 'Hello, REST API!'}
    return Response(data)


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@permission_classes([AllowAny])
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

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@permission_classes([AllowAny])
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

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
