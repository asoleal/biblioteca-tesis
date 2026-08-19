---
citekey: bertinMeasuringMethaneEmissions2026
title: "Measuring Methane Emissions in Ambient Air with a Low-Cost, Portable Sensor System: Focus on Scalability and Transferability of the Model"
authors: ["Bertin, Lorenzo", "Mentasti, Matteo", "Pittorino, Fabrizio", "Villa, Veronica", "Zanni, Emanuele", "Viscardi, Gabriele", "Ponzani, Yuri", "Massara, Andrea", "Roveri, Manuel", "Dellaca’, Raffaele", "Capelli, Laura"]
year: 2026
type: journalArticle
doi: "10.3390/s26134321"
url: "https://www.mdpi.com/1424-8220/26/13/4321"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# Measuring Methane Emissions in Ambient Air with a Low-Cost, Portable Sensor System: Focus on Scalability and Transferability of the Model

- **Citekey:** `bertinMeasuringMethaneEmissions2026`  - **Año:** 2026  - **Tipo:** journalArticle
- **DOI:** [10.3390/s26134321](https://doi.org/10.3390/s26134321)

## Resumen

Desarrollo y validación de una "caja de sensores" portátil del proyecto europeo ESCAPE para monitoreo de emisiones de metano en aire ambiente, con énfasis en escalabilidad y transferibilidad de modelos de calibración entre unidades idénticas. El sistema integra sensores MOX (TGS2611-E00/C00, SGP40) y un NDIR de CH4 (MH-441D) en una cámara de PTFE de 23.5 mL, con bomba de succión brushless, microcontrolador ESP32, BLE y app móvil. Se calibraron dos unidades (V2 y V3) en laboratorio con un sistema mezclador de gases automatizado (CH4 1–1000 ppm, CO2, etanol, acetona, HR 20–80 %) y se validaron en campo en dos rellenos sanitarios italianos con un FID portátil como referencia. Un modelo XGBoost entrenado con señales brutas de sensores predijo concentraciones de CH4, identificando correctamente los puntos calientes. La transferencia del modelo de V2 a V3 (y viceversa) no mostró reducción estadísticamente significativa de desempeño, aunque se observó un retardo de 2–6 s entre el sensor y el FID atribuido a la dinámica de respuesta del MOX.

## Montaje experimental

### Hardware de la caja de sensores ESCAPE

- **Cámara:** PTFE, 23.5 mL (17.5 mL neto), con flujo continuo regulado por amortiguador de flujo.
- **Sensores integrados:**
  - **TGS2611-E00** (Figaro): MOX analógico con filtro de carbón activado, selectivo a CH4 (~€20).
  - **TGS2611-C00** (Figaro): MOX sin filtro, más sensible a interferentes (VOCs) (~€20).
  - **SGP40** (Sensirion): MOX digital para VOCs, con compensación T/HR integrada (~€10).
  - **MH-441D** (Winsen): NDIR de CH4, umbral ~1000 ppm, usado como alarma de alta concentración (~€90).
  - **SHT40**: temperatura y HR (~€5).
- **Electrónica:** ESP32-WROOM-32, ADC ADS1115, I2C/UART, PCB de 4 capas con separación analógica/digital.
- **Adquisición:** 1 Hz; transmisión BLE a app Android; georreferenciación GPS; alimentación por power bank USB.
- **Seguridad:** bomba brushless downstream (sin chispas cerca de gas).

### Calibración en laboratorio

- **Sistema mezclador:** 4 líneas de gas con controladores de flujo masico (MFC Alicat): aire seco, aire húmedo (burbujeador), CH4, interferente.
- **Protocolo "solo metano":** 18 pasos de 600 s, CH4 = 1, 5, 10, 50, 100, 500, 1000 ppm; HR = 20, 40, 60, 80 % (2 réplicas cada una).
- **Protocolo con interferentes:** 31 pasos de 600 s con CH4 (10–1000 ppm) + CO2 (5–1000 ppm), etanol (1–150 ppm) o acetona (1–150 ppm); HR 30 y 60 %.
- Ambas cajas V2 y V3 se calibraron simultáneamente desde la misma cámara de estabilización.

### Campañas de campo

- **Sitios:** dos rellenos sanitarios activos en Italia (Landfill A y Landfill B).
- **Walkovers:** NW1, NW2, NW3 en Landfill A; NW4_1 y NW4_2 en Landfill B.
- **Referencia:** FID portátil (Gastec/Crowcon) con tubo de succión unido a la misma punta de muestreo telescópica.
- **Muestreo:** punta telescópica a pocos cm de la superficie; operador caminando; 1 Hz; datos sincronizados posteriormente.

### Modelo de machine learning

- **Algoritmo:** XGBoost regressor.
- **Features:** señales brutas de TGS2611-E00, TGS2611-C00, SGP40, MH-441D, T, HR.
- **Target:** concentración de CH4 medida por FID.
- **Hiperparámetros:** n_estimators=800, max_depth=8, learning_rate=0.05, subsample=0.8, reg_lambda=1.0.
- **Evaluación:** R², MAE, RMSE; train/test por walkovers y unidades; NW3 como hold-out; validación cruzada entre dispositivos (V2→V3, V3→V2).

## Resultados principales

### Respuesta de sensores en laboratorio

- TGS2611 detectó pasos de CH4 desde ~5 ppm; C-00 respondió más que E-00.
- MH-441D solo respondió apreciablemente a ~1000 ppm, confirmando su rol de alarma alta.
- En presencia de acetona, C-00 respondió al interferente mientras E-00 (con filtro) no lo hizo; esta diferencia es explotable por ML para mitigar interferencias.

### Desempeño del modelo (solo datos de campo)

| Configuración | R² | MAE (ppm) | RMSE (ppm) |
|---|---|---:|---:|
| V2 → V2 | 0.35 | 79.0 | 422.6 |
| V3 → V3 | −0.08 | 100.3 | 551.2 |

- El error está dominado por picos de alta concentración (>200 ppm, ~6 % de muestras).
- En el rango 0–50 ppm el MAE es de ~11–18 ppm, adecuado para detección de hotspots.

### Efecto de añadir datos de laboratorio

| Configuración | R² | MAE (ppm) | RMSE (ppm) |
|---|---|---:|---:|
| V2 → V2 | 0.47 | 71.2 | 382.9 |
| V3 → V3 | −0.01 | 91.1 | 532.9 |

- Incluir datos de laboratorio mejora el desempeño, especialmente en línea base y rangos bajos, pero no elimina completamente el error en picos.

### Corrección por retardo temporal

- El modelo MOX presenta un retardo de 2 s (V2) y 5–6 s (V3) respecto al FID.
- Tras aplicar el desplazamiento óptimo, el desempeño mejora notablemente:
  - V2 → V2: R² = 0.75, MAE ≈ 51 ppm, RMSE ≈ 250 ppm.
  - V3 → V3: R² = 0.77, MAE ≈ 51 ppm, RMSE ≈ 250 ppm.
  - V3 → V2: R² = 0.77, MAE = 59.6 ppm, RMSE = 253.4 ppm.
  - V2 → V3: R² = 0.49, MAE = 63.8 ppm, RMSE = 379.0 ppm.
- El retardo es una característica del hardware/dispositivo, no del modelo; su corrección requiere modelado dinámico (LSTM/GRU, derivadas, medias móviles).

### Transferibilidad entre dispositivos

- Entrenar en V2 y probar en V3 (y viceversa) mantuvo capacidad de identificar hotspots y sus amplitudes.
- Las métricas cruzadas son comparables a las mismas-unidad tras corregir el retardo, lo que respalda la escalabilidad del sistema.
- Se requiere más investigación sobre deriva a largo plazo y estrategias de recalibración.

## Relevancia para la tesis

- **Arquitectura de referencia para IoT en BSF:** la caja ESCAPE muestra cómo combinar MOX + NDIR + T/HR + ESP32 + BLE en un sistema portátil y de bajo costo, directamente adaptable a cámaras de BSF.
- **Transferibilidad de modelos:** es posible entrenar un modelo en una unidad y desplegarlo en otra idéntica, reduciendo costos de calibración individual. Esto es clave si se planea una red de varias cámaras de BSF.
- **Complementariedad MOX–NDIR:** MOX para detección de bajas concentraciones (ppm) y NDIR para rangos altos/alarmas, similar a lo que podría necesitarse en respirometría de BSF (CO2 bajo con NDIR, CH4/NH3 con MOX/electroquímicos).
- **Importancia de datos de laboratorio + campo:** la combinación mejora la robustez; para BSF, conviene generar matrices de calibración controladas (gas patrón, HR, T) y luego validar con referencia en la cámara real.
- **Retardo dinámico:** si se usan MOX para control en tiempo real de ventilación o dosificación, hay que considerar el tiempo de respuesta (decenas de segundos) y posiblemente implementar compensación dinámica.
- **Limitaciones:** el FID no es selectivo a CH4 (mide cualquier compuesto combustible); en BSF, NH3 y H2S podrían interferir si no se filtran o compensan.

## Oportunidades de integración

- Comparar con **Mitchell (2024)** y **Riddick (2020)** para discutir la evolución de sensores MOX de CH4: del TGS2600 al TGS2611 y al sistema multi-sensor ESCAPE.
- Vincular con **Dubey (2024)** sobre corrección de humedad/temperatura y modelos ensemble; y con **Yasuda (2012)** sobre selectividad de NDIR vs. químicos.
- Relacionar con **Schøn (2024/2026)** en cuanto a que respirometría robusta requiere referencia (LI-COR/Sable), mientras que sensores de bajo costo son útiles para monitoreo distribuido/tendencias.

## Preguntas abiertas / seguimiento

- [ ] ¿Se puede replicar la arquitectura ESCAPE con sensores de CO2, CH4, N2O y NH3 para una cámara de BSF?
- [ ] ¿Qué retardo de respuesta es aceptable para el control de ventilación o para detectar eventos de anoxia en BSF?
- [ ] ¿Cómo se mitigará la deriva de sensores MOX en un experimento de BSF de semanas?

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado