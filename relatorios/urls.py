from atexit import register
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('registrar/', view=register_user, name="register_user"),
    path('login/', view=login_user, name='login_user')
]
