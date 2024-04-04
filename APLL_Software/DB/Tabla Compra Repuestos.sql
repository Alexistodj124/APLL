CREATE TABLE CompraRep (
    CompraRID             INTEGER NOT NULL,
    RepuestoID            INTEGER NOT NULL,
    Costo                 DECIMAL(9, 2) NOT NULL,
    ProveedorID           INTEGER NOT NULL,
    Proveedor_ProveedorID INTEGER NOT NULL
);

COMMENT ON TABLE CompraRep IS
    'CompraRep';

ALTER TABLE CompraRep ADD CONSTRAINT CompraRep_pk PRIMARY KEY ( CompraRID );
