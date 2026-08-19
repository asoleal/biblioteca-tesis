---
citekey: mitchellCalibrationLowCostMethane2024
title: "Calibration of a Low-Cost Methane Sensor Using Machine Learning"
authors: ["Mitchell, Hazel Louise", "Cox, Simon J.", "Lewis, Hugh G."]
year: 2024
type: journalArticle
doi: "10.3390/s24041066"
url: "https://www.mdpi.com/1424-8220/24/4/1066"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# Calibration of a Low-Cost Methane Sensor Using Machine Learning

- **Citekey:** `mitchellCalibrationLowCostMethane2024`  - **Año:** 2024  - **Tipo:** journalArticle
- **DOI:** [10.3390/s24041066](https://doi.org/10.3390/s24041066)

## Resumen

Calibración de un sensor de metano de bajo costo (Figaro NGM2611-E13, basado en TGS2611-E00 MOX) para concentraciones bajas (0–200 ppm) usando regresión no lineal y machine learning. El sensor, pensado originalmente para fugas de gas natural (>300 ppm), se expuso en cámara de vacío a mezclas de 200 ppm CH4 en aire, variando temperatura (5–30 °C) y humedad relativa (40–80 %). Se probaron 22 formas de modelo; la mejor fue la Ecuación 16, con términos exponenciales para la señal del sensor y logarítmicos para temperatura, humedad e interacción temperatura×voltaje, logrando RMSE = 5.1 ppm y R² = 0.997 en los datos de calibración. Los experimentos de decaimiento de metano validaron el modelo y revelaron que modelos demasiado complejos (Ec. 22) sufren sobreajuste. El estudio demuestra que es posible calibrar sensores MOX de CH4 sin instrumentos de referencia caros, usando solo dos gases de calibración y un modelo interpretable.

## Montaje experimental

- **Sensor:** Figaro NGM2611-E13 (TGS2611-E00 MOX con filtro de carbón activado); costo < GBP 30; alimentación 5 V; tamaño 27 × 12.5 × 14.1 mm.
- **Principio:** semiconductor metálico (TiO2); al aumentar CH4 disminuye la resistencia del sensor (RS). La salida es un voltaje divisor con RL = 10 kΩ.
- **Variables ambientales:** temperatura (T, °C) y humedad relativa (H, %) medidas dentro de la cámara.
- **Cámara de vacío:** cuatro sensores NGM2611-E13 dentro de una cámara sellada; bomba de vacío para evacuar y rellenar con gas de calibración (200 ppm CH4 en aire o aire de calibración 20.9 % O2 en N2).
- **Datalogger:** Arduino Uno + ADC ADS1115 16-bit; lecturas cada 2–3 s.
- **Rango de calibración:** 0–200 ppm CH4, 5–30 °C, 40–85 % HR; >50 000 puntos de datos.
- **Validación:** dos experimentos de decaimiento de metano (4 días a 19–25 °C; 2 días a 8–30 °C) para detectar sobreajuste.
- **Referencia:** no se usó un analizador de referencia costoso; en su lugar se usaron gases de calibración certificados.

## Resultados principales

### Forma de modelo y selección

- La relación entre voltaje de salida (Vout) y concentración de CH4 es exponencial: M = C1·e^(C2·Vout).
- Temperatura y humedad afectan logarítmicamente la salida; se incluyeron términos de interacción (T×Vout, H×Vout, T×H).
- Se probaron 22 ecuaciones; la Ec. 16 ofreció el mejor compromiso rendimiento/complejidad:
  - **CH4 = C1 + C2·exp(C3·Vout − C4·ln(T+65) − C5·ln(H)) − C7·ln((T+65)·Vout)**
  - RMSE = 5.09 ppm, R² = 0.997, complejidad = 12.

### Comparación de modelos destacados (datos experimentales 0–200 ppm)

| Modelo | Ecuación | RMSE (ppm) | R² | Complejidad |
|---|---|---:|---:|---:|
| Solo voltaje | 1 | 1350 | 0.724 | 3 |
| Lineal con offset | 2 | 1270 | 0.758 | 4 |
| + T (log) | 5 | 55 | 0.684 | 6 |
| + T + H | 11 | 19.2 | 0.962 | 8 |
| + T + H + T×Vout | 16 | **5.09** | **0.997** | 13 |
| + T + H + H×Vout | 18 | 5.1 | 0.997 | 12 |
| + T + H + T×Vout + H×Vout | 20 | 5.09 | 0.997 | 16 |
| Variante con offsets 273.15 / H+50 | 21 | 4.5 | 0.998 | 23 |
| Variante sin offset humedad | 22 | 4.79 | 0.998 | 20 |

- Los modelos 21 y 22 tienen menor RMSE pero mayor complejidad; el modelo 22 mostró sobreajuste en los experimentos de decaimiento (picos en dientes de sierra asociados a cambios de temperatura).
- **Conclusión:** el modelo 16 es el recomendado por su balance entre precisión y robustez.

### Validación con decaimiento de metano

- Los modelos 16, 18 y 20 reproducen correctamente: concentración inicial <50 ppm, pico ~200 ppm y decaimiento suave.
- Los modelos con poca complejidad (5, 6, 11, 12) subestiman o sobreestiman el pico.
- El modelo 22 falla al compensar temperatura/humedad, evidenciando sobreajuste.

## Relevancia para la tesis

- **Sensor MOX de metano aplicable a BSF:** aunque el estudio se hizo en turberas, el rango 0–200 ppm cubre las concentraciones esperadas en cámaras de bioconversión con BSF si se usa CH4 como trazador de actividad anaerobia o emisiones fugitivas.
- **Calibración sin referencia costosa:** el enfoque de cámara de vacío + gases certificados (< GBP 500 total) es reproducible en un laboratorio de BSF.
- **Importancia de las interacciones T×Vout y H×Vout:** demuestra que compensar solo T y H por separado no es suficiente; los términos de interacción reducen el error de ~19 ppm a ~5 ppm.
- **Advertencia contra sobreajuste:** modelos más complejos no siempre generalizan mejor; se requiere validación con datos independientes (decaimiento).
- **Limitaciones para BSF:** el TGS2611 tiene sensibilidad cruzada con H2, etanol, iso-butano y CO; en digestión con BSF podría haber NH3, N2O, CO2 y VOCs que interfieren. Se recomienda complementar con sensores específicos o validar con cromatografía/referencia.

## Oportunidades de integración

- Comparar con **Riddick et al. (2020)**, que usa TGS2600 (MOX más antiguo) para concentraciones ambientales de CH4 (1.8–6 ppm) y encuentra gran variabilidad entre unidades.
- Relacionar con **Bertin et al. (2026)**, que usa TGS2611-E00/C00 + SGP40 + MH-441D (NDIR) en caja portátil con XGBoost, validando transferibilidad entre dispositivos.
- Vincular con **Dubey et al. (2024)** en cuanto a la corrección por HR y T para sensores de CO2; la misma lógica aplica a MOX de CH4.

## Preguntas abiertas / seguimiento

- [ ] ¿Cuál es el rango esperado de CH4 en la cámara de BSF? Si es <200 ppm, el NGM2611-E13 calibrado como Mitchell es viable; si es >1000 ppm, conviene un NDIR como MH-441D.
- [ ] ¿Se dispone de gases certificados de CH4 en aire para calibración en el laboratorio?
- [ ] ¿Qué interferentes esperamos (NH3, H2S, etanol, acetona, CO2) y cómo corregimos la selectividad del MOX?

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado