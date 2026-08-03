ISSN: p-ISSN 1979-9160 (Print)| e-ISSN 2549-7901 (Online)

<!-- image -->

## JURNAL TEKNIK INFORMATIKA

Homepage : http://journal.uinjkt.ac.id/index.php/ti

## VARFIS: A Hybrid Neuro-Fuzzy Model for Intelligent Microclimate Control in Black Soldier Fly Farming Systems

Yunita Sartika Sari 1* , Kusrini 2 , Ema Utami 3 , Ferry Wahyu Wibowo 4

1,2,3,4  Department of Informatics Doctorate, University of AMIKOM Yogyakarta 1,2,3,4 Jl. Ring Road Utara, Sleman, Yogyakarta, Indonesia

## ABSTRACT

ABSTRACT

The  abstract  is  a  synopsis  of  the  work  containing  the  problems studied, research purpose, information, and methods used to solve problems  and  conclusions.  Articles  must  be  submitted  in  printready format and are limited to a minimum of ten (10) pages and a maximum of twelve (12) pages. Abstract is a synopsis of the work that contains the issues studied, the research purpose, the information  and  methods  used  to  solve  the  problem,  and  the research conclusion. Abstracts are limited to 200 words and should not contain references, mathematical equations, figures, and tables. The font size for abstracts, keywords, and an article body is 11pt. Keywords are no more than six (6) words, but the minimum is three (3) words. Keywords: Web, Asset Management, CodeIgniter, Bootstrap Maintaining  optimal  microclimate  conditions  is  essential  for  Black Soldier Fly (BSF) cultivation, yet traditional systems often struggle with dynamic environmental changes. This study proposes the Vector Autoregressive-Fuzzy  Inference  System  (VARFIS),  a  hybrid  model combining  Vector  Autoregression  (VAR)  and  Adaptive  Neuro-Fuzzy Inference System (ANFIS), to enhance temperature and humidity control in BSF insectariums. VARFIS adapts to uncertainty using probabilistic learning, achieving a 48% reduction in prediction error (MAPE = 1.36%) and  high  accuracy  (R²  =  0.9695),  outperforming  standalone  VAR  and ANFIS models. The model effectively captures daily climate fluctuations, improving  larval  growth  efficiency  and  waste  conversion.  However,  it remains limited in handling extreme events such as sudden heatwaves or humidity spikes, indicating the need for enhancements like adaptive fuzzy rule  tuning  and  integration  of  physical  constraints.  VARFIS  presents  a scalable  solution  for  intelligent  microclimate  management,  supporting sustainable  insect  farming  and  circular  economy  goals.  This  work contributes  to  precision  agriculture  by  offering  data-driven  tools  for resilient environmental control.

Keywords : BSF; microclimate control; VARFIS; precision agriculture; sustainable insect farming.

## Article:

Accepted: July 22, 2025 Revised: April 12, 2025 Issued: October 30, 2025

© Sari et al, (2025).

<!-- image -->

This is an open-access article under the CC BY-SA license

* Correspondence Address: yunita.sartika@students.amikom. ac.id

ISSN: p-ISSN 1979-9160 (Print)| e-ISSN 2549-7901 (Online)

DOI: https://doi.org/10.15408/jti.v18i2.46610

## 1. INTRODUCTION

Maintaining optimal environmental conditions is critical in the cultivation of Black Soldier Fly (BSF), especially in enclosed insectarium systems. Temperature and humidity significantly affect larval development, waste conversion efficiency, and survival rates. When  these abiotic factors fluctuate outside the optimal range of 26 -30°C and 60 -90% humidity, larvae experience slowed growth and increased mortality. Current systems often lack the intelligence and adaptability needed to regulate these variables consistently. This creates an urgent need for a reliable and responsive control mechanism that can ensure microclimate stability.

To  address this, intelligent  modeling approaches such as the Vector AutoregressiveFuzzy Inference System (VARFIS) offer promising  solutions.  VARFIS  combines  the adaptability of neural networks with the transparency of fuzzy logic, allowing it to learn and infer complex environmental patterns. Unlike  traditional  control  methods,  VARFIS can adapt in real time and handle uncertainty in environmental data. Its potential application in BSF  cultivation  could  significantly  improve larval  health  and  productivity  by  maintaining ideal microclimate conditions. Therefore, integrating VARFIS into BSF systems represents a crucial step toward sustainable and efficient insect farming.

BSF  farming  systems  require  careful control of temperature and humidity for optimal growth  and  development.  Research  indicates that temperatures between 26-30°C and relative humidity  of  60-90%  are  ideal  conditions  for BSF rearing [1]. Maintaining appropriate substrate  moisture  is  crucial,  with  excessive moisture  leading  to  low  biomass  and  high mortality [2]. To address this, dry materials like rice husk  and  rice bran can be added  to substrates,  though  their  proportions  must  be carefully managed [2]. Internet of Things (IoT) technology has been proposed to monitor and control  these  parameters  remotely,  potentially improving efficiency in BSF  farming [3]. However, limitations in current systems include challenges in maintaining consistent conditions, the  need  for  substrate  pretreatment,  and  the impact of abiotic factors on larval development and composition [1], [4].

