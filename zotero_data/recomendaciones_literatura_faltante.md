# Recomendaciones de literatura científica faltante

**Tesis:** Modelo matemático DEB para larvas de *Hermetia illucens*: predicción de biomasa y emisiones de CO₂/CH₄ con sensores IoT.

**Nota previa:** He cruzado las búsquedas con tu archivo `biblioteca.csv` (768 registros). Los artículos listados abajo **no aparecen en tu biblioteca** al momento de la revisión. Al final de cada eje indico también referencias clave que **ya tienes** y que puedes seguir usando.

---

## 1. Modelo DEB original de Kooijman

| # | Referencia | DOI | ¿Por qué lo necesitas? |
|---|------------|-----|------------------------|
| 1.1 | **Kooijman, S.A.L.M. (2010).** *Dynamic Energy Budget Theory for Metabolic Organisation* (3rd ed.). Cambridge University Press. | `10.1017/CBO9780511805400` | Es la biblia de DEB. Define el modelo estándar, las reglas κ, la dinámica de reserva/estructura, el efecto de temperatura (Arrhenius) y las extensiones para diferentes organismos. Imprescindible para fundamentar el marco teórico. |
| 1.2 | **Kooijman, S.A.L.M. (1986).** Energy budgets can explain body size relations. *Journal of Theoretical Biology*, 121, 269-282. | `10.1016/S0022-5193(86)80107-2` | Artículo seminal donde Kooijman introduce las bases de la teoría DEB. Sirve para citar el origen histórico y la justificación desde principios físico-químicos. |
| 1.3 | **van der Meer, J. (2006).** An introduction to Dynamic Energy Budget (DEB) models with special emphasis on parameter estimation. *Journal of Sea Research*, 56(2), 85-102. | `10.1016/j.seares.2006.03.001` | Tutorial clásico sobre el modelo estándar y, sobre todo, sobre cómo estimar parámetros DEB a partir de datos de crecimiento y reproducción. Te será útil para la calibración con datos de biomasa larval. |
| 1.4 | **Nisbet, R.M., Muller, E.B., Lika, K., & Kooijman, S.A.L.M. (2000).** From molecules to ecosystems through dynamic energy budget models. *Journal of Animal Ecology*, 69(6), 913-926. | `10.1111/j.1365-2656.2000.00448.x` | Conecta el modelo individual con escalamiento a poblaciones y ecosistemas. Importante si piensas extrapolar predicciones de biomasa/emisiones de individuos a un biorreactor. |
| 1.5 | **Jusup, M., Sousa, T., Domingos, T., Labinac, V., Marn, N., Wang, Z., & Klanjšček, T. (2017).** Physics of metabolic organization. *Physics of Life Reviews*, 20, 1-39. | `10.1016/j.plrev.2016.09.001` | Revisión moderna y rigurosa de la base termodinámica y física de DEB. Da respaldo académico al uso de balance energético y flujos de masa en tu modelo. |
| 1.6 | **Kearney, M.R., Domingos, T., & Nisbet, R.M. (2015).** Dynamic Energy Budget Theory: An Efficient and General Theory for Ecology. *BioScience*, 65(1), 34-35. | `10.1093/biosci/biv013` | Artículo de divulgación científica breve que resume por qué DEB es una teoría general de la ecología. Útil para introducir el marco en la tesis. |

**Referencias de este eje que ya tienes en biblioteca:** ninguna de las anteriores; solo aparece la cita a Kooijman 2010 dentro del artículo de Padmanabha et al. (2020), pero no el libro en sí.

---

## 2. Modelos bioenergéticos de insectos y extensiones del DEB

