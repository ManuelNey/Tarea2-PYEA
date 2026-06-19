"""
Parte 1 - Acceso a datos y muestreo
"""

import pandas as pd

# Paso 1: Carga del dataset original descargado de catalogodatos.gub.uy
lectura = pd.read_csv('./Data/turismo_emisivo_original.csv')

print("Dimensiones del dataset original:", lectura.shape)
print("Columnas:", lectura.columns.tolist())
print("Destinos distintos:", lectura['Destino'].nunique())
print("Total de valores nulos:", lectura.isnull().sum().sum())

# Paso 2: Muestreo aleatorio simple de 2000 filas
# - replace=False: ninguna fila se repite (todas las observaciones son distintas)
# - random_state=77: se fija la semilla para que el muestreo sea siempre el mismo, es decir, 
#   que cada vez que se ejecute este script se obtenga la misma muestra de datos. 
#   cualquiera que corra este script obtiene exactamente la misma muestra
muestra_2000_datos = lectura.sample(n=2000, replace=False, random_state=77)

print("\nDimensiones de la muestra:", muestra_2000_datos.shape)
print("Destinos distintos en la muestra:", muestra_2000_datos['Destino'].nunique())
print("Valores nulos en la muestra:", muestra_2000_datos.isnull().sum().sum())

# Paso 3: Exportación de la muestra trabajan con ella en la Parte 2
archivo_muestra = 'muestra_2000_datos.csv'
muestra_2000_datos.to_csv(archivo_muestra, index=False)
print(f"\nMuestra exportada correctamente a {archivo_muestra}")