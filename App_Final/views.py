from django.shortcuts import render, redirect
from App_Final.models import *
from App_Final.forms import *
from django.contrib import messages
import django
from django.contrib.auth.decorators import login_required



# Create your views here.

# Vistas simples
def inicio(request):
    contexto = {}
    return render(request, 'index.html', contexto)

def contacto(request):
    contexto = {}
    return render(request, 'App_Final/contacto.html', contexto)

def terminos(request):
    contexto = {}
    return render(request, 'App_Final/terminos.html', contexto)

def privacidad(request):
    contexto = {}
    return render(request, 'App_Final/privacidad.html', contexto)

def acerca(request):
    contexto = {}
    return render(request, 'App_Final/acerca.html', contexto)

def resumen_anime(request):
    animes = Anime.objects.all()

    contexto = {
        'animes': animes
    }

    return render(request, 'App_Final/resumen_anime.html', contexto)

# Vistar de formularios
@login_required
def animeformulario(request):

    if request.method == 'POST':
        mi_formulario = Animeform(request.POST, request.FILES)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            anime_1 = Anime(titulo=data.get('titulo'),
                          fecha_de_creacion=data.get('fecha_de_creacion'),
                          episodios=data.get('episodios'),
                          temporadas=data.get('temporadas'),
                          origen=data.get('origen'),
                          personaje_principal=data.get('personaje_principal'),
                          sinopsis=data.get('sinopsis'),
                          autor=data.get('autor'),
                          genero=data.get('genero'),
                          imagen_del_anime=data.get('imagen_del_anime'),
                          puntuacion=data.get('puntuacion'),
                          creador=request.user)
            anime_1.save()

            messages.success(request, f"El anime {anime_1.titulo} fue creado con exito")

            return redirect('anime_form')

    contexto = {
        'form': Animeform(),
        'name_submit': 'Ingreso Anime',
        'name_form': 'Ingrese nuevo Anime'
    }

    return render(request, 'App_Final/formulario_general.html', contexto)

@login_required
def autorformulario(request):

    if request.method == 'POST':
        mi_formulario = Autorform(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            autor_1 = Autor(nombre_editorial=data.get('nombre_editorial'),
                          bibliografia=data.get('bibliografia'),
                          nacionalidad=data.get('nacionalidad'))
            autor_1.save()
            messages.success(request, f"El autor {autor_1.nombre_editorial} fue ingresado con exito")

            return redirect('autor_form')

    contexto = {
        'form': Autorform(),
        'name_submit': 'Ingreso Autor',
        'name_form': 'Ingrese nuevo Autor'
    }

    return render(request, 'App_Final/formulario_general.html', contexto)

@login_required
def generoformulario(request):

    if request.method == 'POST':
        mi_formulario = Generoform(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            genero_1 = Genero(nombre=data.get('nombre'),
                              detalle=data.get('detalle'))
            genero_1.save()
            messages.success(request, f"El anime {genero_1.nombre} fue creado con exito")

            return redirect('genero_form')

    contexto = {
        'form': Generoform(),
        'name_submit': 'Ingreso Genero',
        'name_form': 'Ingrese nuevo Genero'
    }

    return render(request, 'App_Final/formulario_general.html', contexto)

# Mostrando datos de DB
def mostrar_anime(request):

    animes = Anime.objects.all()

    contexto = {
        'animes': animes
    }

    return render(request, 'App_Final/mostrar_anime.html', contexto)

def mostrar_autor(request):

    autores = Autor.objects.all()

    contexto = {
        'autores': autores
    }

    return render(request, 'App_Final/mostrar_autor.html', contexto)

def mostrar_genero(request):

    generos = Genero.objects.all()

    contexto = {
        'generos': generos
    }

    return render(request, 'App_Final/mostrar_genero.html', contexto)

# Busqueda de datos
def buscar_anime_get(request):
    titulo = request.GET.get('titulo')

    animes = Anime.objects.filter(titulo__icontains=titulo)

    contexto ={
        'animes': animes
    }

    return render(request, 'App_Final/mostrar_anime.html', contexto)

def buscar_anime(request):
    
    contexto = {
        'form': Animebuscarform,
        'name_submit': 'Buscar Anime',
        'name_form': 'Escribe el nombre del anime que buscas'
    }

    return render(request, 'App_Final/mostrar_anime.html', contexto)

# Eliminar Datos
@login_required
def eliminar_anime(request, titulo):

    anime_eliminar = Anime.objects.get(titulo=titulo)
    anime_eliminar.delete()

    messages.success(request, f"El anime {anime_eliminar.titulo} fue eliminado con exito")

    return redirect("mostrar_anime")

@login_required
def eliminar_autor(request, nombre_editorial):

    autor_eliminar = Autor.objects.get(nombre_editorial=nombre_editorial)
    autor_eliminar.delete()

    messages.success(request, f"El autor {autor_eliminar.nombre_editorial} fue eliminado con exito")

    return redirect("mostrar_autor")

@login_required
def eliminar_genero(request, nombre):

    genero_eliminar = Genero.objects.get(nombre=nombre)
    genero_eliminar.delete()

    messages.success(request, f"El genero {genero_eliminar.nombre} fue eliminado con exito")

    return redirect("mostrar_genero")

# Editar Datos
@login_required
def editar_anime(request, titulo):

    anime_editar = Anime.objects.get(titulo=titulo)

    if request.method == 'POST':
        mi_formulario = Animeform(request.POST, request.FILES)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            anime_editar.titulo = data.get('titulo')
            anime_editar.autor = data.get('autor')
            anime_editar.fecha_de_creacion = data.get('fecha_de_creacion')
            anime_editar.episodios = data.get('episodios')
            anime_editar.temporadas = data.get('temporadas')
            anime_editar.origen = data.get('origen')
            anime_editar.genero = data.get('genero')
            anime_editar.personaje_principal = data.get('personaje_principal')
            anime_editar.sinopsis = data.get('sinopsis')
            anime_editar.imagen_del_anime = data.get('imagen_del_anime')
            anime_editar.puntuacion = data.get('puntuacion')
            try:
                anime_editar.save()
                messages.success(request, f"El anime {anime_editar.titulo} fue editado con exito")
            except django.db.utils.IntegrityError:
                messages.error(request, "La modificacion fallo por que en anime ya existe")

            return redirect('mostrar_anime')


    contexto = {
        'form': Animeform(
            initial={
                "titulo": anime_editar.titulo,
                "autor": anime_editar.autor,
                "fecha_de_creacion": anime_editar.fecha_de_creacion,
                "episodios": anime_editar.episodios,
                "temporadas": anime_editar.temporadas,
                "origen": anime_editar.origen,
                "genero": anime_editar.genero,
                "personaje_principal": anime_editar.personaje_principal,
                "sinopsis": anime_editar.sinopsis,
                "imagen_del_anime": anime_editar.imagen_del_anime,
                "puntuacion": anime_editar.puntuacion
            }
        ),
        'name_form': 'Ingrese nuevos datos',
        'name_submit': 'Editar anime'
    }


    return render(request, 'App_Final/formulario_general.html', contexto)