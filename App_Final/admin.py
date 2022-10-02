from django.contrib import admin
from App_Final.models import *

# Register your models here.
@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    # readonly_fields= ('titulo','autor')
    list_display=('id', 'titulo', 'autor', 'genero', 'episodios', 'temporadas', 'origen', 'fecha_de_creacion', 'personaje_principal', 'sinopsis', 'imagen_del_anime', 'puntuacion')
    ordering=('id',)
    search_fields=('titulo',)
    list_display_links=('titulo',)
    list_filter=('genero',)
    list_per_page=20


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display=('id','nombre_editorial', 'nacionalidad', 'bibliografia')
    ordering=('id',)
    search_fields=('nombre_editorial',)
    list_display_links=('nombre_editorial',)
    list_per_page=20


@admin.register(Genero)
class GeneroAdmon(admin.ModelAdmin):
    list_display=('id','nombre', 'detalle')
    ordering=('id',)
    search_fields=('nonbre',)
    list_display_links=('nombre',)
    list_per_page=20




