---
citekey: yanMachineLearningEnhancedNDIR2025
title: "Machine Learning-Enhanced NDIR Methane Sensing Solution for Robust Outdoor Continuous Monitoring Applications"
authors: ["Yan, Yang", "Mijiddorj, Lkhanaajav", "Beringer, Tyler", "Mijiddorj, Bilguunzaya", "Ho, Alex", "Weng, Binbin"]
year: 2025
type: journalArticle
doi: "10.3390/s25247691"
url: "https://www.mdpi.com/1424-8220/25/24/7691"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# Machine Learning-Enhanced NDIR Methane Sensing Solution for Robust Outdoor Continuous Monitoring Applications

- **Citekey:** `yanMachineLearningEnhancedNDIR2025`  - **Año:** 2025  - **Tipo:** journalArticle
- **DOI:** [10.3390/s25247691](https://doi.org/10.3390/s25247691)

## Resumen

Desarrollo del sensor portátil AIMNet para monitoreo continuo de CH4 basado en el módulo NDIR comercial Senseair K96 (límite de detección ~0.5 ppm) integrado con BME280 para T/HR/P. El dispositivo (8.5 × 11.5 cm, 1.4 W) incluye microcontrolador STM32U083, módem LTE SIM7070G, bomba ZR370-02PM, filtro de entrada y alimentación solar. Se entrenaron >10 algoritmos de ML con 13,125 puntos de calibración en laboratorio (CH4 0–65 ppm, HR 0–80 %, T 25–55 °C). Los mejores modelos fueron Multilayer Perceptron (MLP) y Elastic Net, con R² > 0.8 en escenarios indoor y outdoor, y RMSE inter-sensor <1.5 ppm entre cuatro unidades idénticas. Validación de campo cerca de una planta de tratamiento de aguas residuales mostró buena correlación con LI-COR y detección de fugas hasta 18 ppm.

## Montaje experimental

### Hardware AIMNet

- **Sensor NDIR:** Senseair K96 (CH4 + BME280 integrado); detección ~0.5 ppm; abs. 3.3 µm.
- **Microcontrolador:** STM32U083RCT6 en PCB custom.
- **Comunicación:** módem celular SIM7070G + LTE; datos en la nube con procesamiento GIS.
- **Alimentación:** ~1.4 W; diseñado para operación solar autónoma.
- **Muestreo:** 1 Hz interno; intervalo de subida configurable (1 Hz a horas).
- **Almacenamiento local:** microSD para respaldo.
- **Dimensiones:** 8.5 × 11.5 cm; carcasa sellada.

### Calibración en laboratorio

- **Mezclador de gas:** dos MFC Alicat para CH4 y N2; línea con bubujeador para HR controlada.
- **Cámara climática:** horno para control de T.
- **Referencia:** LI-COR 7810 (precisión ~0.25 ppb para CH4 ambiente).
- **Matriz de calibración:**
  - HR: 0, 20, 40, 60, 80 %
  - T: 25, 30, 35, 40, 45, 50, 55 °C
  - CH4: 0–15 ppm en pasos de 3 ppm; 15–65 ppm en pasos de 10 ppm
- **Datos:** >15,000 puntos; tras filtrado: 13,125 puntos válidos.
- **Split:** 80 % train / 20 % validation; dos test sets adicionales (indoor con bomba, outdoor con gas portátil).

### Validación de campo

- **Balcony test:** 0.5, 1, 1.5 ft de distancia; 10, 50, 100 ppm CH4; condiciones soleado, noche, lluvia, tormenta.
- **Driving test:** sensor en techo de vehículo cerca de planta de tratamiento de aguas residuales; referencia LI-COR 7700 (open-path, ppb-level).

## Resultados principales

### Desempeño de modelos (R²)

| Modelo | Data-test1 (indoor) | Data-test2 (outdoor) |
|---|---:|---:|
| Multiple Linear Regression | <0.7 | <0.7 |
| Random Forest | <0.7 | <0.7 |
| Support Vector Regression | ~0.88 | ~0.72 |
| CatBoost | 0.93 | 0.74 |
| Elastic Net | 0.919 | **0.804** |
| **Multilayer Perceptron (MLP)** | **0.948** | **0.908** |

- MLP y Elastic Net fueron seleccionados para validación posterior.
- Cuatro unidades idénticas mostraron RMSE <1 ppm (MLP) y <1.5 ppm (Elastic Net), confirmando reproducibilidad.

### Validación en balcón (RMSE)

| Condición | Elastic Net | MLP |
|---|---:|---:|
| Día soleado | 1.24 ppm | 0.92 ppm |
| Noche | 1.44 ppm | 1.57 ppm |
| Día lluvioso | 2.73 ppm | 1.17 ppm |
| Tormenta | 3.91 ppm | 1.55 ppm |

- MLP es más robusto a cambios rápidos de HR y presión.
- Elastic Net muestra fluctuaciones espurias posiblemente por sensibilidad a presión atmosférica.

### Driving test

- **MLP:** RMSE = 2.98 ppm; capturó picos principales (~18 ppm) en esquina suroeste de la planta.
- **Elastic Net:** RMSE = 4.73 ppm; detectó picos dentro de la planta pero falló en carretera suroeste.
- Algunos picos menores (5–10 ppm) no fueron capturados por el AIMNet, posiblemente por tasa de bombeo baja (250 sccm) y dilución del pluma.

## Relevancia para la tesis

- **Solución NDIR comercial + ML lista para campo:** el AIMNet demuestra que un sensor NDIR de bajo costo (K96) con calibración ML puede operar outdoor y detectar fugas de CH4 de forma confiable.
- **MLP vs. Elastic Net:** MLP generaliza mejor en condiciones variables (lluvia, tormenta, driving), mientras que Elastic Net es más interpretable pero más sensible a presión/HR.
- **Reproducibilidad entre unidades:** cuatro sensores idénticos con RMSE <1.5 ppm respaldan estrategias de calibración transferible, como en Bertin et al. (2026).
- **Limitaciones para BSF:** el rango de calibración llega a 65 ppm; si la cámara de BSF produce concentraciones mayores, se necesitaría extender la matriz o usar NDIR de mayor rango.
- **Diseño de referencia:** la arquitectura STM32 + LTE + bomba + microSD es adaptable a una red de cámaras de BSF.

## Oportunidades de integración

- Comparar con **Dong et al. (2025)** (NDIR custom) y **Bertin et al. (2026)** (caja ESCAPE con MOX+NDIR).
- Relacionar con **Mitchell (2024)** y **Kiplimo (2024)** sobre calibración ML de MOX de CH4.
- Vincular con **Dubey (2024)** sobre validación outdoor de sensores NDIR y corrección ambiental.

## Preguntas abiertas / seguimiento

- [ ] ¿El rango de CH4 en BSF está dentro de 0–65 ppm o requiere sensor de mayor rango?
- [ ] ¿Se prefiere un modelo interpretable (Elastic Net) o uno de mayor precisión (MLP) para la aplicación?
- [ ] ¿Se necesita edge inference (TensorFlow Lite) o el procesamiento puede hacerse en la nube?

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado