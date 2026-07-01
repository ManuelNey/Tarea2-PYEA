"""
Parte 3.5 - Regresión lineal simple.

Se ajusta un modelo de regresión lineal simple entre la cantidad de personas
(Gente) y el gasto total del viaje (GastoTotal).
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from utils import RUTA_MUESTRA, leer_muestra, validar_columnas

COLUMNAS_REQUERIDAS = ["Gente", "GastoTotal"]


def main() -> None:
    # Paso 1: Carga de la muestra generada en la Parte 1.
    muestra = leer_muestra()
    validar_columnas(muestra, COLUMNAS_REQUERIDAS)

    # Paso 2: Limpieza de datos.
    datos = muestra[COLUMNAS_REQUERIDAS].dropna().astype(float)
    x = datos["Gente"]
    y = datos["GastoTotal"]

    # Paso 3: Ajuste del modelo de regresión lineal simple.
    regresion = stats.linregress(x, y)
    beta1 = regresion.slope
    beta0 = regresion.intercept
    r2 = regresion.rvalue ** 2

    salida = Path("salida_parte3")
    salida.mkdir(exist_ok=True)
    ruta_figura = salida / "regresion_gente_gastototal.png"

    # Paso 4: Generación de la recta estimada para graficar el modelo.
    x_linea = np.linspace(x.min(), x.max(), 100)
    y_linea = beta0 + beta1 * x_linea

    # Paso 5: Construcción y exportación del gráfico.
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=0.45)
    plt.plot(x_linea, y_linea)
    plt.xlabel("Gente")
    plt.ylabel("GastoTotal (USD)")
    plt.title("Regresión lineal simple: Gente vs. GastoTotal")
    plt.tight_layout()
    plt.savefig(ruta_figura, dpi=160)
    plt.close()

    # Paso 6: Presentación de resultados.
    print("PARTE 3.5 - Regresión lineal simple: Gente vs GastoTotal")
    print(f"Archivo usado: {RUTA_MUESTRA}")
    print()
    print(f"Tamaño muestral = {len(datos)}")
    print(f"Intercepto beta_0 = {beta0:.4f}")
    print(f"Pendiente beta_1 = {beta1:.4f}")
    print(f"Recta: GastoTotal = {beta0:.4f} + {beta1:.4f} * Gente")
    print(f"Coeficiente de determinación R^2 = {r2:.4f}")
    print(f"Coeficiente de correlación r = {regresion.rvalue:.4f}")
    print(f"p-valor de la pendiente = {regresion.pvalue:.6e}")
    print(f"Figura guardada en: {ruta_figura}")


if __name__ == "__main__":
    main()
