from django.urls import path
from . import views #esto significa que el viws esta en la misma carpeta

urlpatterns = [
    path('cursosP/',views.cursosP, name="CursosP"),
    path('cursosP/crearCurso/',views.crearCurso, name="crearCurso"),
    path('cursosE/',views.cursosE, name="CursosE"),
    path('cursoP/<int:curso_id>/',views.detalleCurso,name='detalleCurso')
    
]