| # | Referencia | DOI | ¿Por qué lo necesitas? |
|---|------------|-----|------------------------|
| 2.1 | **Llandres, A.L., Marques, G.M., Maino, J.L., Kooijman, S.A.L.M., Kearney, M.R., & Casas, J. (2015).** A dynamic energy budget for the whole life-cycle of holometabolous insects. *Ecological Monographs*, 85(3), 353-371. | `10.1890/14-0976.1` | El artículo clave para adaptar DEB a insectos holometábolos (huevo-larva-pupa-imago). Propone el modelo hax/hex con aceleración metabólica; es la base más directa para construir un DEB de *H. illucens*. |
| 2.2 | **Maino, J.L., & Kearney, M.R. (2015).** Testing mechanistic models of growth in insects. *Proceedings of the Royal Society B: Biological Sciences*, 282(1819), 20151973. | `10.1098/rspb.2015.1973` | Evalúa modelos mecanicistas de crecimiento en 50 especies de insectos. Argumenta que la asimilación específica aumenta durante el crecimiento larval, lo cual es relevante para ajustar el modelo a las curvas de biomasa de BSF. |
| 2.3 | **Jager, T., Martin, B.T., & Zimmer, E.I. (2013).** DEBkiss or the quest for the simplest generic model of animal life history. *Journal of Theoretical Biology*, 328, 9-18. | `10.1016/j.jtbi.2013.03.011` | Presenta DEBkiss, una versión simplificada de DEB sin compartimento explícito de reserva. Es una alternativa si tus datos de biomasa no permiten identificar bien los parámetros del modelo completo. |
| 2.4 | **Marques, G.M., Augustine, S., Lika, K., Pecquerie, L., Domingos, T., & Kooijman, S.A.L.M. (2018).** The AmP project: Comparing species on the basis of dynamic energy budget parameters. *PLOS Computational Biology*, 14(5), e1006100. | `10.1371/journal.pcbi.1006100` | Describe el proyecto Add-my-Pet (AmP), la base de datos de parámetros DEB para ~3000 especies. Útil para buscar parámetros iniciales o priors de especies próximas a dípteros y para la metodología de estimación. |
| 2.5 | **Lika, K., Kearney, M.R., Freitas, V., van der Veer, H.W., van der Meer, J., Wijsman, J.W.M., Pecquerie, L., & Kooijman, S.A.L.M. (2011).** The "covariation method" for estimating the parameters of the standard Dynamic Energy Budget model I: Philosophy and approach. *Journal of Sea Research*, 66(4), 270-277. | `10.1016/j.seares.2011.07.010` | Método de estimación de parámetros DEB usado en AmP. Necesario si vas a estimar parámetros a partir de múltiples fuentes de datos (crecimiento, reproducción, respiración). |
| 2.6 | **Klagkou, E., Gergs, A., Kriehuber, R., & Preuss, T.G. (2024).** Modeling the Bioenergetics and Life History Traits of *Chironomus riparius* — Consequences of Food Limitation. *Insects*, 15(11), 848. | `10.3390/insects15110848` | Aplicación reciente de un modelo hax DEB a un díptero acuático, incluyendo alimentación limitada y pupación. Es un ejemplo metodológico muy cercano a lo que podrías hacer con *H. illucens*. |
| 2.7 | **Thomas, Y., Mazarié, B., & Le Moullac, G. (2011).** Application of a bioenergetic growth model to larvae of the pearl oyster *Pinctada margaritifera*. *Aquatic Living Resources*, 24(3), 245-252. | `10.1051/alr/2011137` | Aunque es un bivalvo larvario, muestra cómo un modelo bioenergético puede predecir crecimiento larval bajo distintas condiciones de alimento y temperatura. Puede servir como referencia comparativa para la fase larval. |

**Referencias de este eje que ya tienes en biblioteca:**
- Padmanabha, M., Kobelski, A., Hempel, A.J., & Streif, S. (2020). A comprehensive dynamic growth and development model of *Hermetia illucens* larvae. *PLOS ONE*, 15(9), e0239084. `10.1371/journal.pone.0239084`
- Kobelski, A., Hempel, A.J., Padmanabha, M., Klüber, P., Wille, L.C., & Streif, S. (2024). Model-based process optimization of black soldier fly egg production. *Frontiers in Bioengineering and Biotechnology*, 12, 1404776. `10.3389/fbioe.2024.1404776`

---

## 3. Emisiones de GEI (CO₂ y CH₄) en la cría de *Hermetia illucens*

