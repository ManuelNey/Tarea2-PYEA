
import pandas as pd
import matplotlib.pyplot as plt
from parte2_descriptiva import (
    tabla_frecuencias_intervalos,
    histograma_gasto,
    boxplot_gasto,
    diagrama_dispersion
)
# Paso 1: Carga del dataset de la muestra exportada en la Parte 1
lectura = pd.read_csv('./muestra_2000_datos.csv')

absolutas = lectura["Destino"].value_counts()
relativas = lectura["Destino"].value_counts(normalize=True)

tabla_destino = pd.DataFrame({
    'Frecuencia absoluta': absolutas,
    'Frecuencia relativa': relativas.round(4)
})

print(tabla_destino)

# Ejercicio 3: Gráfico de barras para la variable Destino

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6)) # Establecemos el tamaño de la figura para que sea más legible
plt.bar(absolutas.index, absolutas.values) # Creamos un gráfico de barras usando los índices (destinos) y los valores (frecuencias absolutas)
plt.xlabel('Destino') # Etiqueta del eje x
plt.ylabel('Frecuencia absoluta') # Etiqueta del eje y
plt.title('Frecuencia absoluta de Destinos') # Título del gráfico
plt.xticks(rotation=50) # Rotamos las etiquetas del eje x para mejor visualización
plt.tight_layout() # Ajustamos el diseño para que no se solapen los elementos
plt.show() # Mostramos el gráfico de barras

# Ejercicio 3: Gráfico de circula para la variable Destino

plt.figure(figsize=(8, 8)) # Establecemos el tamaño de la figura para que sea más legible
plt.pie(absolutas.values, labels=absolutas.index, autopct='%1.1f%%', startangle=140) # Creamos un gráfico circular usando los valores (frecuencias absolutas) y las etiquetas (destinos)
plt.title('Distribución de Destinos') # Título del gráfico
plt.axis('equal') # Aseguramos que el gráfico circular sea un círculo perfecto
plt.show() # Mostramos el gráfico circular



# Ejercicio 4: Tabla de frecuencias por intervalos para una variable de gasto

# Se selecciona GastoAlojamiento porque representa un componente relevante
# del gasto turístico y se reutiliza en los ejercicios 5 y 6.
variable_gasto = "GastoAlojamiento"

tabla_alojamiento = tabla_frecuencias_intervalos(
    lectura,
    variable_gasto,
    bins=10
)

print(tabla_alojamiento)


# Ejercicio 5: Histograma para la variable de gasto seleccionada

histograma_gasto(
    lectura,
    variable_gasto,
    bins=10
)

# Ejercicio 6: Diagrama de cajas para la variable de gasto seleccionada

resumen_boxplot = boxplot_gasto(
    lectura,
    variable_gasto
)

print(resumen_boxplot)

# Ejercicio 7: Diagrama de dispersión entre Gente y GastoTotal

diagrama_dispersion(
    lectura,
    "Gente",
    "GastoTotal"
)