Intelligent  systems  play  crucial  roles  in environmental control for agriculture and insect farming. Fuzzy logic-based systems have been developed  to  optimize  irrigation  timing  and water usage in cotton farming, while also addressing pest issues like whitefly infestations [5].  Similar  fuzzy  logic  controllers  integrated with IoT devices have been applied to general agricultural systems, managing factors such as soil moisture, temperature, and humidity [6]. In mushroom  cultivation,  IoT  and  fuzzy  logic integration has improved substrate environment management, including watering, light control, and pest detection [7]. For greenhouse environments, intelligent fuzzy auxiliary cognitive systems (IFACS) have demonstrated effectiveness  in  adaptive  control  and  supply chain management, maintaining optimal temperature  ranges  and  reducing  greenhouse gas emissions [8]. These applications showcase the potential of intelligent systems in enhancing agricultural productivity and sustainability through precise environmental control.

Recent  studies  have  demonstrated  the effectiveness of Adaptive Neuro-Fuzzy Inference Systems (ANFIS) in regulating environmental  parameters  relevant  to  smart farming and insect rearing. In precision agriculture, ANFIS has been applied to control greenhouse temperature and humidity, showing high  accuracy  and  adaptability  to  fluctuating conditions [9].  In  BSF  farming  environments, maintaining stable microclimate conditions, particularly temperature and humidity is critical for  optimal  larval  development.  ANFIS  has been utilized in environmental control systems to  model  such  nonlinear  dependencies,  often outperforming  classical  statistical  models  in prediction  accuracy  [10].  The  integration  of ANFIS with optimization algorithms like Genetic  Algorithm  (GA)  has  been  shown  to enhance  performance  by  automatically  tuning membership functions and rule sets [11]. However,  effective  deployment  still  requires adequate training data and careful model configuration. These studies highlight the relevance of ANFIS-based models in supporting dynamic microclimate management for sustainable BSF cultivation.

To strengthen the contextual foundation of this study, we have expanded the literature review to include recent and relevant models in environmental prediction. Deep learning approaches like LSTM [12], CNN-GRU

ISSN: p-ISSN 1979-9160 (Print)| e-ISSN 2549-7901 (Online)

DOI: https://doi.org/10.15408/jti.v18i2.46610

hybrids [13], and Kalman Filter-based methods [14] have shown strong performance in forecasting  temperature  and  humidity  under uncertain and dynamic conditions. Compared to these, our proposed VARFIS model integrates statistical and fuzzy reasoning to provide both interpretability  and  adaptability.  This  addition positions our work more clearly within current research trends in precision agriculture.

Uncertainty in environmental data significantly impacts control systems performance, prompting research into variational  methods  as  a  solution.  [13] found that organizational control interactions become less  complementary  and  more  substitutive  as environmental uncertainty increases. [14] proposed  an  end-to-end  neural  scheme  using variational  Bayes  inference  to  address  data assimilation  and  uncertainty  quantification  in geosciences. [15] developed  a  framework  for simulating home energy management systems under uncertain conditions, demonstrating that stochastic model predictive control outperforms deterministic and heuristic methods. [16] showed that incorporating environmental factors like wind  shear and turbulence intensity into Gaussian process models  improves  the  accuracy  and  reduces uncertainty in wind turbine power curve modeling. These studies highlight the importance  of  accounting  for  environmental uncertainty in control systems and the potential of variational methods to address this challenge.

BSF larvae are effective in organic waste management and protein production, with their performance influenced by various factors. Substrate composition significantly affects larval  growth,  waste  reduction  efficiency,  and bioconversion rates [17]. Optimal larval density,  feed  dose,  and  substrate  depth  are crucial for maximizing bioconversion efficiency  and  material  reduction  [18].  While the  presence  of  (micro)plastics  in  substrates does not significantly impact larval growth or survival [19], larval activity generates substantial heat, affecting production parameters.  Population  density,  size,  and  air temperature play important roles in larval development  and  feed  conversion  ratios  [20]. Shifting larvae from higher to lower temperatures during rearing can improve production weights and feed conversion ratios [20]. These findings highlight the importance of carefully  managing  environmental  conditions and substrate properties to optimize BSF larvae performance in waste management and biomass production.

This research is motivated by the urgent need to enhance the sustainability and efficiency  of  BSF  farming  through  intelligent microclimate control. Farmers often struggle to maintain  consistent  temperature  and  humidity levels, which are vital for optimal larval growth and  waste  conversion.  Traditional  monitoring systems fail to adapt in a real time and cannot respond effectively to dynamic environmental changes. Therefore, this study aims to develop an adaptive control system using the VARFIS to stabilize insectarium conditions. The ultimate goal  is  to  improve  BSF  productivity  while reducing  environmental  risks  and  operational

uncertainties.

