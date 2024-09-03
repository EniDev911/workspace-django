from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pregunta, Categoria
from django.utils.safestring import mark_safe

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class CrearPreguntasForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['categoria_id', 'pregunta', 'resp_correcta', 'resp_incorrecta1', 'resp_incorrecta2', 'resp_incorrecta3']
        widgets = {
            'pregunta': forms.TextInput(attrs={'class': 'form-control'}),
            'resp_correcta': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categorias = [(x.id, x.nombre) for x in Categoria.objects.filter()]

        def ordenar_nombre(e):
            return e[1]
        categorias.sort(key=ordenar_nombre)
        self.fields['categoria_id'].choices = categorias
        self.fields['categoria_id'].label=mark_safe("Categoría ( <a href='/crear_categoria' class='text-warning'>nueva categoría</a> )")

    resp_correcta = forms.CharField(label="Respuesta correcta")
    resp_incorrecta1 = forms.CharField(label="Respuesta incorrecta 1")
    resp_incorrecta2 = forms.CharField(label="Respuesta incorrecta 2")
    resp_incorrecta3 = forms.CharField(label="Respuesta incorrecta 3")


class CrearCategoriaForm(forms.Form):
    nombre = forms.CharField(label='Nombre categoría', widget=forms.TextInput(attrs={
        'placeholder': 'tecnología',
        'class': 'form-control'
    }))

class RespuestaForm(forms.Form):
    pass