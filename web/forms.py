from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, SolicitudArriendo

class UsuarioRegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'password','email', 'rut', 'direccion', 'telefono', 'tipo_usuario')


class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ['mensaje']
        widgets = {
            'arrendatario': forms.HiddenInput(),
            'inmueble': forms.HiddenInput(),
        }
