from django.contrib.auth.models import AbstractUser
from django.db import models
class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )
    rut = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=13)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    
    # Utilizando los related_name por defecto
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='Los grupos a los que pertenece el usuario. '
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Los permisos específicos concedidos a este usuario.'
    )
    
    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")
    
    
class Inmueble(models.Model):
    TIPO_INMUEBLE_CHOICES = (
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela','Parcela'),
    )
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, related_name='inmuebles', on_delete=models.CASCADE)
    tipo_inmueble = models.CharField(max_length=20, choices=TIPO_INMUEBLE_CHOICES)
    precio = models.DecimalField(max_digits=8, decimal_places=0)
    descripcion = models.TextField(max_length=1000)
    m2_construidos = models.DecimalField(max_digits=10, decimal_places=2)
    m2_terreno = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_estacionamientos = models.PositiveIntegerField()
    cantidad_habitaciones = models.PositiveIntegerField()
    cantidad_banios = models.PositiveIntegerField()
    imagen =models.ImageField(upload_to='')
    disponible = models.BooleanField(default=True)
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inmuebles',limit_choices_to={'tipo_usuario': 'arrendador'})
    
    def __str__(self) -> str:
        return (f"{self.nombre}")
    
class SolicitudArriendo(models.Model):
    ESTADO_SOLICITUD_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
        ('cancelada', 'Cancelada'),
    )
    arrendatario = models.ForeignKey(Usuario, related_name='solicitudes', on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, related_name='solicitudes', on_delete=models.CASCADE)
    mensaje = models.TextField(blank=True)
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    
    estado = models.CharField(choices=ESTADO_SOLICITUD_CHOICES, default='pendiente')
    def __str__(self):
        return f"Solicitud de {self.inmueble.nombre} por {self.arrendatario.nombres} {self.arrendatario.apellidos}"    