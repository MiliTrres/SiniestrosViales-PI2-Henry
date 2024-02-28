<p align=center><img src=https://github.com/MiliTrres/SiniestrosViales-PI2-Henry/blob/main/Img/imgHenry.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº 2** </h1>

# <h1 align=center>**HOMICIDIOS EN SINIESTROS VIALES**</h1>

<p align=center><img src=https://github.com/MiliTrres/SiniestrosViales-PI2-Henry/blob/main/Img/Captura%20de%20pantalla%202024-02-27%20173918.png><p>

## Introducción

En áreas urbanas, los accidentes de tráfico, también llamados siniestros viales, son eventos preocupantes que involucran vehículos en la via pública y son causados por colisiones entre autos, motos, bicicletas o peatones, atropellos, choques contra objetos fijos o vuelcos de vehículos. Estos incidentes pueden causar daños materiales, lesiones graves e incluso la muerte.

En ciudades grandes como Buenos Aires, los accidentes viales son un problema importante debido al gran número de vehículos y la densidad de población. Estos incidentes afectan significativamente la seguridad de los residentes, visitantes, la infraestructura vial y los servicios de emergencia.

La tasa de mortalidad por accidentes viales es un indicador crítico de seguridad vial en muchas regiones. Se calcula como la cantidad de muertes por cada cierto número de habitantes o vehículos registrados. Reducir esta tasa es una prioridad y se logra mediante educación vial, respeto a las normas de tránsito y seguridad en las carreteras y calles.

En Argentina, hay alrededor de 4000 muertes al año debido a accidentes viales, siendo esta la principal causa de muertes violentas en el país. Por esta razón, el Observatorio de Movilidad y Seguridad Vial (OMSV) solicita nuestra participación en un proyecto de análisis de datos para ayudar a las autoridades locales a reducir la cantidad de muertes en accidentes viales.

## Fuente de datos:
La fuente de datos pricipal utilizada para este proyecto, fue obtenida desde la página *Buenos Aires Data*, donde se comparten datos abiertos para el público en general.

Puedes acceder a la página desde el siguiente enlace [Buenos Aires Data](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales).

