---
citekey: riddickCalibrationDeploymentLowcost2020
title: "The calibration and deployment of a low-cost methane sensor"
authors: ["Riddick, Stuart N.", "Mauzerall, Denise L.", "Celia, Michael", "Allen, Grant", "Pitt, Joseph", "Kang, Mary", "Riddick, John C."]
year: 2020
type: journalArticle
doi: "10.1016/j.atmosenv.2020.117440"
url: "https://linkinghub.elsevier.com/retrieve/pii/S1352231020301771"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# The calibration and deployment of a low-cost methane sensor

- **Citekey:** `riddickCalibrationDeploymentLowcost2020`  - **Año:** 2020  - **Tipo:** journalArticle
- **DOI:** [10.1016/j.atmosenv.2020.117440](https://doi.org/10.1016/j.atmosenv.2020.117440)

## Resumen

Prueba de concepto del uso del sensor MOX de muy bajo costo Figaro TGS2600 (~USD 10) para medir razones de mezcla de metano cercanas al ambiente (1.8–5.8 ppm) y estimar emisiones de una terminal de gas natural durante tres meses. El sensor se calibró lado a lado con un Los Gatos Research Ultra-portable Greenhouse Gas Analyzer (UGGA) en laboratorio y campo. El algoritmo lineal publicado por Eugster & Kling (2012) no funcionó para el sensor de Riddick, por lo que derivaron una relación empírica no lineal que concuerda con el UGGA dentro de ±0.01 ppm. El TGS2600 mostró deriva de 0.002 ppm/día, alta variabilidad entre unidades (offset de 1.45 kΩ entre dos sensores idénticos) e incertidumbre a HR <40 %. Con el modelo de pluma gaussiana, estimaron emisiones medias de 9.6 g CH4 s⁻¹ para la terminal Norte y 1.6 g CH4 s⁻¹ para la terminal Sur (ya desmantelada). El trabajo demuestra la viabilidad de redes de sensores de bajo costo para monitoreo continuo de CH4, pero subraya que cada unidad requiere calibración individual con instrumento de referencia.

## Montaje experimental

- **Sensor:** Figaro TGS2600 (MOX de TiO2, ~USD 10, ~0.5 W).
- **Principio:** cuando el TiO2 se calienta, el CH4 adsorbido reduce la resistencia del sensor (RS). La relación RS/R0 (resistencia en aire limpio) es proporcional a la concentración de CH4.
- **Datalogger:** Arduino Uno; voltaje DC del sensor; registro de T, HR, fecha/hora en tarjeta SD cada 1 minuto.
- **Alimentación de campo:** batería de plomo-ácido 35 Ah, suficiente para 7 días de operación autónoma.
- **Calibración:** tres periodos lado a lado con UGGA (Los Gatos Research):
  - 21–22 abr 2018: laboratorio indoor, Univ. Manchester.
  - 24 jun 2018: St Michael's Church, Rampside.
  - 24 ago – 3 sep 2018: Plumpton Hall Farm, Lancashire.
- **Rango de calibración:** 1.85–5.85 ppm CH4.
- **Despliegue de campo:** 4 may – 15 jul 2018 en St Michael's Church, Rampside, UK, a 1.5 km de la terminal de gas Rampside.
- **Meteorología:** estación inalámbrica a 2 m de altura y 10 m del sensor; viento, T, HR, lluvia, irradiancia, presión cada 1 min.
- **Modelo de emisiones:** pluma gaussiana simplificada; filtrado por dirección del viento (270–315° para terminal Norte; 225–270° para terminal Sur); clase de estabilidad Pasquill-Gifford.

## Resultados principales

### Variabilidad entre unidades

- Dos TGS2600 idénticos mostraron respuesta temporal casi idéntica (R² = 0.995, pendiente = 1.015).
- Sin embargo, había un offset de **1.45 kΩ** en la resistencia al mismo CH4 (1.9–3.3 ppm).
- **Implicación:** cada sensor requiere calibración individual; no se puede usar un algoritmo genérico de otro estudio.

### Comparación de algoritmos de calibración

| Algoritmo | Ecuación | R² vs UGGA | Área bajo curva | Nota |
|---|---|---:|---:|---|
| Eugster & Kling (2012) | [CH4] = 1.828 + 0.0288·(RS/R0)corr | 0.27 | 31,537 | Subestima fuertemente; sensor se comporta diferente |
| Lineal empírico | [CH4] = −7.37 + 12.74·(RS/R0)corr | 0.57 | 43,833 | Mejor R² pero sobreestima masa en 25 % |
| No lineal empírico | [CH4] = 1.8 + 0.09·exp(11.669·(RS/R0)corr − 0.7083) | 0.23 | 34,690 | Mejor área (masa); error medio −0.004 ppm; incertidumbre ±0.01 ppm |

- El modelo no lineal (Ec. 5) fue seleccionado porque reproduce mejor la masa total (área bajo la curva), aunque no coincida punto a punto temporalmente con el UGGA.
- El TGS2600 responde más lentamente que el UGGA porque es pasivo (no tiene bomba forzada).

### Despliegue de campo

- **Rango medido:** 1.82–5.40 ppm CH4 (fondo ~2.0 ppm; pico 5.4 ppm el 2 jun 2018).
- **Deriva:** 0.002 ppm/día; se recomienda recalibración cada ~2 meses (drift acumulado 0.12 ppm).
- **Condiciones problemáticas:** HR <40 % produce salida inestable; no se puede calibrar con gases secos certificados.

### Emisiones estimadas (pluma gaussiana)

| Terminal | Emisión media | Emisión máxima | Estado |
|---|---:|---:|---|
| Norte | 9.6 g CH4 s⁻¹ | 238 g CH4 s⁻¹ | Activa |
| Sur | 1.6 g CH4 s⁻¹ | — | Desmantelada (emisiones residuales) |

- La emisión anual extrapolada para el Norte (~0.30 Gg CH4 año⁻¹) es comparable a la estimación del inventario nacional UK (0.45 Gg año⁻¹).
- El método de un solo sensor probablemente subestima las emisiones porque no siempre muestrea el centro de la pluma.
- **Incertidumbre total:** ±18 % (RMSD), dominada por temperatura (±13 %), velocidad del viento (±9 %) y medición de CH4 (±8 %).

## Relevancia para la tesis

- **Pionero en sensores MOX de CH4 de muy bajo costo:** demuestra que un sensor de ~USD 10 puede medir variabilidad de CH4 cerca del fondo ambiental si se calibra frecuentemente.
- **Advertencia crítica para BSF:** la gran variabilidad entre unidades y la necesidad de calibración individual implican que no se pueden desplegar sensores MOX "de caja" sin caracterización previa.
- **Deriva y mantenimiento:** en experimentos de BSF de semanas, la deriva de 0.002 ppm/día puede ser significativa; se necesitan puntos de control periódicos o calibración continua con referencia.
- **HR <40 %:** en cámaras de BSF con aire forzado y baja HR, el TGS2600/TGS2611 puede ser inestable; conviene humidificar o usar sensores con compensación integrada.
- **Modelo gaussiano:** si se despliegan sensores alrededor de la cámara de BSF, se podría estimar flujo de emisión de CH4/NH3 con un enfoque similar, aunque la geometría de fuente difusa es más compleja que un punto.
- **No apto para cuantificación absoluta sin referencia:** el estudio concluye que estos sensores son útiles para redes de detección y tendencias, no para mediciones de precisión absoluta sin calibración frecuente.

## Oportunidades de integración

- Contrastar con **Mitchell (2024)** y **Bertin (2026)**, que usan TGS2611 (más selectivo) y modelos ML, mostrando la evolución desde el TGS2600 de Riddick.
- Relacionar con **Soontronprasatporn (2024)** y **Gacuthi (2026)** sobre sensores MQ para GEI en BSF: mismas limitaciones de selectividad, deriva y calibración individual.
- Vincular con **Dubey (2024)** en cuanto a que sensores de bajo costo necesitan compensación de HR y T, y validación contra referencia.

## Preguntas abiertas / seguimiento

- [ ] ¿Se usarán sensores de CH4 en modo de detección de tendencias o para cuantificación de flujos de emisión?
- [ ] ¿Cómo se garantizará HR >40 % dentro de la cámara o línea de muestreo?
- [ ] ¿Con qué frecuencia se recalibrarán los sensores MOX durante un ensayo de BSF?

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado