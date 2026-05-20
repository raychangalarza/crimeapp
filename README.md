# Dashboard de datos de crímenes en Puerto Rico (2013-2016)

Webapp interactiva de para visualización y exploración de los datos de crímenes disponibles de Puerto Rico entre 2013 y 2016. Principalmente por una visualización a través de un mapa interactivo y un gráfico de barras, además de filtros para seleccionar que datos ver. Los datos provienen de la policía de Puerto Rico. 

---

Los filtros permiten seleccionar que área policiaca el usuario quiere ver, filtrar los delitos que quiere ver, si ocurrió en horas AM o PM y filtrar el día de la semana. El webapp enseña tres métricas del conjunto de datos filtrados, además del mapa interactivo y el gráfico de barras enseñando la cantidad de delitos de cada tipo filtrado.

---

## Setup para correr localmente

### Requisitos

- Python
- Pandas
- plotly
- streamlit

### Instalación de dependencias:

`pip install pandas streamlit plotly`

Además de descargar los datos (`crime_processed.csv`) que se encuentra en el repositorio, y el logo `crimeapp_logo.png`.

### Correr la aplicación

`streamlit run crimeapp_rgalarza.py`

Se inicializará en el `localhost:8501`

---

## Funcionalidad

### Filtros (sidebar)

* **Área policiaca** (selectbox) - Muestra los datos de una área policiaca seleccionada o de todas las áreas.
* **Delito** (multiselect) - Filtra los tipos de delitos los cuales el usuario quiere ver sus datos, todos seleccionados al primero usar la aplicación. Puede tener uno o más tipos de delitos seleccionados.
* **Día de semana** (multiselect) - Filtra los días de la semana las cuales el usuario quiera ver sus datos, al primer usar la aplicación los 7 días de la semana están seleccionados. Puede seleccionar uno o más días de la semana.
* **AM ó PM**  (selectbox) - Muestra los datos dentro de todas las horas del  día, de las horas de AM o las horas PM.

### Métricas

* **Cantidad de incidentes** - Número de incidentes en los datos filtrados
* **Delito más frecuente** - Delito más común en los datos filtrados
* **Área con más incidentes** - Área policiaca con mayor cantidad de casos en los datos filtrados.

### Visualizaciones

* **Mapa de puntos** - Ubicación de cada uno de los casos en los datos filtrados. Con colores para significar la gravedad del delito registrado. Cada punto al apuntarlo con el "mouse" enseña el área, delito, fecha, hora y día de la semana en la que ocurrió el delito.
* **Gráfico de barras** - Distribución de los delitos por el área policiaca seleccionada, en los datos filtrados.

---

## Bibliotecas

- [pandas](https://pandas.pydata.org/) — carga y manipulación del conjunto de datos
- [streamlit](https://streamlit.io/) — interfaz gráfica interactiva
- [plotly](https://plotly.com/python/) — mapa y gráfica de barras interactivos

---
 
## Autor
 
**Raychan J. Galarza Rodríguez**  
Proyecto Final — Comp3082: Introducción a la Programación y la Ciencia de Cómputos II  
Mayo 2026 | Ciencia de Datos  
Universidad de Puerto Rico en Humacao