Para acceder directamente al dataset utilizado en este proyecto, haz click en el siguiente enlace [Dataset Homicidios](https://github.com/MiliTrres/SiniestrosViales-PI2-Henry/blob/main/Data/homicidios.xlsx).

Para comprender mejor el dataset y sus variables, puedes acceder al siguiente enlace [Diccionario de Datos](https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/NOTAS_HOMICIDIOS_SINIESTRO_VIAL.pdf).

# Fuentes de datos adicionales:
Ademas de la fuente de datos principal, se accedieron a fuentes de datos complementarias para un analisis más preciso.

Se obtuvo información de las comunas a traves de la página *Buenos Aires Ciudad*. 
Puede acceder a la página desde el siguiente enlace [Buenos Aires Ciudad / Comuna](https://buenosaires.gob.ar/jefaturadegabinete/atencion-ciudadana-y-gestion-comunal/gestion-comunal/comunas).

Se obtuvo información de los barrios que conforman cada comuna de la ciudad, también desde la pagina *Buenos Aires Ciudad*. Puede acceder a la página desde el siguiente enlace [Buenos Aires Ciudad / Barrios](https://buenosaires.gob.ar/laciudad/barrios).

Y por último, se obtuvo información de la población de la ciudad por comuna y por sexo. Puede descargar el dataset desde el siguiente enlace [Buenos Aires Ciudad / Población](https://www.estadisticaciudad.gob.ar/eyc/?p=28146).

## Tecnologias y herramientas utilizadas:

Para el desarrollo del EDA (*Exploratory Data Analysis*), se utilizaron las siguientes herramientas y tecnologias:

![VSCode](https://img.shields.io/badge/-VSCode-333333?style=flat&logo=visual-studio-code)
![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)
![Jupyter](https://img.shields.io/badge/-Jupyter-333333?style=flat&logo=jupyter)
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat&logo=WordCloud)
![Seaborn](https://img.shields.io/badge/Seaborn-333333?style=flat&logo=Seaborn)

Para el desarrollo del dashboard, se utilizaron las siguientes herramientas:

![PowerBI](https://img.shields.io/badge/PowerBI-333333?style=flat&logo=powerbi)
![DAX](https://img.shields.io/badge/DAX-333333?style=flat&logo=DAX)













## Datasets

Para desarrollar el proyecto se utilizaron tres archivos en formato JSON:

`**output_steam_games.json**`: Contiene información sobre los juegos; el nombre, el editor, el desarrollador, los precios y las etiquetas.

`**australian_users_items.json**`: Contiene información sobre los juegos utilizados por los usuarios y el tiempo que cada usuario pasa en cada juego.

`**australian_users_reviews.json**`: Contiene los comentarios que los usuarios realizaron sobre los juegos que usan, así como recomendaciones o críticas sobre esos juegos, ID del usuario y su URL.

## Tareas realizadas

### ETL (Extract, Transform and Load)
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![VSCode](https://img.shields.io/badge/-VSCode-333333?style=flat&logo=visual-studio-code)
![Jupyter](https://img.shields.io/badge/-Jupyter-333333?style=flat&logo=jupyter)
![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)

En esta fase, se llevo a cabo la ingesta de datos. Se convirtieron los datasets en DataFrames para poder trabajar de manera optima, se desanidaron columnas anidadas, se trasnformaron y limpiaron datos. Para ser más precisos, en esta etapa se realizaron tareas como las siguientes: Análisis y limpieza de valores nulos,
se completaron datos faltantes, se eliminaron algunas columnas y se cambiaron el nombre de otras, se transformaron los tipos de datos, etc. 

> Para ver en detalle las tareas realizadas en esta etapa, ingrese al siguiente link: [ETL](/ETL.ipynb)

### Feature Engineering
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![VSCode](https://img.shields.io/badge/-VSCode-333333?style=flat&logo=visual-studio-code)
![Jupyter](https://img.shields.io/badge/-Jupyter-333333?style=flat&logo=jupyter)
![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)
![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-333333?style=flat&logo=beautiful)
![TextBlob](https://img.shields.io/badge/TextBlob-333333?style=flat&logo=textblob)

Esta etapa se centró en el análisis de sentimientos de los comentarios de los usuarios, usando la librería TextBlob. 
En en dataset user_reviews se agrego una columna llamada `sentiment_analysis`, donde se categorizan las reseñas de los usuarios en positiva, neutral o negativa.
Siendo: 
  - 0: Negativa
  - 1: Neutra
  - 2: Positiva

Además, se prepararon los conjuntos de datos necesarios para optimizar las consultas y funcionalidades del servicio en la nube.

> Para ver en detalle las tareas realizadas en esta etapa, ingrese al siguiente link: [FeatureEngineering](/FeatureEngineering.ipynb)

### EDA (Exploratory Data Analysis)
![WordCloud](https://img.shields.io/badge/WordCloud-333333?style=flat&logo=WordCloud)
![SciPy](https://img.shields.io/badge/SciPy-333333?style=flat&logo=WordCloud)
![Matplotlib](https://img.shields.io/badge/Matplotlib-333333?style=flat&logo=WordCloud)
![Seaborn](https://img.shields.io/badge/Seaborn-333333?style=flat&logo=Seaborn)

Se llevó a cabo un análisis exploratorio de los tres conjuntos de datos después del proceso de ETL, analizamos el porcentaje de valores nulos, distribución y outliers de los precios de los items, usuarios con más horas jugadas, TOP 5 de los mejores desarrolladores,etc.
Esto permitió visualizar mejor las variables categóricas y numéricas, identificando las que son esenciales para el modelo de recomendación.
También, se prepararon los datasets necesarios para cada una de las funciones.

> Para ver en detalle las tareas realizadas en esta etapa, ingrese al siguiente link: [EDA](/EDA.ipynb)

### Modelamiento (Desarrollo de modelos de aprendizaje automático)
![VSCode](https://img.shields.io/badge/-VSCode-333333?style=flat&logo=visual-studio-code)
![Jupyter](https://img.shields.io/badge/-Jupyter-333333?style=flat&logo=jupyter)
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)

En esta etapa llevamos a cabo nuestro sistema de recomendación, con una relación item-item. Es decir, se toma un item y en base a que tan similar es un item del resto, se recomiendan similares, aplicando la similitud del coseno.

- Item-Item: Se toma un ítem, se encuentran items similares en base a los TAGs que tenemos de informacion y se devuelve 5 items similares.

Para el desarrollo del Sistema de Recomendación, usamos el dataset resultante de etapas anteriores y creamos otro que contiene:

- **id**: ID del juego.
- **app_name**: Nombre del juego.
- **tags**: Etiquetas del juego.
