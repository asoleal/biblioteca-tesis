---
citekey: yasudaComparisonCharacteristicsSmall2012
title: "Comparison of the Characteristics of Small Commercial NDIR CO2 Sensor Models and Development of a Portable CO2 Measurement Device"
authors: ["Yasuda, Tomomi", "Yonemura, Seiichiro", "Tani, Akira"]
year: 2012
type: journalArticle
doi: "10.3390/s120303641"
url: "https://www.mdpi.com/1424-8220/12/3/3641"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# Comparison of the Characteristics of Small Commercial NDIR CO2 Sensor Models and Development of a Portable CO2 Measurement Device

- **Citekey:** `yasudaComparisonCharacteristicsSmall2012`  - **Año:** 2012  - **Tipo:** journalArticle
- **DOI:** [10.3390/s120303641](https://doi.org/10.3390/s120303641)


## Resumen

Este estudio comparó cinco modelos comerciales de sensores NDIR de CO₂ de difusión para observaciones multipunto y desarrolló un dispositivo portátil de medición. Se caracterizaron las tendencias de salida en función de la temperatura ambiente, el tiempo de uso y el offset, utilizando cuatro gases patrón (0, 407, 1.110 y 1.810 ppm de CO₂ en N₂). Los modelos K30 (SenseAir) y AN100 mostraron relaciones lineales con la temperatura y el tiempo de uso, lo que permitió aplicar coeficientes de corrección comunes a varios sensores del mismo modelo. Tras la corrección, el error RMS relativo del K30 disminuyó del 24 % al 4 %. El modelo K30 fue seleccionado para construir un dispositivo portátil (100 × 100 × 150 mm, 900 g, alimentado por 6 baterías AA, 5 h de autonomía) que registra CO₂, T, HR, presión atmosférica, GPS y hora en tarjeta SD. En una validación en un aula frente al analizador de referencia LI-6262 (Licor), el dispositivo portátil mostró una diferencia de error RMS relativo del 3.5 % cuando se aplicaron correcciones por temperatura, presión de vapor de agua y presión atmosférica.

## Modelos de sensores comparados

| Modelo | Fabricante | Dimensiones (mm) | Peso (g) | Rango (ppm) | Exactitud catalogada | Tiempo respuesta | Voltaje |
|--------|-----------|------------------|---------:|------------:|---------------------:|-----------------:|--------:|
| GMM222C | Vaisala | Cilindro Ø18 × 140 | 220 | 0–2,000 | 30 ppm + 2% lectura | 30 s (63%) | 11–20 VDC |
| **K30** | **SenseAir** | 51 × 57 × 14 | 17 | 0–5,000 | 30 ppm + 5% lectura | 20 s (63%) | 4.5–14 VDC |
| S100 | ELT | 33 × 33 × 13 | 10 | 0–5,000 | 30 ppm + 5% lectura | 60 s (90%) | 5.0–5.5 VDC |
| AN100 | KCD | 82 × 45 × 18 | 29 | 0–5,000 | 200 ppm + 3% lectura | 30 s (63%) | 8–14 VDC |
| T6615 | GE Sensing | 57 × 35 × 15 | 17 | 0–5,000 | 75 ppm o 10% lectura | <120 s (90%) | 5 VDC |

- **Sensor de referencia:** Vaisala GMM222C (0–2,000 ppm).
- **Tres individuos de cada modelo** fueron evaluados.

## Montaje experimental de caracterización

| Parámetro | Valor |
|-----------|-------|
| **Cámara de sensores** | Caja de polietileno 230 × 170 × 40 mm (1.5 L) |
| **Temperaturas evaluadas** | 10, 25 y 40 °C |
| **Tiempos de uso evaluados** | 1, 37, 106 y 306 días |
| **Gases patrón** | 0, 407, 1.110, 1.810 ppm CO₂ en N₂ |
| **Flujo de gas** | 1 L/min |
| **Tiempo de estabilización** | 5 min por gas |
| **Registro** | Cada 1 s durante 3 min |
| **Incubadora** | Yamato DKM600 |
| **Data logger** | Campbell Scientific CR1000 |

## Método de calibración

La calibración consta de dos etapas:

1. **Corrección de offset (zero):**
   ```
   CO2_offset = CO2_obs − offset_obs
   ```
   - El offset se mide con gas N₂ puro.
   - El offset no dependió de la temperatura (10–40 °C) ni del tiempo de uso (1–306 días).

2. **Corrección de span por T, tiempo de uso y presión:**
   ```
   CO2_correct = K_std · C_T · C_day · C_p · CO2_offset / (1 − X_W)
   ```
   donde:
   - `C_T = 1 + α_T(T − 25)`
   - `C_day = 1 + α_day(day − 1)`
   - `C_p = 1 + α_P(P − 1013)`
   - `X_W` = fracción molar de vapor de agua
   - `K_std` = factor de span promedio de tres sensores a condiciones estándar

Para el **K30**, los coeficientes determinados fueron:
- `α_T = 0.00141`
- `α_day = 0.000478`

## Resultados de calibración (error RMS relativo, RRMS)

| Sensor | Sin corrección | Offset + T | Offset + T + día | Offset + T + día + presión |
|--------|---------------:|-----------:|-----------------:|---------------------------:|
| GMM222C | — | ~bajo | ~bajo | ~bajo |
| **K30 (modelo)** | 24% | 7.3% | 4.5% | **4.4%** |
| **K30 (individual)** | — | 7.7% | 5.0% | **4.8%** |
| AN100 (modelo) | — | 9.6% | 11.1% | 11.5% |
| S100 (modelo) | — | 13.0% | 15.3% | 14.5% |
| T6615 (modelo) | — | 20.5% | 18.3% | 17.3% |

- El **K30** fue el único modelo en el que los coeficientes comunes del modelo funcionaron casi igual de bien que la calibración individual.
- El AN100 también mostró linealidad, pero con mayor error.
- S100 y T6615 no mostraron relaciones lineales claras, por lo que el método de corrección no fue adecuado.

## Tiempos de respuesta (90%)

| Modelo | Tiempo de respuesta 90% |
|--------|------------------------:|
| GMM222C | ~37 s |
| K30 | ~88 s |
| S100 | ~142 s |
| AN100 | ~152 s |
| T6615 | ~190 s |

- Los sensores pequeños fueron más lentos que el sensor de referencia, probablemente por difusión unilateral en la célula de IR y resistencia del filtro anti-polvo.

## Dispositivo portátil desarrollado

| Especificación | Valor |
|----------------|-------:|
| **Dimensiones** | 100 × 100 × 150 mm |
| **Peso** | 900 g |
| **Sensor CO₂** | K30 (SenseAir) |
| **T/HR** | Sensirion SHT-71 |
| **Presión atmosférica** | SCP1000-D01 (Akitsuki) |
| **GPS** | Garmin GPS 18× |
| **Microcontrolador** | ATmega2560 |
| **Almacenamiento** | Tarjeta SD 2 GB |
| **Alimentación** | 6 baterías AA Li-ion |
| **Autonomía** | 5 h |
| **Costo estimado** | ~USD 770 |
| **Intervalo de muestreo** | 30 s |

## Validación frente a LI-6262

- **Lugar:** Aula de la Shizuoka Prefectural Science and Technology High School
- **Fecha:** 7 de febrero de 2011
- **Referencia:** LI-6262 (Licor), calibrado con N₂ y gas patrón 407 ppm
- **Resultado:** RRMS difference del dispositivo portátil vs. LI-6262 = **3.5%** (con correcciones aplicadas)

## Relevancia para la tesis

- Justifica el uso del **SenseAir K30** como sensor NDIR de CO₂ de bajo costo para aplicaciones de monitoreo ambiental.
- Proporciona un **método de calibración simplificado** por modelo de sensor, evitando calibrar cada unidad individualmente.
- Muestra la importancia de corregir por **temperatura, presión atmosférica y presión de vapor de agua**.
- Demuestra que sensores NDIR pequeños pueden alcanzar precisión aceptable (RRMS < 5%) frente a analizadores de referencia tipo LI-6262.
- El diseño del dispositivo portátil es una referencia útil para pensar en un sistema de monitoreo móvil de GEI en BSF.

## Limitaciones

- Los coeficientes de calibración fueron determinados para un año de uso; pueden no ser válidos para periodos más largos.
- El método de corrección lineal no funcionó bien para todos los modelos (S100, T6615).
- Los tiempos de respuesta de los sensores pequeños son lentos (~1.5–3 min), lo que debe considerarse para mediciones dinámicas.

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado
- [ ] Citado en borrador de tesis