from django.shortcuts import render
from .models import Producto
from django.db import connection

def listar_productos(request):

    productos = Producto.objects.all() # sintaxis ORM

    # productos_raw = Producto.objects.raw("SELECT * FROM store_producto")

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM store_producto"
        )
        productos_cursor = cursor.fetchall()
        print(productos_cursor)

    return render(request, "listar_productos.html", {
        "productos": productos
    })






















# Create your views here.

# WHERE precio > 100 or stock < 10

# WHERE precio > 100 and stock > 5

# NOT precio < 50


# precio > 50
# stock > 5
# ORDER BY PRECIO DESC

# >>> productos = Producto.objects.raw("SELECT * FROM store_producto")
# >>> for p in productos: print(p.nombre, p.precio)
# ...
# Laptop 1200.00
# Mouse 50.00
# >>> productos = Producto.objects.raw("SELECT * FROM store_producto WHERE precio > 100")
# >>> for p in productos: print(p.nombre, p.precio)
# ...
# Laptop 1200.00
# >>> productos = Producto.objects.raw("SELECT * FROM store_producto ORDER BY precio DESC")
# >>> for p in productos: print(p.nombre, p.precio)
# ...
# Laptop 1200.00
# Mouse 50.00
# >>> productos = Producto.objects.raw("SELECT * FROM store_producto ORDER BY precio ASC")
# >>> for p in productos: print(p.nombre, p.precio)
# ...
# Mouse 50.00
# Laptop 1200.00

