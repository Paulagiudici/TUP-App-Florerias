from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='home'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('categoria/<int:pk>/', views.categoria_lista, name='categoria_lista'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_item_carrito, name='eliminar_item_carrito'),
    path('checkout/', views.checkout, name='checkout'),
    path('pedido/confirmado/<int:pedido_id>/', views.pedido_confirmado, name='pedido_confirmado'),
]
