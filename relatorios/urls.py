from atexit import register
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('registrar', view=register_user, name="register_user"),
    path('tableEvent', view=table_event, name='table_event')
]
