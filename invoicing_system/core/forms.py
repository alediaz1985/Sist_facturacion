from django import forms

from .models import Venta, DetalleVenta, Cliente, Producto

class ClienteForm(forms.ModelForm):
    """
    Formulario para la creación y edición de clientes.
    Incluye todos los campos relevantes del modelo Cliente.
    """
    class Meta:
        model = Cliente
        fields = ['dni_cuit', 'nombre', 'direccion', 'telefono', 'email']
        labels = {
            'dni_cuit': 'DNI/CUIT',
            'nombre': 'Nombre completo',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Correo electrónico'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dni_cuit': forms.TextInput(attrs={'class': 'form-control'})
        }

class VentaForm(forms.ModelForm):
    """
    Formulario para la creación y edición de ventas.
    Incluye el cliente asociado, la fecha de la venta y el tipo de factura.
    """
    class Meta:
        model = Venta
        fields = ['cliente', 'fecha_venta', 'tipo_factura']
        widgets = {
            'fecha_venta': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tipo_factura': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'})
        }

class DetalleVentaForm(forms.ModelForm):
    """
    Formulario para la creación y edición de detalles de venta.
    Incluye el producto y la cantidad de dicho producto en una venta específica.
    """
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'})
        }

class ProductoForm(forms.ModelForm):
    """
    Formulario para la creación y edición de productos.
    Incluye el código de barras, la descripción y el precio del producto.
    """
    class Meta:
        model = Producto
        fields = ['codigo_barra', 'descripcion', 'precio']
        widgets = {
            'codigo_barra': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'})
        }

class BusquedaClienteForm(forms.Form):
    busqueda = forms.CharField(label='Buscar Cliente', max_length=100, required=False, help_text='Ingrese DNI, CUIT o nombre')
