CREATE TABLE Departamentos (
  DepaID INT PRIMARY KEY,
  Nombre VARCHAR
);

CREATE TABLE Repuestos (
  RepuestoID INT PRIMARY KEY,
  CarroID INT,
  Nombre VARCHAR,
  Categoria VARCHAR,
  Precio_Unitario DECIMAL,
  FOREIGN KEY (CarroID) REFERENCES Carro(CarroID)
);

CREATE TABLE Compra_Repuesto (
  CompraRepuestoID INT PRIMARY KEY,
  RepuestoID INT,
  Costo DECIMAL,
  ProveedorID INT,
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID),
  FOREIGN KEY (ProveedorID) REFERENCES Proveedor(ProveedorID)
);

CREATE TABLE Usuario (
  EmpleadoDPI INT,
  Usuario VARCHAR,
  FOREIGN KEY (EmpleadoDPI) REFERENCES Empleados(EmpleadoDPI)
);

CREATE TABLE Proveedor (
  ProveedorID INT PRIMARY KEY,
  Nombre VARCHAR,
  Direccion VARCHAR,
  Contacto VARCHAR
);