# leer_csv.R — Cargar el reporte CSV del ERP (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/leer_csv.R

# TODO 1: carga data/ventas.csv con readr::read_csv en un data.frame
library(readr)

ventas <- read_csv("data/ventas.csv")

# TODO 2: imprime las dimensiones (dim) del data.frame
print("Dimensiones:")
print(dim(ventas))

# TODO 3: imprime las primeras filas (head) para revisar las columnas
print("Primeras filas:")
print(head(ventas))