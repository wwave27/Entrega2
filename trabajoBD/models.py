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
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return 'nombre :%s, apellido :%s, direccion :%s, edad :%s' % (self.nombre, self.apellido, self.direccion, self.edad)

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to = '' ,null = True)
    created = models.DateTimeField(auto_now_add=True, null = True)
    update = models.DateTimeField(auto_now_add=True, null = True)

class Lanzamientos(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=300)
    imagen = models.ImageField(null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null = True)
    update = models.DateTimeField(auto_now_add=True, null = True)

class Reviews(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    imagen = models.ImageField(null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null = True)
    update = models.DateTimeField(auto_now_add=True, null = True)

class Tags(models.Model):
    nombre = models.CharField(max_length=30)
    sigla = models.CharField(max_length=10 , null = True)
    sigla2 = models.CharField(max_length=10, null = True, blank=True)