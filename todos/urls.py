from django.urls import path
from .views import TodoList, TodoDetail, TodoHighlight
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'todos'
urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('highlight/', TodoHighlight.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
