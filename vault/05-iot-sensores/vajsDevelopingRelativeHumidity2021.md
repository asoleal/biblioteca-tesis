---
citekey: vajsDevelopingRelativeHumidity2021
title: "Developing Relative Humidity and Temperature Corrections for Low-Cost Sensors Using Machine Learning"
authors: ["Vajs, Ivan", "Drajic, Dejan", "Gligoric, Nenad", "Radovanovic, Ilija", "Popovic, Ivan"]
year: 2021
type: journalArticle
doi: "10.3390/s21103338"
url: "https://www.mdpi.com/1424-8220/21/10/3338"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# Developing Relative Humidity and Temperature Corrections for Low-Cost Sensors Using Machine Learning

- **Citekey:** `vajsDevelopingRelativeHumidity2021`  - **Año:** 2021  - **Tipo:** journalArticle
- **DOI:** [10.3390/s21103338](https://doi.org/10.3390/s21103338)

## Resumen

Estudio de calibración de sensores de bajo costo para monitoreo de calidad del aire, enfocado en compensar los efectos de temperatura (T) y humedad relativa (HR) mediante machine learning. Se comparan regresión lineal (LR), red neuronal artificial (ANN) y random forest (RF) para estimar CO, NO2 y PM10 a partir de señales brutas de sensores de bajo costo colocalizados con estaciones de referencia. Los resultados muestran que incluir T y HR como entradas mejora significativamente el desempeño de todos los modelos. RF fue superior cuando se incluyeron T y HR, mientras que ANN fue mejor cuando solo se usaban señales brutas. Los mejores R² alcanzados fueron 0.93–0.97 para CO, 0.82–0.94 para NO2 y 0.73–0.89 para PM10, dependiendo de la época del año.

## Montaje experimental

- **Sensores de bajo costo:** electrolíticos para CO y NO2; óptico para PM10.
- **Variables ambientales:** temperatura y humedad relativa medidas en cada unidad.
- **Referencia:** estaciones de monitoreo público/referencia gubernamentales.
- **Período de medición:** datos de 2019; análisis por meses (febrero, abril, agosto, octubre) para capturar variación estacional.
- **Preprocesamiento:** escalado/normalización de datos; división 70 % train / 30 % test (50/50 para meses individuales por tamaño reducido).
- **Validación cruzada:** 10-fold cross-validation para evaluar robustez.
- **Métricas:** R², RMSE, NRMSE (Root Mean Squared Error normalizado).

## Resultados principales

### Impacto de incluir T y HR

- Incluir T y HR como features mejoró consistentemente los resultados para CO, NO2 y PM10, tanto en calibración como en test.
- La influencia de HR y T no puede modelarse con funciones simples debido a procesos electroquímicos (CO, NO2) y crecimiento de partículas por absorción de agua (PM10).

### Comparación de algoritmos (datos completos)

| Algoritmo | CO R² test | NO2 R² test | PM10 R² test |
|---|---:|---:|---:|
| LR (solo raw) | ~0.80 | ~0.70 | ~0.70 |
| ANN (raw) | ~0.85 | ~0.78 | ~0.79 |
| ANN (raw + T + HR) | **0.93–0.97** | 0.82–0.94 | 0.73–0.89 |
| RF (raw + T + HR) | **0.93–0.97** | **0.82–0.94** | **0.73–0.89** |

- **CO:** ANN ligeramente mejor que RF en la mayoría de meses; ambos mucho mejores que LR.
- **NO2 y PM10:** RF fue consistentemente el mejor algoritmo cuando se incluyeron T y HR.
- **Mayor mejora relativa:** NO2 con RF, donde el modelo captura no-linealidades fuertes.

### Variación estacional

- **Febrero:** CO ANN mejor; NO2 y PM10 RF mejor.
- **Abril:** similar a febrero.
- **Agosto:** menores R² con LR para todos los contaminantes; RF superior para todos.
- **Octubre:** CO ANN mejor; NO2 y PM10 RF mejor.

### Conclusiones de los autores

- Los sensores de bajo costo pueden usarse como red complementaria a las estaciones de referencia si se calibran adecuadamente.
- Es necesario incluir T y HR en los modelos de calibración.
- RF y ANN son herramientas efectivas; la elección depende del contaminante y de si se dispone de variables ambientales.

## Relevancia para la tesis

- **Generalización del problema T/HR:** aunque el estudio es para CO/NO2/PM10, la conclusión de que sensores de bajo costo requieren compensación de T y HR es directamente aplicable a sensores de GEI (CO2, CH4, NH3) en cámaras de BSF.
- **Comparación de algoritmos:** RF y ANN/MLP son opciones viables; RF puede ser preferido cuando hay múltiples variables ambientales correlacionadas.
- **Variación estacional:** si el experimento de BSF dura meses, se debe considerar la deriva/variación estacional y posiblemente reentrenar modelos.
- **Limitación:** no incluye CO2, CH4 ni NH3; los sensores electroquímicos/ópticos tienen mecanismos diferentes a MOX/NDIR, pero el principio de compensación ambiental es el mismo.

## Oportunidades de integración

- Relacionar con **Dubey (2024)** y **Yan (2025)** sobre corrección de HR/T/P en sensores NDIR.
- Vincular con **Mitchell (2024)** sobre modelos no lineales con interacciones T×Vout y H×Vout para MOX de CH4.
- Contrastar con **Bertin (2026)** y **Yavari (2023)** sobre plataformas IoT multisensor.

## Preguntas abiertas / seguimiento

- [ ] ¿Se medirán T y HR dentro de la cámara de BSF con suficiente precisión para compensar sensores de GEI?
- [ ] ¿Se usará RF, MLP o un modelo híbrido según el contaminante?
- [ ] ¿Cómo se manejará la variación estacional en un experimento de larga duración?

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado