from django.shortcuts import render,redirect
from .forms import FormularioP,FormularioLoginP
from django.contrib.auth.hashers import check_password
from .models import Profesor

# Create your views here.



def login(request):
    if request.method == 'POST':
        # Procesar el formulario
        form = FormularioLoginP(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                # Buscar el profesor por correo
                profesor = Profesor.objects.get(user__email=email)

                # Validar la contraseña
                if check_password(password, profesor.user.password):
                    # Guardar información en la sesión
                    request.session['profesor_id'] = profesor.id
                    return redirect('/cursos/')
                else:
                    return render(request, 'login.html', {'form': form, 'error': 'Contraseña incorrecta'})
            except Profesor.DoesNotExist:
                return render(request, 'login.html', {'form': form, 'error': 'Correo no registrado como profesor'})
    else:
        form = FormularioLoginP()

    return render(request, 'login/login.html', {'form': form})


def registroP(request):
    if request.method == 'POST':
        form=FormularioP(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormularioP()
    return render(request,"login/registroP.html",{'form':form})

