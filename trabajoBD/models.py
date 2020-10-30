from django.db import models

#superuser vgonzalez
#pass 1234
# Create your models here.
#user2 jaraya
#pass duoc2020

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    edad = models.IntegerField();
    email = models.EmailField();

    def __str__(self):
        return 'nombre :%s, apellido :%s, direccion :%s, edad :%s' % (self.nombre, self.apellido, self.direccion, self.edad)

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=500)
    link = models.URLField();

class Lanzamientos(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=300)

class Reviews(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    link = models.URLField();