| # | Referencia | DOI | ¿Por qué lo necesitas? |
|---|------------|-----|------------------------|
| 3.1 | **Xiang, F., Han, L., Jiang, S., Xu, X., & Zhang, Z. (2024).** Black soldier fly larvae mitigate greenhouse gas emissions from domestic biodegradable waste by recycling carbon and nitrogen and reconstructing microbial communities. *Environmental Science and Pollution Research*, 31(23), 33347-33359. | `10.1007/s11356-024-33308-8` | Tienes la versión preprint en ResearchSquare, pero falta el artículo publicado. Mide reducciones de CO₂ (62%), CH₄ (87%) y N₂O (95%) y explica los mecanismos microbianos. Fundamental para vincular tu modelo con datos de emisiones. |
| 3.2 | **Soontronprasatporn, K., Arunrungrusmi, S., Tunlasakun, K., Mungkung, N., & Tamrongkunannun, T. (2024).** Applying the internet of things (IoT) for raising black soldier fly in closed system to minimize greenhouse gas emissions. *Edelweiss Applied Science and Technology*, 8(6), 886-895. | `10.55214/25768484.v8i6.2182` | Artículo muy específico para tu tesis: combina cría de BSF + sensores IoT (MQ-4, MQ-135) + monitoreo de CO₂/CH₄ en sistema cerrado. Te sirve como referencia directa para tu componente de sensores. |
| 3.3 | **Perednia, D.A., Anderson, J., & Rice, A. (2017).** A comparison of the greenhouse gas production of black soldier fly larvae versus aerobic microbial decomposition of an organic feed material. *Research & Reviews: Journal of Ecology and Environmental Sciences*, 5(3), 10-16. | (no DOI encontrado) | Compara directamente emisiones de BSF frente a descomposición microbiana aerobia. Es uno de los estudios pioneros citados por casi todas las revisiones posteriores; útil para contextualizar tus mediciones. |
| 3.4 | **Salomone, R., Saija, G., Mondello, G., Giannetto, A., Fasulo, S., & Savastano, D. (2017).** Environmental impact of food waste bioconversion by insects: application of life cycle assessment to process using *Hermetia illucens*. *Journal of Cleaner Production*, 140, 890-905. | `10.1016/j.jclepro.2016.06.154` | Uno de los primeros ACV aplicado a BSF. Te da una visión sistémica de huella de carbono y puntos calientes del proceso, complementando tu enfoque de modelo dinámico. |
| 3.5 | **Guo, H., Jiang, C., Zhang, Z., Lu, W., & Wang, H. (2021).** Material flow analysis and life cycle assessment of food waste bioconversion by black soldier fly larvae (*Hermetia illucens* L.). *Science of the Total Environment*, 750, 141656. | `10.1016/j.scitotenv.2020.141656` | Combina análisis de flujos de materia (carbono/nitrógeno) con ACV. Útil para validar el balance de carbono que generará tu modelo DEB y contrastarlo con emisiones medidas por sensores. |

