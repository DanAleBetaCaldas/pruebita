from contextlib import ContextDecorator
from django.shortcuts import render
from appWeb.models import Marca
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password #permite encriptar la clave

# Create your views here.
def plantillaejm (request):
    return render(request, 'plantilla.html', {})

def registro(request):
    if request.method == 'POST':
        nombre = request.POST ["txtNombre"]
        correo = request.POST ["txtCorreo"]
        clave = request.POST ["txtClave"]
        
def marca (request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    mensaje = ""
    lista = {}
    item = {}
    #detecta si hay una solicitud
    if request.method == "POST":
        #captura los valores entregados por los usuarios
        id = int("0" + request.POST["txtId"]) #convertir a int
        nombre = request.POST["txtNombre"]
        activo = request.POST["chkActivo"]

        #detecta que botono presiono el usuario
        if 'btnGrabar' in request.POST:
            if id < 1: #un nuevo registro
                Marca.objects.create(nombre = nombre, activo = activo) #registra los datos
            else:
                item = Marca.objects.get(pk = id)
                item.nombre = nombre
                item.activo = activo
                item.save() # guarda los cambios 
                item = {}

            mensaje ="Datos Guardados"
        elif 'btnBuscar' in request.POST:
                item = Marca.objects.get(pk = id)

                if isinstance(item, Marca):
                    mensaje = "Registro no encontrado"
                    item = {}

        elif 'btnListar' in request.POST:
            lista = Marca.objects.all()

        elif 'btnEliminar' in request.POST:
                item = Marca.objects.get(pk = id) #obtiene el registro segun id

                if isinstance(item, Marca):
                    item.delete()
                    mensaje = "Registro  Eliminado"
                    item = {}
    #context es la informacion que se envia a la plantilla para procesar
    contexto = {'mensaje': mensaje, 'lista':lista, 'item':item}


    return render(request, 'marca.html', contexto)