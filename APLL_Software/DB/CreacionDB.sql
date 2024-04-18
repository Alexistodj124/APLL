-- CREACIÓN DE TABLAS --
CREATE TABLE Cliente (
  NIT INT PRIMARY KEY,
  Nombre_Cliente VARCHAR(255),
  Contacto VARCHAR(255),
  Tipo VARCHAR(50)
);

CREATE TABLE Carro (
  CarroID SERIAL PRIMARY KEY,
  Marca VARCHAR(255),
  Linea VARCHAR(255),
  Modelo VARCHAR(10),
  Transmision VARCHAR(20)
);

CREATE TABLE Proveedor (
  ProveedorID SERIAL PRIMARY KEY,
  Nombre VARCHAR(255),
  Direccion VARCHAR(255),
  Contacto VARCHAR(255)
);

CREATE TABLE Empleados (
  EmpleadoDPI SERIAL PRIMARY KEY,
  Nombres VARCHAR(255),
  Apellidos VARCHAR(255),
  Sueldo DECIMAL(10, 2)
);


CREATE TABLE Venta (
  Numero_Orden SERIAL PRIMARY KEY,
  CajaDPI INT,
  BodegaDPI INT,
  NIT INT,
  Total DECIMAL(10, 2),
  MetodoPago VARCHAR(50),
  Fecha TIMESTAMP,
  FOREIGN KEY (NIT) REFERENCES Cliente(NIT)
);

CREATE TABLE Departamentos (
  DepaID SERIAL PRIMARY KEY,
  Nombre VARCHAR(255)
);

CREATE TABLE Repuestos (
  RepuestoID SERIAL PRIMARY KEY,
  CarroID INT,
  Nombre VARCHAR(255),
  Categoria VARCHAR(50),
  Precio_Unitario DECIMAL(10, 2),
  FOREIGN KEY (CarroID) REFERENCES Carro(CarroID)
);

CREATE TABLE Detalles_Venta (
  Detalles_VentaID SERIAL PRIMARY KEY,
  Numero_Orden INT,
  RepuestoID INT,
  Cantidad INT,
  Rebaja DECIMAL(10, 2),
  SubTotal DECIMAL(10, 2),
  FOREIGN KEY (Numero_Orden) REFERENCES Venta(Numero_Orden),
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID)
);


CREATE TABLE Compra_Repuesto (
  CompraRepuestoID SERIAL PRIMARY KEY,
  RepuestoID INT,
  Costo DECIMAL(10, 2),
  ProveedorID INT,
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID),
  FOREIGN KEY (ProveedorID) REFERENCES Proveedor(ProveedorID)
);

CREATE TABLE Usuario (
  EmpleadoID SERIAL PRIMARY KEY,
  EmpleadoDPI INT,
  Usuario VARCHAR(50),
  FOREIGN KEY (EmpleadoDPI) REFERENCES Empleados(EmpleadoDPI)
);


CREATE TABLE Inventario (
  CarroID INT,
  RepuestoID INT,
  Existencia INT,
  Cantidad_Minima INT,
  FOREIGN KEY (CarroID) REFERENCES Carro(CarroID),
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID)
);


CREATE TABLE Pagos (
  MetodoPagoID SERIAL PRIMARY KEY,
  MetodoPago VARCHAR(50),
  Usuario VARCHAR(50),
  EmpleadoDPI INT,
  FOREIGN KEY (EmpleadoDPI) REFERENCES Empleados(EmpleadoDPI)
);



CREATE TABLE Comisiones (
  ComisionID SERIAL PRIMARY KEY,
  EmpleadoDPI INT,
  NumOrden INT,
  Tipo VARCHAR(50),
  FOREIGN KEY (EmpleadoDPI) REFERENCES Empleados(EmpleadoDPI),
  FOREIGN KEY (NumOrden) REFERENCES Venta(Numero_Orden)
);


CREATE TABLE Cotizacion (
  CotizacionID SERIAL PRIMARY KEY,
  VendedorID INT,
  Total DECIMAL(10, 2),
  Fecha TIMESTAMP,
  FOREIGN KEY (VendedorID) REFERENCES Empleados(EmpleadoDPI)
);

CREATE TABLE Cotizacion_Detalle (
  CotizacionDetalleID SERIAL PRIMARY KEY,
  CotizacionID INT,
  RepuestoID INT,
  Cantidad INT,
  Precio_Unitario DECIMAL(10, 2),
  Precio_Total DECIMAL(10, 2),
  Numero_Linea INT,
  FOREIGN KEY (CotizacionID) REFERENCES Cotizacion(CotizacionID),
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID)
);

CREATE TABLE Compra_Carro (
  Fecha TIMESTAMP,
  Cantidad INT,
  CarroID INT,
  FOREIGN KEY (CarroID) REFERENCES Carro(CarroID)
);



CREATE TABLE Bitacora_Alertas (
  AlertaID SERIAL PRIMARY KEY,
  RepuestoID INT,
  Fecha TIMESTAMP,
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID)
);

CREATE TABLE Historial_Cambio (
  CambioID SERIAL PRIMARY KEY,
  Tipo_Cambio VARCHAR(50),
  Tabla_Afectada VARCHAR(50),
  ID_Registro INT,
  Usuario VARCHAR(50),
  Fecha TIMESTAMP,
  Comentario VARCHAR(255)
);

CREATE TABLE Cambios_Salarios (
  Cambio_SalarioID SERIAL PRIMARY KEY,
  EmpleadoDPI INT,
  Fecha_Cambio TIMESTAMP,
  Salario_Anterior DECIMAL(10, 2),
  Salario_Nuevo DECIMAL(10, 2),
  Motivo VARCHAR(255),
  FOREIGN KEY (EmpleadoDPI) REFERENCES Empleados(EmpleadoDPI)
);