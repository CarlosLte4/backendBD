from django.shortcuts import render

# Create your views here.

# Create your views here.
def cursos(request):
    
    return render(request, "cursos/cursosP.html") #en comillas esta la capeta en la que esta el archivo html 
    