---
citekey: dubeyLowCostCO2NDIR2024
title: "Low-Cost CO2 NDIR Sensors: Performance Evaluation and Calibration Using Machine Learning Techniques"
authors: ["Dubey, Ravish", "Telles, Arina", "Nikkel, James", "Cao, Chang", "Gewirtzman, Jonathan", "Raymond, Peter A.", "Lee, Xuhui"]
year: 2024
type: journalArticle
doi: "10.3390/s24175675"
url: "https://www.mdpi.com/1424-8220/24/17/5675"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# Low-Cost CO2 NDIR Sensors: Performance Evaluation and Calibration Using Machine Learning Techniques

- **Citekey:** `dubeyLowCostCO2NDIR2024`  - **Año:** 2024  - **Tipo:** journalArticle
- **DOI:** [10.3390/s24175675](https://doi.org/10.3390/s24175675)

## Resumen

Evaluación comparativa de tres sensores NDIR de CO2 de distintos rangos de precio contra un analizador de referencia Los Gatos Research (LGR). Los autores prueban sensores de bajo costo (Sunrise AB y K30 de Senseair) y uno de gama alta (GMP343 de Vaisala) en ambientes controlados y en exteriores, aplicando después cinco algoritmos de machine learning para corregir las lecturas. El modelo *stacked ensemble* logró reducir el RMSE promedio de 27.6 ppm a 9.5 ppm (~65 % de mejora), aunque los autores advierten que entrenar con datos de cámara de crecimiento y validar en campo empeoró el desempeño, por lo que recomiendan calibraciones *in-situ* o con datos ambientales representativos.

## Montaje experimental

- **Instrumento de referencia:** Analizador Los Gatos Research (LGR) para gases de efecto invernadero (precisión ~70 ppb para CO2); mide vapor de agua y reporta CO2 como mezcla molar en aire seco.
- **Sensores evaluados (3 réplicas de cada uno):**
  - **Senseair Sunrise AB** (~USD 100–150): NDIR de bajo costo con compensación automática de presión (ABC) desactivada.
  - **Senseair K30** (~USD 85): NDIR de muy bajo costo.
  - **Vaisala GMP343** (~USD 6.000): NDIR de referencia de gama alta, precisión fabricante ±3 ppm + 1 % de lectura.
- **Variables ambientales auxiliares:** BME280 para temperatura, humedad relativa (HR) y presión atmosférica.
- **Condiciones de prueba:**
  1. **Ambiente exterior (rooftop):** 8 ago – 14 oct 2023, New Haven, CT. CO2 ~431 ppm, T 9–38 °C, HR 25–100 %.
  2. **Cámara de crecimiento ambiental:** ciclo 24 h, T 14–32 °C, HR no controlada, dos rangos de CO2: 418–850 ppm (ambiente) y 458–871 ppm (inyección de CO2 puro).
- **Corrección de humedad:** los sensores de bajo costo reportan CO2 húmedo; se convierte a CO2 seco con HR, T y P mediante ecuaciones de volumen de aire seco.
- **Métricas de evaluación:** pendiente, intercepto, R², RMSE y sesgo (%), comparando cada sensor contra LGR mediante regresión lineal.
- **Calibración ML:** 85 % de los datos ambientales para entrenar, 15 % para probar (datos no vistos). Variables predictoras: CO2_seco, HR, temperatura y presión. Target: CO2 del LGR.
- **Modelos probados:** regresión lineal múltiple, árbol de decisión, gradient boosting, random forest y *stacked ensemble* (linear + gradient boosting + random forest como nivel 0, linear como meta-modelo).

## Resultados principales

### Desempeño sin calibrar (ambiente exterior)

| Sensor | R² medio | Pendiente media | RMSE medio (ppm) | Sesgo absoluto medio |
|---|---|---|---|---|
| Vaisala GMP343 | 0.92 | 0.92 | 13 | 2.6 % |
| Senseair Sunrise | 0.86 | 0.80 | 21 | 4.0 % |
| Senseair K30 | 0.75 | 0.70 | 59 | 10 % |

- El K30 mostró mayor ruido (varianza media 1283 ppm²) y sobreestimó en dos de tres réplicas; la K30-1 tuvo RMSE de 131 ppm.
- Sunrise tuvo desempeño razonable dado que cuesta ~60 veces menos que Vaisala.
- Vaisala cumplió con su especificación de precisión; Sunrise estuvo cerca; K30 fue ~2× peor que su especificación de ±30 ppm.

### Desempeño tras calibración con ML (datos de prueba no vistos)

| Modelo | RMSE medio (ppm) | Mejora respecto a sin calibrar |
|---|---|---|
| Sin calibrar | 27.6 | — |
| Stacked ensemble | 9.5 | ~65 % |
| Regresión lineal | 10.5 | ~62 % |
| Gradient boosting | 11.1 | ~60 % |
| Random forest | 13.8 | ~50 % |
| Decision tree | 15.9 | ~42 % |

- **Vaisala:** RMSE de 10.7 ppm → 4.3 ppm.
- **Sunrise:** RMSE de 13.7 ppm → 8.5 ppm.
- **K30:** RMSE de 58.3 ppm → 15.8 ppm (K30-1 pasó de 127 ppm a ~16 ppm, reducción ~87 %).
- Los modelos de árbol mejoran datos no lineales; la regresión lineal extrapola mejor; el *ensemble* combina ambas fortalezas.

### Calibración con datos de cámara de crecimiento

- Entrenar modelos con datos de cámara y validar en rooftop **empeoró** el desempeño en dos de tres Sunrise (RMSE sin calibrar 13.5 ppm vs. 21.6 ppm tras calibrar con variaciones ambientales de cámara).
- La causa probable es la diferencia de distribución entre datos de laboratorio y campo (HR, T, P).
- Esto subraya que las calibraciones *in-situ* o con condiciones ambientales representativas son preferibles.

## Relevancia para la tesis

- **Justifica el uso de sensores NDIR de bajo costo (Sunrise, K30) para monitoreo de CO2 en BSF**, siempre que se calibren contra un patrón o con ML usando HR, T y P.
- El estudio muestra que **no basta aplicar corrección de humedad y temperatura**; es necesario un entrenamiento local para reducir sesgos de unidad a unidad.
- **Advertencia metodológica clave:** entrenar en cámara/clima artificial y desplegar en campo puede degradar el desempeño. Para la tesis, conviene recolectar datos propios de cámara BSF y calibrar *in-situ* o con estándar de gas.
- Proporciona métricas de error cuantificables para discutir incertidumbre en sensores de CO2 de bajo costo frente a analizadores de referencia tipo LGR.
- El *stacked ensemble* es una opción viable si se dispone de suficientes datos colocalizados; si no, una regresión lineal multivariada ofrece buena relación simplicidad/rendimiento.

## Oportunidades de integración

- Comparar estos resultados con el montaje de **Yasuda et al. (2012)** sobre NDIR y sensores químicos de CO2.
- Relacionar con **Soontronprasatporn et al. (2024)** y **Gacuthi (2026)**, que usan sensores MQ para GEI en BSF: Dubey demuestra que NDIR (especialmente Sunrise) pueden dar mejor especificidad y precisión que MQ para CO2.
- Vincular con **Schøn et al. (2024/2026)** en cuanto a la necesidad de un analizador de referencia (LI-COR/Sable) para validar sensores de bajo costo en respirometría.

## Preguntas abiertas / seguimiento

- [ ] ¿Qué temperatura/HR alcanza el interior de la cámara de BSF y cuánto afecta la lectura de CO2 en sensores NDIR sin compensar?
- [ ] ¿Se dispone de un estándar de CO2/N2O/CH4 para calibración *in-situ* o se recurrirá a colocación con analizador de referencia?
- [ ] ¿Es factible implementar el modelo *stacked ensemble* con los datos limitados de una cámara de BSF, o es preferible una regresión lineal robusta?

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado