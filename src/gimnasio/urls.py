from django.urls import path
from gimnasio.views import *

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('profesores/', profesores, name = "profesores"),
    path('clientes/', clientes, name = "clientes"),
    path('actividades/', actividades, name = "actividades"),
    path('actividad/crear/', crear_actividad, name = "crear_actividad"),
    path('login', login, name = "login"),
    path('login/profesores', login_profesor, name = "login"),
]