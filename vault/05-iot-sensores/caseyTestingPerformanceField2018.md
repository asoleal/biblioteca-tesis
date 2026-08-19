---
citekey: caseyTestingPerformanceField2018
title: "Testing the performance of field calibration techniques for low-cost gas sensors in new deployment locations: across a county line and across Colorado"
authors: ["Casey, Joanna Gordon", "Hannigan, Michael P."]
year: 2018
type: journalArticle
doi: "10.5194/amt-11-6351-2018"
url: "https://amt.copernicus.org/articles/11/6351/2018/"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# Testing the performance of field calibration techniques for low-cost gas sensors in new deployment locations: across a county line and across Colorado

- **Citekey:** `caseyTestingPerformanceField2018`  - **Año:** 2018  - **Tipo:** journalArticle
- **DOI:** [10.5194/amt-11-6351-2018](https://doi.org/10.5194/amt-11-6351-2018)

## Resumen

Evaluación de la transferibilidad espacial y temporal de modelos de calibración de campo para sensores de bajo costo de O3 y CO2. Se comparan modelos lineales (LM) y redes neuronales artificiales (ANN) entrenados en una ubicación y aplicados en otra, en múltiples sitios de Colorado y Nuevo México (cuencas DJ y SJ, sitios urbanos y periurbanos influenciados por oil & gas). El estudio encuentra que no hay un único modelo ganador: el mejor tipo de modelo y sus entradas dependen del par train/test, de las fuentes de emisión dominantes, del momento de calibración y de la extrapolación fuera del espacio de parámetros. Para O3, los ANN generalmente superan a LM (6/7 casos), especialmente cuando se incluyen sensores metálicos secundarios. Para CO2, ANN es mejor cuando el entrenamiento abarca antes y después del período de prueba, pero LM extrapola mejor en el tiempo cuando solo hay datos posteriores. Los modelos de O3 son más sensibles a la ubicación; los de CO2 más sensibles al tiempo.

## Montaje experimental

### Sistemas U-Pod

- **Sensores de gas de bajo costo (7 por unidad):**
  - NDIR CO2: ELT S-300 (`eltCO2`)
  - MOX CH4: Figaro TGS 2600 (`figCH4`)
  - MOX VOCs (CxHy): Figaro TGS 2602 (`figCxHy`)
  - MOX O3: e2v MiCS-2611 (`e2vO3`)
  - MOX VOCs: e2v MiCS-5521 (`e2vVOC`)
  - MOX CO: e2v MiCS-5525 (`e2vCO`)
  - Electrochemical CO: Alphasense CO-B4 (`alphaCO`)
- **Variables ambientales:** temperatura (`temp`), humedad relativa (RHT03), presión (BMP085).
- **Cálculo adicional:** humedad absoluta (`absHum`).

### Despliegues

- **Sitios:** Denver (CAMP, urbano), Boulder County (Dawson, periurbano), BAO (Boulder Atmospheric Observatory), GRET (Greeley), San Juan Basin (Navajo Dam, Sub Station, Bloomfield, Fort Lewis, Shiprock).
- **Período:** 2014–2017.
- **Estrategia:** co-localización con instrumentos de referencia antes y después de despliegues distribuidos de ~1 mes.

### Modelos

- **Linear Models (LM):** simple y múltiple regresión lineal.
- **Artificial Neural Networks (ANN):** redes neuronales feed-forward.
- **Inputs evaluados:** desde sensor primario + T + HR hasta arrays completos de sensores metálicos.

## Resultados principales

### O3 — comparación ANN vs LM

| Caso de estudio | Mejor modelo | R² | RMSE (ppb) | MBE (ppb) | Notas |
|---|---|---:|---:|---:|---|
| Dawson summer 2014 (urbano → periurbano) | **LM** | 0.95 | 0.35 | −0.46 | ANN con más sensores empeoró por diferente química atmosférica |
| SJ Basin spring 2015 | ANN | 0.86 | 7.74 | 3.69 | Extrapolación temporal; T más fría que en entrenamiento |
| SJ Basin summer 2015 | ANN | 0.85 | 7.03 | 4.89 | Mejor con sensores MOX secundarios |
| BAO summer 2015 | ANN | 0.93 | 4.26 | 1.45 | Mismo sitio, train antes/después |
| BAO summer 2016 (GRET 2017 → BAO 2016) | **LM** | 0.89 | 6.25 | −0.20 | Extrapolación temporal significativa; LM más estable |
| GRET fall 2016 | ANN (sin HR) | 0.95 | 3.99 | 2.14 | HR "prestada" de Picarro degradó el modelo; sensores MOX capturan mejor HR |
| GRET spring 2017 | ANN | 0.98 | 2.59 | 1.49 | Mejor caso, train representativo |

### CO2 — comparación ANN vs LM

| Caso de estudio | Mejor modelo | R² | RMSE (ppm) | MBE (ppm) | Notas |
|---|---|---:|---:|---:|---|
| SJ Basin summer 2015 | ANN | 0.65 | 8.42 | −0.62 | Train antes/después |
| BAO summer 2015 | ANN | 0.75 | 9.98 | −2.60 | Train antes/después |
| BAO summer 2016 (GRET 2017 → BAO 2016) | **LM** | 0.73 | 11.82 | 0.73 | Extrapolación temporal fuerte; LM con tiempo como input mejor |
| GRET fall 2016 | LM | 0.82 | 8.62 | −3.46 | Problemas con HR prestada |
| GRET spring 2017 | ANN | 0.83 | 6.31 | 0.59 | Mejor caso |

### Hallazgos clave

- **O3:** ANN generalmente mejor que LM (6/7 casos), especialmente cuando se incluyen sensores MOX secundarios para resolver interferencias. Los modelos de O3 son más sensibles a la **ubicación** que al tiempo.
- **CO2:** ANN mejor cuando train "abraza" el período de prueba. LM mejor cuando hay **extrapolación temporal** (train solo después). Los modelos de CO2 son más sensibles al **tiempo** (deriva del sensor NDIR por polvo/degradación de lámpara).
- **Sensores secundarios:** ayudan cuando la química atmosférica es similar (BAO → SJ Basin), pero pueden empeorar cuando cambian las fuentes dominantes (urbano → periurbano, o plantas de carbón cerca de Sub Station).
- **Humedad:** medir HR con el propio sensor de la U-Pod es mejor que "prestar" HR de otro instrumento, porque los sensores MOX responden a la HR local del recinto.
- **Deriva:** se observó deriva sistemática descendente en sensores NDIR CO2 (ELT S-300) a lo largo de 2015–2017.

## Relevancia para la tesis

- **Transferibilidad de calibraciones:** directamente relevante si se planea calibrar sensores en un laboratorio/clima controlado y desplegarlos en cámaras de BSF. El estudio advierte que la extrapolación en espacio y tiempo puede degradar el desempeño.
- **ANN vs LM:** no siempre ANN es mejor; para extrapolación temporal o cuando cambian las condiciones químicas, LM puede ser más robusto.
- **Importancia de sensores secundarios:** en BSF, donde hay CO2, NH3, H2S, VOCs e H2O, incluir sensores adicionales puede ayudar a resolver interferencias, pero solo si el entrenamiento cubre esas condiciones.
- **Deriva y recalibración:** los sensores NDIR de CO2 pierden sensibilidad con el tiempo; se requiere estrategia de recalibración periódica o modelado de deriva.
- **Humedad medida localmente:** usar HR/T medidas dentro del mismo recinto que el sensor es crucial; no basta con datos de referencia externos.

## Oportunidades de integración

- Comparar con **Dubey (2024)** y **Yan (2025)** sobre NDIR + ML; Casey muestra el problema de extrapolación temporal.
- Relacionar con **Bertin (2026)** sobre transferibilidad entre dispositivos idénticos; Casey amplía a transferibilidad espacial/temporal.
- Vincular con **Rivera Martinez (2021)** sobre MLP para MOX de CH4 y sensibilidad a H2O.

## Preguntas abiertas / seguimiento

- [ ] ¿La calibración se hará in-situ en la cámara de BSF o en laboratorio/clima artificial?
- [ ] ¿Cómo se manejará la deriva de sensores en experimentos de semanas/meses?
- [ ] ¿Se incluirán sensores secundarios (NH3, H2S, VOCs) para resolver interferencias cruzadas?

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado