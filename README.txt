#Proyecto: Dashboard Climático Global 2025 (NOAA)

## Descripción
Este proyecto es una aplicación web interactiva desarrollada en Python utilizando el framework Dash y Plotly. Su objetivo principal es visualizar y analizar el comportamiento de fenómenos meteorológicos (Temperatura Máxima, Temperatura Mínima y Precipitación) a nivel global durante el año 2025. Los datos fueron extraídos de la base de datos pública Global Historical Climatology Network Daily (GHCN-D) de la NOAA.

## Estructura del Proyecto
- `app.py`: Archivo principal que levanta el servidor web y contiene los controladores interactivos (callbacks) y las gráficas.
- `EDA.ipynb`: Jupyter Notebook con el Análisis Exploratorio de Datos preliminar, limpieza y tratamiento de nulos.
- `data/`: Carpeta destinada a alojar el archivo de datos masivo (`2025.csv`).

## Requisitos y Librerías
Para ejecutar este dashboard, el entorno de Python debe contar con:
- pandas
- dash
- plotly

## Instrucciones de Ejecución (Servidor Local)
1. Asegúrate de tener el archivo de datos original (`2025.csv`) ubicado dentro de la carpeta `data`.
2. Abre la terminal en la raíz del proyecto.
3. Activa el entorno virtual (recomendado): `.\env\Scripts\activate`
4. Ejecuta la aplicación: `python app.py`
5. Abre el navegador web e ingresa a la dirección local: `http://127.0.0.1:8050/`


## Link del Dataset: https://noaa-ghcn-pds.s3.amazonaws.com/index.html#csv/by_year/

## Autores
- Víctor Sánchez - 20-70-7342
- Arquimedes Moran - 8-991-1628

