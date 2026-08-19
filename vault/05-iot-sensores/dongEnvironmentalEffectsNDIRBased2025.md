---
citekey: dongEnvironmentalEffectsNDIRBased2025
title: "Environmental Effects on NDIR-Based CH<sub>4</sub> Monitoring: Characterization and Correction"
authors: ["Dong, Wei", "Sasaki, Kyuro", "Zhang, Hemeng", "Wang, Yongjun", "Zhang, Xiaoming", "Sugai, Yuichi"]
year: 2025
type: journalArticle
doi: "10.1021/acs.est.4c11110"
url: "https://pubs.acs.org/doi/10.1021/acs.est.4c11110"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# Environmental Effects on NDIR-Based CH<sub>4</sub> Monitoring: Characterization and Correction

- **Citekey:** `dongEnvironmentalEffectsNDIRBased2025`  - **Año:** 2025  - **Tipo:** journalArticle
- **DOI:** [10.1021/acs.est.4c11110](https://doi.org/10.1021/acs.est.4c11110)

## Resumen

Este trabajo caracteriza los efectos ambientales sobre un sensor NDIR de CH4 de diseño propio (detector piroeléctrico MEMS + fuente IR de medio infrarrojo) y propone correcciones basadas en machine learning. A diferencia de sensores NDIR comerciales con cámara cerrada, el sensor custom utiliza una celda de aluminio de ~30 cm (46.2 mL) con filtros Fabry-Pérot centrados en 3346 nm (ventana óptima con fuerte absorción de CH4 y mínima interferencia de H2O/CO2). Se evaluaron influencias de temperatura, humedad relativa, presión y CO2, y se entrenaron modelos de regresión (linear, decision tree, random forest, gradient boosting, LightGBM, XGBoost) con optimización Bayesiana de hiperparámetros. LightGBM mostró el mejor balance entre precisión y generalización. El estudio incluye una validación de campo de 21 h en suelos (INAS) comparando contra LI-840A de CO2/H2O de LI-COR, evidenciando que fluctuaciones de CO2 pueden influir en la señal de CH4 incluso en ambientes estables.

> **Nota:** el PDF disponible en Zotero es el *supporting information* del artículo principal. La ficha se basa en ese material suplementario, que incluye metodología detallada, curvas de aprendizaje y análisis de selectividad.

## Montaje experimental

- **Sensor NDIR custom:** detector piroeléctrico LiTaO3 + interferómetro Fabry-Pérot (LFP-3144C-337, InfraTec, 3100–4400 nm) + fuente IR EMIRS200 (Axetris, 2–14 µm).
- **Celda de gas:** aluminio, longitud ~30 cm, volumen ~46.2 mL; ventanas de cuarzo ultra-transparente selladas con adhesivo siliconado.
- **Longitud de onda óptima:** 3346 nm (verificada por simulaciones HITRAN y experimentos).
- **Flujo:** 500 mL/min; válvulas solenoides cierran entrada/salida durante la medición.
- **Variables controladas:** temperatura (baño de agua/horno), humedad (generador de punto de rocío Licor LI-610), concentración de CH4 (mezcla de cilindros), CO2, presión.
- **Referencia de campo:** LI-840A CO2/H2O analyzer (LI-COR) para CO2; aire atmosférico como referencia para CH4 (asumiendo variaciones diurnas despreciables).
- **Adquisición:** tarjeta FPI conectada por USB; termopares para T de celda y ambiente.

## Resultados principales

### Sensibilidad ambiental

- **Temperatura:** la respuesta del detector cambia con la temperatura; se observaron histéresis durante ciclos de calentamiento/enfriamiento. La regresión lineal por rangos de T alcanzó R² = 0.999 (calentamiento) y 0.998 (enfriamiento), pero no fue robusta en todo el rango dinámico.
- **Humedad:** a alta T y baja HR los límites de detección mejoran porque se reduce la interferencia por bandas de absorción de H2O. A baja T y alta HR, el solapamiento H2O-CH4 se amplifica y pueden aparecer condensación/punto de rocío.
- **CO2:** concentraciones <500 ppm no afectan significativamente la señal de CH4; a 1000 ppm se observa un aumento notable en la relación de respuesta de CH4 debido a aumento de absorción IR.
- **Campo:** en una prueba de 21 h en suelo sin emisiones significativas de CH4, la señal de CH4 siguió la tendencia de CO2, confirmando la necesidad de corregir interferencia cruzada de CO2.

### Modelos de corrección de bias

| Modelo | Observaciones |
|---|---|
| Regresión lineal | R² alto en rangos estrechos, pero pobre generalización a cambios dinámicos de T |
| Decision tree / Random forest / Gradient boosting | Mejoran con más datos; gradient boosting generaliza mejor que random forest |
| XGBoost | Buen control de sobreajuste, pero mayor desviación estándar en validación cruzada |
| **LightGBM** | **Mejor consistencia entre entrenamiento y validación; robusto a tamaños de datos pequeños; seleccionado como mejor opción** |

- La optimización Bayesiana se usó para minimizar MSE, con rangos de hiperparámetros documentados (max_depth, n_estimators, learning_rate, subsample, etc.).

## Relevancia para la tesis

- **Diseño de sensores NDIR custom:** demuestra que es posible construir sensores NDIR de bajo costo con celdas de camino óptico largo y filtros Fabry-Pérot, aunque requieren caracterización cuidadosa de efectos ambientales.
- **Importancia de la longitud de onda:** la selección de 3346 nm minimiza interferencias de H2O y CO2, relevante si se considera diseñar un sensor propio para BSF.
- **CO2 como interferente en CH4:** en cámaras de BSF donde CO2 puede alcanzar miles de ppm, un sensor NDIR de CH4 podría verse afectado si no se corrige.
- **LightGBM para corrección:** ofrece una alternativa robusta a redes neuronales y ensemble más pesados, especialmente con datasets medianos.
- **Limitación:** el estudio se enfoca en suelos/emisiones difusas; el rango de CH4 en BSF puede ser mayor, por lo que se requiere validación específica.

## Oportunidades de integración

- Comparar con **Yan et al. (2025)**, que usa el sensor comercial Senseair K96 + MLP/Elastic Net para CH4 NDIR en campo.
- Relacionar con **Dubey et al. (2024)** sobre corrección de HR/T/P para sensores NDIR de CO2.
- Vincular con **Rivera Martinez et al. (2021)** y **Riddick et al. (2020)** sobre sensores MOX de CH4 y sus interferencias.

## Preguntas abiertas / seguimiento

- [ ] ¿Se usará un sensor NDIR comercial (K96, Sunrise, K30) o un diseño custom para CH4/CO2 en BSF?
- [ ] ¿Cuál es el rango esperado de CO2 en la cámara y cómo se corregirá la posible interferencia en CH4?
- [ ] ¿Se dispone de un generador de punto de rocío o cámara climática para caracterizar sensores antes del despliegue?

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado