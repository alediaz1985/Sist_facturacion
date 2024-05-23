from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/alta/', views.alta_cliente, name='alta_cliente'),
    path('clientes/buscar/', views.buscar_cliente, name='buscar_cliente'),
    path('venta/nueva/', views.nueva_venta, name='nueva_venta'),
    path('venta/guardar/', views.guardar_comprobante, name='guardar_comprobante'),
    path('venta/buscar/', views.buscar_comprobante, name='buscar_comprobante'),
    path('venta/anular/', views.anular_comprobante, name='anular_comprobante'),
    path('venta/reimprimir/', views.reimprimir_comprobante, name='reimprimir_comprobante'),
    path('caja/extraccion-ingreso/', views.extraccion_ingreso_caja, name='extraccion_ingreso_caja'),
    path('caja/apertura/', views.apertura_caja, name='apertura_caja'),
    path('caja/cierre/', views.cierre_caja, name='cierre_caja'),
    path('caja/cerradas/', views.ver_cajas_cerradas, name='ver_cajas_cerradas'),
    path('venta/detalle/<int:venta_id>/', views.ver_detalle_venta, name='ver_detalle_venta'),
]