**Referencias de este eje que ya tienes en biblioteca (¡no necesitas buscarlas!):**
- Boakye-Yiadom, K.A., Ilari, A., & Duca, D. (2022). Greenhouse Gas Emissions and Life Cycle Assessment on the Black Soldier Fly (*Hermetia illucens* L.). *Sustainability*, 14(16), 10456. `10.3390/su141610456`
- Lindberg, L., Ermolaev, E., Vinnerås, B., & Lalander, C. (2022). Process efficiency and greenhouse gas emissions in black soldier fly larvae composting of fruit and vegetable waste with and without pre-treatment. *Journal of Cleaner Production*, 338, 130552. `10.1016/j.jclepro.2022.130552`
- Ermolaev, E., Lalander, C., & Vinnerås, B. (2019). Greenhouse gas emissions from small-scale fly larvae composting with *Hermetia illucens*. *Waste Management*, 96, 65-74. `10.1016/j.wasman.2019.07.011`
- Mertenat, A., Diener, S., & Zurbrügg, C. (2019). Black Soldier Fly biowaste treatment — Assessment of global warming potential. *Waste Management*, 84, 173-181. `10.1016/j.wasman.2018.11.040`
- Rossi, G., Ojha, S., Berg, W., Herppich, W.B., & Schlüter, O.K. (2024). Estimating the dynamics of greenhouse gas emission during black soldier fly larvae growth under controlled environmental conditions. *Journal of Cleaner Production*, 470, 143226. `10.1016/j.jclepro.2024.143226`
- Pang, W., Hou, D., Nowar, E.E., Chen, H., Zhang, J., Zhang, G., Li, Q., & Wang, S. (2020). The influence on carbon, nitrogen recycling, and greenhouse gas emissions under different C/N ratios by black soldier fly. *Environmental Science and Pollution Research*, 27, 42767-42777. `10.1007/s11356-020-09909-4`
- Pang, W., Hou, D., Nowar, E.E., Chen, H., Zhang, J., Li, Q., Wang, S., Chen, J., Hu, R., Yu, Z., & Li, Z. (2020). Reducing greenhouse gas emissions and enhancing carbon and nitrogen conversion in food wastes by the black soldier fly. *Journal of Environmental Management*, 260, 110066. `10.1016/j.jenvman.2020.110066`
- Chen, J., Tomberlin, J.K., Pang, W., Hou, D., Nowar, E.E., Hu, R., Zhang, J., Li, Q., Xie, J., & Yu, Z. (2019). Effect of moisture content on greenhouse gas and NH₃ emissions from pig manure converted by black soldier fly. *Science of the Total Environment*, 697, 133840. `10.1016/j.scitotenv.2019.133840`
- Cuesta-Parra, D.M., Montenegro-Marín, C.E., Ortega-Rosano, G., & Sanchez-Ruiz, F.J. (2025). Validation of a bioreactor for the growth of black soldier fly larvae: Test with animal feces, agave residues and vinasse. *Environmental Challenges*, 16, 101090. `10.1016/j.envc.2025.101090`

---

## 4. Sensores IoT y técnicas de medición de gases (adicional)

Aunque ya tienes varios artículos en esta línea, estos dos complementan el apartado anterior:

| # | Referencia | DOI | ¿Por qué lo necesitas? |
|---|------------|-----|------------------------|
| 4.1 | **Yasuda, T., Yonemura, S., & Tani, A. (2012).** Comparison of the Characteristics of Small Commercial NDIR CO₂ Sensor Models and Development of a Portable CO₂ Measurement Device. *Sensors*, 12(3), 3641-3654. | `10.3390/s120303641` | Ya lo tienes en biblioteca, pero lo recuerdo porque es la referencia clásica para calibración de sensores NDIR de CO₂ de bajo costo. |
| 4.2 | **Biagi, R., Ferrari, M., Venturi, S., Sacco, M., Montegrossi, G., & Tassi, F. (2024).** Development and machine learning-based calibration of low-cost multiparametric stations for the measurement of CO₂ and CH₄ in air. *Heliyon*, 10(9), e29772. | `10.1016/j.heliyon.2024.e29772` | También lo tienes. Útil si vas a calibrar sensores MQ/NDIR con machine learning para CH₄/CO₂. |

---

## Priorización sugerida para descarga

1. **Imprescindibles (descargar primero):**
   - Kooijman (2010) — DEB original.
   - Llandres et al. (2015) — DEB para insectos holometábolos.
   - van der Meer (2006) — estimación de parámetros.
   - Maino & Kearney (2015) — crecimiento insectil mecanicista.
   - Xiang et al. (2024) publicado — emisiones GEI en BSF.
   - Soontronprasatporn et al. (2024) — IoT + BSF + CO₂/CH₄.

2. **Muy recomendables:**
   - Jusup et al. (2017), Nisbet et al. (2000), Marques et al. (2018), Jager et al. (2013).

3. **Complementarios:**
   - Kooijman (1986), Kearney et al. (2015), Lika et al. (2011), Klagkou et al. (2024), Thomas et al. (2011), Salomone et al. (2017), Guo et al. (2021), Perednia et al. (2017).

---

*Generado el 2026-08-15 a partir de búsquedas web y cruce con `biblioteca.csv`.*