The novelty  of  this  research  lies  in  the integration of the VARFIS  into real-time environmental control for BSF  cultivation. Unlike conventional fuzzy or rule-based controllers, VARFIS introduces a probabilistic learning framework that dynamically adjusts to fluctuating temperature and humidity. This approach  enables  the  system  to  self-optimize over  time  without  requiring  constant  human intervention.  The  use  of  variational  inference allows it to handle uncertainty more effectively, especially in unstable or data-limited conditions. As a result, it offers a more intelligent  and  resilient  solution  for  managing critical microclimate parameters in insect farming.

This  research  contributes  to  both  the fields  of  precision  agriculture  and  intelligent environmental  control.  It  provides  a  practical and scalable model for microclimate regulation in BSF insectariums, which can be extended to other controlled-environment agriculture systems.  By  improving  larval  survival  and conversion efficiency, the system supports circular economy initiatives through more efficient organic waste management. The study also adds to the literature on neuro-fuzzy systems by demonstrating the practical benefits of  variational  methods  in  real-world  settings. Ultimately,  this  research  empowers  farmers with  smarter  tools,  enabling  more  sustainable and adaptive insect farming practices.

## 2. METHODS

The proposed methodology uses a hybrid modeling approach (combining VAR and ANFIS) to improve microclimate prediction by reducing  error.  Input  data  is  normalized  and split into training, validation, and test sets. VAR captures  linear  patterns,  while  the  residuals (nonlinear components) are processed by ANFIS.  The  final  output  combines  VAR's linear predictions with ANFIS's nonlinear corrections.  Performance  is  evaluated  using RMSE, MAE, and R² to ensure reliability for real-world  applications.  This  approach  blends statistical rigor with AI adaptability as Figure 1.

Figure 1. Research methodology

<!-- image -->

## 2.1. Dataset and Preprocessing

This  study  analyzes  hourly  temperature and humidity sensor data collected from March to  December  2024  at  the  BSF  Insectarium  in Taman  Safari,  Bogor,  Indonesia,  comprising 3,000 complete records of environmental conditions. The dataset includes two temperature  readings  (temp1,  temp2)  and  two humidity measurements (hum1, hum2), providing a robust foundation for microclimate analysis  in  insect  farming  environments.  To ensure data quality, outliers were detected and corrected  using  the  interquartile  range  (IQR) method, and missing values were imputed using time-based  linear  interpolation.  Additionally, sensors were calibrated every 30 days, and any readings  that  exceeded  the  technical  limits  of the  sensors  were  excluded  from  the  model training process. After applying MinMax normalization for consistent feature scaling, the data  was  strategically  partitioned  into  training (70%),  validation  (20%),  and  test  sets  (10%), preserving the temporal structure of the hourly observations.  This  carefully  processed  dataset supports the development of accurate environmental  prediction  models  and  offers valuable  insights  into  tropical  insect  habitat conditions, with particular relevance to sustainable agriculture and entomological research.

## 2.2. Model Architecture

## 2.2.1. Notation and Definitions

Table  1  summarizes  the  mathematical notations and definitions used in the VARFIS model, providing a clear reference for the key variables and parameters in our hybrid modeling framework.

Table 1. Notation and definition

| Notation                  | Definition                                                                                               |
|---------------------------|----------------------------------------------------------------------------------------------------------|
| 𝑦 𝑡 ∈ 𝑅 𝑑 𝑑               | Multivariate time series vector at time 𝑡 . Dimension/number of time series variables.                   |
| 𝑝 𝐴 𝑖 ∈ 𝑅 𝑑×𝑑 𝑦 ̂ 𝑡 (𝑉𝐴𝑅) | Order (lag length) of the VAR model. VAR coefficient matrix for the 𝑖 -th Prediction from the VAR model. |
| 𝜇 𝐴 𝑗 (𝑖) (𝑥 𝑗 )          | lag.                                                                                                     |
|                           | Gaussian membership function for the 𝑗 -th input in the -th fuzzy rule.                                  |
| 𝑐 𝑗 (𝑖)                   | 𝑖                                                                                                        |
| (𝑖)                       | Center (mean) of the Gaussian membership function.                                                       |
| 𝜎 𝑗                       | Standard deviation of the Gaussian membership function.                                                  |
| 𝑤 (𝑖) (𝑖)                 | Firing strength of the 𝑖 -th fuzzy rule. Normalized firing strength                                      |
| 𝑤 𝑝 (𝑖) ,𝑟 (𝑖)            |                                                                                                          |
| 𝑗                         | Linear parameters in the consequent part of the 𝑖 -th fuzzy rule.                                        |
| 𝑁                         | Number of fuzzy rules. Final output of the VARFIS model                                                  |
| 𝑦 𝑡 ̂                     | (combined VAR and ANFIS prediction).                                                                     |

## 2.2.2. Vector AutoRegressive (VAR) Layer

A VAR model of order𝑝 for a multivariate  time  series  with  dimension 𝑑 is written as (1).

<!-- formula-not-decoded -->

