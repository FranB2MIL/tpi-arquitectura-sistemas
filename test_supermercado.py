import pytest
from supermercado import (
    calcular_importe_producto,
    producto_mayor_importe,
    producto_menor_importe,
    calcular_total_sucursal,
    ordenar_filas,
    procesar_csv,
)

# --- calcular_importe_producto ---

def test_importe_producto_una_fila():
    filas = [["S1", "P001", "2024", "PROV1", "10", "5.0"]]
    unidades, importe = calcular_importe_producto(filas)
    assert unidades == 10
    assert importe == 50.0

def test_importe_producto_multiples_filas():
    filas = [
        ["S1", "P001", "2024", "PROV1", "10", "5.0"],
        ["S1", "P001", "2024", "PROV1", "5", "5.0"],
    ]
    unidades, importe = calcular_importe_producto(filas)
    assert unidades == 15
    assert importe == 75.0

# --- producto_mayor_importe ---

def test_mayor_importe_normal():
    productos = {"P001": 500.0, "P002": 1200.0, "P003": 300.0}
    assert producto_mayor_importe(productos) == "P002"

def test_mayor_importe_dict_vacio():
    assert producto_mayor_importe({}) is None

# --- producto_menor_importe ---

def test_menor_importe_normal():
    productos = {"P001": 500.0, "P002": 1200.0, "P003": 300.0}
    assert producto_menor_importe(productos) == "P003"

def test_menor_importe_dict_vacio():
    assert producto_menor_importe({}) is None

# --- calcular_total_sucursal ---

def test_total_sucursal():
    productos = {"P001": 500.0, "P002": 1200.0, "P003": 300.0}
    assert calcular_total_sucursal(productos) == 2000.0

def test_total_sucursal_vacia():
    assert calcular_total_sucursal({}) == 0

# --- ordenar_filas ---

def test_ordenar_filas():
    datos = [["S3", "x"], ["S1", "x"], ["S2", "x"]]
    resultado = ordenar_filas(datos)
    assert resultado[0][0] == "S1"
    assert resultado[1][0] == "S2"
    assert resultado[2][0] == "S3"

def test_ordenar_filas_ya_ordenadas():
    datos = [["S1", "x"], ["S2", "x"], ["S3", "x"]]
    resultado = ordenar_filas(datos)
    assert resultado[0][0] == "S1"


# --- tests con CSV real ---

def test_procesar_csv_carga_filas():
    filas = procesar_csv("COMPRAS_supermercado.csv")
    assert len(filas) > 0

def test_procesar_csv_estructura_correcta():
    filas = procesar_csv("COMPRAS_supermercado.csv")
    # cada fila debe tener 6 columnas: PRSUC, PRCOD, PRFEC, PRPROV, PRCANT, PRPRE
    assert len(filas[0]) == 6

def test_ordenar_filas_con_csv_real():
    filas = procesar_csv("COMPRAS_supermercado.csv")
    ordenadas = ordenar_filas(filas)
    # la primera sucursal debe ser <= la última
    assert ordenadas[0][0] <= ordenadas[-1][0]