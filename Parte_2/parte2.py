
import pandas as pd

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

