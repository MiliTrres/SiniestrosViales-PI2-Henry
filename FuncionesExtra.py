import pandas as pd
import requests
from bs4 import BeautifulSoup


def porcentaje_valores_nulos(dataframe):
    '''
    Función que recibe como parametro un DataFrame
    y retorna el porcentaje de valores nulos por columna.

    '''
    total_filas = dataframe.shape[0]
    porcentaje_nulos = (dataframe.isnull().sum() / total_filas) * 100
    
    for columna, porcentaje in porcentaje_nulos.items():
        print(f'La columna {columna} tiene un {porcentaje: .2f} % de valores nulos')


def normalizacion_columnas(df):
    '''
    Función que recibe como parametro un DataFrame 
    y retorna las columnas normalizadas, con el formato de titulo.
    
    '''
    df.columns = df.columns.str.title()
    return df


def hojas_archivo_excel(archivo):
    '''
    Función que recibe como parametro un archivo de excel
    y retorna el nombre de las hojas que contiene el archivo.
    
    '''
    for sheet_name in archivo:
         print(sheet_name)


def tipo_de_datos(df):
    '''
    Función que recibe como parametro un DataFrame
    y retorna un DataFrame con el nombre de las columnas y el tipo de dato que contiene.
    
    '''
    diccionario = {"Nombre de la columna":[], "Tipo de dato":[]}

    for columna in df.columns:
        diccionario["Nombre de la columna"].append(columna)
        diccionario["Tipo de dato"].append(df[columna].apply(type).unique())
    df = pd.DataFrame(diccionario)
    return df


def registros_duplicados(df):
    '''
    Función que recibe como parametro un DataFrame
    y retorna un DataFrame con los registros duplicados.
    
    '''
    df = df[df.duplicated(keep=False)]
    return df

def porcentaje_valores_sd(df):
    '''
    Función que recibe como parametro un DataFrame
    y retorna el porcentaje de valores iguales a 'SD' por columna.

    '''
    porcentaje_sd = (df.eq('SD').sum()) / (len(df)) * 100

    for columna, porcentaje in porcentaje_sd.items():
        print(f'La columna {columna} tiene un {porcentaje: .2f} % de valores "SD"')


def categorizar_dia(nombre_dia):
    '''
    Función que recibe como parametro el nombre de un día
    y retorna si es un día de semana o fin de semana.
    
    '''
    if nombre_dia in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']:
        return 'Día de semana'
    else:
        return 'Fin de semana'
    

def verificar_comunas():
    '''
    Función que accede a la página web del gobierno de la ciudad de Buenos Aires
    y retorna una lista con las comunas de la ciudad, para verificar las comunas que tenemos en el dataset son correctas.

    '''

    url = 'http://buenosaires.gob.ar/jefaturadegabinete/atencion-ciudadana-y-gestion-comunal/gestion-comunal/comunas'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        comunas = []
        for item in soup.find_all('h4'):
            comuna = item.text.strip()
            comunas.append(comuna)
            comunas = [elem for elem in comunas if elem.startswith('Comuna')]
        print(comunas)
    else:
        print('No se pudo acceder al sitio web')


def consultar_barrio(latitud, longitud): 
    '''
    Función que recibe como parametro la latitud y longitud de un punto
    y retorna el barrio al que pertenece.
    
    '''
    url = "https://datosabiertos-usig-apis.buenosaires.gob.ar/datos_utiles"
    params = {
            "x": longitud,
            "y": latitud,
            "formato": "json"
        }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        if "barrio" in data:
            return data["barrio"]
        else:
            return "Desconocido"
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)
        return "Desconocido"