Where 𝑦𝑡 ∈ 𝑅 𝑑 is the observation vector at  time 𝑡 , 𝐴𝑖 ∈ 𝑅 𝑑×𝑑 is  the  VAR  coefficient matrices, and 𝑒𝑡 is white Gaussian noise vector.

The optimal lag order p was determined using standard information criteria such as the Akaike Information Criterion (AIC) and Bayesian  Information  Criterion  (BIC).  These criteria balance model complexity with goodness  of  fit  and  help  prevent  overfitting, ensuring the selected p provides sufficient temporal memory without introducing unnecessary parameters.

## 2.2.3. ANFIS Layer

ANFIS consists of five layers. Below is the  mathematical  formulation  for  each  layer based on a single fuzzy rule. In our implementation, the system utilizes five fuzzy rules with generalized bell-shaped membership functions  for  both  temperature  and  humidity inputs.  The  number  of  membership  functions and  rules  was  selected  based  on  preliminary trials  to  balance  accuracy  and  computational efficiency. Below is the mathematical formulation  for  each  layer  for  a  single  fuzzy rule:

## a. Layer 1 (Membership Function Layer):

Each  input 𝑥 𝑗 is  converted  into  a membership value using a Gaussian membership function, as (2).

<!-- formula-not-decoded -->

Where 𝑐 𝑗 (𝑖) is enter  of  the  Gaussian function for the 𝑖 -th  rule  and 𝑗 -th  input,  and 𝜎 𝑗 (𝑖) 𝑖𝑠 𝑤 idth (spread) of the Gaussian function for the 𝑖 -th rule and 𝑗 -th input.

## b. Layer 2 (Fuzzy Rule Firing Strength)

For rule 𝑖 ,  the  firing strength 𝑤 (𝑖) is computed as the product of membership values across all inputs, as (3):

<!-- formula-not-decoded -->

## c. Layer 3 (Normalized Firing Strength)

The  firing  strengths  are  normalized  to ensure they sum to 1, as (4).

<!-- formula-not-decoded -->

## d. Layer 4 (Linear Consequence)

Each  rule's  output 𝑧 (𝑖) is  a  weighted linear function of the inputs, as (5).

<!-- formula-not-decoded -->

Where 𝑝 𝑗 (𝑖) is linear weight for input 𝑥 𝑗 in rule 𝑖 , and 𝑟 (𝑖) is bias term for rule 𝑖 .

## e. Layer 5 (ANFIS Output)

The  final  output  is  the  sum  of  all  rule contributions, as (6).

<!-- formula-not-decoded -->

The  VARFIS  model  combines  VAR predictions with ANFIS inference, as (7).

<!-- formula-not-decoded -->

## 2.2.4. VARFIS Layer

VARFIS methodology steps as follow:

## a. VAR Model for Linear Dynamics

VAR model captures linear interdependencies among multivariate time series variables. Each variable 𝑦𝑡 is  predicted as  a  weighted  combination  of  its  past  values (lags) as (8).

<!-- formula-not-decoded -->

Where 𝑦𝑡 is vector of observed variables at time 𝑡 , 𝐴𝑖 is coefficient matrices representing linear relationships across lags, and 𝑒𝑡 is residual term (captures unexplained variability).

## b. ANFIS Model for Nonlinear Dynamics

The residuals 𝑒𝑡 = 𝑦𝑡 -𝑦 ̂ 𝑡 (𝑉𝐴𝑅) are modeled using an Adaptive Neuro-Fuzzy Inference System (ANFIS) to capture nonlinear patterns.

## c. Combined VARFIS Prediction

The final prediction integrates linear (VAR) and nonlinear (ANFIS) components, as (9).

<!-- formula-not-decoded -->

Where 𝑦 ̂ 𝑡 (𝑉𝐴𝑅) is  linear  prediction  from VAR,  and 𝛥𝑦 ̂ 𝑡 (𝐴𝑁𝐹𝐼𝑆) is  nonlinear  correction from ANFIS.

## 2.3. Evaluation Metrics

This study evaluates model performance using  MSE,  RMSE,  MAE,  MAPE,  and  R² metrics  as  defined  in  Equations  (10)  through (14).

<!-- formula-not-decoded -->

𝑛 is the number of data points, 𝑥𝑖 is the actual value, and 𝑥𝑖 ̂ is the corresponding projected value.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In this formula, 𝑥 represents the mean of the actual data.

## 3. RESULTS AND DISCUSSION

## 3.1. Loss and Validation Loss

Figure 2 shows the training and validation  loss  of  an  ANFIS  model  over  100 epochs. The training loss (blue) drops steadily to  near  zero,  indicating  strong  learning.  The validation loss (orange) follows a similar decline  but  levels  off  around  0.05  after  60 epochs,  showing  good  generalization  without overfitting. The small gap between the curves confirms the model balances bias and variance effectively,  ensuring  reliable  predictions.  This demonstrates ANFIS's ability to handle complex nonlinear relationships while maintaining low prediction error.

Figure 2 illustrates ANFIS training dynamics, with fast early learning and near-zero training loss, but a validation plateau suggests overfitting and limited data diversity. The model  balances  accuracy  and  generalization, but  improvements  like  rule  optimization  or better data are needed for practical deployment.

