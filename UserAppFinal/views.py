from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from UserAppFinal.forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.success(request, 'Inicio de sesion satisfactorio. Bienvenido a tu sitio')
            else:
                messages.info(request, 'Inicio de sesión fallido. Verifique Usuario y Contraseña')
        else:
            messages.error(request, 'Inicio de sesion fallo. Intente nuevamente colocando los valores correctos.')

        return redirect('App_Final_Inicio')

    contexto = {
        'form': AuthenticationForm(),
        'name_form': 'Iniciar Sesión',
        'name_submit': 'Ingresar'
    }
    return render(request, 'UserAppFinal/formulario_user.html', contexto)

def registro(request):
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():
        
            form.save()
            messages.info(request, 'El usuario fue registrado satisfactoriamente.')
        else:
            messages.info(request, 'El usuario no puedo ser registrado')

        return redirect('App_Final_Inicio')

    contexto = {
        # 'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'name_form': 'Registro',
        'name_submit': 'Registrar Usuario'
    }

    return render(request, 'UserAppFinal/formulario_user.html', contexto)

@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserEditForm(request.POST)

        if form.is_valid():
        
            data = form.cleaned_data

            usuario.username = data.get('username')
            usuario.email = data.get('email')
            usuario.first_name = data.get('first_name')
            usuario.last_name = data.get('last_name')

            usuario.save()

            messages.success(request, 'El usuario fue modificado satisfactoriamente.')
        else:
            messages.error(request, 'El usuario no puedo ser modificado')

        return redirect('App_Final_Inicio')


    contexto = {
        # 'form': UserCreationForm(),
        'form': UserEditForm(
            initial={
                'username': usuario.username,
                'email': usuario.email, 
                'first_name': usuario.first_name,
                'last_name': usuario.last_name
            }),
        'name_form': 'Datos de usuario',
        'name_submit': 'Guardar cambios'
    }

    return render(request, 'UserAppFinal/formulario_user.html', contexto)

@login_required
def upload_avatar(request):
    """Update user's avatar."""

    user = request.user
    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.imagen.url
    except:
        avatar = ''

    if request.method != "POST":
        formulario = AvatarForm()
        
    else:
        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():
            avatars = Avatar.objects.filter(user=user)

            if len(avatars) > 0:
                new_avatar = avatars[0]
                new_avatar.imagen = formulario.cleaned_data['imagen']
                new_avatar.save()

                messages.success(request, 'El avatar fue modificado satisfactoriamente.')
            else:
                new_avatar = Avatar(user=user, imagen=formulario.cleaned_data['imagen'])
                new_avatar.save()

                messages.success(request, 'El avatar fue ingresado satisfactoriamente')

        
        return redirect("App_Final_Inicio")
    
    contexto = {
        'form': AvatarForm,       
        'name_form': 'Avatar',
        'name_submit': 'Cargar Avatar',
    }

    return render(request, 'UserAppFinal/formulario_user.html', contexto)


@login_required
def mensajes(request):
    user = request.user

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        form = MensajesForm()
    
    else:
        # Data submitted. Paso formulario con datos ingresados por POST
        form = MensajesForm(data=request.POST)
        if form.is_valid():

            mensajes = form.save(commit=False)
            mensajes.envia = request.user
            mensajes.save()

            return redirect('mensajes_todos')
    
    context = {
        'form': form,
        'title': 'Nuevo mensaje',
    }
    return render(request, 'UserAppFinal/nuevo_mensaje.html', context)

@login_required
def mensajes_todos(request):
    
    user = request.user
    
    mensaje = Mensajes.objects.filter(Q(recibe=user) | Q(envia=user)).order_by('-enviado')
    recibe = mensaje.filter(recibe=user).order_by('-enviado')
    envia = mensaje.filter(envia=user).order_by('-enviado')

    context = {
        'title': 'Correo',
        'user': user,
        'mensajes': mensajes,
        'recibe': recibe,
        'envia':envia,
    }
    return render(request, 'UserAppFinal/mensajes_todos.html', context)

@login_required
def eliminar_mensaje(request, mensaje_id):


        mensaje_eliminar = Mensajes.objects.get(id=mensaje_id)
        mensaje_eliminar.delete()

        messages.warning(request, f"El anime {mensaje_eliminar.mensaje} fue eliminado con exito")

        return redirect('mensajes_todos')
