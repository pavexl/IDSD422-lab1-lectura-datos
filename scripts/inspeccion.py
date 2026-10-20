# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

import pandas as pd

ventas = pd.read_csv("data/ventas.csv")

print("Tipos de columnas:")
print(ventas.dtypes)

# Crear la columna derivada ticket
ventas["ticket"] = ventas["ventas"] / ventas["clientes"]

print("\nDatos con la columna ticket: ")
print(ventas)

#1. Venta promedio por sucursal
print("\nVenta promedio por sucursal:")
print(ventas.groupby("sucursal")["ventas"].mean())
#         - venta promedio por sucursal M
print("===== Ventas por sucursal =====")
print(ventas[['sucursal', 'ticket']])
print("==============================")

#2. Ticket promedio general
ticket_promedio = ventas["ventas"].sum() / ventas["clientes"].sum()
print("\nTicket promedio general:")
print(ticket_promedio)

#3. Sucursal con mayor y menor venta
indice_mayor = ventas["ventas"].idxmax()
indice_menor = ventas["ventas"].idxmin()

print("\nSucursal con mayor venta:")
print("Sucursal:", ventas.loc[indice_mayor, "sucursal"])
print("Ventas:", ventas.loc[indice_mayor, "ventas"])

print("\nSucursal con menor venta:")
print("Sucursal:", ventas.loc[indice_menor, "sucursal"])
print("Ventas:", ventas.loc[indice_menor, "ventas"])

# 4. Region con mayor venta total
ventas_por_region = ventas.groupby("region")["ventas"].sum()

print("\nVentas totales por region: ")
print(ventas_por_region)

print("\nRegion con mayor venta total:")
print(ventas_por_region.idxmax())
