"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from todos.views import hello_rest_api, api_root
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', hello_rest_api, name='hello_rest_api'),
    path('', api_root),
    path('todos/', include('todos.urls')),
    path('users/', include('users.urls')),
]
# add login
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
