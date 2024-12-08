from django.shortcuts import render,redirect
from .models import Curso
from django.contrib.auth.decorators import login_required
# Create your views here.

# Create your views here.
def cursos(request):
    
    return render(request, "cursos/cursosP.html") 

def crearCurso(request):    

    return render(request, "cursos/crearCurso.html")