"""
Funciones auxiliares comunes para la Parte 3.

Este módulo centraliza la lectura de la muestra y la validación de columnas
para evitar repetir el mismo código en los ejercicios 3.3, 3.4 y 3.5.
"""

from pathlib import Path

import pandas as pd


# Ubicación actual de la muestra dentro del proyecto:
# Tarea2-PYEA/muestra_2000_datos.csv
RUTA_MUESTRA = Path(__file__).resolve().parent.parent / "muestra_2000_datos.csv"

# Carpeta común para guardar salidas generadas por los scripts de Parte 3.
RUTA_SALIDA = Path(__file__).resolve().parent.parent / "salida_parte3"


def leer_muestra() -> pd.DataFrame:
    """Carga la muestra de 2000 datos generada en la Parte 1."""
    if not RUTA_MUESTRA.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de muestra en la ruta esperada: {RUTA_MUESTRA}"
        )

    return pd.read_csv(RUTA_MUESTRA)


def validar_columnas(df: pd.DataFrame, columnas_requeridas: list[str]) -> None:
    """Verifica que el archivo CSV tenga las columnas necesarias para el análisis."""
    faltantes = [columna for columna in columnas_requeridas if columna not in df.columns]

    if faltantes:
        raise ValueError(f"Faltan columnas requeridas en el CSV: {faltantes}")


def crear_carpeta_salida() -> Path:
    """Crea, si no existe, la carpeta donde se guardan las salidas de Parte 3."""
    RUTA_SALIDA.mkdir(exist_ok=True)
    return RUTA_SALIDA