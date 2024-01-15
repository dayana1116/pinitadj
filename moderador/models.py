from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Moderador(models.Model):
    idmoderador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    fechanacimiento = models.DateField(db_column='fechaNacimiento')  # Field name made lowercase.
    nacionalidad = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=120)
    telefono = models.CharField(max_length=10)
    email_mod = models.CharField(max_length=40)
    observaciones = models.CharField(max_length=200)
    password = models.CharField(max_length=12)

    class Meta:
        managed = True
        db_table = 'moderador'

class Post(models.Model):
    idpost = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=110)
    contenido = models.CharField(max_length=5000)
    imagen = models.TextField()
    tipoimagen = models.CharField(max_length=45)
    fecha = models.DateField()
    autor = models.CharField(max_length=80)
    extracto = models.CharField(max_length=400)
    idmoderador = models.ForeignKey(Moderador, models.DO_NOTHING, db_column='idmoderador')

    def __str__(self):
        return self.titulo
   
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

        super(Post, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'post'

   