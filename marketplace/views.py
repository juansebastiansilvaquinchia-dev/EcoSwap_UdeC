from django.shortcuts import render
from .models import Producto, Categoria

def lista_productos(request):
    # Capturamos el parámetro 'categoria' de la URL (si existe)
    categoria_id = request.GET.get('categoria')
    
    # 1. Filtramos los productos según la categoría o traemos todos si no se especificó ninguna
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()

    # Traemos todas las categorías para pintar los botones en la plantilla
    categorias = Categoria.objects.all()

    # 2. Guardamos la información en el diccionario de contexto
    contexto = {
        "productos": productos,
        "categorias": categorias,
        "categoria_actual": categoria_id,
    }

    # 3. Enviamos los datos a la plantilla HTML "catalogo.html"
    return render(request, "catalogo.html", contexto)