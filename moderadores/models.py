from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Moderadore(models.Model):
    idmoderador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=41)
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    nacionalidad = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=120)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=40)
    observaciones = models.CharField(max_length=200)
    password = models.CharField(max_length=12)


    class Meta:
        managed = True
        db_table = 'moderadore'

class Post(models.Model):
    idpost = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=110, validators=[MinLengthValidator(1)])
    contenido = models.CharField(max_length=5000, validators=[MinLengthValidator(1)])
    fecha = models.DateField(default=timezone.now)
    autor = models.CharField(max_length=80, blank=True) # Permitir autor vacío
    extracto = models.CharField(max_length=400, validators=[MinLengthValidator(1)])
    


    class Meta:
        managed = True
        db_table = 'post'

    def __str__(self):
        return self.name

