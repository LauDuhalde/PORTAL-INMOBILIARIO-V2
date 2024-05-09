from django.contrib import admin
from .models import Usuario, Inmueble, SolicitudArriendo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Inmueble)
admin.site.register(SolicitudArriendo)
