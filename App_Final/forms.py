from ctypes import alignment
from distutils.command.upload import upload
from django import forms

class Autorform(forms.Form):

    nombre_editorial = forms.CharField(max_length=40)
    nacionalidad = forms.CharField(max_length=40)
    bibliografia = forms.CharField(max_length=500, widget=forms.Textarea)

class Generoform(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    detalle = forms.CharField(max_length=500, widget=forms.Textarea)

class Animeform(forms.Form):

    titulo = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    episodios = forms.IntegerField(min_value=1)
    temporadas = forms.IntegerField(min_value=1)
    origen = forms.CharField(max_length=40)    
    fecha_de_creacion = forms.DateField()
    personaje_principal = forms.CharField(max_length=40)
    sinopsis = forms.CharField(widget=forms.Textarea)
    imagen_del_anime = forms.ImageField()
    puntuacion = forms.IntegerField(min_value=1, max_value=10)

class Animebuscarform(forms.Form):
    titulo = forms.CharField(max_length=40)



