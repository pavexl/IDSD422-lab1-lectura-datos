# inspeccion.R — Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# TODO 1: carga data/ventas.csv
library(readr)
library(dplyr)

ventas <- read_csv("data/ventas.csv", show_col_types = FALSE)
# TODO 2: imprime la estructura (str) para ver los tipos
#         (fija si region llegó como character o factor)
str(ventas)

# Reviso si region es character o factor
print(class(ventas$region))

# TODO 3: crea la columna derivada "ticket" = ventas / clientes
ventas <- ventas %>%
mutate(ticket = ventas / clientes)

print("Datos de la columna ticket:")
print(ventas)
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal (aggregate o dplyr)
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

# 1. Venta promedio por sucursal
print("Venta promedio por sucursal:")
print(ventas %>% group_by(sucursal) %>% summarise(venta_promedio = mean(ventas)))

# 2. Ticket promedio general
ticket_promedio <- sum(ventas$ventas) / sum(ventas$clientes)
print("Ticket promedio general:")
print(ticket_promedio)

# 3. Sucursal con mayor y menor venta
print("Sucursal con mayor venta:")
print(ventas[which.max(ventas$ventas), c("sucursal", "ventas")])

print("Sucursal con menor venta: ")
print(ventas[which.min(ventas$ventas), c("sucursal", "ventas")])

# 4. Region con mayor venta total
ventas_por_region <- ventas %>%
group_by(region) %>%
summarise(venta_total = sum(ventas), .groups = "drop")

print("Ventas totales por región:")
print(ventas_por_region)

print("Region con mayor venta total:")
print(ventas_por_region[which.max(ventas_por_region$venta_total),])