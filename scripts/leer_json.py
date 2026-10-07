# leer_json.py — Cargar el reporte JSON de la API (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_json.py

# TODO 1: importa json y pandas
# TODO 2: carga data/ventas.json con json.load
# TODO 3: convierte la lista de diccionarios en un DataFrame
#         (recuerda del cap. 2: el JSON no llega como tabla directa)
# TODO 4: imprime las dimensiones y las primeras filas

## ACTIVIDAD LEER ARCHIVO JSON

#leo archivo json usando pandas
import json
import pandas as pd

# abro archivo json
with open("data/ventas.json", encoding = "utf-8") as f:
  datos = json.load(f)

#normalizo json y retorno 
ventas = pd.json_normalize(datos)

print(ventas.head())

#imprimir las dimensiones
print("Dimensiones: ", ventas.shape)

#imprimir los tipos de columna
print("\nTipos de columna\n")
print(ventas.dtypes)