from django.contrib import admin
from django.urls import path, include
from relatorios import views

urlpatterns = [
    path('test/', views.relatorio_table, name="relatorio_table"),
]
