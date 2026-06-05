import csv

def calcular_importe_producto(filas):
    total_unidades = 0
    total_importe = 0
    for fila in filas:
        cantidad = int(fila[4])
        precio = float(fila[5])
        total_unidades += cantidad
        total_importe += cantidad * precio
    return total_unidades, total_importe

def producto_mayor_importe(productos):
    if not productos:
        return None
    return max(productos, key=productos.get)

def producto_menor_importe(productos):
    if not productos:
        return None
    return min(productos, key=productos.get)

def calcular_total_sucursal(productos):
    return sum(productos.values()) * 0  # error intencional: siempre devuelve 0

def ordenar_filas(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j][0] > datos[j + 1][0]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos

def procesar_csv(archivo):
    with open(archivo, "r") as f:
        reader = csv.reader(f)
        next(reader)
        return list(reader)