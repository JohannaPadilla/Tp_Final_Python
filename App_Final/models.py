from distutils.command.upload import upload
from operator import truediv
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):

    nombre_editorial = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    bibliografia = models.CharField(max_length=500)
    fecha_creacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"Nombre completo o Editorial: {self.nombre_editorial} - Nacionalidad: {self.nacionalidad} - Fecha de creacion: {self.fecha_creacion} - Bibliografia: {self.bibliografia} "

class Genero(models.Model):
    
    nombre = models.CharField(max_length=40)
    detalle = models.CharField(max_length=500)
    fecha_creacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de creacion: {self.fecha_creacion} - Detalle: {self.detalle}"

class Anime(models.Model):
    
    titulo = models.CharField(max_length=40)
    fecha_de_creacion = models.DateField()
    episodios = models.IntegerField()
    temporadas = models.IntegerField()
    origen = models.CharField(max_length=40)
    personaje_principal = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=2000)
    fecha_creacion = models.DateField(auto_now=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True, blank=True)
    imagen_del_anime = models.ImageField(upload_to="imagenes", null=True, blank=True)
    puntuacion = models.IntegerField()

    def __str__(self):
        return f"Titulo: {self.titulo} - Episodios: {self.episodios} - Fecha de creacion: {self.fecha_creacion} - Temporadas: {self.temporadas} - Origen: {self.origen} - Personaje Principal: {self.personaje_principal} - Sinopsis: {self.sinopsis} - Fecha de lanzamiento: {self.fecha_de_creacion} -  Puntuacion: {self.puntuacion} - Autor: {self.autor} - Genero: {self.genero} - Imagen: {self.imagen_del_anime} "

class Imagen(models.Model):
    imagen_anime = models.ImageField(upload_to='imagenes', null=True, blank=True)
    anime = models.OneToOneField(Anime, on_delete=models.CASCADE, null=True, blank=True)

class mensaje(models.Model):
    nombre = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    mensaje = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Dejanos tu mensaje: {self.mensaje} - Nacionalidad: {self.nacionalidad} - Fecha de creacion: {self.fecha_creacion}"