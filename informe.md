# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** ___/___/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

> **Formato de entrega:** este documento organiza el contenido del informe. El entregable es su versión final en **PDF** según la **plantilla del curso** (aula virtual), con el enlace de tu repositorio en la carátula; el PDF se incluye en `informes/` de tu fork.

---

## Resumen ejecutivo
Se analizaron los reportes de ventas de RetailAndina S. A. en formatos CSV, JSON y Excel mediante Python y R. Los tres archivos presentaron cinco filas y cuatro columnas, y las comparaciones realizadas en R entre CSV–JSON y CSV–Excel devolvieron TRUE. Las ventas totales fueron de 60.040, con un ticket promedio general aproximado de 38,07. Estos resultados pueden tomarse como punto inicial para estudiar la producividad de cada sucursal y obtener un analisis comercial mas profundo.

## 1. ¿Los tres formatos contienen la misma información?

*Carga los tres archivos (CSV, JSON y Excel) en Python y en R, y compara dimensiones y estructura. Completa la tabla:*Se importaron los archivos CSV, JSON y Excel a traves los procedimientos correspondientes en Python y R. Cada archivo contenia cinco registros de sucursales y cuatro columnas

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales |5 | 4|```pandas.read_csv()``` en Python; ```read_csv()``` de ```readr``` en R 
| JSON | API de fidelización | 5| 4|```json.load()``` y ```pd.DataFrame()```en Python; ```fromJSON()```de ```jsonlite``` en R |
| Excel | Consolidado de finanzas | 5| 4|```pandas.read_excel()```en Python; ```read_excel()```de ```readxl```en R |

Las comparaciones realizadas en R entre los datos CSV-JSON y CSV-Excel devolvieron TRUE. Por tanto, esto comprueba que el contenido coincidio en ambas comparaciones y tienen las mismas dimensiones.

*¿La estructura interna del archivo (texto plano, anidada, binaria) cambia el contenido?*

La estructura interna del archivo cambia la forma de leer y organizar los datos, pero no necesariamente su contenido.
- El **CSV** almacena datos en texto delimitado.
- El **JSON** representa los registros mediante una estructura de objetos.
- **Excel** organiza la informacion en hojas de cálculo.Si los tres archivos contienen los mismos registros y valores, pueden representar la misma información sin importar sus diferencias estructurales. 

Si los tres archivos contienen los mismos registros y valores, pueden registrar la misma información sin importar sus diferencias estructurales.

## 2. Tipos de datos y calidad

*Inspecciona los tipos que infiere cada lenguaje. Completa la tabla y comenta si los tipos son los esperados para cada variable:*
Al inspespeccionar los datos, Python y R reconocieron las variables de rtexto y numericaséricascon tipos con tipos diferentes, pero a
| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` |```int64```|```dbl```|Valor numérico de ventas por sucursal|
| `clientes`|```int64``` | ```dbl```| Cantidad numérica de clientes por sucursal|
| `sucursal` |```int64``` | ```dbl```|Nombre de la sucursal; variable de texto|
| `region` |  ```object```| ```chr```| Region a la que pertenece la sucursal; variable de texto|

*¿Qué habría indicado un dato sucio si, por ejemplo, `ventas` llegara como texto?*

Los tipos inferidos fueron apropiados para los calculos realizados. Si la columna ```ventas``` hubiera llegado como texto, podría hacer indicado que existen valores almacenados como cadenas en lugar de números, ya sea por carácteres adicionales o formatos inconsistentes. Esto impediría operaciones aritméticas directas o requerir una limpieza y conversión previa.

## 3. Particularidades técnicas encontradas

*Anota qué encontraste al leer cada formato (una nota por formato): ¿el JSON llegó como tabla? ¿hubo que indicar una hoja en el Excel? ¿cómo se expresan las categóricas en cada lenguaje?*

- **CSV:** En Python utilice `pandas.read_csv()` y en R `read_csv()` de la librería `readr` para importar el archivo `ventas.csv`. En R, el argumento `show_col_types = FALSE` permitió ocultar el mensaje informativo sobre los tipos de columnas detectados. Ambos procedimientos organizaron los registros en una estructura tabular.

- **JSON:** En Python utilicé `json.load()` para leer el archivo `ventas.json`, lo que devolvió una lista de diccionarios. Después, mediante `pd.DataFrame(datos)`, organicé los registros en filas y columnas. En R utilicé `fromJSON()` de la librería `jsonlite` para leer el archivo y `as.data.frame()` para convertir los registros en una estructura tabular.

- **Excel:** en Python utilicé `pandas.read_excel()` y en R la función `read_excel()` de la librería `readxl` para importar el archivo `ventas.xlsx`. En R indiqué explícitamente la hoja que debía leerse mediante el argumento `sheet = "ventas"`.

En cuanto a los tipos de datos, Python identificó las variables de texto como `object` y las numéricas como `int64`, mientras que R las representó como `chr` y `dbl`, respectivamente. Aunque los nombres de los tipos difieren entre ambos lenguajes, fueron los correctos para realizar correctamente las operaciones de la práctica.

## 4. Indicadores para la reunión del lunes

A partir de los datos consolidados de las cinco sucursales, calculé los indicadores solicitados para resumir el desempeño de ventas durante el período analizado.

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal |Cuenca (8.540) <br> Guayaquil Centro (15.200) <br> Guayaquil Norte (13.980) <br> Quito Norte (12.450) <br> Quito Sur (9.870) <br> TOTAL (PROMEDIO): 12.008 |
| Ticket promedio (ventas ÷ clientes) | 38,072|
| Sucursal con mayor venta |Guayaquil Centro (15.200) |
| Sucursal con menor venta |Cuenca (8.540) |
| Región con mayor venta total | Sierra (30.860)|

## 5. Conclusiones y recomendación

1. Los archivos CSV, JSON y Escel presentaron cinco filas y cuatro columnas. Además, las comparaciones CSV-JSON y CSV-Excel realizadas en R devolvieron TRUE, esto corrobora que el contenido es el mismo en las comprobaciones realizadas.
2. Las ventas totales de las sucursales fueron de 60.040 y el ticket promedio general fue de aproximadamente 38,07 para los 1.577 clientes registrados. Guayaquil Centro obtuvo las mayores ventas, con 15.200, mientras que Cuenca obtuvo las menores, con 8.540.
3. La region Sierra registro ventas por 30.0860, superando a la Costa, que obtuvo 29.180, por una diferencia de 1.680. Con los indicadores obtenidos se recomienda a la empresa revisar el desempeño de las sucursales, e indagar a fondo de cuales son las razones que influyen en estas diferencias, asi tambien, complementar este analisis con otros periodos, antes de tomar cualquier decision comercial.
