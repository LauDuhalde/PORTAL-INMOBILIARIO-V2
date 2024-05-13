from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from web.models import SolicitudArriendo, Inmueble, Usuario, Region, Comuna
from .forms import SolicitudArriendoForm,CustomUserCreationForm, CustomUserChangeForm, InmuebleForm
from django.contrib import messages

# def iniciar_sesion(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('index')  # Redirigir al usuario después de iniciar sesión exitosamente
#     else:
#         form = AuthenticationForm()
#     return render(request, 'inicio_sesion.html', {'form': form})

#Para filtrar comunas según región seleccionada
def obtener_comunas(request):
    region_id = request.GET.get('region_id')
    comunas = Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)

def index(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    inmuebles = Inmueble.objects.filter(disponible=True)  # Obtener todos los inmuebles disponibles por defecto o filtrar según tus necesidades
    
    # Lógica para filtrar inmuebles por región y comuna si se han seleccionado
    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')
    selected_region = None
    if region_id:
        selected_region = Region.objects.get(pk=region_id)
        if not comuna_id:
            inmuebles = Inmueble.objects.filter(comuna__region=selected_region, disponible=True)
        else:
            inmuebles = Inmueble.objects.filter(comuna_id=comuna_id, disponible=True)
    
    return render(request, 'index.html', {'regiones': regiones, 'comunas': comunas, 'inmuebles': inmuebles, 'selected_region': selected_region})

@login_required
def detalle_inmueble(request, id):
    inmueble=Inmueble.objects.get(id=id)
    return render(request, 'detalle_inmueble.html',{'inmueble':inmueble})

def registro_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir al usuario después del registro exitoso
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro_usuario.html', {'form': form})


def crear_solicitud_arriendo(request, inmueble_id):
    # Obtener instancia del inmueble y el usuario
    inmueble = Inmueble.objects.get(pk=inmueble_id)
    usuario = request.user
            
    if request.method == 'POST':
        form = SolicitudArriendoForm(request.POST)
        if form.is_valid():
            # Asignar los IDs al formulario y guardar la solicitud de arriendo
            solicitud = form.save(commit=False)
            solicitud.inmueble = inmueble
            solicitud.arrendatario = usuario
            solicitud.save()
            
            return redirect('success')
    else:
        form = SolicitudArriendoForm(initial={'arrendatario': usuario.id, 'inmueble': inmueble.id})
    return render(request, 'solicitud_arriendo.html', {'form': form, 'usuario':usuario, 'inmueble':inmueble})

def success(request):
    return render(request, 'success.html',{})

def mi_perfil(request):
    usuario = request.user
    inmuebles_y_solicitudes = None
    solicitudes_arrendatario = None
    if usuario.tipo_usuario == 'arrendador':
        # Consultar todos los inmuebles del usuario
        inmuebles_arrendador = Inmueble.objects.filter(arrendador=usuario)

        # Inicializar una lista para almacenar los inmuebles y sus solicitudes asociadas
        inmuebles_y_solicitudes = []

        # Iterar sobre los inmuebles del usuario
        for inmueble in inmuebles_arrendador:
            # Consultar todas las solicitudes asociadas a este inmueble
            solicitudes = SolicitudArriendo.objects.filter(inmueble=inmueble)
            
            # Agregar el inmueble y sus solicitudes asociadas a la lista
            inmuebles_y_solicitudes.append({
                'inmueble': inmueble,
                'solicitudes': solicitudes
            })
    else:
        # Consultar todas las solicitudes de arriendo realizadas por el arrendatario
        solicitudes_arrendatario = SolicitudArriendo.objects.filter(arrendatario=usuario)
    return render(request,'mi_perfil.html',{'inmuebles_y_solicitudes':inmuebles_y_solicitudes, 'solicitudes_arrendatario':solicitudes_arrendatario})

@login_required
def dashboard(request):
    if request.user.tipo_usuario == 'arrendatario':
        solicitudes = SolicitudArriendo.objects.filter(arrendatario=request.user)
        return render(request, 'dashboard_arrendatario.html', {'solicitudes': solicitudes})
    
    elif request.user.tipo_usuario == 'arrendador':
        # Obtener las solicitudes recibidas por el arrendador
        solicitudes_recibidas = SolicitudArriendo.objects.filter(inmueble__arrendador=request.user)
        # Obtener los inmuebles del arrendador
        inmuebles = Inmueble.objects.filter(arrendador=request.user)
        return render(request, 'dashboard_arrendador.html', {'solicitudes_recibidas': solicitudes_recibidas, 'inmuebles': inmuebles})
    
@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus datos se han actualizado correctamente.')
            return redirect('mi_perfil')
    else:
        form = CustomUserChangeForm(instance=usuario)
    
    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def crear_inmueble(request):
    regiones = Region.objects.all()
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = request.user
            inmueble.save()
            return redirect('index') 
    else:
        form = InmuebleForm()
    return render(request, 'ingresar_inmueble.html', {'form': form, 'regiones': regiones})


@login_required
def actualizar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'editar_inmueble.html',{'form':form })
        
@login_required
def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('index')
    else:
        return render(request,'eliminar_inmueble.html', {'inmueble':inmueble} )
    
@login_required
def solicitudes_arrendador(request):
    # Verificar si el usuario es un arrendador
    if request.user.tipo_usuario == 'arrendador':
        # Obtener todas las solicitudes recibidas por el arrendador
        solicitudes = SolicitudArriendo.objects.filter(inmueble__arrendador=request.user)
        return render(request, 'solicitudes_arrendador.html', {'solicitudes': solicitudes})
    else:
        # Redirigir a otra página si el usuario no es un arrendador
        return redirect('index') 

@login_required
def cambiar_estado_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudArriendo, pk=solicitud_id)
    if solicitud.inmueble.arrendador == request.user or solicitud.arrendatario == request.user:
        if request.method == 'POST':
            nuevo_estado = request.POST.get('nuevo_estado')
            solicitud.estado = nuevo_estado
            solicitud.save()
    return redirect('dashboard')