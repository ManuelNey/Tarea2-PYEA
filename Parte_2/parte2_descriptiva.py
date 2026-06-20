import pandas as pd
import matplotlib.pyplot as plt

#Ejercico 4
# Función reutilizable para construir una tabla de frecuencias por intervalos.
# Recibe el dataframe, el nombre de la variable y la cantidad de intervalos.
def tabla_frecuencias_intervalos(datos, variable, bins=10):

    # Seleccionamos la variable indicada y eliminamos valores faltantes.
    serie = datos[variable].dropna()

    # Agrupamos los valores numéricos en intervalos.
    intervalos = pd.cut(serie, bins=bins)

    # Frecuencia absoluta: cantidad de observaciones en cada intervalo.
    frecuencia_absoluta = intervalos.value_counts().sort_index()

    # Frecuencia relativa: proporción de observaciones en cada intervalo.
    frecuencia_relativa = frecuencia_absoluta / len(serie)

    # Frecuencia relativa acumulada: suma progresiva de las frecuencias relativas.
    frecuencia_relativa_acumulada = frecuencia_relativa.cumsum()

    # Marca de clase: punto medio de cada intervalo.
    marca_clase = [
        (intervalo.left + intervalo.right) / 2
        for intervalo in frecuencia_absoluta.index
    ]

    # Armamos la tabla
    tabla = pd.DataFrame({
        "Intervalo": frecuencia_absoluta.index.astype(str),
        "Marca de clase": marca_clase,
        "Frecuencia absoluta": frecuencia_absoluta.values,
        "Frecuencia relativa": frecuencia_relativa.round(4).values,
        "Frecuencia relativa acumulada": frecuencia_relativa_acumulada.round(4).values
    })

    return tabla

#Ejercico 5
def histograma_gasto(datos, variable, bins=10):
    # Seleccionamos la variable indicada y eliminamos valores faltantes.
    serie = datos[variable].dropna()

    # Creamos el histograma para observar la distribución de la variable.
    plt.figure(figsize=(10, 6))
    plt.hist(serie, bins=bins, edgecolor="black")

    # Agregamos título y etiquetas para que el gráfico sea autocontenido.
    plt.title(f"Histograma de {variable}")
    plt.xlabel(variable)
    plt.ylabel("Frecuencia absoluta")

    # Ajustamos el diseño para evitar superposición de elementos.
    plt.tight_layout()

    # Mostramos el gráfico en pantalla.
    plt.show()


#Ejercico 6
def boxplot_gasto(datos, variable):
    # Seleccionamos la variable indicada y eliminamos valores faltantes.
    serie = datos[variable].dropna()

    # Calculamos las medidas solicitadas por la consigna.
    q1 = serie.quantile(0.25)
    mediana = serie.median()
    q3 = serie.quantile(0.75)
    riq = q3 - q1

    # Calculamos los límites para detectar posibles datos atípicos.
    limite_inferior = q1 - 1.5 * riq
    limite_superior = q3 + 1.5 * riq

    # Identificamos los valores atípicos según la regla del rango intercuartílico.
    atipicos = serie[
        (serie < limite_inferior) | (serie > limite_superior)
    ]

    # Creamos el diagrama de cajas.
    plt.figure(figsize=(8, 6))
    plt.boxplot(serie, vert=False)
    plt.title(f"Diagrama de cajas de {variable}")
    plt.xlabel(variable)
    plt.tight_layout()
    plt.show()

    # Devolvemos las medidas para poder reportarlas en el informe.
    return {
        "Q1": q1,
        "Mediana": mediana,
        "Q3": q3,
        "RIQ": riq,
        "Limite inferior": limite_inferior,
        "Limite superior": limite_superior,
        "Cantidad de atipicos": len(atipicos)
    }

#Ejercicio 7
def diagrama_dispersion(datos, variable_x, variable_y):
    # Seleccionamos las variables indicadas y eliminamos filas con valores faltantes.
    datos_limpios = datos[[variable_x, variable_y]].dropna()

    # Creamos el diagrama de dispersión.
    plt.figure(figsize=(10, 6))
    plt.scatter(
        datos_limpios[variable_x],
        datos_limpios[variable_y],
        alpha=0.6
    )

    # Agregamos título y etiquetas para que el gráfico sea autocontenido.
    plt.title(f"Diagrama de dispersión: {variable_x} y {variable_y}")
    plt.xlabel(variable_x)
    plt.ylabel(variable_y)

    # Ajustamos el diseño.
    plt.tight_layout()

    # Mostramos el gráfico.
    plt.show()