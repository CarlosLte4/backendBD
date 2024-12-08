from django.shortcuts import render,redirect
from .forms import FormularioP

# Create your views here.
def login(request):
    return render(request,"login/login.html")

def registroP(request):
    if request.method == 'POST':
        form=FormularioP(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormularioP()
    return render(request,"login/registroP.html",{'form':form})

