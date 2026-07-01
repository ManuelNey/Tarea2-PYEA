"""
Parte 3.3 - Test de comparación de dos medias.

Se compara el gasto en alimentación con el gasto en compras genéricas para
determinar si, en promedio, los uruguayos gastan más en alimentación cuando
viajan al exterior.
"""
import numpy as np
import pandas as pd
from scipy import stats

from utils import RUTA_MUESTRA, leer_muestra, validar_columnas

ALPHA = 0.05
COLUMNAS_REQUERIDAS = ["GastoAlimentacion", "GastoCompras"]


def main() -> None:
    # Paso 1: Carga de la muestra generada en la Parte 1.
    muestra = leer_muestra()
    validar_columnas(muestra, COLUMNAS_REQUERIDAS)

    # Paso 2: Limpieza de datos.
    # Se eliminan filas con valores faltantes y se convierten las columnas a tipo numérico
    datos = muestra[COLUMNAS_REQUERIDAS].dropna().astype(float)
    alimentacion = datos["GastoAlimentacion"]
    compras = datos["GastoCompras"]

    # Paso 3: Construcción de la variable diferencia.
    # Como ambas variables corresponden a los mismos viajes, corresponde un test t pareado.
    diferencias = alimentacion - compras
    n = diferencias.count()
    media_dif = diferencias.mean()
    desvio_dif = diferencias.std(ddof=1)

    # Paso 4: Cálculo del estadístico de prueba y del p-valor.
    # H0: mu_D = 0
    # H1: mu_D > 0, donde D = GastoAlimentacion - GastoCompras.
    t_stat = media_dif / (desvio_dif / np.sqrt(n))
    p_valor = stats.t.sf(t_stat, df=n - 1)  # p-valor unilateral hacia la derecha

    # Paso 5: Presentación de resultados.
    print("PARTE 3.3 - Test t pareado: GastoAlimentacion vs GastoCompras")
    print(f"Archivo usado: {RUTA_MUESTRA}")
    print(f"Nivel de significación alpha = {ALPHA}")
    print()
    print("Hipótesis:")
    print("H0: mu_D = 0")
    print("H1: mu_D > 0")
    print("D = GastoAlimentacion - GastoCompras")
    print()
    print(f"Tamaño muestral = {n}")
    print(f"Media GastoAlimentacion = {alimentacion.mean():.4f}")
    print(f"Media GastoCompras = {compras.mean():.4f}")
    print(f"Media de diferencias = {media_dif:.4f}")
    print(f"Desvío estándar de diferencias = {desvio_dif:.4f}")
    print(f"Estadístico t = {t_stat:.4f}")
    print(f"p-valor unilateral = {p_valor:.6f}")
    print("Decisión:", "rechazar H0" if p_valor < ALPHA else "no rechazar H0")


if __name__ == "__main__":
    main()
