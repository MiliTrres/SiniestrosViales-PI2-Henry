<p align=center><img src=https://github.com/MiliTrres/SiniestrosViales-PI2-Henry/blob/main/Img/imgHenry.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº 2** </h1>

# <h1 align=center>**`Siniestros viales con victimas fatales`**</h1>

<p align=center><img src=https://github.com/MiliTrres/SiniestrosViales-PI2-Henry/blob/main/Img/Captura%20de%20pantalla%202024-02-27%20173918.png><p>

## Introducción

En el entorno urbano, los siniestros viales, también conocidos como accidentes de tráfico o de tránsito, constituyen eventos preocupantes que involucran vehículos en las calles y carreteras, pudiendo ser causados por colisiones entre automóviles, motocicletas, bicicletas o peatones, atropellos, choques contra objetos estáticos o volcaduras de vehículos. Estos sucesos acarrean consecuencias que van desde daños materiales hasta lesiones graves o incluso fatales para los involucrados.

En ciudades tan grandes, como por ejemplo Buenos Aires, los incidentes viales representan una problema de gran relevancia debido al alto flujo de vehículos y la densidad poblacional. Estos sucesos repecuten de manera significativa en la seguridad, tanto de los habitantes de la ciudad, como los visitantes y turistas, la infraestructura vial, los servicios de emergencia, etc.

La tasa de mortalidad a causa de los siniestros viales, suele ser un indicador critico de seguridad vial en muchas regiones. Esta, se calcula como la cantidad de muertes por cada cierto número de habitantes o por el número de vehiculos registrados. En lugares donde esta tasa es tan alta, es de suma prioridad reducir estos números al minimo posible, y esto se hace a traves de educación vial, respetando y cumpliendo normas de transito; también depende de la seguridad de la infraestructura de carreteras, calles.

En Argentina, son cerca de 4000 mil las victimas fatales por año, a causa de siniestros viales, siendo esta, la principal causa de muertes violentas en nuestro pais. Por eso, el *Observatorio de Movilidad y Seguridad Vial (OMSV)*, centro de estudios que se encuentra bajo la órbita de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires, nos solicita la elaboración de un proyecto de anális de datos, con el fin de generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales. 

## Descripción del proyecto

El proyecto busca superar con exito dos desafios esenciales:

**Análisis de Sentimientos de Usuarios:** El primer desafío consiste en analizar y clasificar los comentarios de los usuarios. Para ello, se emplea la librería TextBlob, una herramienta de *Procesamiento del Lenguaje Natural* (NLP). TextBlob determina la polaridad del sentimiento en cada comentario y lo clasifica como negativo, neutral o positivo.

**Sistema de Recomendación de Juegos:** El segundo desafío, radica en construir un *Sistema de Recomendación de Videojuegos*. Este sistema proporciona recomendaciones de juegos a los usuarios basándose en sus preferencias y comportamientos anteriores.

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
