<p align=center><img src=https://github.com/MiliTrres/SiniestrosViales-PI2-Henry/blob/main/Img/imgHenry.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº 2** </h1>

# <h1 align=center>**HOMICIDIOS EN SINIESTROS VIALES**</h1>

<p align=center><img src=https://github.com/MiliTrres/SiniestrosViales-PI2-Henry/blob/main/Img/Captura%20de%20pantalla%202024-02-27%20173918.png><p>

# *Introducción*

En áreas urbanas, los accidentes de tráfico, también llamados siniestros viales, son eventos preocupantes que involucran vehículos en la via pública y son causados por colisiones entre autos, motos, bicicletas o peatones, atropellos, choques contra objetos fijos o vuelcos de vehículos. Estos incidentes pueden causar daños materiales, lesiones graves e incluso la muerte.

En ciudades grandes como Buenos Aires, los accidentes viales son un problema importante debido al gran número de vehículos y la densidad de población. Estos incidentes afectan significativamente la seguridad de los residentes, visitantes, la infraestructura vial y los servicios de emergencia.

La tasa de mortalidad por accidentes viales es un indicador crítico de seguridad vial en muchas regiones. Se calcula como la cantidad de muertes por cada cierto número de habitantes o vehículos registrados. Reducir esta tasa es una prioridad y se logra mediante educación vial, respeto a las normas de tránsito y seguridad en las carreteras y calles.

En Argentina, hay alrededor de 4000 muertes al año debido a accidentes viales, siendo esta la principal causa de muertes violentas en el país. Por esta razón, el Observatorio de Movilidad y Seguridad Vial (OMSV) solicita nuestra participación en un proyecto de análisis de datos para ayudar a las autoridades locales a reducir la cantidad de muertes en accidentes viales.

# *Fuente de datos:*
La fuente de datos pricipal utilizada para este proyecto, fue obtenida desde la página *Buenos Aires Data*, donde se comparten datos abiertos para el público en general.

Puedes acceder a la página desde el siguiente enlace [Buenos Aires Data](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales).

Para acceder directamente al dataset utilizado en este proyecto, haz click en el siguiente enlace [Dataset Homicidios](https://github.com/MiliTrres/SiniestrosViales-PI2-Henry/blob/main/Data/homicidios.xlsx).

Para comprender mejor el dataset y sus variables, puedes acceder al siguiente enlace [Diccionario de Datos](https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/NOTAS_HOMICIDIOS_SINIESTRO_VIAL.pdf).

## *Fuentes de datos adicionales:*
Ademas de la fuente de datos principal, se accedieron a fuentes de datos complementarias para un analisis más preciso.

Se obtuvo información de las comunas a traves de la página *Buenos Aires Ciudad*. 
Puede acceder a la página desde el siguiente enlace [Buenos Aires Ciudad / Comuna](https://buenosaires.gob.ar/jefaturadegabinete/atencion-ciudadana-y-gestion-comunal/gestion-comunal/comunas).

Se obtuvo información de los barrios que conforman cada comuna de la ciudad, también desde la pagina *Buenos Aires Ciudad*. Puede acceder a la página desde el siguiente enlace [Buenos Aires Ciudad / Barrios](https://buenosaires.gob.ar/laciudad/barrios).

Y por último, se obtuvo información de la población de la ciudad por comuna y por sexo. Puede descargar el dataset desde el siguiente enlace [Buenos Aires Ciudad / Población](https://www.estadisticaciudad.gob.ar/eyc/?p=28146).

# *Tecnologias y herramientas utilizadas:*

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

# EDA *(Exploratory Data Analysis)*:

Durante esta etapa se visualizo el dataset en formato `xlsx`, y los datos que contenia cada página. Las páginas eran:

- ***HECHOS:*** Esta página contiene información de las siniestros viales, incluyendo ID del siniestro, fecha del mismo, hora, calle, altura, cruce, comuna, puntos geograficos, tipo de calle, número de victimas fallecidas, vehiculo manejado por las victimas, vehiculo manejado por el acusado, etc.
  
- ***VICTIMAS:*** Esta página contiene información de la victima, incluyendo el ID del siniestro, sexo de la victima, edad, fecha de fallecimiento, fecha del siniestro, vehiculo manejado por la misma.
  
- ***DICCIONARIO_HECHOS:*** Esta página contiene un glosario con las variables de la tabla *HECHOS*.
  
- ***DICCIONARIO_VICTIMAS:*** Esta página contiene un glosario con las variables de la tabla *VICTIMAS*.

Luego de visualizar el dataset, almacenamos cada página/tabla en un DataFrame distinto que posteriormente se guardo en formato `xlsx`.

Analizamos de manera minuciosa los DataFrames que contenian las tablas *HECHOS* y *VICTIMAS*, abordando valores nulos, valores de tipo *SD* (Sin Dato), outliers, registros duplicados, análisis estadistico en todas las columnas *(tanto variables númericas como categoricas)*, conteo de ocurrencias en variables categoricas. 

Se realizaron algunas tranformaciones en el tipo de datos, los nombres de las columnas, generamos columnas a partir de los datos brindados por el dataset, agrupando valores de ciertas variables, para un análisis más general, y generamos otra columna, obteniendo los datos mediante *Web Scraping*, desde la API de la página de *Buenos Aires Data* para obtener los barrios de la ciudad, en base a la latitud y longitud de los hechos. 

Por último, llevamos a cabo el desarrollo de visualizaciones, acompañado de conclusiones.

> Puede acceder al archivo desde el siguiente enlace: [EDA](https://github.com/MiliTrres/SiniestrosViales-PI2-Henry/blob/main/EDA.ipynb)

# Análisis a partir de las visualizaciones:

<p align=center><p>



  











