from django.contrib import admin
from .models import Usuario, TipoUsuario, Inmueble, TipoInmueble, Comuna, Region, SolicitudArriendo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Inmueble)
admin.site.register(TipoInmueble)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(SolicitudArriendo)