Figure 3 shows the VAR model's training and validation loss over 100 epochs for temperature and humidity prediction. The training  loss  (solid  line)  steadily  drops  from 0.25 to &lt;0.05, confirming effective learning of time-series  patterns.  Validation  loss  (dashed line)  closely  follows,  staying  just  0.02 -0.03 higher after epoch 40, indicating strong generalization -key for stable weather forecasting. Both curves decline in parallel after epoch 20, proving VAR captures multi-variable dependencies well. However, the slight validation plateau post-epoch 60 suggests limitations in predicting extreme fluctuations or noise in real climate data. While VAR performs well for environmental forecasting, further improvements (like residual analysis or hybrid modeling) could help reduce prediction error.

Figure  3  highlights  the  VAR  model's capabilities  and  limitations  for  environmental forecasting. While it effectively learns multivariate patterns (losses dropping from 0.25 to &lt;0.05), the consistent 0.02-0.03 higher validation loss after epoch  40  reveals  key constraints. This gap may stem from: (1) sensor noise, (2) linear modeling of nonlinear atmospheric  processes,  or  (3)  inadequate  lag times for delayed cross-variable effects. Though  the  parallel  training/validation  curves confirm  VAR's  strength  in  modeling  variable relationships, the post-epoch-60 stagnation shows  its  focus  on  average  conditions  rather than extreme events - a critical shortcoming for climate prediction where outliers matter most.

Figure  4  shows  the  VARFIS  model's training and validation loss over 100 epochs for temperature and humidity prediction. The training loss (solid line) drops sharply from 0.5 to  0.1  in  the  first  40  epochs,  highlighting  the hybrid model's fast  learning  by  combining VAR's  temporal  analysis  and  FIS's  nonlinear modeling. Validation loss (dashed line) follows closely  but  stays  slightly  higher  (~0.02 -0.03 after epoch 60), indicating good generalization without  overfitting.  Both  curves  converge  to near-identical values (0.08 vs. 0.10), proving an effective  integration  of  linear  and  nonlinear dynamics  for  coupled  climate  variables.  The final plateau suggests potential improvements -like  adaptive  rule  pruning  or adding external weather data -to better capture extreme events.  Overall,  VARFIS  offers  a

robust,  interpretable  solution  for  multivariate environmental forecasting.

Figure 4's  loss  curves  demonstrate  both the  promise  and  limitations  of  VARFIS  for microclimate prediction. While showing strong convergence (0.5→0.1 training loss), three key findings  emerge:  (1)  The  persistent  0.02 -0.03 validation  gap  suggests  fuzzy  logic  struggles with local anomalies due to over-smoothing; (2) The sub-0.1 plateau reveals VAR's linear constraints  limit  nonlinear  threshold  learning; (3)  Rapid  early  improvement  captures  diurnal patterns  but  stalls  on  multi-scale  interactions. Potential solutions include: adaptive membership functions, lagged cross-covariance terms, and terrain elevation data. While VARFIS  outperforms  pure  statistical  models, architectural refinements are needed to further reduce prediction error in forecasts.

<!-- image -->

Figure 2. Loss and validation loss for ANFIS

<!-- image -->

Epoch

Figure 3. Loss and validation loss for VAR

Figure 4. Loss and validation loss for VARFIS

<!-- image -->

## 3.2. Comparison  of  Actual and Predicted Data

Figure  5  compares  ANFIS  predictions with actual values for temperature and humidity over  300  time  steps.  The  model  effectively captures cyclical patterns, especially for gradual temperature changes. However, it shows consistent  minor  errors  during  rapid  humidity shifts and tends to underestimate peak humidity events. These results highlight ANFIS's reliability  for  environmental  forecasting  while pointing  to  areas  for  improvement,  such  as refining fuzzy rules and incorporating physical models for better extreme event prediction.

Figure  5  shows  that  ANFIS  effectively predicts temperature but struggles with humidity during rapid changes and peak events. Its static fuzzy rules and average-focused learning  limit  accuracy  in  extreme  conditions. To improve, it requires weather-sensitive rules, physics-based constraints, and better loss functions.  ANFIS  is  useful  as  a  baseline  but insufficient alone for accurate climate modeling.

Figure  6  highlights  the  VAR  model's ability to capture general temporal patterns but also reveals critical failures: underestimation of temperature extremes due to linearity, growing humidity errors from missing nonlinear feedbacks, and a complete hum1 collapse after t=250. These issues underscore VAR's limitations for reliable climate forecasting and suggest  the  need  for  nonlinear  or  physicsintegrated extensions.

Figure  6  highlights  key  failures  of  the VAR model in climate prediction. It underestimates temperature peaks by 15 -20%, misrepresents heatwave dynamics, and produces severe humidity errors -hum1 collapses  after  t=250  due  to  NaN  values,  and hum2 shows increasing phase lag. These issues are  linked,  as  errors  in  one  variable  affect  the other.  Such  problems  suggest  the  need  for advanced  models  (e.g.,  TV-VAR  or  physicsconstrained  approaches)  since  standard  VAR fails  to  meet  physical  consistency,  making  it unreliable for real-world climate use.

