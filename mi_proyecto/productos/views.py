from django.shortcuts import render
from .models import Producto

def index(request):
    return render(request, 'index.html')

def productos_view(request):
    return render(request, 'productos.html')

# ORM para recuperar todos los productos

def lista_productos(request):
    productos = Producto.objects.all()
    total_productos = productos.count()
    productos_disponibles = productos.filter(disponible=True).count()
    productos_no_disponibles = total_productos - productos_disponibles
    productos_caros = Producto.objects.filter(precio__gt=50)
    productos_start_a = Producto.objects.filter(nombre__startswith='a') or Producto.objects.filter(nombre__startswith='A')
    context = {
        'productos': productos,
        'total_productos': total_productos,
        'productos_disponibles': productos_disponibles,
        'productos_no_disponibles': productos_no_disponibles,
        'productos_caros': productos_caros,
        'productos_start_a': productos_start_a
    }
    return render(request, 'productos.html', context)