from django.db import models

from django.db import models


class Cliente(models.Model):
    NIT = models.IntegerField(primary_key=True)
    Nombre_Cliente = models.CharField(max_length=255)
    Contacto = models.CharField(max_length=255)
    Tipo = models.CharField(max_length=50)

class Carro(models.Model):
    CarroID = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=255)
    Linea = models.CharField(max_length=255)
    Modelo = models.CharField(max_length=10)
    Transmision = models.CharField(max_length=20)

class Proveedor(models.Model):
    ProveedorID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Direccion = models.CharField(max_length=255)
    Contacto = models.CharField(max_length=255)

class Empleados(models.Model):
    EmpleadoDPI = models.IntegerField(primary_key=True)
    Nombres = models.CharField(max_length=255)
    Apellidos = models.CharField(max_length=255)
    Sueldo = models.DecimalField(max_digits=10, decimal_places=2)

class Venta(models.Model):
    Numero_Orden = models.AutoField(primary_key=True)
    Nombre_Cliente = models.CharField(max_length=255)
    NIT = models.IntegerField()
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    Fecha = models.DateTimeField(auto_now_add=True)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, related_name='venta')

class Departamentos(models.Model):
    DepaID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)

class Repuestos(models.Model):
    RepuestoID = models.AutoField(primary_key=True)
    CarroID = models.IntegerField()
    Nombre = models.CharField(max_length=255)
    Categoria = models.CharField(max_length=50)
    Precio_Unitario = models.DecimalField(max_digits=10, decimal_places=2)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

class Detalles_Venta(models.Model):
    Detalles_VentaID = models.AutoField(primary_key=True)
    Numero_Orden = models.IntegerField()
    RepuestoID = models.IntegerField()
    Cantidad = models.IntegerField()
    Rebaja = models.DecimalField(max_digits=10, decimal_places=2)
    SubTotal = models.DecimalField(max_digits=10, decimal_places=2)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuestos, on_delete=models.CASCADE)

class Compra_Repuesto(models.Model):
    CompraRepuestoID = models.AutoField(primary_key=True)
    RepuestoID = models.IntegerField()
    Costo = models.DecimalField(max_digits=10, decimal_places=2)
    ProveedorID = models.IntegerField()
    repuesto = models.ForeignKey(Repuestos, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Usuario(models.Model):
    EmpleadoID = models.AutoField(primary_key=True)
    EmpleadoDPI = models.IntegerField()
    Usuario = models.CharField(max_length=50)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)

class Inventario(models.Model):
    CarroID = models.IntegerField()
    RepuestoID = models.IntegerField()
    Existencia = models.IntegerField()
    Cantidad_Minima = models.IntegerField()
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuestos, on_delete=models.CASCADE)

class Pagos(models.Model):
    PagoID = models.AutoField(primary_key=True)
    MetodoPago = models.CharField(max_length=50)
    Monto = models.DecimalField(max_digits=10, decimal_places=2)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='pagos')

class Comisiones(models.Model):
    ComisionID = models.AutoField(primary_key=True)
    EmpleadoDPI = models.IntegerField()
    NumOrden = models.IntegerField()
    Tipo = models.CharField(max_length=50)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

class Cotizacion(models.Model):
    CotizacionID = models.AutoField(primary_key=True)
    VendedorID = models.IntegerField()
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    Fecha = models.DateTimeField()
    vendedor = models.ForeignKey(Empleados, on_delete=models.CASCADE)

class Cotizacion_Detalle(models.Model):
    CotizacionDetalleID = models.AutoField(primary_key=True)
    CotizacionID = models.IntegerField()
    RepuestoID = models.IntegerField()
    Cantidad = models.IntegerField()
    Precio_Unitario = models.DecimalField(max_digits=10, decimal_places=2)
    Precio_Total = models.DecimalField(max_digits=10, decimal_places=2)
    Numero_Linea = models.IntegerField()
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuestos, on_delete=models.CASCADE)

class Compra_Carro(models.Model):
    Fecha = models.DateTimeField()
    Cantidad = models.IntegerField()
    CarroID = models.IntegerField()
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

class Bitacora_Alertas(models.Model):
    AlertaID = models.AutoField(primary_key=True)
    RepuestoID = models.IntegerField()
    Fecha = models.DateTimeField()
    repuesto = models.ForeignKey(Repuestos, on_delete=models.CASCADE)

class Historial_Cambio(models.Model):
    CambioID = models.AutoField(primary_key=True)
    Tipo_Cambio = models.CharField(max_length=50)
    Tabla_Afectada = models.CharField(max_length=50)
    ID_Registro = models.IntegerField()
    Usuario = models.CharField(max_length=50)
    Fecha = models.DateTimeField()
    Comentario = models.CharField(max_length=255)

class Cambios_Salarios(models.Model):
    Cambio_SalarioID = models.AutoField(primary_key=True)
    EmpleadoDPI = models.IntegerField()
    Fecha_Cambio = models.DateTimeField()
    Salario_Anterior = models.DecimalField(max_digits=10, decimal_places=2)
    Salario_Nuevo = models.DecimalField(max_digits=10, decimal_places=2)
    Motivo = models.CharField(max_length=255)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