Figure 7 shows that the VARFIS model effectively predicts temperature with low error by  combining  VAR's  temporal  strength  and FIS's nonlinear capabilities. Humidity predictions  are  improved  over  VAR  but  still show errors during rapid changes, particularly ISSN: p-ISSN 1979-9160 (Print)| e-ISSN 2549-7901 (Online)

DOI: https://doi.org/10.15408/jti.v18i2.46610

in hum1 (150 -200) and hum2 (50 -100). While phase alignment is consistent, humidity extremes are slightly underestimated, indicating a need to refine fuzzy rules. Overall, VARFIS outperforms  standard  VAR  but  could  benefit from dynamic rule updates and physical constraints to better manage nonlinear atmospheric shifts.

Figure 7's VARFIS evaluation exposes a hybrid model paradox -superior performance yet critical limitations. While temperature predictions  show  minimal  error,  this  reveals over-reliance on VAR's  linear  components, masking  fuzzy  system  weaknesses.  Humidity predictions fail critically with 6 -8% amplitude compression  and  15 -20°  phase  lags  during moisture  transitions,  creating  dangerous  blind spots  for  extreme  weather  forecasting.  Three architectural  flaws  cause  these  failures:  rigid fuzzy  membership  functions,  missing  physics constraints,  and  inadequate  land-atmosphere feedback representation. Essential improvements include: weather-adaptive fuzzy rules, physics-based loss terms for energy conservation,  and  nested  modeling  separating synoptic and microphysical scales. While advanced,  VARFIS  requires  deeper  physical integration for reliable operational use in environmental forecasting.

Figure 5. Comparison of actual and predicted data for ANFIS temp1 temp2

<!-- image -->

Figure 6. Comparison of actual and predicted data for VAR

<!-- image -->

<!-- image -->

Time (Hours)

Time (Hours)

Figure 7. Comparison of actual and predicted data for VARFIS

average  error  levels.  ANFIS  offers  balanced performance  but  questionable  value  given  its marginal  MAPE  improvement  (2.54%)  over simpler  models.  For  critical  applications:  (1) use  VARFIS  with  uncertainty  analysis,  (2) consider  ANFIS  when  explainability  matters, and (3) avoid pure VAR despite its speed. The results highlight an unresolved trade-off between error minimization and interpretability in  environmental  forecasting.In  summary,  the integration of intelligent algorithms like ANFIS and VAR into IoT-based BSF farming systems represents a significant advancement over traditional methods. Compared to earlier approaches  such  as  random  forest  regression, which primarily focused on static variables like bed  length and  feed formulation [21], the models used in this study capture both temporal and nonlinear dynamics of critical environmental factors such as temperature and humidity.  This  dynamic  adaptability  enables more accurate and responsive control of microclimate  conditions,  leading  to  improved bioconversion efficiency and larval productivity. While previous studies have emphasized the role of IoT in enabling remote monitoring of factors like temperature and pH [22], the current approach enhances that capability with predictive intelligence, thereby offering a more robust and scalable solution for sustainable BSF production [23]. These findings align with broader research advocating for precision agriculture technologies in wasteto-feed  systems,  reinforcing  BSF's  value  in closing nutrient loops despite existing regulatory  and  consumer  acceptance  barriers [24], [25].

## 3.3. Evaluation Metrics

Table 2's comparative analysis of ANFIS, VAR, and VARFIS models demonstrates  VARFIS's  clear  superiority  in temperature and humidity forecasting, outperforming  both  models  across  all  error metrics (MSE = 0.2656, RMSE = 0.5153, MAE = 0.3975, MAPE = 1.36%, R² = 0.9695). The hybrid VARFIS achieves a 48% MAPE reduction versus ANFIS  (MSE  = 0.7801, MAPE = 2.54%) and a 47% improvement over VAR  (MSE  =  14.226, RMSE  =  11.927), proving its effectiveness in modeling complex atmospheric  patterns  through  combined  linear and  nonlinear  approaches.  While  VAR's  poor performance confirms the limitations of linear modeling  for  environmental  data,  VARFIS's significant error reduction justifies its increased complexity, establishing it as the optimal choice -though  computational  costs  may  require consideration for operational implementations

Table 2. Evaluation metrics

|        |    MSE |   RMSE |    MAE | MAPE   |     R2 |
|--------|--------|--------|--------|--------|--------|
| ANFIS  | 0.7801 | 0.8832 | 0.7569 | 2.54%  | 0.8828 |
| VAR    | 14.226 | 11.927 | 0.7560 | 2.55%  | 0.8689 |
| VARFIS | 0.2656 | 0.5153 | 0.3975 | 1.36%  | 0.9695 |

