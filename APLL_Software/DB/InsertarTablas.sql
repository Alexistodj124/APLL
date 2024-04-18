-- Inserts Ana Paula
/*INSERT INTO Detalles_Venta (Numero_Orden, RepuestoID, Cantidad, Rebaja, SubTotal)
VALUES (1, 101, 1, 0.20, 150.00),
       (1, 102, 2, 0.10, 250.00),
       (2, 103, 3, 0.20, 350.00);

INSERT INTO Compra_Repuesto (CompraRepuestoID, RepuestoID, Costo, ProveedorID)
VALUES (1, 101, 500.00, 001),
       (2, 102, 275.00, 002),
       (3, 103, 150.00, 003);

INSERT INTO Repuestos (RepuestoID, CarroID, Nombre, Categoria, Precio_Unitario)
VALUES (101, 1, 'Filtro de aceite', 'Filtros', 15.00);*/

--PRUEBA--

INSERT INTO Carro (carroid, marca, linea, modelo, transmision)
VALUES (1, 'Mazda', 'Protege', 1999, 'Automático');

INSERT INTO Repuestos (RepuestoID, CarroID, Nombre, Categoria, Precio_Unitario)
VALUES (1, 1, 'Filtro de aceite', 'Filtros', 15.00);
