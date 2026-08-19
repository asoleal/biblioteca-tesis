---
citekey: gacuthiValorizationOrganicWastes2026
title: "Valorization of organic wastes through black soldier fly larvae bioconversion: reducing greenhouse gas emissions"
authors: ["Gacuthi, Virginia Wamboi", "Raude, James M.", "Ngumba, Elijah K.", "Matheka, Rosemary M."]
year: 2026
type: journalArticle
doi: "10.2166/washdev.2026.240"
url: "https://iwaponline.com/washdev/article/16/5/391/111764/Valorization-of-organic-wastes-through-black"
tema: 01-bsf-gei
tags: []
pdf: true
citado_tesis: false
origen: zotero
notas_enriquecidas: true
---

# Valorization of organic wastes through black soldier fly larvae bioconversion: reducing greenhouse gas emissions

- **Citekey:** `gacuthiValorizationOrganicWastes2026`  - **Año:** 2026  - **Tipo:** journalArticle
- **DOI:** [10.2166/washdev.2026.240](https://doi.org/10.2166/washdev.2026.240)


## Resumen

Este estudio cuantificó las emisiones de gases de efecto invernadero (GEI) y amoníaco (NH₃) durante la bioconversión con larvas de mosca soldado negra (BSFL, *Hermetia illucens*) de tres sustratos orgánicos: materia fecal humana (FM), estiércol de cerdo (PM) y estiércol de pollo (CM). Se compararon tratamientos con BSFL contra controles sin larvas, y se realizó un análisis de ciclo de vida (ACV) de cuna a puerta para estimar el potencial de calentamiento global (GWP) en CO₂-equivalente. Los resultados mostraron que el tratamiento con BSFL redujo significativamente las emisiones en todos los sustratos. El GWP de los controles fue mayor en CM (0.194 kg CO₂-eq), seguido de FM (0.072 kg CO₂-eq) y PM (0.005 kg CO₂-eq). Con BSFL, los valores se redujeron a 0.011 kg CO₂-eq para CM, 0.006 kg CO₂-eq para FM y 0.001 kg CO₂-eq para PM. La mayor reducción relativa se observó en CM (94.3 %), indicando que los sustratos ricos en nitrógeno y con baja relación C/N se benefician más de la bioconversión con BSFL. Los autores concluyen que la bioconversión con BSFL es una estrategia sostenible para reducir emisiones de GEI y valorizar residuos orgánicos dentro de una bioeconomia circular.

## Montaje experimental clave

### Sustratos

| Sustrato | Origen | C (%) | N (%) | C/N | Humedad inicial |
|----------|--------|------:|------:|----:|-----------------|
| Materia fecal humana (FM) | UDDT, Gachororo Primary School, Juja, Kenya | 43.57 ± 0.54 | 5.12 ± 0.00 | 14.65 ± 0.11 | No reportada (secado a 104 °C para análisis elemental) |
| Estiércol de cerdo (PM) | Granja privada, Juja, Kenya | 28.19 ± 3.06 | 2.41 ± 0.15 | 11.68 ± 0.51 | No reportada |
| Estiércol de pollo (CM) | Granja privada, Juja, Kenya | 24.52 ± 1.87 | 1.68 ± 0.00 | 8.51 ± 1.21 | No reportada |

- Análisis elemental: vario MACRO cube CHNS (Elementar) en Aarhus University, Dinamarca.

### Diseño experimental

| Parámetro | Valor |
|-----------|-------|
| **Diseño** | Completamente al azar |
| **Tratamientos** | 3 sustratos × 2 condiciones (con BSFL / sin BSFL) = 6 tratamientos |
| **Réplicas** | 3 por tratamiento |
| **Larvas** | 250 larvas de 7 días de edad por unidad experimental |
| **Ayuno previo** | 24 h de ayuno para vaciar tracto digestivo |
| **Cantidad de sustrato** | 0.25 kg por unidad experimental |
| **Cámara/contenedor** | Recipiente ventilado de **115 × 115 × 140 mm** |
| **Ubicación** | Invernadero en Jomo Kenyatta University of Agriculture and Technology (JKUAT), Nairobi, Kenya |
| **Temperatura** | 27.75 ± 2 °C (registrada, no controlada) |
| **Humedad relativa** | 60.72 ± 4 % (registrada, no controlada) |
| **Duración** | **15 días** |

### Sensores y medición de gases

| Gas | Sensor | Modelo / método |
|-----|--------|-----------------|
| **CH₄** | Sensor semiconductor | **MQ-4** |
| **CO₂** | Sensor semiconductor | **MQ-135** |
| **NH₃** | Sensor semiconductor | **MQ-135** |
| **N₂O** | Sensor semiconductor | **MQ-135** |
| **Temperatura / HR** | DHT22 | — |

- **Calibración:** periodo de quemado de 72 h; resistencia de línea base en aire limpio y seco; cálculo de concentración con ecuación log-log y parámetros m (pendiente) e b (intercepto) del datasheet.
- **Red inalámbrica:** microcontroladores + transceptores; datos enviados a plataforma ThingSpeak.
- **Frecuencia de calibración automática:** cada 3 min.
- **Frecuencia de medición de gases:** cada 30 min durante 15 días.

### Parámetros de calibración de sensores

| Gas | m | b | R₀ (kΩ) | Rₛ (kΩ) |
|-----|---|----|--------:|--------:|
| CH₄ | −2.3 | 0.72 | 10 | 1 |
| CO₂ | −2.2 | 0.42 | 30 | 2 |
| NH₃ | −1.9 | 0.53 | 30 | 2 |
| N₂O | −1.5 | 1.05 | 30 | 5 |

### Cálculos

- Conversión ppm → mg/kg según Oyatokun (2023) a 25 °C y 1 atm (comportamiento de gas ideal).
- GWP100 según IPCC 2021: CH₄ = 27.2, CO₂ = 1, N₂O = 273.
- NH₃ no tiene factor GWP en este estudio, pero se incluye en el ACV como output gaseoso.
- ACV realizado en OpenLCA v2.4 con base de datos ecoinvent y método GWP100.
- Unidad funcional: tratamiento de 0.25 kg de sustrato.
- Límites del sistema: incluye sustrato, agua, huevos de BSFL, alimento para crías, combustible de transporte, emisiones gaseosas y frass. Excluye infraestructura, producción de alimento inicial, electricidad y uso posterior del frass.

## Resultados numéricos destacados

### Concentraciones acumuladas de gases (15 días, ppm)

| Tratamiento | CH₄ | CO₂ | NH₃ | N₂O |
|-------------|-----:|-----:|-----:|-----:|
| BSF_FM | 195.75 ± 3.00 | 195.38 ± 1.00 | 0.97 ± 0.20 | 0.10 ± 0.11 |
| FM (control) | 2,205.32 ± 160.00 | 10,210.99 ± 22.00 | 87.58 ± 58.00 | 3,619.55 ± 100.00 |
| BSF_PM | 20.30 ± 1.29 | 126.14 ± 1.03 | 1.22 ± 0.69 | 0.16 ± 0.60 |
| PM (control) | 148.58 ± 0.89 | 1,176.20 ± 1.70 | 53.26 ± 0.34 | 0.55 ± 0.01 |
| BSF_CM | 393.57 ± 1.50 | 138.22 ± 1.80 | 19.95 ± 0.59 | 0.83 ± 0.01 |
| CM (control) | 3,544.37 ± 74.00 | 94,853.59 ± 350.00 | 219.00 ± 1.50 | 44,294.91 ± 200.00 |

### Reducciones porcentuales con BSFL

| Sustrato | Reducción CH₄ | Reducción CO₂ | Reducción NH₃ | Reducción N₂O | Reducción GWP |
|----------|--------------:|--------------:|--------------:|--------------:|--------------:|
| CM | 88.90 % | **99.85 %** | 90.89 % | **99.00 %** | **94.3 %** |
| FM | **91.13 %** | 98.09 % | **98.89 %** | ~100 % | 91.7 % |
| PM | 86.34 % | 89.27 % | 97.71 % | ~70 % | 80.0 % |

### Potencial de calentamiento global (GWP)

| Sustrato | Control (kg CO₂-eq) | BSFL (kg CO₂-eq) | Reducción |
|----------|--------------------:|-----------------:|----------:|
| CM | 0.194 | 0.011 | 94.3 % |
| FM | 0.072 | 0.006 | 91.7 % |
| PM | 0.005 | 0.001 | 80.0 % |

## Relevancia para la tesis

- Proporciona datos de reducción de GEI en bioconversión de residuos orgánicos con BSFL en contexto tropical/africano.
- Muestra que sustratos con bajo C/N (CM) tienen alto potencial de emisión pero también la mayor reducción relativa con BSFL.
- Utiliza sensores MQ (similares a Soontronprasatporn 2024) pero con calibración reportada, aunque los autores reconocen limitaciones de precisión y sensibilidad cruzada.
- Incluye ACV de cuna a puerta, útil para comparar con otros estudios de GWP en BSF.
- Destaca la importancia de la relación C/N del sustrato como variable controladora de emisiones.

## Limitaciones metodológicas

- Los sensores MQ no son de grado analítico; los autores interpretan resultados como tendencias más que valores absolutos.
- No se reporta un método de validación contra estándares de gas patrón ni contra cromatografía de gases.
- La temperatura y humedad no fueron controladas, solo registradas.
- La conversión ppm → mg/kg asume gas ideal y condiciones estándar, lo que puede introducir incertidumbre.

## Citado en la tesis

_(aún no citado)_

## Notas de lectura

- [x] Leído completo
- [x] Fichado
- [ ] Citado en borrador de tesis