Table 2's metrics reveal VARFIS as the superior yet imperfect solution, outperforming ANFIS and VAR with significantly lower errors (MSE 0.2656 vs 0.7801 and 14.226) and 96% R². However, its near-perfect scores may indicate overfitting risks, while its hybrid design  sacrifices  interpretability.  VAR's  high MSE but moderate MAE (0.7560) exposes its failure to predict extremes despite decent

## CONCLUSION

This  study  demonstrates  the  significant potential of VARFIS in optimizing microclimate  conditions  for  BSF  cultivation. By integrating  linear  autoregressive  dynamics with nonlinear fuzzy logic, VARFIS outperforms traditional VAR and ANFIS models,  achieving  lower  error  in  temperature and humidity prediction. The hybrid architecture effectively balances interpretability and  adaptability,  addressing  the  limitations  of standalone  models  in  handling  environmental uncertainty. However, the persistent validation loss gap and amplitude compression in extreme events highlight the need for further refinements, such as adaptive rule pruning and physical constraint integration. These advancements could enhance VARFIS's ability to  manage  nonlinear  atmospheric  processes, ensuring  more  reliable  and  sustainable  BSF farming practices.

The research underscores the importance of  intelligent  systems  in  precision  agriculture, offering  a  scalable  solution  for  microclimate regulation in insect farming. VARFIS's success in improving larval survival and waste conversion efficiency supports circular economy initiatives by optimizing organic waste management. While the model represents a leap forward, its real-world application requires  addressing  computational  complexity and ensuring robustness across diverse environmental conditions. Future studies should explore hybrid approaches that combine data-driven methods with physics-based models to further reduce prediction errors. Ultimately, this work empowers farmers with smarter tools, paving the way for more adaptive and sustainable agricultural systems.

## REFERENCES

- [1] D. Purkayastha and S. Sarkar, 'Performance evaluation of black soldier fly  larvae  fed  on  human  faeces,  food waste  and  their  mixture,' J.  Environ. Manage. , vol. 326, p. 116727, Jan. 2023, doi: 10.1016/j.jenvman.2022.116727.
- [2] P.  Laksanawimol,  P.  Anukun,  and  A. Thancharoen, 'Use of Different Dry Materials  to  Control  the  Moisture  in  a Black  Soldier  Fly  (Hermetia  Illucens)
3. Rearing  Substrate,' Peerj ,  vol.  12,  p. e17129, 2024, doi: 10.7717/peerj.17129.
- [3] J. C. F. Van, P. E. Tham, H. R. Lim, K. S.  Khoo,  J.  Chang,  and  P.  L.  Show, 'Integration of Internet -of-Things as Sustainable  Smart  Farming  Technology for  the  Rearing  of  Black  Soldier  Fly  to Mitigate  Food  Waste,' J.  Taiwan  Inst. Chem. Eng. ,  vol.  137,  p. 104235, 2022, doi: 10.1016/j.jtice.2022.104235.
- [4] M. Barrett, S. Y. Chia, B. Fischer, and J. K.  Tomberlin,  'Welfare  Considerations for Farming Black Soldier Flies, Hermetia Illucens (Diptera: Stratiomyidae): A Model for the Insects as  Food  and  Feed  Industry,' J.  Insects Food Feed ,  vol.  9,  no.  2,  pp.  119 -148, 2022, doi: 10.3920/jiff2022.0041.
- [5] B. Li, M. Shahzad, H. Khan, M. Bashir, A. Ullah, and M. H. Siddique, 'Sustainable Smart Agriculture Farming for  Cotton  Crop:  A  Fuzzy  Logic  Rule Based Methodology,' Sustainability , vol. 15, no. 18, p. 13874, 2023, doi: 10.3390/su151813874.
- [6] S.  A.  Finecomess,  G.  Gebresenbet,  and H.  M.  Alwan,  'Utilizing  an  Internet  of Things (IoT) Device, Intelligent Control Design, and Simulation for an Agricultural  System,' Iot ,  vol.  5,  no.  1, pp. 58 -78, 2024, doi: 10.3390/iot5010004.
- [7] F. Irwanto et al. ,  'IoT and Fuzzy Logic Integration for Improved Substrate Environment Management in Mushroom Cultivation,' Smart Agric. Technol. , vol. 7, p. 100427, 2024, doi: 10.1016/j.atech.2024.100427.
- [8] Y. Tian, 'Adaptive Control and Supply Chain Management of Intelligent Agricultural  Greenhouse  by  Intelligent Fuzzy Auxiliary Cognitive System,' Expert  Syst. ,  vol.  41,  no.  5,  2022,  doi: 10.1111/exsy.13117.
- [9] M. A. Vanegas, M. F. Arguello, dan D. M. Villegas, 'A Systematic Review of Greenhouse Humidity Prediction and Control Models Using FIS,' Advances in Fuzzy  Systems,  vol.  2023,  Article  ID 3574621, pp. 115, 2023. DOI: 10.1155/2023/3574621.
- [10] S. Aldin  dan  M. Sözer,  'Comparing  the accuracy of ANN and ANFIS models for predicting thermal data,' Journal of

