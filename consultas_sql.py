import os, django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmobiliaria.settings')
django.setup()

from arriendos.models import Inmueble, Comuna

def inmuebles_comuna():
    sql = """SELECT comuna.nombre, inmueble.id, inmueble.nombre, inmueble.descripcion 
        FROM arriendos_inmueble AS inmueble
        INNER JOIN arriendos_comuna AS comuna
        ON inmueble.comuna_id=comuna.id
        WHERE inmueble.arrendado = false
        GROUP BY comuna.nombre, inmueble.id, inmueble.nombre, inmueble.descripcion
        ORDER BY comuna.nombre;"""
        
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()

    with open("inmuebles_comuna.txt", "w", encoding='UTF-8') as archivo:
        for inmueble in rows:
            archivo.write(f'{str(inmueble[0])} : {str(inmueble[2])} - {str(inmueble[3])}\n')
            
def inmuebles_region():
    sql = """SELECT region.nombre, inmueble.nombre, inmueble.descripcion 
        FROM arriendos_inmueble AS inmueble
        INNER JOIN arriendos_comuna AS comuna
        ON inmueble.comuna_id=comuna.id
        INNER JOIN arriendos_region as region
        ON comuna.region_id=region.id
        WHERE inmueble.arrendado = false
        GROUP BY region.nombre, inmueble.nombre, inmueble.descripcion
        ORDER BY region.nombre;"""
        
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()

    with open("inmuebles_region.txt", "w", encoding='UTF-8') as archivo:
        for inmueble in rows:
            archivo.write(f'{str(inmueble[0])} : {str(inmueble[1])} - {str(inmueble[2])}\n')