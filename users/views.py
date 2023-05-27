
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework import permissions
# Create your views here.


@permission_classes([AllowAny])
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes([AllowAny])
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
