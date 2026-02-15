from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Carrito, ItemCarrito, Pedido, DetallePedido
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
from django.db import transaction

def index(request):
    productos = Producto.objects.filter(disponible=True)
    categorias = Categoria.objects.all()
    return render(request, 'tienda/index.html', {'productos': productos, 'categorias': categorias})

def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk, disponible=True)
    return render(request, 'tienda/producto_detalle.html', {'producto': producto})

def categoria_lista(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    productos = Producto.objects.filter(categoria=categoria, disponible=True)
    return render(request, 'tienda/categoria_lista.html', {'categoria': categoria, 'productos': productos})

def obtener_carrito(request):
    if request.user.is_authenticated:
        carrito, created = Carrito.objects.get_or_create(usuario=request.user, activo=True)
        return carrito
    # fallback por sesión: usar carrito anon (simplificado)
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        try:
            return Carrito.objects.get(id=carrito_id, activo=True)
        except Carrito.DoesNotExist:
            pass
    carrito = Carrito.objects.create()
    request.session['carrito_id'] = carrito.id
    return carrito

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, disponible=True)
    carrito = obtener_carrito(request)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    messages.success(request, f'Agregaste {producto.nombre} al carrito.')
    return redirect('tienda:ver_carrito')

def ver_carrito(request):
    carrito = obtener_carrito(request)
    return render(request, 'tienda/carrito.html', {'carrito': carrito})

def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    carrito = obtener_carrito(request)
    if item.carrito == carrito:
        item.delete()
    return redirect('tienda:ver_carrito')

@login_required
@transaction.atomic
def checkout(request):
    carrito = obtener_carrito(request)
    if carrito.items.count() == 0:
        messages.error(request, "El carrito está vacío.")
        return redirect('tienda:index')

    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        total = carrito.total()
        pedido = Pedido.objects.create(
            usuario=request.user,
            total=total,
            direccion_envio=direccion
        )
        for item in carrito.items.all():
            DetallePedido.objects.create(
                pedido=pedido,
                producto=item.producto,
                cantidad=item.cantidad,
                subtotal=item.subtotal()
            )
        # marcar carrito inactivo
        carrito.activo = False
        carrito.save()
        # opcional limpiar sesión
        request.session.pop('carrito_id', None)
        return redirect('tienda:pedido_confirmado', pedido_id=pedido.id)

    return render(request, 'tienda/checkout.html', {'carrito': carrito})

def pedido_confirmado(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'tienda/pedido_confirmado.html', {'pedido': pedido})