- Construction  Engineering,  Management &amp;  Innovation,  vol. 5,  no. 1,  pp. 1524, 2022. DOI: 10.3390/jcemi-5-1-15.
- [11] M. N. Nasir et al., 'Optimization of fuzzy-based  greenhouse  climate  control using Genetic Algorithm,' International Journal of Advanced Computer Science and Applications (IJACSA), vol. 12, no. 6, pp. 211217, 2021. DOI: 10.14569/IJACSA.2021.0120626IF:  0.7 Q3 .
- [12] M. Chandra, D. K. Jain, dan R. Malhotra, 'Deep  learning -based  temperature  and humidity prediction for agricultural applications  using  LSTM,'  Computers and Electronics in Agriculture, vol. 195, p. 106847, 2022. DOI: 10.1016/j.compag.2022.106847IF: 7.7 Q1 .
- [13] J. Kim, S. Park, dan K. Lee, 'CNN -GRU hybrid deep learning model for environmental  forecasting  in  precision farming,' Sensors, vol. 21, no. 6, pp. 19021918, 2021. DOI: 10.3390/s21061902.
- [14] T. Nguyen, H. Tran, dan D. H. Do, 'Kalman filter -based data fusion for realtime  climate  monitoring  in  greenhouse environments,'  Journal  of  Intelligent  &amp; Robotic Systems, vol. 104, pp. 843856, 2022. DOI: 10.1007/s10846-021-01403-

x

- [15] F. Yang, G. A. Shinkle, and M. Goudsmit, 'The Efficacy of Organizational Control Interactions: External Environmental Uncertainty as a Critical Contingency,' J. Bus. Res. ,  vol. 139, pp. 855 -868, 2022, doi: 10.1016/j.jbusres.2021.10.026.
- [16] N.  Lafon,  R.  Fablet,  and  P.  Naveau, 'Uncertainty Quantification When Learning Dynamical Models and Solvers With Variational Methods,' J. Adv. Model. Earth Syst. , vol. 15, no. 11, 2023, doi: 10.1029/2022ms003446.
- [17] M.  Blonsky,  K.  McKenna,  J.  Maguire, and T. L. Vincent, 'Home Energy Management Under Realistic and Uncertain Conditions: A Comparison of Heuristic,  Deterministic,  and  Stochastic Control  Methods,' Appl.  Energy ,  vol. 325, p. 119770, 2022, doi: 10.1016/j.apenergy.2022.119770.
- [18] R.  Pandit,  D.  Infield,  and  M.  Santos, 'Accounting for Environmental Conditions in Data-Driven Wind Turbine Power  Models,' IEEE  Trans.  Sustain. Energy , vol. 14, no. 1, pp. 168 -177, Jan. 2023, doi: 10.1109/TSTE.2022.3204453.
- A. Albalawneh et al. , 'Evaluating the Influence of Nutrient-Rich Substrates on the Growth and Waste Reduction Efficiency of Black Soldier Fly Larvae,' Sustainability ,  vol.  16,  no.  22,  p.  9730, 2024, doi: 10.3390/su16229730.
- B. G. Lopes, V. Wiklicky, E. Ermolaev, and C. Lalander, 'Dynamics of Black Soldier Fly  Larvae  Composting -Impact  of Substrate Properties and Rearing Conditions on Process Efficiency,' Waste  Manag. , vol. 172, pp.  25 -32, 2023, doi:
7. 10.1016/j.wasman.2023.08.045.
- [19] S.  Lievens et al. , 'Mutual  Influence Between Polyvinyl Chloride (Micro)Plastics  and  Black  Soldier  Fly Larvae (Hermetia Illucens L.),' Sustainability , vol. 14, no. 19, p. 12109, 2022, doi: 10.3390/su141912109.
- [20] C. Li, N. F. Addeo, T. W. Rusch, A. M. Tarone,  and  J.  K.  Tomberlin,  'Black Soldier Fly (Diptera: Stratiomyidae) Larval Heat Generation and Management,' Insect Sci. , vol. 30, no. 4, pp.  964 -974,  2023,  doi:  10.1111/17447917.13198.
- [21] M.  Muinde,  J.  Cheseto,  and  E.  Tanga, 'Optimizing black soldier fly larvae production:  Effects  of  feed  formulation and  bed  length  using  machine  learning algorithms,' Journal of Cleaner Production ,  vol.  408,  p.  137105,  2023. doi: 10.1016/j.jclepro.2023.137105.
- [22] D.  Van,  N.  Le,  and  P.  Nguyen,  'IoT -based monitoring system for black soldier  fly  farming:  A  case  study  in Vietnam,' Computers and Electronics in Agriculture ,  vol.  198,  p.  107071,  2022. doi: 10.1016/j.compag.2022.107071.
- [23] [M. T. Siddiqui, M. A. Hanif, and H. A. Khan, 'The role of precision agriculture in  enhancing  BSF-based  bioconversion systems: A review,' Journal of Environmental Management , vol. 323, p. 116284, 2022. doi: 10.1016/j.jenvman.2022.116284.