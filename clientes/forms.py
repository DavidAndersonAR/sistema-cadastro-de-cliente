from django import forms
from .models import NomeUsuario


class UserForm(forms.ModelForm):
    
    class Meta:
        model = NomeUsuario
        fields = ('nome', 'email', 'cel', 'cpf', 'estado_civil', 'genero', 'rua', 'complemento', 'cidade', 'estado', 'cep')