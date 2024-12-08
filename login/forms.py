from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profesor

class FormularioP(UserCreationForm):
    foto=forms.ImageField(required=True)
    direccion=forms.CharField(max_length=255,required=True)

    class Meta:
        model=User
        fields=['first_name','last_name','email','password1','password2']

    def save(self,commit=True):
        user=super(FormularioP,self).save(commit=False)
        if commit:
            user.save()
            Profesor.objects.create(
                user=user,
                foto=self.cleaned_data['foto'],
                direccion=self.cleaned_data['direccion']
            )
        return user
    
from django import forms


class FormularioLoginP(forms.Form):
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Ingresa tu correo"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Ingresa tu contraseña"})
    )
