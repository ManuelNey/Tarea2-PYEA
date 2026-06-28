import numpy as np
import pandas as pd
from scipy import stats

# Ej 1: Contruir intervalos de confianza para todas las variables de gasto.
def calcular_ic_media(columna, confianza=0.95):
    """
    Calcula el intervalo de confianza para la media poblacional
    a partir de una muestra (columna de un DataFrame).
    Retorna media, s, n, t_crítico, margen_error, LI, LS.
    """
    # Convertir a numérico y eliminar valores faltantes (por precaución)
    datos = pd.to_numeric(columna, errors="coerce").dropna()
    n = datos.count()
    media = datos.mean()
    s = datos.std(ddof=1)
    alpha = 1 - confianza
    # Valor crítico t 
    t_crit = stats.t.ppf(1 - alpha/2, df=n-1)
    margen = t_crit * s / np.sqrt(n)
    li = media - margen
    ls = media + margen
    return media, s, n, t_crit, margen, li, ls

# Leer datos 
df = pd.read_csv("../muestra_2000_datos.csv")

gasto_vars = [
    "GastoTotal", "GastoAlojamiento", "GastoAlimentacion",
    "GastoTransporteInternac", "GatoTransporteLocal",
    "GastoCultural", "GastoTours", "GastoCompras", "GastoResto"
]

# Iterar sobre variables de gasto y mostrar resultados
for var in gasto_vars:
    media, s, n, t_val, margen, li, ls = calcular_ic_media(df[var], confianza=0.95)
    print(f"{var}: media={media:.2f}, s={s:.2f}, n={n}, IC95% = ({li:.2f}, {ls:.2f})")
