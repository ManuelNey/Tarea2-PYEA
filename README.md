# Turismo Emisivo — Probabilidad y Estadística Aplicada

## Estructura del proyecto

```
PYA/
├── Data/
│   ├── turismo_emisivo_original.csv   # dataset completo descargado (32.109 filas)
│   └── muestra_2000_datos.csv          # muestra de 2000 filas (USAR ESTA de acá en más)
├── prueba_Parte_1/
│   └── parte1.py                       # script de muestreo (Parte 1)
├── Parte_2/
│   └── parte2.py                       # script de análisis descriptivo (Parte 2)
└── README.md
```

## Importante:

A partir de la Parte 2, **todos los scripts deben leer `muestra_2000_datos.csv`**,
no el dataset completo. Así garantizamos todos trabajamos con los mismos datos

```python
import pandas as pd
muestra = pd.read_csv('Data/muestra_2000_datos.csv')
```

## Cómo correr el código

1. Clonar el repo.
2. Instalar dependencias:
   ```
   pip install pandas numpy matplotlib scipy
   ```
3. Correr los scripts desde la carpeta correspondiente.

## Estado del trabajo

- [x] Parte 1 — Acceso a datos y muestreo
- [ ] Parte 2 — Análisis descriptivo
- [ ] Parte 3 — Inferencia estadística
- [ ] Informe final (LaTeX)

## Datos

Fuente: [Ministerio de Turismo — Turismo Emisivo](https://catalogodatos.gub.uy/dataset/ministerio-de-turismo-turismo-emisivo)
Descargado el: 19/06/2026
