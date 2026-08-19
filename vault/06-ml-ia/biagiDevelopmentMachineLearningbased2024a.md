---
citekey: biagiDevelopmentMachineLearningbased2024a
title: "Development and machine learning-based calibration of low-cost multiparametric stations for the measurement of CO2 and CH4 in air"
authors: ["Biagi, R.", "Ferrari, M.", "Venturi, S.", "Sacco, M.", "Montegrossi, G.", "Tassi, F."]
year: 2024
type: journalArticle
doi: "10.1016/j.heliyon.2024.e29772"
url: "https://linkinghub.elsevier.com/retrieve/pii/S2405844024058031"
tema: 06-ml-ia
tags: []
pdf: true
citado_tesis: true
origen: zotero
notas_enriquecidas: true
---

# Development and machine learning-based calibration of low-cost multiparametric stations for the measurement of CO2 and CH4 in air

- **Citekey:** `biagiDevelopmentMachineLearningbased2024a`
- **Año:** 2024
- **Tipo:** journalArticle
- **DOI:** [10.1016/j.heliyon.2024.e29772](https://doi.org/10.1016/j.heliyon.2024.e29772)

## Resumen

Seis estaciones multiparamétricas de bajo costo (M, 1–5) para CO₂ y CH₄ se calibraron mediante un algoritmo de *Linear Forest Regression* (LFR) frente a un analizador de referencia Picarro G2201i (CRDS, 1 s⁻¹). El objetivo fue corregir la respuesta de sensores de bajo costo en condiciones ambientales reales, usando como predictores la señal cruda del sensor (CO₂ en ppm; razón Rs/R0 para CH₄), temperatura y humedad relativa. Los modelos LFR mostraron excelente ajuste en entrenamiento (R² 0,9855–0,9974 para CO₂; 0,9611–0,9918 para CH₄) y buena generalización en el 15 % de datos de prueba (R² 0,8781–0,9827 para CO₂; 0,7312–0,9410 para CH₄). Los errores absolutos medios en prueba fueron menores a 4 ppm para CO₂ y menores a 40 ppb para CH₄, con errores porcentuales absolutos medios inferiores al 1 % para CO₂ y entre 0,3 % y 2 % para CH₄. Los autores concluyen que el LFR es una herramienta prometedora para monitorizar gases de efecto invernadero con sensores de bajo costo.

## Objetivo y alcance

- Calibrar estaciones de bajo costo para CO₂ y CH₄ en aire mediante aprendizaje automático.
- Evaluar la transferibilidad entre ubicaciones y condiciones ambientales variadas (urbana, sub-urbana, humedal, zonas geotérmicas, industrial).

## Sensores y referencia

| Componente | Descripción |
|------------|-------------|
| Sensores CO₂ | Sensores NDIR de bajo costo (concentración en ppm) |
| Sensores CH₄ | Sensores metalóxido Figaro TGS (señal como razón Rs/R0) |
| Referencia | Picarro G2201i (CRDS), alta precisión: ±0,2 ppm CO₂, ±0,05 ppm CH₄ |
| Variables ambientales | Temperatura (°C) y humedad relativa (%) |

## Metodología

- **Algoritmo:** *Linear Forest Regression* (LFR), disponible en `linear-tree` (Cerliani, 2022). Combina un modelo lineal global con un bosque aleatorio entrenado sobre los residuos del modelo lineal.
- **Razón del LFR:** supera las limitaciones de RF puro (subajuste/sobreajuste, imposibilidad de extrapolar) al incorporar el comportamiento lineal global.
- **Preprocesamiento:** limpieza de valores atípicos mediante rango intercuartílico (IQR).
- **División de datos:** 70 % entrenamiento, 15 % validación, 15 % prueba.
- **Optimización:** `GridSearchCV` (scikit-learn) para ajuste de hiperparámetros.
- **Evaluación de incertidumbre:** 1000 muestras bootstrap sobre el conjunto de entrenamiento para estimar intervalos de confianza del 95 % en R² y MAE.
- **Métricas:** coeficiente de determinación R², error absoluto medio (MAE), error porcentual absoluto medio (MAPE).

## Sitios y período de medición

- **Ubicaciones:** Scandicci (Florencia), Galluzzo, Renazzo y Barbiano (llanura del Po), Vulcano (Sicilia), Pozzuoli (Nápoles), Montepulciano (planta industrial de CO₂), Padule di Fucecchio (humedal).
- **Período:** verano, otoño e invierno de 2022; invierno y primavera de 2023.
- **Resolución temporal:** promedios de 1 min.

## Resultados principales

### CO₂

- **Entrenamiento:** R² 0,9855 [0,9844, 0,9865] (estación 5) a 0,9974 [0,9972, 0,9975] (estación 1); MAE 0,71–1,44 ppm.
- **Prueba:** R² 0,8781 (estación 5) a 0,9827 (estación 1); MAE 1,95–3,76 ppm; MAPE 0,45–0,81 %.
- Las rectas de regresión en prueba tuvieron pendientes cercanas a 1, aunque las estaciones 4 y 5 presentaron interceptos notables (−10,03 y +6,08 ppm).

### CH₄

- **Entrenamiento:** R² 0,9611 [0,9598, 0,9624] (estación 1) a 0,9918 [0,9912, 0,9924] (estación M); MAE 0,0023–0,0127 ppm.
- **Prueba:** R² 0,7312 (estación 1) a 0,9410 (estación M); MAE 0,01–0,03 ppm.
- El menor rendimiento en CH₄ se atribuye a la menor variabilidad de concentraciones cercanas al fondo atmosférico y a conjuntos de entrenamiento más pequeños.

### Comparación con señal cruda

- Las señales crudas de los sensores mostraron correlaciones inadecuadas con la referencia: R² entre −21,35 y −0,19 para CO₂, y entre −2506 y −403 para CH₄, evidenciando la necesidad de calibración.

## Relevancia para la tesis

- Demuestra que LFR puede reducir drásticamente los errores de sensores de bajo costo para CO₂/CH₄ en condiciones de campo reales.
- Proporciona métricas cuantitativas de referencia (R², MAE, MAPE) útiles para comparar con otros enfoques de calibración basados en ML.
- Subraya la importancia de incluir temperatura y humedad como covariables y de usar datasets de entrenamiento diversificados para mejorar la transferibilidad.

## Limitaciones y perspectivas

- Algunos modelos podrían beneficiarse de un ajuste adicional de hiperparámetros.
- Se recomienda recopilar datos específicos del sitio antes de desplegar las estaciones para fines de investigación o monitoreo.
- Los autores proponen integrar transmisión remota mediante LoRaWAN para crear redes densas de monitoreo en tiempo real.

## Citado en la tesis

- `tesis-BSF/tesis/Capitulos/cap2_materiales_metodos.tex`
- `tesis-BSF/tesis/Capitulos/cap2_sec04_protocolo.tex`
- `tesis-BSF/tesis/Capitulos/cap2_sec05_calibracion.tex`
- `tesis-BSF/tesis/Capitulos/cap2_sec06_resultados.tex`
- `tesis-BSF/tesis/Capitulos/cap2_sec07_conclusiones.tex`
- `tesis-BSF/tesis/Capitulos/cap4_sec01_introduccion.tex`
- `tesis-BSF/tesis/Capitulos/discusion_capitulo2.tex`
- `tesis-BSF/tesis/Capitulos/intro_capitulo2.tex`

## Notas de lectura

- [x] Leído completo
- [x] Fichado