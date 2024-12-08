from django.urls import path
from . import views #esto significa que el viws esta en la misma carpeta

urlpatterns = [
    path('',views.cursos, name="Cursos"),
    path('crearCurso/',views.crearCurso, name="crearCurso"),
]