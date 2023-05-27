from django.urls import path
from .views import UserList, UserDetail
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'users'
urlpatterns = format_suffix_patterns([
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
])
