from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SolicitudArriendoForm, UserUpdateForm, RegistrationForm
from .models import Usuario, TipoUsuario, Inmueble
from .services import obtener_inmueble


# Create your views here.

def indexView(request):
    inmuebles = Inmueble.objects.all()
    inmuebles_disponibles = Inmueble.objects.filter(arrendado = False)
    context = {
        'inmuebles' : inmuebles,
        'inmuebles_disponibles' : inmuebles_disponibles
    }
    return render(request, 'index.html', context)

@login_required
def arrendador(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'arrendador.html', {'inmuebles' : inmuebles})

def nuevaSolicitud(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id= inmueble_id)
    
    if request.method == 'POST':
        form = SolicitudArriendoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.inmueble = inmueble
            solicitud.save()
            
            return redirect('exito')
    else:
        form = SolicitudArriendoForm()
        
    context = {
        'form': form,
        'inmueble': inmueble
        }
            
    return render(request, 'solicitud.html', context)

def exito(request):
    return render(request,'exito_solicitud.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username, email, password)
            
            nombres = request.POST['nombres']
            apellidos = request.POST['apellidos']
            user.first_name = nombres
            user.last_name = apellidos
            user.save()
            
            rut = request.POST['rut']
            direccion = request.POST['direccion']
            telefono = request.POST['telefono']
            tipo_usuario = TipoUsuario.objects.get(pk=2)        
            usuario = Usuario(rut=rut, direccion=direccion, telefono=telefono, tipo_usuario=tipo_usuario)
            usuario.save()
        return redirect('login')
        
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'registro.html', context)

@login_required
def userUpdate(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            
            rut = request.POST['rut']
            direccion = request.POST['direccion']
            telefono = request.POST['telefono']
            tipo_usuario = TipoUsuario.objects.get(pk=2)        
            usuario = Usuario(rut=rut, direccion=direccion, telefono=telefono, tipo_usuario=tipo_usuario)
            usuario.save()
            
            usuario = Usuario.objects.update_or_create(
                user=user,
                defaults={
                    'rut': rut,
                    'direccion': direccion,
                    'telefono': telefono,
                    'tipo_usuario': tipo_usuario
                }
            )
            return redirect('login')
    else:
        form = UserUpdateForm(instance=request.user)
        context = {'form': form}
        return render(request, 'update_usuario.html', context)