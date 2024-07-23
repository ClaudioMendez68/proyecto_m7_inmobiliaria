from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=20, null=False, blank=False)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.tipo}'

class Usuario(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    rut = models.CharField(max_length=9, null=False, blank=False, unique=True)
    # nombres = models.CharField(max_length=50, null=False, blank=False)
    # apellidos = models.CharField(max_length=50, null=False, blank=False)
    direccion = models.CharField(max_length=30, null=False, blank=False)
    telefono = models.CharField(max_length=10, null=False, blank=False)
    tipo_usuario = models.ForeignKey(TipoUsuario, related_name='usuarios', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

class TipoInmueble(models.Model):
    tipo = models.CharField(max_length=20, null=False, blank=False)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.tipo}'
    
class Region(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.nombre}'

class Comuna(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.nombre}'

class Inmueble(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField()
    m2_construidos = models.FloatField(null=False, blank=False)
    m2_totales = models.FloatField(null=False, blank=False)
    estacionamientos = models.PositiveIntegerField()
    habitaciones = models.PositiveIntegerField(null=False, blank=False)
    banios = models.PositiveIntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=100)
    arriendo_mensual = models.DecimalField(max_digits=10, decimal_places=0, null=False, blank=False)
    image_url = models.URLField(null=True)
    arrendado = models.BooleanField(default=False, null=False, blank=False)
    comuna = models.ForeignKey(Comuna, related_name='inmuebles_comuna', on_delete=models.CASCADE)
    tipo_inmueble = models.ForeignKey(TipoInmueble, related_name='inmuebles_tipo', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.id}: {self.nombre} - {self.direccion}'

class SolicitudArriendo(models.Model):
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('aceptada', 'Aceptada'), ('rechazada', 'Rechazada'), ('pendiente', 'Pendiente')], default='pendiente')
    usuario = models.ForeignKey(Usuario, related_name='solicitudes_usuario', on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, related_name='solicitudes_inmueble',on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.id}: {self.fecha_solicitud} - {self.estado}'