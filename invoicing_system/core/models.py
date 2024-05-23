from django.db import models

class Cliente(models.Model):
    dni_cuit = models.CharField(max_length=20, unique=True, default='00000000000')
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    ciudad = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

class Producto(models.Model):
    codigo_barra = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateField()
    tipo_factura = models.CharField(max_length=50, default='X')
    total = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
