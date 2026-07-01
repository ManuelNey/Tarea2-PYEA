"""
Parte 3.4 - Test Chi-Cuadrado de independencia.

Se analiza si existe independencia entre la duración de la estadía y el lugar de
salida. Para aplicar el test, la variable Estadia se agrupa en intervalos.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

from utils import RUTA_MUESTRA, leer_muestra, validar_columnas

ALPHA = 0.05
COLUMNAS_REQUERIDAS = ["Estadia", "Lugar Salida"]


def main() -> None:
    # Paso 1: Carga de la muestra generada en la Parte 1.
    muestra = leer_muestra()
    validar_columnas(muestra, COLUMNAS_REQUERIDAS)

    # Paso 2: Limpieza de datos.
    datos = muestra[COLUMNAS_REQUERIDAS].dropna().copy()
    datos["Estadia"] = datos["Estadia"].astype(float)

    # Paso 3: Agrupación de la variable Estadia.
    # Estadía se agrupa para tratarla como variable categórica en el test Chi-Cuadrado.
    bins_estadia = [0, 3, 7, 14, np.inf]
    labels_estadia = ["1 a 3 días", "4 a 7 días", "8 a 14 días", "Más de 14 días"]
    datos["EstadiaAgrupada"] = pd.cut(
        datos["Estadia"],
        bins=bins_estadia,
        labels=labels_estadia,
        include_lowest=True,
    )

    # Paso 4: Agrupación de Lugar Salida.
    # Para evitar frecuencias esperadas demasiado bajas, se conservan los seis lugares
    # de salida más frecuentes y el resto se agrupa como "Otros".
    top6_salidas = datos["Lugar Salida"].value_counts().head(6).index
    datos["LugarSalidaAgrupado"] = np.where(
        datos["Lugar Salida"].isin(top6_salidas),
        datos["Lugar Salida"],
        "Otros",
    )

    # Paso 5: Construcción de la tabla de contingencia.
    datos = datos.dropna(subset=["EstadiaAgrupada", "LugarSalidaAgrupado"])
    tabla = pd.crosstab(datos["EstadiaAgrupada"], datos["LugarSalidaAgrupado"])

    # Paso 6: Aplicación del test Chi-Cuadrado de independencia.
    # H0: Estadia y Lugar Salida son independientes.
    # H1: Estadia y Lugar Salida no son independientes.
    chi2, p_valor, grados_libertad, esperadas = stats.chi2_contingency(tabla)

    # Paso 7: Exportación de la tabla de contingencia.
    salida = Path("salida_parte3")
    salida.mkdir(exist_ok=True)
    ruta_tabla = salida / "tabla_contingencia_estadia_lugarsalida.csv"
    tabla.to_csv(ruta_tabla, encoding="utf-8-sig")

    # Paso 8: Presentación de resultados.
    print("PARTE 3.4 - Test Chi-Cuadrado: Estadia vs Lugar Salida")
    print(f"Archivo usado: {RUTA_MUESTRA}")
    print(f"Nivel de significación alpha = {ALPHA}")
    print()
    print("Hipótesis:")
    print("H0: Estadia y Lugar Salida son independientes")
    print("H1: Estadia y Lugar Salida no son independientes")
    print()
    print("Tabla de contingencia:")
    print(tabla)
    print()
    print(f"Estadístico Chi-Cuadrado = {chi2:.4f}")
    print(f"Grados de libertad = {grados_libertad}")
    print(f"p-valor = {p_valor:.6e}")
    print(f"Frecuencia esperada mínima = {esperadas.min():.4f}")
    print("Decisión:", "rechazar H0" if p_valor < ALPHA else "no rechazar H0")
    print(f"Tabla guardada en: {ruta_tabla}")


if __name__ == "__main__":
    main()
