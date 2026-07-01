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

print("Ejercicio 1:")
# Iterar sobre variables de gasto y mostrar resultados
for var in gasto_vars:
    media, s, n, t_val, margen, li, ls = calcular_ic_media(df[var], confianza=0.95)
    print(f"{var}: media={media:.2f}, s={s:.2f}, n={n}, IC95% = ({li:.2f}, {ls:.2f})")

# Ej 2: Test de hipótesis para gasto promedio en alojamiento

def test_media_alojamiento(alpha=0.05):

    # Se reutiliza la función del ejercicio anterior, pero solo con s y n como parámetros
    media, s, n, _, _, _, _ = calcular_ic_media(
        df["GastoAlojamiento"]
    )

    mu0 = 350

    # Estadístico t del test:
    # mide qué tan alejada quedó la media observada respecto
    # al valor planteado en H0 (350 USD), expresado en errores estándar.
    # Fórmula:
    # t = [(x̄ - μ0) /s]*√n, aunque despejando también se puede hacer: (x̄ - μ0) / (s / √n)
    t_obs = (
                    media - mu0
            ) / (
                    s / np.sqrt(n)
            )


    # Cálculamos el p-valor (test unilateral izquierdo).
    # Obtiene la probabilidad de observar un valor tan extremo
    # como el obtenido, suponiendo que H0 sea verdadera.
    # Se calcula el área acumulada a la izquierda de t_obs:
    # p = P(T ≤ t_obs)
    p_valor = stats.t.cdf(
        t_obs,
        df=n - 1
    )

    # Decisión final
    if p_valor < alpha:
        decision = "Rechazar H0"
        conclusion = (
            "Existe evidencia estadística suficiente para afirmar "
            "que el gasto promedio en alojamiento es menor a 350 USD."
        )
    else:
        decision = "No rechazar H0"
        conclusion = (
            "No existe evidencia estadística suficiente para afirmar "
            "que el gasto promedio en alojamiento es menor a 350 USD."
        )

    return {
        "estadistico_t": round(t_obs, 4),
        "p_valor": round(p_valor, 4),
        "decision": decision,
        "conclusion": conclusion
    }

print("Ejercicio 2:")

#Para probarlo se ejecuta los siguiente:
resultado = test_media_alojamiento()

for k, v in resultado.items():
    print(f"{k}: {v}")