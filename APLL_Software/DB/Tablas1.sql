CREATE TABLE Venta (
  Numero_Orden INT PRIMARY KEY,
  CajaDPI INT,
  BodegaDPI INT,
  NIT INT,
  Total DECIMAL,
  MetodoPago VARCHAR,
  Fecha TIMESTAMP,
  FOREIGN KEY (NIT) REFERENCES Cliente(NIT)
);

CREATE TABLE Detalles_Venta (
  Numero_Orden INT,
  RepuestoID INT,
  Cantidad INT,
  Rebaja DECIMAL,
  SubTotal DECIMAL,
  FOREIGN KEY (Numero_Orden) REFERENCES Venta(Numero_Orden),
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID)
);

CREATE TABLE Cliente (
  NIT INT PRIMARY KEY,
  Nombre_Cliente VARCHAR,
  Contacto VARCHAR,
  Tipo VARCHAR
);

CREATE TABLE Pagos (
  MetodoPagoID INT PRIMARY KEY,
  MetodoPago VARCHAR,
  Usuario VARCHAR,
  EmpleadoDPI INT,
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