from django.urls import path
from .views import TodoList, TodoDetail, TodoHighlight, TodoListHighlight
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'todos'
urlpatterns = format_suffix_patterns([
    path('', TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('<int:pk>/highlight', TodoHighlight.as_view(), name='todo-highlight'),
    path('highlight/', TodoListHighlight.as_view(), name='todo-list-highlight'),
])
