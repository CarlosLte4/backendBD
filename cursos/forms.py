from django import forms
from .models import Curso

class FormularioCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre']  # Incluye solo el campo editable por el usuario
