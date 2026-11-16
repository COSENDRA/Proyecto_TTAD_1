#CARGAR LOS DATOS
import json

def cargar_ventas():
    with open("data.json", "r") as archivo:
        datos = json.load(archivo)

    return datos["ventas"]   

#TOTAL FACTURADO
def total_facturado():
    ventas = cargar_ventas()
    total = 0

    for venta in ventas:
        total = total + venta["cantidad"] * venta["precio_unitario"]

    return total
print("TOTAL FACTURADO:", total_facturado())


#VENTAS POR CATEGORÍA
def ventas_por_categoria():
    ventas = cargar_ventas()
    categorias = {}

    for venta in ventas:
        categoria = venta["categoria"]
        importe = venta["cantidad"] * venta["precio_unitario"]

        if categoria in categorias:
            categorias[categoria] = categorias[categoria] + importe
        else:
            categorias[categoria] = importe

    return categorias
print("VENTAS POR CATEGORIA:", ventas_por_categoria())


#PRODUCTOS MÁS VENDIDOS
def producto_mas_vendido():
    ventas = cargar_ventas()
    productos = {}

    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]

        if producto in productos:
            productos[producto] = productos[producto] + cantidad
        else:
            productos[producto] = cantidad

    mas_vendido = max(productos, key=productos.get)

    return mas_vendido
print("PRODUCTO MAS VENDIDO:", producto_mas_vendido())