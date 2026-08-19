---
citekey: riveramartinezPotentialLowCostTinOxide2021
title: "The Potential of Low-Cost Tin-Oxide Sensors Combined with Machine Learning for Estimating Atmospheric CH4 Variations around Background Concentration"
authors: ["Rivera Martinez, Rodrigo", "Santaren, Diego", "Laurent, Olivier", "Cropley, Ford", "Mallet, Cécile", "Ramonet, Michel", "Caldow, Christopher", "Rivier, Leonard", "Broquet, Gregoire", "Bouchet, Caroline", "Juery, Catherine", "Ciais, Philippe"]
year: 2021
type: journalArticle
doi: "10.3390/atmos12010107"
url: "https://www.mdpi.com/2073-4433/12/1/107"
tema: 05-iot-sensores
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# The Potential of Low-Cost Tin-Oxide Sensors Combined with Machine Learning for Estimating Atmospheric CH4 Variations around Background Concentration

- **Citekey:** `riveramartinezPotentialLowCostTinOxide2021`  - **Año:** 2021  - **Tipo:** journalArticle
- **DOI:** [10.3390/atmos12010107](https://doi.org/10.3390/atmos12010107)

## Resumen

Evaluación de sensores MOX de óxido de estaño (Figaro TGS2600, TGS2611-C00, TGS2611-E00) para reconstruir variaciones atmosféricas de CH4 cerca del fondo (~1.9–2.5 ppm) usando un perceptrón multicapa (MLP). Se caracterizaron interferencias de CO y H2O en laboratorio y se entrenó el MLP con 49,103 observaciones de 1 minuto durante 47 días en una habitación climatizada, usando como referencia un Picarro G2401 CRDS. El modelo MLP alcanzó RMSE <0.2 ppm en promedio en el conjunto de prueba, cumpliendo el objetivo de precisión, excepto cuando la distribución de entrenamiento no representaba las condiciones de prueba (peor caso RMSE >0.4 ppm). El sensor TGS2611-C00 fue el más adecuado. Se demostró que H2O es el predictor más crítico; CO, temperatura y presión tuvieron menor influencia en este dataset. Añadir múltiples versiones de sensores Figaro no mejoró el desempeño.

## Montaje experimental

### Laboratorio: caracterización de interferencias

- **Sensores:** 6 sensores Figaro en cámara de acero inoxidable/vidrio de 120 mL.
  - TGS 2600 (calidad del aire/CH4)
  - TGS 2611-C00 (CH4, sin filtro)
  - TGS 2611-E00 (CH4, con filtro de carbón activado)
- **Datalogger:** Raspberry Pi 3B+; divisor de voltaje con resistor 5 kΩ; ADC ADCPiPlus 17-bit.
- **Variables:** T (SHT75, ±0.3 °C), HR (SHT75, ±1.8 %), presión (BMP180, ±0.12 %).
- **Gases:** cilindros de aire seco con CH4 1.9 ppm y 8.999 ppm; mezcla con MFC para 6 niveles de CH4 (1.9–8.985 ppm).
- **Humedad:** generador de punto de rocío Licor LI-610 para 4 niveles de H2O (0.65, 1, 1.5, 2.5 %).
- **CO:** cilindro con 1.5 ppm CO + 2 ppm CH4; combinación con Sofnocat 514 para remover CO; 8 niveles de CO (0–1.5 ppm) a 3 niveles de H2O.
- **Referencia:** Picarro G2401 CRDS (precisión CH4 <1 ppb).

### Campo: habitación climatizada

- **Duración:** 47 días (27 abr – 12 jun 2018).
- **CH4 ambiente:** 1.95–2.5 ppm.
- **Sensores:** 6 Figaro + DHT22 (T/HR) + BMP180 (P).
- **Referencia:** Picarro G2401.
- **Preprocesamiento:** filtro Savitzky-Golay + mediana; robust scaler; 70 % train / 30 % test; 50 combinaciones de períodos train/test.

### Modelo MLP

- **Arquitectura:** 4 capas — entrada (5 unidades), dos ocultas (14 y 19 neuronas, activación tanh), salida lineal (1 unidad).
- **Optimizador:** BFGS (quasi-Newton), 300 iteraciones.
- **Regularización:** L2 weight decay + early stopping.
- **Inputs:** resistencia TGS 2611-C00, fracción molar H2O, CO, T, P.

## Resultados principales

### Sensibilidades de laboratorio

- **H2O:** la resistencia de los sensores es muy sensible al vapor de agua; afecta fuertemente la señal de CH4.
- **CH4:** TGS 2611-C00 fue el más sensible: pendiente −1.85 kΩ/ppm CH4 a 1 % H2O.
- **CO:** se cuantificó la contribución con modelo cuadrático bivariado y se corrigió en las mediciones de CH4-H2O.

### Desempeño del MLP en aire de habitación

| Métrica | Promedio train | Promedio test |
|---|---:|---:|
| MSD (ppm²) | 0.00135 | 0.0149 |
| RMSE (ppm) | 0.0368 | 0.122 |

- RMSE promedio en test <0.2 ppm, cumpliendo el requisito.
- **Mejor caso (período 7):** distribución de test contenida dentro de train → buen ajuste.
- **Peor caso (período 50):** train con bajos valores de H2O, test con altos valores de H2O y bajas T → RMSE >0.4 ppm.
- El modelo tiende a comportarse como filtro pasa-bajos: reproduce bien frecuencias bajas pero suaviza anomalías de alta frecuencia.
- Correlación promedio predicción vs. observación: r = 0.54; sesgo medio <0.1 ppm.

### Análisis de sensibilidad a inputs

| Input removido | Efecto |
|---|---|
| Presión | Mejor ligero desempeño en test (menor influencia) |
| Temperatura | Ligera mejora en test en este dataset |
| CO | Sin diferencia apreciable |
| **H2O** | **Mayor degradación del desempeño; variable más crítica** |
| Múltiples tipos de sensores | Degradación del test error (RMSE ~0.15 ppm); la inconsistencia entre versiones empeora el modelo |
| Dos sensores del mismo tipo | También empeora ligeramente |

- **Conclusión:** usar solo TGS 2611-C00 + H2O + T/P/CO es suficiente y mejor que combinar varios sensores.

## Relevancia para la tesis

- **Precisión objetivo para CH4 ambiental:** demuestra que sensores MOX de CH4 pueden alcanzar RMSE ≤0.2 ppm con ML, suficiente para detectar plomas industriales o fugas.
- **H2O como variable crítica:** en cámaras de BSF con HR variable, medir y compensar H2O es esencial para cualquier sensor MOX de CH4/NH3.
- **Problema de transferibilidad:** el modelo falla cuando la distribución de entrenamiento no cubre las condiciones de prueba. Para BSF, conviene entrenar con datos representativos del rango completo de T/HR/concentración.
- **No mejora con arrays de sensores:** a diferencia de otros estudios (Casey, Spinelle), aquí añadir más sensores Figaro empeoró el modelo por inconsistencias entre unidades. Esto refuerza la necesidad de caracterización individual.
- **Limitación:** rango muy bajo de CH4 (1.95–2.5 ppm); no se probó en plomas de varios ppm como en BSF o landfills.

## Oportunidades de integración

- Comparar con **Riddick (2020)** y **Mitchell (2024)** sobre TGS2600/TGS2611 y calibración individual.
- Relacionar con **Bertin (2026)** sobre uso combinado de TGS2611-E00/C00 + SGP40; Rivera Martinez sugiere que más sensores no siempre ayudan.
- Vincular con **Kiplimo (2024)** sobre ML para TGS2600/TGS2611 en campo.

## Preguntas abiertas / seguimiento

- [ ] ¿El rango de CH4 en BSF será principalmente cercano al fondo ambiente o habrá picos de varios ppm?
- [ ] ¿Se contará con un analizador de referencia tipo Picarro/LI-COR para entrenar el modelo MLP?
- [ ] ¿Cómo se asegurará que el dataset de entrenamiento cubra todo el espacio de T/HR esperado en la cámara?

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado