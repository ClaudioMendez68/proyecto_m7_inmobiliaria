from django.utils import timezone
from .models import TipoUsuario, TipoInmueble, Usuario, Inmueble, Region, Comuna, SolicitudArriendo

def crear_tipo_usuario(p_tipo):
    tipo_usuario = TipoUsuario(tipo=p_tipo)
    tipo_usuario.save()
    return tipo_usuario
    
def obtener_tipo_usuario(id):
    return TipoUsuario.objects.get(pk=id).tipo

def crear_usuario(p_rut, p_nombres, p_apellidos, p_direccion, p_telefono, p_email, tipo_usuario_id):
    tipo_usuario = obtener_tipo_usuario(tipo_usuario_id)
    usuario = Usuario(
        rut=p_rut,
        nombres=p_nombres,
        apellidos = p_apellidos,
        direccion=p_direccion,
        telefono=p_telefono,
        email=p_email,
        tipo_usuario=tipo_usuario
    )
    usuario.save()
    return usuario

def obtener_usuario(id):
    return Usuario.objects.get(pk=id)

def modificar_usuario(id, p_rut, p_nombres, p_apellidos, p_direccion, p_telefono, p_email, tipo_usuario_id):
    usuario = obtener_usuario(id)
    tipo_usuario = TipoUsuario.objects.get(pk=tipo_usuario_id)
    usuario.rut=p_rut,
    usuario.nombres=p_nombres,
    usuario.apellidos = p_apellidos,
    usuario.direccion=p_direccion,
    usuario.telefono=p_telefono,
    usuario.email=p_email,
    usuario.tipo_usuario=tipo_usuario
    usuario.save()
    return usuario

def borrar_usuario(id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return True

def listar_usuarios():
    usuarios = Usuario.objects.all()
    for usuario in usuarios:
        print(f'ID: {usuario.id}')
        print(f'Nombre: {usuario.nombres} {usuario.apellidos}')
        print(f'Dirección: {usuario.direccion}')
        print(f'Teléfono: {usuario.telefono}')
        print(f'Email: {usuario.email}')
        print(f'Tipo: {usuario.tipo_usuario}')
        
def crear_region(nombre):
    region = Region(nombre)
    region.save()
    return region

def obtener_region(id):
    return Region.objects.get(pk=id)

def modificar_region(id, nombre):
    region = obtener_region(id)
    region.nombre = nombre
    region.save()
    return region

def crear_comuna(p_nombre, region_id):
    region = obtener_region(region_id)
    comuna = Comuna(nombre=p_nombre, region=region)
    comuna.save()
    return comuna

def obtener_comuna(id):
    return Comuna.objects.get(pk=id)

def modificar_comuna(id, p_nombre, region_id):
    region = obtener_region(region_id)
    comuna = obtener_comuna(id)
    comuna.nombre = p_nombre
    comuna.region = region
    comuna.save()
    return comuna
        
def crear_tipo_inmueble(p_tipo):
    tipo_inmueble = TipoInmueble(tipo=p_tipo)
    tipo_inmueble.save()
    return tipo_inmueble
    
def obtener_tipo_inmueble(id):
    return TipoInmueble.objects.get(pk=id).tipo

def modificar_tipo_inmueble(id, tipo):
    tipo_inmueble = obtener_tipo_inmueble(id)
    tipo_inmueble.tipo = tipo
    tipo_inmueble.save()
    return tipo_inmueble

def borrar_tipo_inmueble(id):
    tipo_inmueble = obtener_tipo_inmueble(id)
    tipo_inmueble.delete()
    return True

def crear_inmueble(p_nombre, p_descripcion, p_m2_construidos, p_m2_totales, p_estacionamientos, p_habitaciones, p_banios, p_direccion, p_arriendo_mensual, p_arrendado, comuna_id, tipo_inmueble_id):
    tipo_inmueble = obtener_tipo_inmueble(tipo_inmueble_id)
    comuna = obtener_comuna(comuna_id)
    inmueble = Inmueble(
        nombre=p_nombre,
        descripcion = p_descripcion,
        m2_construidos = p_m2_construidos,
        m2_totales = p_m2_totales,
        estacionamientos = p_estacionamientos,
        habitaciones = p_habitaciones,
        banios = p_banios,
        direccion=p_direccion,
        arriendo_mensual=p_arriendo_mensual,
        arrendado=p_arrendado,
        comuna=comuna,
        tipo_inmueble=tipo_inmueble
    )
    inmueble.save()
    return inmueble

def obtener_inmueble(id):
    return Inmueble.objects.get(pk=id)

def modificar_inmueble(id, p_nombre, p_descripcion, p_m2_construidos, p_m2_totales, p_estacionamientos, p_habitaciones, p_banios, p_direccion, p_arriendo_mensual, p_arrendado, comuna_id, tipo_inmueble_id):
    inmueble = obtener_inmueble(id)
    comuna = obtener_comuna(comuna_id)
    tipo_inmueble = obtener_tipo_inmueble(tipo_inmueble_id)
    inmueble.nombre=p_nombre,
    inmueble.descripcion = p_descripcion,
    inmueble.m2_construidos = p_m2_construidos,
    inmueble.m2_totales = p_m2_totales,
    inmueble.estacionamientos = p_estacionamientos,
    inmueble.habitaciones = p_habitaciones,
    inmueble.banios = p_banios,
    inmueble.direccion=p_direccion,
    inmueble.arriendo_mensual=p_arriendo_mensual,
    inmueble.arrendado=p_arrendado,
    inmueble.comuna=comuna,
    inmueble.tipo_inmueble=tipo_inmueble
    inmueble.save()
    return inmueble

def borrar_inmueble(id):
    inmueble = Inmueble.objects.get(pk=id)
    inmueble.delete()
    return True

def crear_solicitud_arriendo(p_estado, usuario_id, inmueble_id):
    usuario = obtener_usuario(pk=usuario_id)
    inmueble = obtener_inmueble(pk=inmueble_id)
    solicitud_arriendo = SolicitudArriendo(
        estado = p_estado,
        usuario = usuario,
        inmueble = inmueble
    )
    solicitud_arriendo.save()
    return solicitud_arriendo

def obtener_solicitud_arriendo(id):
    return SolicitudArriendo.objects.get(pk=id)

def modificar_solicitud_arriendo(id, p_estado, usuario_id, inmueble_id):
    solicitud_arriendo = obtener_solicitud_arriendo(id)
    usuario = obtener_usuario(usuario_id)
    inmueble = obtener_inmueble(inmueble_id)
    solicitud_arriendo.fecha_solicitud = timezone.now()
    solicitud_arriendo.estado = p_estado
    solicitud_arriendo.usuario = usuario
    solicitud_arriendo.inmueble = inmueble
    solicitud_arriendo.save()
    return solicitud_arriendo

def borrar_solicitud_arriendo(id):
    solicitud_arriendo = obtener_solicitud_arriendo(id)
    solicitud_arriendo.delete()
    return True