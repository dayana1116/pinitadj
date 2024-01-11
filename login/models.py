from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
""" class Usuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=10)
    password = models.CharField(max_length=12)

    class Meta:
        managed = True
        db_table = 'usuario' """
