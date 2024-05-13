from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario, SolicitudArriendo, Inmueble

class UsuarioForm(UserCreationForm):
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
        
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name','email','rut', 'direccion', 'telefono', 'tipo_usuario')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name','email', 'direccion', 'telefono',)

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        exclude = ('arrendador',)  # Excluimos el campo 'propietario' del formulario
