from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    users = models.ManyToManyField('self', related_name='user', symmetrical=False)

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()