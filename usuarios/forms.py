from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    campos = (
        ('administrador','admin'),
        ('compras', 'compras'),
        ('moderador', 'moderador')
    )
    email = forms.EmailField()
    grupo = forms.ChoiceField(choices=campos)

    class Meta:
        model = User
        fields = ['username', 'email', 'grupo', 'password1', 'password2']

