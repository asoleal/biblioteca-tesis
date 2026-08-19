---
citekey: kiplimoAddressingLowCostMethane2024
title: "Addressing Low-Cost Methane Sensor Calibration Shortcomings with Machine Learning"
authors: ["Kiplimo, Elijah", "Riddick, Stuart N.", "Mbua, Mercy", "Upreti, Aashish", "Anand, Abhinav", "Zimmerle, Daniel J."]
year: 2024
type: journalArticle
doi: "10.3390/atmos15111313"
url: "https://www.mdpi.com/2073-4433/15/11/1313"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# Addressing Low-Cost Methane Sensor Calibration Shortcomings with Machine Learning

- **Citekey:** `kiplimoAddressingLowCostMethane2024`
- **Año:** 2024
- **Tipo:** journalArticle
- **DOI:** [10.3390/atmos15111313](https://doi.org/10.3390/atmos15111313)

## Resumen

Este trabajo investiga el uso de *Random Forest* (RF) para calibrar sensores metalóxido de bajo costo (TGS2600 y TGS2611) frente a un analizador de referencia Aeris MIRA Ultra durante liberaciones controladas de metano en el centro METEC de Colorado State University. La calibración tradicional basada en el método de Eugster y Kling (2012) fracasó para estos sensores específicos debido a una relación señal-ruido muy baja (R² ≈ 0,0016). En cambio, el modelo RF logró capturar relaciones no lineales entre Rs, temperatura, humedad relativa y la concentración de referencia de CH₄. Los valores medios calculados fueron 2,42 ppm (TGS2600) y 2,40 ppm (TGS2611), frente a 2,40 ppm del analizador. Los coeficientes de solapamiento de histogramas fueron 0,95 y 0,94, respectivamente. Aunque los resultados muestran buen acuerdo, los R² de prueba (0,34 y 0,38) indican que aún existe margen de mejora antes de que estos sensores igualen la precisión de analizadores de trazas de gama alta.

## Objetivo

- Evaluar si un modelo de aprendizaje automático (RF) puede superar los problemas de calibración tradicional en sensores TGS2600/TGS2611 con baja relación señal-ruido.
- Comparar las concentraciones de CH₄ derivadas por ML con las medidas por un analizador de referencia de precisión.

## Instrumentación

| Componente | Descripción |
|------------|-------------|
| Sensores de bajo costo | Figaro TGS2600 y TGS2611 (metalóxido de SnO₂) |
| Adquisición de datos | Raspberry Pi 4 + conversor ADS1115 de 16 bits; lectura cada 1 s |
| T/RH | Sensor DHT22 |
| Analizador de referencia | Aeris MIRA Ultra Mobile LDS (espectroscopía de absorción láser medio-IR), rango 10 ppb–10 000 ppm, etano simultáneo; 5 Hz promediado a 1 s |

## Diseño experimental

- **Ubicación:** METEC, Colorado State University, Fort Collins, CO, EE. UU. (~40,60° N, 105,14° W).
- **Período:** 1 de marzo de 2024 a 2 de mayo de 2024.
- **Liberaciones controladas:** 0,005 a 8 kg CH₄ h⁻¹; emisiones simples y múltiples desde cabezales de pozo, separadores y tanques (pads 4 y 5).
- **Condiciones ambientales:** temperatura exterior entre −22 °C y +30 °C; durante las mediciones, T de 27 °C a −5 °C y HR de 18 % a 91 %.
- **Datos:** 1,6 millones de puntos iniciales; 424 000 descartados por pérdidas de energía, caídas del mástil y periodos de precalentamiento. Conjunto final de modelado: 518 168 puntos.

## Métodos de calibración

### Método tradicional (Eugster & Kling, 2012)

- Corrige la razón Rs/R0 por temperatura y humedad relativa mediante una ecuación empírica.
- En este estudio no funcionó: el resistor del puente de Wheatstone fue 20 veces mayor que el recomendado, lo que generó una señal muy ruidosa.
- R² entre (Rs/R0)corregido y CH₄ de referencia: 0,0016 para ambos sensores; correlación prácticamente nula en el resto de la campaña.

### Machine Learning: Random Forest Regressor

- **Entorno:** Google Colab (GPU).
- **Librerías:** Pandas, scikit-learn, Joblib, Matplotlib.
- **Entradas (3 features):** resistencia del sensor (Rs), temperatura (°C), humedad relativa (%).
- **Target:** concentración de CH₄ del analizador Aeris MIRA.
- **División:** 70 % entrenamiento / 30 % prueba, aleatoria.
- **Validación cruzada:** k-fold estratificado con 5 folds.
- **Hiperparámetro:** `max_features = 3` (se usaron todas las features por ser pocas).

## Resultados principales

### Comparación de promedios y máximos

| Sensor | CH₄ promedio calculado | CH₄ máximo calculado |
|--------|------------------------|----------------------|
| TGS2600 + RF | 2,42 ppm | 117,5 ppm |
| TGS2611 + RF | 2,40 ppm | 106,3 ppm |
| Aeris MIRA (referencia) | 2,40 ppm | 147,6 ppm |

### Métricas de desempeño del modelo RF

| Métrica | TGS2600 | TGS2611 |
|---------|---------|---------|
| R² test (regresión lineal vs referencia) | 0,34 | 0,38 |
| MSE | 1,40 | 1,32 |
| RMSE | 1,18 ppm | 1,14 ppm |
| MAPE | 7,21 % | 8,11 % |
| Explained variance | 33 % | 38 % |
| R² entrenamiento | 0,81 | 0,79 |
| R² test (validación cruzada) | 0,69 | 0,71 |

- El descenso de R² entre entrenamiento y test indica cierto sobreajuste; se sugiere ajuste de hiperparámetros o mayor tamaño del conjunto de entrenamiento.

### Importancia de variables

| Variable | TGS2600 | TGS2611 |
|----------|---------|---------|
| Humedad relativa | 35,8 % | 39,5 % |
| Resistencia (Rs) | 33,5 % | 32,1 % |
| Temperatura | 30,7 % | 28,4 % |

- La humedad relativa fue la variable más influyente en ambos sensores, lo que refuerza su papel crítico en la calibración de sensores metalóxido.

### Comparación de distribuciones

- Coeficiente de solapamiento (overlap coefficient) entre histogramas de concentraciones medidas y calculadas:
  - TGS2600: **0,95**
  - TGS2611: **0,94**

### Comparación con regresión lineal

- R² de la regresión lineal tradicional: 0,004 (TGS2600) y 0,005 (TGS2611).
- El RF mejoró sustancialmente el ajuste gracias a su capacidad de modelar relaciones no lineales.

## Relevancia para la tesis

- Muestra un caso real en el que la calibración tradicional falla por baja relación señal-ruido y cómo el RF puede recuperar información útil.
- Proporciona métricas de desempeño (R², RMSE, MAPE, importancia de variables) para TGS2600/TGS2611 en un rango amplio de concentraciones (fondo a ~150 ppm).
- Destaca la necesidad de incluir humedad y temperatura como covariables en modelos de calibración de sensores metalóxido.
- Sirve de contraste con estudios que usan relación señal-ruido más alta o calibraciones lineales más exitosas.

## Limitaciones

- Relación señal-ruido muy baja por el resistor inadecuado, lo que dificultó la calibración tradicional.
- Sobreajuste del RF (R² entrenamiento >> R² test); se recomienda ajuste de hiperparámetros y/o más datos.
- Los R² de prueba (0,34–0,38) indican que, aunque mejora respecto a métodos lineales, el desempeño aún no es comparable con analizadores de referencia de alta gama.

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado