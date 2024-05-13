from django.contrib import admin
from .models import Usuario, Inmueble, SolicitudArriendo
from django.contrib.auth.admin import UserAdmin, User
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['username', 'first_name', 'last_name', 'password','email', 'rut', 'direccion', 'telefono', 'tipo_usuario',]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('rut', 'direccion', 'telefono', 'tipo_usuario')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('rut', 'direccion', 'telefono', 'tipo_usuario')}),)

admin.site.register(Usuario, CustomUserAdmin)

# Register your models here.
admin.site.register(Inmueble)
admin.site.register(SolicitudArriendo)
