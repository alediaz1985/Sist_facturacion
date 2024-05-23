from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Venta, Cliente
from .forms import VentaForm, ClienteForm
from django.contrib import messages

def index(request):
    """
    Vista para la página de inicio.
    """
    return render(request, 'core/index.html')

def guardar_comprobante(request):
    """
    Vista para guardar un nuevo comprobante de venta.
    """
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Comprobante guardado exitosamente.")
            return redirect('index')
    else:
        form = VentaForm()
    return render(request, 'core/guardar_comprobante.html', {'form': form})

def buscar_comprobante(request):
    """
    Vista para buscar un comprobante por criterios específicos.
    """
    return HttpResponse("Placeholder para buscar un comprobante")

def anular_comprobante(request):
    """
    Vista para anular un comprobante.
    """
    return HttpResponse("Placeholder para anular un comprobante")

def reimprimir_comprobante(request):
    """
    Vista para reimprimir un comprobante.
    """
    return HttpResponse("Placeholder para reimprimir un comprobante")

def extraccion_ingreso_caja(request):
    """
    Vista para manejar extracciones e ingresos de caja.
    """
    return HttpResponse("Placeholder para extracción/ingreso de caja")

def apertura_caja(request):
    """
    Vista para la apertura de caja del día.
    """
    return HttpResponse("Placeholder para apertura de caja")

def cierre_caja(request):
    """
    Vista para el cierre de caja del día.
    """
    return HttpResponse("Placeholder para cierre de caja")

def ver_cajas_cerradas(request):
    """
    Vista para visualizar cajas cerradas anteriormente.
    """
    return HttpResponse("Placeholder para ver cajas cerradas")

def alta_cliente(request):
    """
    Vista para el registro de un nuevo cliente.
    """
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente guardado correctamente.')
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'core/alta_cliente.html', {'form': form})

def buscar_cliente(request):
    dni_cuit = request.GET.get('dni_cuit')
    if dni_cuit:
        try:
            cliente = Cliente.objects.get(dni_cuit=dni_cuit)
            return JsonResponse({
                'success': True,
                'nombre': cliente.nombre,
                'domicilio': cliente.direccion,
                'ciudad': cliente.ciudad,
                'telefono': cliente.telefono,
                'email': cliente.email
            })
        except Cliente.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Cliente no encontrado'})
    return JsonResponse({'success': False, 'message': 'DNI/CUIT no proporcionado'})

def nueva_venta(request):
    """
    Vista para crear una nueva venta.
    """
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            messages.success(request, "Venta creada exitosamente.")
            return redirect('ver_detalle_venta', venta_id=venta.id)
    else:
        form = VentaForm()
    return render(request, 'core/nueva_venta.html', {'form': form})

def ver_detalle_venta(request, venta_id):
    """
    Vista para mostrar los detalles de una venta específica.
    """
    venta = Venta.objects.get(id=venta_id)
    detalles = venta.detalles.all()
    return render(request, 'core/ver_detalle_venta.html', {'venta': venta, 'detalles': detalles})