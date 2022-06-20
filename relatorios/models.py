from secrets import choice
from django.db import models
from .choices_coordenacao import LISTA_COORDENACAO
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    sector_name = models.CharField(max_length=100, choices=LISTA_COORDENACAO)

    def __str__(self):
        return f'{self.sector_name}'
