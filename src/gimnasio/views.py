from django.shortcuts import render
from django.http import HttpResponse
from gimnasio.models import Profesores, Clientes, Actividad

# Create your views here.
def inicio(request):
    return render(request, "gimnasio/index.html")

def profesores(request):

    profesores = Profesores.objects.all()

    context = {
        "profesores": profesores
    }

    return render(request, "gimnasio/profesores.html", context)

def clientes(request):
    clientes = Clientes.objects.all()

    context = {
        "clientes": clientes
    }

    return render(request, "gimnasio/clientes.html", context)

def actividades(request):
    actividades = Actividad.objects.all()

    context = {
        "actividades": actividades
    }

    return render(request, "gimnasio/actividades.html", context)

def formulario(request):
    return render(request, "gimnasio/formularios.html")

def crear_actividad(request):
    if request.method == "GET":
        return render(request, "gimnasio/formularios.html")
    else:
        nombre_actividad = request.POST["nombre_actividad"]
        actividad = Actividad(nombre_actividad = nombre_actividad) 
        actividad.save()
        return render(request, "gimnasio/index.html")

def login(request):
    if request.method == 'GET':
        return render (request, "gimnasio/login_cliente.html")
    else:
        usuario = request.POST["usuario"]
        apellido = request.POST["apellido"]
        dni = request.POST["dni"]
        email = request.POST["email"]
        password = request.POST["password"]
        login = Clientes(nombre = usuario, apellido = apellido, email = email, dni = dni) 
        login.save()
        return render(request, "gimnasio/index.html")

def login_profesor(request):
    if request.method == 'GET':
        return render (request, "gimnasio/login_profesores.html")
    else:
        usuario = request.POST["usuario"]
        apellido = request.POST["apellido"]
        profesion = request.POST["profesion"]
        password = request.POST["password"]
        login_profe = Profesores(nombre = usuario, apellido = apellido, profesion = profesion) 
        login_profe.save()
        return render(request, "gimnasio/index.html")
