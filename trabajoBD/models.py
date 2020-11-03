from django.db import models

#superuser vgonzalez
#pass 1234
#user2 jaraya
#pass duoc2020
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    fecnac = models.DateField()
    email = models.EmailField()
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    playstation = models.BooleanField()
    xbox = models.BooleanField()
    nintendo = models.BooleanField()
    pc = models.BooleanField()
    retro = models.BooleanField()

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to = '' ,null = True)
    created = models.DateTimeField(auto_now_add=True, null = True)
    update = models.DateTimeField(auto_now_add=True, null = True)
    playstation = models.BooleanField()
    xbox = models.BooleanField()
    nintendo = models.BooleanField()
    pc = models.BooleanField()
    retro = models.BooleanField()

    def __str__(self):
        return self.titulo

class Lanzamientos(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=300)
    imagen = models.ImageField(null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null = True)
    update = models.DateTimeField(auto_now_add=True, null = True)
    playstation = models.BooleanField()
    xbox = models.BooleanField()
    nintendo = models.BooleanField()
    pc = models.BooleanField()
    retro = models.BooleanField()

    def __str__(self):
        return self.titulo

class Reviews(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    imagen = models.ImageField(null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null = True)
    update = models.DateTimeField(auto_now_add=True, null = True)
    playstation = models.BooleanField()
    xbox = models.BooleanField()
    nintendo = models.BooleanField()
    pc = models.BooleanField()
    retro = models.BooleanField()

    def __str__(self):
        return self.titulo


class Tags(models.Model):
    nombre = models.CharField(max_length=30)
    sigla = models.CharField(max_length=10 , null = True)
    sigla2 = models.CharField(max_length=10, null = True, blank=True)
