from django.shortcuts import render
from .models import Producto
from django.db.models import F
from django.db import connection

def index(request):
    return render(request, 'index.html')

def productos_view(request):
    return render(request, 'productos.html')

# Vista para mostrar los resultados de todas las consultas
def lista_productos(request):
    # 1. Todos los registros
    todos_los_productos = Producto.objects.all()

    # 2. Filtros
    productos_precio_gt_50 = Producto.objects.filter(precio__gt=50)
    productos_nombre_A = Producto.objects.filter(nombre__startswith='A')
    productos_disponibles_orm = Producto.objects.filter(disponible=True)

    # 3. Consulta Raw
    productos_raw_lt_100 = Producto.objects.raw("SELECT * FROM productos_producto WHERE precio < 100")

    # 6. Exclusión de Campos
    productos_defer = Producto.objects.defer('disponible')

    # 7. Anotaciones
    productos_anotados = Producto.objects.annotate(precio_con_impuesto=F('precio') * 1.16)

    # 8. Raw con parámetros
    valor_limite = 150
    productos_raw_params = Producto.objects.raw('SELECT * FROM productos_producto WHERE precio < %s', [valor_limite])

    # 9. SQL Directo (Ejemplo: se ejecuta una actualización)
    # Por seguridad y para no alterar datos en cada carga, esta línea está comentada.
    # with connection.cursor() as cursor:
    #     cursor.execute("UPDATE productos_producto SET nombre = %s WHERE id = %s", ['Nombre Actualizado', 1])

    # 10. Conexiones y Cursores para leer
    cursor_data = None
    with connection.cursor() as cursor:
        cursor.execute("SELECT nombre, precio FROM productos_producto WHERE disponible = %s", [True])
        cursor_data = cursor.fetchall()

    # 11. Procedimiento Almacenado (ejemplo conceptual)
    # La llamada real está comentada para evitar errores si el procedimiento no existe.
    # with connection.cursor() as cursor:
    #     cursor.callproc('obtener_productos_por_precio', [100])
    #     procedimiento_data = cursor.fetchall()

    context = {
        'todos_los_productos': todos_los_productos,
        'productos_precio_gt_50': productos_precio_gt_50,
        'productos_nombre_A': productos_nombre_A,
        'productos_disponibles_orm': productos_disponibles_orm,
        'productos_raw_lt_100': productos_raw_lt_100,
        'productos_defer': productos_defer,
        'productos_anotados': productos_anotados,
        'productos_raw_params': productos_raw_params,
        'valor_limite_raw': valor_limite,
        'cursor_data': cursor_data,
    }
    return render(request, 'productos.html', context)