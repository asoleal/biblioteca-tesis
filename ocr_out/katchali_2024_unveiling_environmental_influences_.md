Citation: Katchali, M.; Senagi, K.;
Richard, E.; Beesigamukama, D.;
Tanga, C.M.; Athanasiou, G.;
Zahariadis, T.; Casciano, D.; Lazarou,
A.; Tonnang, H.E.Z. Unveiling
Environmental Influences on
Sustainable Fertilizer Production
through Insect Farming. Sustainability
2024, 16, 3746. https://doi.org/
10.3390/su16093746
Academic Editors: Zongguo Wen,
Yuan Tao, Fan Fei and Yanyan Tang
Received: 23 March 2024
Revised: 22 April 2024
Accepted: 24 April 2024
Published: 30 April 2024
Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
sustainability
Article
Unveiling Environmental Influences on Sustainable Fertilizer
Production through Insect Farming
Malontema Katchali 1,2
, Kennedy Senagi 1,*
, Edward Richard 2
, Dennis Beesigamukama 1
,
Chrysantus M. Tanga 1
, Gina Athanasiou 3
, Theodore Zahariadis 3,4
, Domenica Casciano 5
,
Alexandre Lazarou 5
and Henri E. Z. Tonnang 1,6
1
Data Management, Modeling and Geo-Information Unit, International Centre of Insect Physiology and
Ecology, Nairobi P.O. Box 30772-00100, Kenya; mkatchali@icipe.org (M.K.); dbeesigamukama@icipe.org (D.B.);
ctanga@icipe.org (C.M.T.); htonnang@icipe.org (H.E.Z.T.)
2
Department of Applied Mathematics, Pan African University Institute for Basic Sciences, Technology, and
Innovation, Nairobi P.O. Box 62000-00200, Kenya; edward.onyango@jkuat.ac.ke
3
Synelixis Solutions S.A., Farmakidou 10, 34100 Chalkida, Greece; athanasiou@synelixis.com (G.A.);
zahariad@synelixis.com (T.Z.)
4
Department of Agricultural Development, Agri-Food and Natural Resources, National and Kapodistrian
University of Athens, 11528 Athens, Greece
5
Zanasi & Partners, 41124 Modena, Italy; domenica.casciano@zanasi-alessandro.eu (D.C.);
alexandre.lazarou@zanasi-alessandro.eu (A.L.)
6
School of Agricultural, Earth, and Environmental Sciences, University of KwaZulu-Natal,
Pietermaritzburg 3209, South Africa
*
Correspondence: ksenagi@icipe.org
Abstract:
Entomocomposting is fast and environmentally friendly, boosts soil quality and crop
production, and improves resilience to climate change. The black soldier fly larvae (BSFL) catalyze
the composting process, but their efficiency is highly influenced by environmental factors and the
quality of the substrate. This study employs response surface methodology to discern physical–
chemical factors that influence the nutrient quality of BSF frass fertilizer. Internet of Things (IoT)
sensors were deployed to monitor in real-time both independent variables (air temperature, moisture
content, humidity, and substrate temperature) and dependent variables (nitrogen, phosphorous, and
potassium); the data were relayed to the cloud. A non-linear regression model was used to study the
relationship between the dependent and independent variables. Results showed that air humidity
and air temperature did not have a significant effect on nitrogen and phosphorus accumulation
in frass fertilizer, respectively, but phosphorus was significantly influenced by air humidity. On
the other hand, neither air temperature nor moisture content has a significant effect on potassium
concentration in frass fertilizer. We found that an air temperature of 30 ◦C and 41.5 ◦C, substrate
temperature of 32.5 ◦C and 35 ◦C, moisture content between 70 and 80%, and relative humidity
beyond 38% can be conducive for the production of high-quality BSF frass fertilizer. Model validation
results showed better robustness of prediction with R2 values of 63–77%, and R2
adj values of 62–76%
for nitrogen, phosphorous, and potassium. Our findings highlight the potential for the application of
digital tools as a fast and cost-effective decision support system to optimize insect farming for the
production of high-quality frass fertilizer for use in sustainable agriculture and crop production.
Keywords: waste recycling; black soldier fly; frass fertilizer quality; response surface methodology;
Internet of Things; sustainable agriculture
1. Introduction
Composting is the process of converting organic matter into organic fertilizer [1].
The natural process of organic matter decomposition is mainly driven by microorganisms
found in the organic wastes [2]. Besides the microorganisms playing an important role in
the decomposition process, their activities are highly influenced by temperature, oxygen
Sustainability 2024, 16, 3746. https://doi.org/10.3390/su16093746
https://www.mdpi.com/journal/sustainability

Sustainability 2024, 16, 3746
2 of 16
content, water, pH, moisture level, and carbon-to-nitrogen (C/N) ratio. The final product
(i.e., organic fertilizer) is a dark brown, humus-like substance that can be handled, stored,
and utilized as an excellent soil conditioner with ease and safety [3,4]. The long production
time and low-quality of organic fertilizer associated with conventional composting [5] have
encouraged a major shift to the use of insects in recycling organic waste since insects shorten
the composting time from 12–24 weeks to only 5 weeks [6]. For instance, the black soldier
fly (BSF) (Hermetia illucens (L.) (Diptera: Stratiomydiae) can accelerate the composting of
organic wastes into quality organic fertilizer and nutrient-rich insect biomass that can be
used as a source of feed for poultry, fish, pigs, and other animals [7–11]. The efficacy of
BSF frass fertilizer in boosting soil health, plant defense mechanism, crop productivity,
and profit margins has been clearly demonstrated [6,7,12]. Notably, the agronomic effec-
tiveness of frass fertilizer is largely influenced by the quality in terms of nutrients and
level of maturity and stability [7]. On the other hand, frass fertilizer quality depends on
the type and physical–chemical properties of the insect-rearing substrates and environ-
mental conditions (such as temperature, humidity, and aeration rate) provided during the
waste valorization process [9,13]. The provision of sub-optimal conditions and low-quality
substrates affects the bioconversion process and the quality of frass fertilizer generated.
Therefore, it is critical to optimize the entomocomposting process to improve the efficiency
and quality of frass fertilizer. Physical, chemical, and biological strategies have been used
to optimize the composting process with varying levels of success [14,15].
Improvements and optimization in the composting process can be further achieved
through the application of mathematical models. Petric and Mustafi´c [16] introduced a
mathematical model focused on microbial kinetics offering insights into the complex nature
of the composting system. This model considers various parameters such as temperature
and oxygen, among others, to better understand the dynamics within the composting
environment. Similarly, Vasiliadou et al. [17] established a comprehensive first-order
kinetics model for composting olive mill waste. This model incorporates considerations
for heat transport, organic substrate degradation, oxygen consumption, carbon dioxide
generation, and the presence of biological matter, providing a detailed framework for
analyzing and optimizing the composting process.
Composting models can be constructed using either analytical or numerical methods,
providing valuable insights into the optimization of the composting process. Courvoisier
and Clark [18] employed the finite difference method to create a numerical model of the
composting process. The study elucidated complex interactions such as heat transfer, gas
exchange, and microbial population dynamics. This model has implications for improving
waste management practices and enhancing environmental sustainability. Bongochgetsakul
and Ishida [19] presented a novel approach for optimizing large-scale composting facilities
by integrating numerical modeling with a 3D finite element system. Their method enabled
the calculation of mass/energy distribution influenced by biological activities, leading to
cost-effective and efficient facility design without the need for trial tests. Furthermore, math-
ematical models coupled with real-time data can significantly improve the management of
insect-driven waste composting processes. These models take into account environmental
parameters such as relative humidity and ambient temperature, which are crucial for insect
growth, organic matter decomposition, and nutrient transformation processes [20–23].
Through the use and application of such strategies, composting facility management and
design can be revolutionized, leading to improved performance, economic viability, and the
advancement of sustainable waste management solutions. Many interconnected factors,
such as population expansion, changes in high household consumption habits, economic
development, shifts in income, urbanization, and industrialization, have been linked to the
increase in waste production and its diversity [24]. The increasing variety of waste cate-
gories, including electronic, urban, hospital, and industrial waste, highlights the necessity
of accurately classifying garbage and developing efficient management standards [25–27].
As a result, Zafaranlouei et al. [28] addressed the complexities of waste management in
Iran by assessing 21 types of waste across economic, social, and environmental criteria.

Sustainability 2024, 16, 3746
3 of 16
The methods employed included a novel decision-making approach combining the base
criterion method (BCM) and combined compromise solution (CoCoSo) under fuzzy Z-
numbers. Sensitivity analysis revealed direct profit and reduced landfill as crucial criteria
for sustainable waste management with electronic waste requiring particular attention for
recycling and sustainable management. However, the study’s focus on a specific urban set-
ting and the complexity of incorporating Z-numbers pose a limitation to its generalizability
as suggested by [26].
In the BSF-assisted waste valorization process, previous studies focused on optimizing
the quality of larvae for animal feeding purposes [21], while others focused on substrates pa-
rameters only [20]. Nonetheless, it is necessary to unravel crucial environmental parameters
in the BSF-assisted composting process. This study employs a response surface method-
ology (RSM) approach to model the prediction of nutrient levels in BSF frass fertilizer
assessing how various environmental factors impact the nutrient concentrations within the
produced organic fertilizer generated. Through the RSM approach, non-linear regression
models are utilized to uncover the complex relationships between nutrient concentrations
in frass fertilizer and principal environmental factors that drive the BSF-assisted organic
waste valorization process, thereby providing a more comprehensive understanding of
how to improve the efficiency and outcome of this sustainable waste management strategy.
The following are the key contributions of this research work:
•
The integration of the response surface methodology (RSM) and Internet of Things
(IoT) technology to optimize black soldier fly larvae (BSFL) entomocomposting process
(based on environmental factors) in the production of high-quality frass fertilizer.
•
Implementation of a data-driven solution to discern important environmental vari-
ables that influence the nutrients generated in the BSFL composting process.
•
Proposing a sustainable resilient framework for organic waste valorization and man-
agement through BSFL-driven recycling systems toward a circular economy.
The rest of this paper is structured as follows: the experimental setup, data acquisition,
and the RSM model’s design are described in Section 2; Section 3 outlines the results, which
are then discussed in Section 4; and Section 5 concludes this article.
2. Materials and Methods
2.1. Frass Fertilizer Production Experiments
Black solder fly-rearing experiments were conducted at the animal rearing and quaran-
tine unit of the International Center of Insect Physiology and Ecology (icipe), Nairobi, Kenya.
The purpose of these experiments was to assess the influence of environmental factors
on substrate decomposition and nutrient accumulation during BSF-driven composting.
The experiments were conducted using potato waste from a local food-processing facility
situated in Nairobi Kenya and 5-day-old BSF larvae. Before commencing the experiments,
comprehensive laboratory analyses were conducted on the potato waste to evaluate various
physical–chemical properties. During the experiments, equal amounts of organic wastes
(potato waste) and 14.3 g of 5-day-old BSFL sourced from a colony meticulously maintained
at icipe were introduced into plastic trays measuring 55 cm × 38 cm × 10 cm. These trays
held 10 kg of potato waste: equivalent to 2 kg of dry weight. Following the protocols
outlined in [6], the BSFL were reared until they reached the harvesting stage. Thereafter,
the FarmShield [29] Internet of Things (IoT) device was placed in the trays to collect the
following variables: substrate temperature in ◦C, air temperature in ◦C, moisture content of
the substrate in percentage (%), relative humidity in percentage (%), and substrate nutrients
(that is, nitrogen, potassium, and phosphorus in mg/kg). The IoT transmitted this set
of data to the icipe cloud database platform in real-time every hour. The experimental
environment was set up with an average air temperature of 33.35 ◦C. BSFL were reared on
potato peelings as organic waste (i.e., the substrate). This continuous stream of information
served as a foundation for our computational modeling efforts, allowing us to analyze the
environmental factors influencing the BSFL ability in their role of substrate decomposition

Sustainability 2024, 16, 3746
4 of 16
and nutrient accumulation. This dataset played a pivotal role in the validation of our model
and in estimating critical parameters. The treatmentswere replicated three times.
2.2. Design of the Response Surface Methodology (RSM)
In this study, the RSM was employed to investigate the nutrient content within de-
composing organic waste during the rearing of BSFL. The investigation focused on four
independent variables: air and substrate temperatures, moisture content, and relative
humidity with nitrogen (N), phosphorus (P), and potassium (K) serving as the dependent
variables. A non-linear regression model, a variant of RMS, was developed to establish
the relationship between the response (N-P-K) and the independent variables. This rela-
tionship was articulated using a second-order polynomial equation [30,31] referred to as
Equation (1). The equations tailored to each dependent variable were coded into MINITAB
21.4.1 [32] software for analysis. The collected experimental data were then used to cal-
ibrate these equations, enabling a comprehensive understanding of how environmental
conditions influence the nutrient concentrations in the resulting frassfertilizer:
y = co +
n
∑
i=1
cixi +
n
∑
i=1
ciix2
i +
n−1
∑
i=1
n
∑
j=1
cijxixj
(1)
where
y is the predicted response level;
co is the constant coefficient;
ci is the coefficients of linear terms;
cij is the interaction coefficients;
cii is the coefficients of quadratic terms;
xi, xj are the values of the experimental variables.
2.3. Model Fitting and Evaluation
The analytical process, described in Equation (1), served as the foundation model for
analyzing the relationship between independent variables (air and substrate temperatures,
moisture content, and relative humidity) and the dependent variables (nutrient concentra-
tions of nitrogen, phosphorus, and potassium) in the context of composting with BSFL. The
range of independent variables, derived from experimental data, is incorporated in Table 1
to determine the estimated coefficients for the models. With these coefficients in place,
the non-linear (Equation (1)) was evaluated using the coefficient of determination R2 as in
Equation (3) and adjusted-R2 presented in Equation (4). The model’s statistical significance
was evaluated using the analysis of variance (ANOVA) components based on the signif-
icance level compared to the threshold value 0.05, i.e, Adjusted Sum of Squares (Adj SS)
and adjusted mean squares (Adj MS), defined in Equations (5) and (6), respectively. Further
statistical evaluation included examining the F-value and p-value, essential ANOVA compo-
nents for assessing model validity, and the strength of the relationships between variables.
To ascertain the statistical significance and identify any biases within the model, plots of the
normal probability distribution and the standard residuals were generated. This analytical
step was crucial for visually assessing the distribution of residuals and their conformity to
normal distribution, essential for validating the model’s assumptions. The integration of
actual data into the non-linear model, which had been fitted with the estimated coefficients,
provides deeper insights into the modeling experiments. The visualization of these pat-
terns, through the lens of normal probability distribution and standardized residual figures,
facilitates a comprehensive understanding of the model’s performance and its alignment
with empirical observations. This approach not only highlights the model’s accuracy in
capturing the relationships between variables but also aids in identifying potential areas of
improvement by revealing systematic deviations or anomalies in the data fit.

Sustainability 2024, 16, 3746
5 of 16
Table 1. Levels of experimental independent variables considered during the study.
Variables
SI Units
Annotation
Lower Value
Upper Value
Air humidity
Percentage (%)
x1
29.1
41.9
Air temperature
Degree Celsius (◦C)
x2
22
46.7
Moisture content
Percentage (%)
x3
27.0
148.4
Substrate temperature
Degree Celsius (◦C)
x4
30
43
RSS =
n
∑
i=1
(yi −ˆyi)2
(2)
R2 = 1 −RSS
TSS
(3)
R2
adj = 1 −(1 −R2)· (n −1)
n −k −1
(4)
Adj SS = SS −TSS
k
(5)
Adj MS = Adj SS
DF
(6)
where,
RSS is the sum of squares of residuals;
TSS is the total sum of squares;
n
is the number of observations;
k
is the number of independent variables;
SS
is the sum of squares;
DF
is the degree of freedom.
3. Results
3.1. Nitrogen Accumulation in Frass Fertilizer
The ANOVA results presented in Table 2 show that regression (linear, square, and inter-
action) relationships within the independent variables were significant (with a
p < 0.05). Table 3 highlights the estimated regression coefficients for response (N) and
other statistical validation values and shows that air humidity was not significant (with a
p-value > 0.05) for the generation of nitrogen, while the remaining variables were found
significant for the process.
From Table 3, the positive sign in front of the terms (independent variable) indicates
a favorable effect while a negative sign indicates an unfavorable effect. Therefore, the air
temperature, the substrate temperature, the rapid fluctuation effect of the moisture content,
the interaction of the air humidity and moisture content, the interaction of the air humidity
and substrate temperature, the interaction of the air temperature and moisture content,
and the interaction of the air temperature and substrate temperature play an important role
in increasing the nitrogen yield. Conversely, the accelerated changes in the air humidity
and air temperature, the interaction between the air humidity and air temperature, and the
interaction between the moisture content and substrate temperature exhibit a negative
influence, leading to a decrease in nitrogen yield.
The normal probability plot presented in Figure 1a indicates a normal distribution of
residuals obtained from the model. In Figure 1b, the residuals’ consistent spread, around
(y = 0, which means the error is zero), suggests that the model maintains a steady level of
accuracy across a range of projected values. The overall prediction accuracy has an R2 of
76.9% and R2
adj of 76%.
Considering the most significant variables stated in Table 3, the corresponding three-
dimensional response surface plots for nitrogen presented in Figure 2a show that the
maximum nitrogen content was obtained at an air temperature of approximately between

Sustainability 2024, 16, 3746
6 of 16
41.5 ◦C and 45 ◦C and a substrate temperature of 32.5 ◦C. The maximum nitrogen was
generated when the air temperature was 42.5 ◦C and the moisture content was toward 90%
(Figure 2b). It was noted that a combination of substrate temperatures (between 25 ◦C and
32 ◦C) and high moisture levels (approximately 80%) would produce fertilizer with the
maximum nitrogen levels (Figure 2c).
Table 2. ANOVA for the full regression model for nitrogen concentration in frass fertilizer, elucidating
the significance of terms within the model analysis.
Source
DF
SS
Adj SS
Adj MS
F-Value
p-Value
Regression Model
14
826,514
826,514
59,036.7
86.68
0.000
Linear
4
472,732
171,535
42,883.7
62.96
0.000
Square
4
178,450
74,321
18,580.4
27.28
0.000
Interaction between factors
6
175,332
175,332
29,221.9
42.90
0.000
Residual Error
365
248,607
248,607
681.1
Lack-of-Fit
338
248,607
248,607
735.5
Pure Error
27
0
0
0.0
Total
379
1,075,121
Table 3. Estimated regression coefficients for nitrogen accumulation in frass fertilizer.
Term
Estimated Coefficient
Standard Error of Coefficient
T-Statistic
p-Value
Remarks
Constant (co)
121.021
5.336
22.680
0.000
Air humidity
15.878
9.345
1.699
0.090
Non-significant
Air temperature
39.474
10.944
3.607
0.000
Significant
Moisture content
54.828
15.060
3.641
0.000
Significant
Substrate temperature
85.977
10.569
8.135
0.000
Significant
Air humidity2
−8.700
16.095
−0.541
0.589
Non-significant
Air temperature2
−121.940
14.898
−8.185
0.000
Significant
Moisture content2
38.811
19.309
2.010
0.045
Significant
Substrate temperature2
23.092
8.814
2.620
0.009
Significant
Air humidity × air temperature
−112.653
24.145
−4.666
0.000
Significant
Air humidity × moisture content
85.410
24.480
3.489
0.001
Significant
Air humidity × substrate temperature
58.580
14.427
4.061
0.000
Significant
Air temperature × moisture content
92.589
37.313
2.481
0.014
Significant
Air temperature × substrate temperature
148.590
15.596
9.527
0.000
Significant
Moisture content × substrate temperature
−84.313
17.982
−4.689
0.000
Significant
Variables (air temperature, moisture content, and substrate temperature) with p-value of <0.05 were considered
to be the most significant variables.
(a)
(b)
Figure 1. The normal probability and the residual depiction indicating a normal distribution (a),
the randomness and consistent spread of residuals around zero (b), validating the model’s unbiased
nitrogen predictions and uniform accuracy across predicted values.

Sustainability 2024, 16, 3746
7 of 16
(a)
(b)
(c)
Figure 2. Three-dimensional trends of nitrogen accumulation in frass fertilizer by pairing (a) air
temperature and moisture content, (b) air temperature and substrate temperature and (c) moisture
content and air temperature.
3.2. Phosphorus Accumulation in Frass Fertilizer
The results in Table 4 show that regression (linear, square, and interaction) relationships
within the independent variables have a significant (p < 0.05) impact on P accumulation
in frass fertilizer. After fitting the generalized non-linear regression model expressed
in Equation (1) with actual data parameters, the resulting empirical model is given in
Table 5. While humidity, substrate temperature and moisture emerge as key contributors in
phosphorus manufacturing, the air temperature is non-significant, leading to an antagonist
effect when combined with other factors (such as moisture content).
In Table 5, the positive coefficients associated with moisture content, substrate tem-
perature, rapid fluctuations in air temperature, substrate temperature and interactions
between air humidity–air temperature and moisture content–substrate temperature show
their importance in enhancing phosphorus accumulation. An evaluation of the model
accuracy revealed R2 and R2
adj of 63.6% and 62.63%, respectively. The normal probability
and standardized residual plot presented in Figure 3a,b highlight the range of occurred
errors associated with their occurrence probability within the data.
The substrate moisture content, substrate temperature, rapid fluctuations in air tem-
perature, and substrate temperature, and the interactions between air humidity and air
temperature, and moisture content and substrate temperature were positively correlated
with phosphorus accumulation.

Sustainability 2024, 16, 3746
8 of 16
It was found that air humidity of 34% to 37.5% combined with a substrate moisture
content of between 50% and 74% reduced phosphorus accumulation in frass fertilizer (less
than 100 mg/kg) (Figure 4a). Similarly, within the same range of air humidity coupled
with a substrate temperature of 33.5 ◦C to 36.5 ◦C, a plateau concentration of phosphorus,
presumably greater than or equal to 100 mg/kg was observed (Figure 4b). On the other
hand, phosphorus concentration increased with the rise in substrate temperature up to
36 ◦C, accompanied by a monotonic increase in moisture content (Figure 4c). However,
beyond 36 ◦C, the phosphorus concentration started to decrease.
Table 4. ANOVA for the full quadratic model for phosphorus accumulation in frass fertilizer
elucidating the significance of terms within the model analysis.
Source
DF
Adj SS
Adj MS
F-Value
p-Value
Regression Model
14
1,075,885
76,848.9
64.81
0.000
Linear
4
160,725
40,181.1
33.89
0.000
Square
4
117,409
29,352.2
24.76
0.000
Interaction between factors
6
53,672
8945.4
7.54
0.000
Error
519
615,361
1185.7
Lack-of-Fit
481
614,881
1278.3
Pure Error
38
481
12.6
Total
533
1,691,247
Table 5. Regression coefficients and level of significance of factors influencing phosphorus accumula-
tion in frass fertilizer.
Term
Estimated Coefficient
Standard Error of Coefficient
T-Statistic
p-Value
Remarks
Constant (co)
−881
4.51
20.21
0.000
Significant
Air humidity
−46.3
9.15
−5.41
0.000
Significant
Air temperature
−17.4
8.58
−1.00
0.316
Non-significant
Moisture content
120.7
8.76
4.49
0.000
Significant
Substrate temperature
2.56
12.2
1.98
0.049
Significant
Air humidity2
1.03
20.1
2.44
0.015
Significant
Air temperature2
0.12
16.3
6.80
0.000
Significant
Moisture content2
−0.65
8.82
2.89
0.004
Significant
Substrate temperature2
0.05
7.97
−4.02
0.000
Significant
Air humidity × air temperature
0.51
27.9
3.82
0.000
Significant
Air humidity × moisture content
−1.48
20.0
−2.57
0.011
Significant
Air humidity × substrate temperature
−0.1
14.4
−4.93
0.000
Significant
Air temperature × substrate temperature
−0.01
17.5
−4.21
0.000
Significant
Air temperature × moisture content
−0.34
22.9
−1.00
0.316
Non-significant
Moisture content × substrate temperature
0.03
12.9
−2.00
0.031
Significant
The variables (air humidity, moisture content, and substrate temperature) with p-value of <0.05 were considered
to be the most significant.
(a)
(b)
Figure 3. The normal probability and the residual depiction indicating a normal distribution (a),
the randomness and consistent spread of residuals around zero (b), validating the model’s unbiased
phosphorus predictions and uniform accuracy across predicted values.

Sustainability 2024, 16, 3746
9 of 16
(a)
(b)
(c)
Figure 4. Three-dimensional trends of phosphorus accumulation in frass fertilizer by pairing (a) air
humidity and moisture content, (b) air humidity and substrate temperature and (c) moisture content
and substrate temperature.
3.3. Potassium Accumulation in Frass Fertilizer
Table 6 reveals that just like in the case of phosphorus, the interaction between factors,
linear combination, and quadratic relationship is pivotal for potassium accumulation in
the frass fertilizer. Table 7 shows that potassium concentration significantly relies on air
humidity and substrate temperature, whereas air temperature and moisture content are
shown to be non-significant. It was observed that air humidity, air temperature, and rapid
fluctuations in moisture content lead to a reduction in potassium levels. Moreover, interac-
tions such as air temperature–moisture content and air humidity–substrate temperature do
not favor potassium accumulation. Figure 5a,b show that the model was fairly accurate to
the data coupled with the overall prediction accuracy of R2 = 63.1%, R2
adj = 62.1% signi-
fying the model’s ability to effectively capture and explain a significant proportion of the
variability in the data, indicating quite good predictive performance for the potassium level.
Considering the two significant independent variables, the corresponding three-
dimensional surface plot is illustrated in Figure 6. Results showed that the potassium
concentration is predominantly high, ranging from around 100 mg/kg to 200 mg/kg and
above, exhibiting a plateau-like pattern. This occurs within the range of air humidity, which
varies from 25% to 37.5%, coupled with substrate temperatures between 35 ◦C and 38 ◦C.
In addition, the combination of favorable factors enhanced the potassium concentration,
indicating increased potassium content.

Sustainability 2024, 16, 3746
10 of 16
Table 6. ANOVA for the full regression model for potassium accumulation in frass fertilizer elucidat-
ing the significance of terms within the model analysis.
Source
DF
Adj SS
Adj MS
F-Value
p-Value
Regression Model
14
961,065
68,647.5
63.41
0.000
Linear
4
114,174
28,543.4
26.37
0.000
Square
4
146,978
36,744.4
33.94
0.000
Interaction between factors
6
52,117
8686.2
8.02
0.000
Error
519
561,831
1082.5
Lack-of-Fit
481
561,350
1167.0
Pure Error
38
481
12.6
Total
533
1,522,896
Table 7. Regression coefficients and statistics regarding potassium accumulation in frass fertilizer.
Term
Estimated Coefficient
Standard Error of Coefficient
T-Statistic
p-Value
Remarks
Constant (C0)
−198
4.31
18.52
0.000
Air humidity
−76
8.74
−5.08
0.000
Significant
Air temperature
−18.5
8.20
−0.73
0.466
Non-significant
Moisture content
119.2
11.7
1.49
0.137
Non-significant
Substrate temperature
0.25
8.37
3.40
0.001
Significant
Air humidity2
1.32
19.2
3.28
0.001
Significant
Air temperature2
0.13
15.6
7.60
0.000
Significant
Moisture content2
−0.68
8.43
4.42
0.000
Significant
Substrate temperature2
0.01
7.61
−4.41
0.000
Significant
Air humidity × air temperature
0.54
26.7
4.29
0.000
Significant
Air humidity × substrate temperature
−0.04
13.8
−4.87
0.000
Significant
Air humidity × moisture content
−1.4
19.1
−1.03
0.302
Non-significant
Air temperature × substrate temperature
−0.02
16.7
−4.57
0.000
Significant
Air temperature × moisture content
−0.36
21.9
−1.61
0.109
Non-significant
Substrate temperature × moisture content
0.03
7.93
2.10
0.036
Significant
The variables (air humidity and substrate temperature) with p-value of <0.05 were considered to be the most
significant.
(a)
(b)
Figure 5. The normal probability and the residual depiction indicating a normal distribution (a),
the randomness and consistent spread of residuals around zero (b), validating the model’s unbiased
potassium predictions and uniform accuracy across predicted values.

Sustainability 2024, 16, 3746
11 of 16
Figure 6. The 3-D trends of the combined effect of air humidity and substrate temperature on the
potassium concentration in frass fertilizer.
4. Discussion
4.1. Effect of Environmental Factors on Nitrogen Accumulation in Frass Fertilizer
Our findings showed that air temperature, moisture content, and substrate tempera-
ture significantly influenced nitrogen accumulation in frass fertilizer. Moreover, the optimal
substrate temperature identified aligns with the 30 ◦C to 35 ◦C reported by Padmanabha
et al. [33] for both nitrogen accumulation and efficient BSF production. The substrate
temperature is pivotal for microbial activities [17], enzymatic processes [34], and chemical
reactions [35] essential in nitrogen transformation. The identified optimal conditions fall
within the mesophilic advantage for mitigating ammonia volatilization prevalent at ther-
mophilic temperatures (>45 ◦C). Previous studies by MacDonald et al. [36] also found that
the rate of microbial respiration and the mineralization of nitrogen waste degradation are
temperature-dependent. In Hu et al. [37], it is further highlighted how moisture variation
impacts microbial activities, oxygen concentration, and nutrient transport. Excessive mois-
ture potentially leads to nitrogen loss via denitrification and impeding BSF larval growth.
Thus, while temperature and moisture content are crucial, their effects might diminish the
perceived impact of air humidity on nitrogen accumulation [38]. Nonetheless, both air
temperature and relative humidity indirectly influence substrate moisture and temperature,
thereby affecting nitrogen transformation during BSF-assisted composting. In essence,
the interplay of air humidity, temperature, and moisture content plays a significant role in
nitrogen accumulation, waste valorization, and BSF growth dynamics.
4.2. Phosphorus and Potassium Accumulation in Frass Fertilizer as Influenced by
Environmental Factors
The observed adverse effect of air humidity on phosphorus accumulation in our study
might be attributed to its potential to limit microbial activity essential for nutrient miner-
alization and organic matter decomposition. Previous studies [39–41] have demonstrated
that the optimal air humidity range for BSFL typically falls within 40% to 70%. Thus,
deviations from this range can impact the nutrient cycling in the composting system. Sub-
optimal air humidity conditions may hinder the efficiency of microbial processes, leading
to decreased phosphorus mineralization and accumulation in the frass fertilizer. More-
over, Alanna and Cory [42] noted that humidity’s impact on reaction kinetics (for instance
mineralization), substrate temperature on reaction rates (for instance, phosphatase enzyme
activities), and moisture’s role in providing a conducive environment are crucial in the
composting process. The identified temperature of 33.5 ◦C to 36.5 ◦C aligns with the study

Sustainability 2024, 16, 3746
12 of 16
of Shah et al. [43], which noted that increasing temperature towards the thermophilic range
reduces microbial activities, especially bacterial ones. It should be noted that temperatures
above 35 °C are not favorable for BSF growth due to the effects on larval feeding and stress
that could lead to larval mortality. Furthermore, Eskander and Saleh [44] noted that high
temperatures enhance evaporation and reduce water availability in the substrate, which
consequently affects BSF feeding, and phosphorus release in the substrate. Therefore, ex-
tremely high temperatures lead to thermal stress, and in some cases result in toxicity, which
contributes to the decline or denaturation of phosphatase enzyme activities, which leads to
poor phosphorus accumulation.
It was also observed that the concentration of potassium is significantly influenced by
air humidity and substrate temperature. According to Van Looveren et al. [45], microbial
activities involved in composting, especially those driven by BSFL, are sensitive to air
humidity and substrate temperature, therefore making these factors critical in regulating
potassium accumulation. Furthermore, Van Peer et al. [46] mentioned that these factors
affect the bacteria population that supports the digestion and the potassium chloride
solution extraction in the composting process. Generally, the substrate temperature within
the optimal range for BSFL development likely contributes to increased metabolic activity,
which can positively influence the potassium composition [47].
4.3. Implications for Scaling of Frass Fertilizer Production Technologies
The results presented in the previous sections unravel the intricate relationships
among environmental variables and their significance in influencing nutrient content
in BSF frass fertilizer. The positive coefficients associated with these pivotal variables
underscore their direct (proportional relationships) effect on nutrient accumulation in frass
fertilizer. This notion aligns with the principles of continuous monitoring and precision
farming technologies advocated by Dinnes et al. [48], where sensors (monitoring) and
precision farming technologies play a crucial role in optimal frass fertilizer production.
Farmers can use enclosed structures greenhouses and insulating techniques to protect
against excessive sunlight and control air and substrate temperatures within acceptable
limits, as they are factors impacting nutrient yield in BSF production systems. The optimal
range of substrate moisture determined is comparable to the moisture content of commonly
organic substrates for BSF production and falls within ideal ranges for maximal nutrient
output. Therefore, BSF farmers will not incur costs of moisture optimization because
the available organic wastes already have optimal moisture levels. To further improve
conditions and raise the quality of frass fertilizer production, farmers can place a priority
on choosing a variety of nutrient-rich organic waste, optimize ventilation techniques for
aeration or oxygen availability, and consider the possibility of integrating intelligence
and sensors for real-time monitoring. For example, by prioritizing significant factors
(such as air temperature, moisture content, and substrate temperature as stated in this
research) that influence nitrogen accumulation, farmers can optimize the investment of the
aforementioned resources. This, however, has cost implications on insect farming and frass
fertilizer production. For the tropical regions where temperatures range between 25 and
35 °C for most of the year, there is little or no requirement for artificial heating since the
determined air temperature falls within the range of tropical region temperatures. This
will go a long way in reducing energy requirements for BSF production for farmers in
the tropical regions compared to counterparts in other parts of the world where artificial
heating is mandatory to maintain optimal temperatures for BSF waste bio-conversion.
The availability of favorable weather in the tropics is an incentive for increased adoption of
BSF and private sector investment in insect farming in Africa and other regions.

Sustainability 2024, 16, 3746
13 of 16
In essence, the results paint a portrait of the intricate relationships within the com-
posting system. This understanding of the impact of individual variables provides a road
map for practitioners seeking to harness the full potential of BSF-composted fertilizer.
Examining the results, stakeholders can adjust composting conditions to orchestrate an
environment conducive to optimal nutrient yield, thereby realizing both the agricultural
and environmental advantages of this sustainable waste-to-resource conversion process.
Optimizing nutrient content in compost translates to enhanced soil health and increased
agricultural productivity. This knowledge empowers agricultural stakeholders to opti-
mize composting processes, resulting in fertilizers enriched with sustenance and essential
nutrients for plant growth [49,50].
5. Conclusions
The optimization of organic fertilizer quality is key for sustainable soil health manage-
ment and crop productivity. We present an information system based on different sensing
capabilities, Internet of Things (IoT), and modeling application for insect frass fertilizer
production. We conclude that air humidity, air temperature (30–41.5 ◦C), moisture content
(70–80%), and substrate temperature (<35 ◦C) play a significant role in the accumulation of
nitrogen, phosphorous, and potassium in frass fertilizer products during waste recycling
using black soldier fly larvae. The development of a digital application to engage end users
and facilitate frass fertilizer quality assessment would ensure quality and enhance trans-
parency in the fertilizer supply chain, empowering farmers to make informed decisions
about the adoption of novel and sustainable fertilizer inputs for improved food security.
The research contributes to IoT-enabled agriculture, demonstrating the potential of digital
techniques in improving fertilizer nutrient management and facilitating informed decision-
making about soil amendments at the farmer level. This information and communication
technologies will enable the creation of low-cost, efficient information systems that can
improve resources management, and increase the productivity and sustainability of agri-
food systems. However, thorough evaluation of the developed device under large-scale
production systems would highlight the capabilities and advantages of the device over
existing traditional approaches of composting, demonstrating its potential to revolutionize
agricultural practices.
Author Contributions:
Conceptualization, M.K., K.S., E.R., D.B., C.M.T., G.A., T.Z., D.C., A.L.
and H.E.Z.T.; Methodology, M.K., K.S., E.R., D.B., C.M.T. and H.E.Z.T.; Software, M.K., K.S., E.R.,
D.B. and C.M.T.; Validation, M.K., K.S., E.R., D.B. and C.M.T.; Formal Analysis, M.K., K.S., E.R.,
D.B. and C.M.T.; Investigation, M.K., K.S. E.R., D.B. and C.M.T.; Resources, M.K., K.S., E.R., D.B.,
G.A., D.C., T.Z. and C.M.T.; Writing—Original Draft Preparation, M.K., K.S., E.R., D.B. and C.M.T.;
Writing—Review and Editing, M.K., K.S., E.R., D.B., C.M.T., G.A., T.Z., D.C., A.L. and H.E.Z.T.;
Visualization, M.K., K.S., E.R., D.B. and C.M.T.; Supervision, K.S., E.R., D.B. and C.M.T.; Project
Administration, K.S. D.B. and C.M.T.; Funding Acquisition, C.M.T., G.A., T.Z., D.C. and A.L. All
authors have read and agreed to the published version of the manuscript.
Funding: The authors gratefully acknowledge the financial support for this research by the following
organizations and agencies: Foreign, Commonwealth & Development Office (FCDO) [IMC-Grant
21108]; Australian Centre for International Agricultural Research (ACIAR) (ProteinAfrica—Grant No:
LS/2020/154), the Rockefeller Foundation (WAVE-IN—Grant No: 2021 FOD 030); Bill & Melinda
Gates Foundation (INV-032416); IKEA Foundation (G-2204-02144), Horizon Europe (NESTLER—Project:
101060762—HORIZON-CL6-2021- FARM2FORK-01), the Curt Bergfors Foundation Food Planet Prize
Award; Norwegian Agency for Development Cooperation, the Section for Research, Innovation and
Higher Education grant number RAF–3058 KEN–18/0005 (CAP–Africa); the Swedish International
Development Cooperation Agency (SIDA); the Swiss Agency for Development and Cooperation
(SDC); the Australian Centre for International Agricultural Research (ACIAR); the Norwegian Agency
for Development Cooperation (NORAD); the German Federal Ministry for Economic Cooperation
and Development (BMZ); the Federal Democratic Republic of Ethiopia; and the Government of the
Republic of Kenya. The funders had no role in study design, data collection and analysis, decision to
publish, or preparation of the manuscript.

Sustainability 2024, 16, 3746
14 of 16
Data Availability Statement: The data is available here [51].
Acknowledgments: The authors wish to thank Pan-African University for co-supervision of this work.
Conflicts of Interest: Authors Gina Athanasiou and Theodore Zahariadis were employed by the com-
pany Synelixis Solutions S.A. Authors Domenica Casciano and Alexandre Lazarou were employed
by the company Zanasi & Partners. The remaining authors declare that the research was conducted
in the absence of any commercial or financial relationships that could be construed as a potential
conflict of interest.
References
1.
Vlyssides, A.; Mai, S.; Barampouti, E. An integrated mathematical model for co-composting of agricultural solid wastes with
industrial wastewater. Bioresour. Technol. 2009, 100, 4797–4806. [CrossRef] [PubMed]
2.
Pant, R.; Gupta, A.; Singh, A.; Srivastava, S.; Patrick, N. A Summary of the Role of Microorganisms in Waste Management. In
Microbial Technology for Sustainable E-waste Management; Springer: Berlin/Heidelberg, Germany, 2023; pp. 337–352. [CrossRef]
3.
Oshins, C.; Michel, F.; Louis, P.; Richard, T.L.; Rynk, R. The composting process. In The Composting Handbook; Elsevier: Amsterdam,
The Netherlands, 2022; pp. 51–101. [CrossRef]
4.
Azis, F.A.; Choo, M.; Suhaimi, H.; Abas, P.E. The Effect of Initial Carbon to Nitrogen Ratio on Kitchen Waste Composting Maturity.
Sustainability 2023, 15, 6191. [CrossRef]
5.
Tumuhairwe, J.B.; Tenywa, J.S.; Otabbong, E.; Ledin, S. Comparison of four low-technology composting methods for market crop
wastes. Waste Manag. 2009, 29, 2274–2281. [CrossRef] [PubMed]
6.
Beesigamukama, D.; Mochoge, B.; Korir, N.K.; Fiaboe, K.K.; Nakimbugwe, D.; Khamis, F.M.; Subramanian, S.; Wangu, M.M.;
Dubois, T.; Ekesi, S.; et al. Low-cost technology for recycling agro-industrial waste into nutrient-rich organic fertilizer using black
soldier fly. Waste Manag. 2021, 119, 183–194. [CrossRef] [PubMed]
7.
Beesigamukama, D.; Tanga, C.M.; Sevgan, S.; Ekesi, S.; Kelemu, S. Waste to value: Global perspective on the impact of entomo-
composting on environmental health, greenhouse gas mitigation and soil bioremediation. Sci. Total Environ. 2023, 902, 166067.
[CrossRef] [PubMed]
8.
Tanga, C.M.; Kababu, M.O. New insights into the emerging edible insect industry in Africa. Anim. Front. 2023, 13, 26–40.
[CrossRef] [PubMed]
9.
Muinde, J.; Tanga, C.M.; Olukuru, J.; Odhiambo, C.; Tonnang, H.E.Z.; Senagi, K. Application of Machine Learning Techniques to
Discern Optimal Rearing Conditions for Improved Black Soldier Fly Farming. Insects 2023, 14, 479. [CrossRef] [PubMed]
10.
Qomi, M.F.; Danaeefard, M.; Farhang, A.; Hosseini, P.; Arast, Y. Effect of Temperature on the Breeding Black Soldier Fly Larvae
in Vitro for Basic Health-oriented Research. Arch. Hyg. Sci. 2021, 10, 67–74.
11.
Diener, S.; Zurbrügg, C.; Tockner, K. Conversion of organic material by black soldier fly larvae: Establishing optimal feeding
rates. Waste Manag. Res. 2009, 27, 603–610. [CrossRef] [PubMed]
12.
Beesigamukama, D.; Mochoge, B.; Korir, N.K.; Fiaboe, K.K.; Nakimbugwe, D.; Khamis, F.M.; Subramanian, S.; Dubois, T.;
Musyoka, M.W.; Ekesi, S.; et al. Exploring black soldier fly frass as novel fertilizer for improved growth, yield, and nitrogen use
efficiency of maize under field conditions. Front. Plant Sci. 2020, 11, 574592. [CrossRef] [PubMed]
13.
Oonincx, D.G.; van Broekhoven, S.; van Huis, A.; van Loon, J.J. Correction: Feed conversion, survival and development, and
composition of four insect species on diets composed of food by-products. PLoS ONE 2019, 14, e0222043. [CrossRef] [PubMed]
14.
Sánchez, Ó.J.; Ospina, D.A.; Montoya, S. Compost supplementation with nutrients and microorganisms in composting process.
Waste Manag. 2017, 69, 136–153. [CrossRef] [PubMed]
15.
Keener, H.; Ekinci, K.; Michel, F. Composting process optimization–using on/off controls. Compost Sci. Util. 2005, 13, 288–299.
[CrossRef]
16.
Petric, I.; Mustafi´c, N. Dynamic modeling the composting process of the mixture of poultry manure and wheat straw. J. Environ.
Manag. 2015, 161, 392–401. [CrossRef] [PubMed]
17.
Vasiliadou, I.A.; Chowdhury, A.K.M.M.B.; Akratos, C.S.; Tekerlekopoulou, A.G.; Pavlou, S.; Vayenas, D.V. Mathematical modeling
of olive mill waste composting process. Waste Manag. 2015, 43, 61–71. [CrossRef] [PubMed]
18.
Courvoisier, P.; Clark, G. A numerical integrated model of composting processes using finite elements methods. In Proceedings
of the XVII World Congress of the International Commission of Agricultural and Biosystems Engineering (CIGR), Québec City,
QC, Canada, 6 July 2010; pp. 1–10.
19.
Bongochgetsakul, N.; Ishida, T. A new analytical approach to optimizing the design of large-scale composting systems. Bioresour.
Technol. 2008, 99, 1630–1641. [CrossRef] [PubMed]
20.
Cheng, J.Y.; Chiu, S.L.; Lo, I.M. Effects of moisture content of food waste on residue separation, larval growth and larval survival
in black soldier fly bioconversion. Waste Manag. 2017, 67, 315–323. [CrossRef] [PubMed]
21.
Yang-Jie, D.; Xiang, F.M.; Tao, X.H.; Jiang, C.L.; Zhang, T.Z.; Zhang, Z.J. A full-scale black soldier fly larvae (Hermetia illucens)
bioconversion system for domestic biodegradable wastes to resource. Waste Manag. Res. 2023, 41, 143–154. [CrossRef] [PubMed]

Sustainability 2024, 16, 3746
15 of 16
22.
Stloukal, P.; Pekaˇrová, S.; Kalendova, A.; Mattausch, H.; Laske, S.; Holzer, C.; Chitu, L.; Bodner, S.; Maier, G.; Slouf, M.; et al.
Kinetics and mechanism of the biodegradation of PLA/clay nanocomposites during thermophilic phase of composting process.
Waste Manag. 2015, 42, 31–40. [CrossRef] [PubMed]
23.
Oudart, D.; Robin, P.; Paillat, J.; Paul, E. Modelling nitrogen and carbon interactions in composting of animal manure in naturally
aerated piles. Waste Manag. 2015, 46, 588–598. [CrossRef] [PubMed]
24.
Dickson, E.M.; Hastings, A.; Smith, J. Energy production from municipal solid waste in low to middle income countries: A case
study of how to build a circular economy in Abuja, Nigeria. Front. Sustain. 2023, 4, 1173474. [CrossRef]
25.
Vishwakarma, A.; Kanaujia, K.; Hait, S. Global scenario of E-waste generation: Trends and future predictions. In Global E-Waste
Management Strategies and Future Implications; Elsevier: Amsterdam, The Netherlands, 2023; pp. 13–30. [CrossRef]
26.
Haseli, G.; Torkayesh, A.E.; Hajiaghaei-Keshteli, M.; Venghaus, S. Sustainable resilient recycling partner selection for urban waste
management: Consolidating perspectives of decision-makers and experts. Appl. Soft Comput. 2023, 137, 110120. [CrossRef]
27.
Waqas, M.; Hashim, S.; Humphries, U.W.; Ahmad, S.; Noor, R.; Shoaib, M.; Naseem, A.; Hlaing, P.T.; Lin, H.A. Composting
processes for agricultural waste management: A comprehensive review. Processes 2023, 11, 731. [CrossRef]
28.
Zafaranlouei, N.; Ghoushchi, S.J.; Haseli, G. Assessment of sustainable waste management alternatives using the extensions of
the base criterion method and combined compromise solution based on the fuzzy Z-numbers. Environ. Sci. Pollut. Res. 2023,
30, 62121–62136. [CrossRef] [PubMed]
29.
Synnefa. 2023. Available online: https://www.synnefa.io/farmshield (accessed on 1 December 2023).
30.
Perry, L.A.; Montgomery, D.C.; Fowler, J.W. Partition experimental designs for sequential processes: Part I—First-order models.
Qual. Reliab. Eng. Int. 2001, 17, 429–438. [CrossRef]
31.
Bosque-Sendra, J.M.; Pescarolo, S.; Cuadros-Rodríguez, L.; García-Campaña, A.M.; Almansa-López, E.M. Optimizing analytical
methods using sequential response surface methodology. Application to the pararosaniline determination of formaldehyde.
Fresenius’ J. Anal. Chem. 2001, 369, 715–718. [CrossRef] [PubMed]
32.
Alin, A. Minitab. Wiley Interdiscip. Rev. Comput. Stat. 2010, 2, 723–727. [CrossRef]
33.
Padmanabha, M.; Kobelski, A.; Hempel, A.J.; Streif, S. A comprehensive dynamic growth and development model of Hermetia
illucens larvae. PLoS ONE 2020, 15, e0239084. [CrossRef] [PubMed]
34.
Vargas-García, M.; Suárez-Estrella, F.; López, M.; Moreno, J. Microbial population dynamics and enzyme activities in composting
processes with different starting materials. Waste Manag. 2010, 30, 771–778. [CrossRef] [PubMed]
35.
Mathur, S.P. Composting processes. In Bioconversion of Waste Materials to Industrial Products; Springer: Boston, MA, USA, 1998;
pp. 154–193. [CrossRef]
36.
MacDonald, N.W.; Zak, D.R.; Pregitzer, K.S. Temperature Effects on Kinetics of Microbial Respiration and Net Nitrogen and
Sulfur Mineralization. Soil Sci. Soc. Am. J. 1995, 59, 233–240. [CrossRef]
37.
Hu, X.; Zhang, Y.; Wang, D.; Ma, J.; Xue, K.; An, Z.; Luo, W.; Sheng, Y. Effects of Temperature and Humidity on Soil Gross
Nitrogen Transformation in a Typical Shrub Ecosystem in Yanshan Mountain and Hilly Region. Life 2023, 13, 643. [CrossRef]
[PubMed]
38.
Mosavian, S.N.; Eisvand, H.R.; Akbari, N.; Moshatati, A.; Ismaili, A. Do nitrogen and zinc application alleviate the adverse effect
of heat stress on wheat (Triticum aestivum L.)? Not. Bot. Horti Agrobot. Cluj-Napoca 2021, 49, 12252–12252. [CrossRef]
39.
Shumo, M.; Osuga, I.M.; Khamis, F.M.; Tanga, C.M.; Fiaboe, K.K.; Subramanian, S.; Ekesi, S.; van Huis, A.; Borgemeister, C. The
nutritive value of black soldier fly larvae reared on common organic waste streams in Kenya. Sci. Rep. 2019, 9, 10110. [CrossRef]
40.
Singh, A.; Marathe, D.; Kumari, K. Black Soldier Fly Hermetia illucens (L.): Ideal environmental conditions and rearing strategies.
Indian J. Entomol. 2022, 84, 743–753. [CrossRef]
41.
Mahmood, S.; Ali, A.; Zurbrügg, C.; Dortmans, B.; Asmara, D.R. Rearing performance of black soldier fly (Hermetia illucens) on
municipal biowaste in the outdoor ambient weather conditions of Pakistan and Indonesia. Waste Manag. Res. 2023, 41, 644–652.
[CrossRef] [PubMed]
42.
Alanna, N., S.; Cory, C., C. The effects of temperature on soil phosphorus availability and phosphatase enzyme activities: A
cross-ecosystem study from the tropics to the Arctic. Biogeochemistry 2020, 151, 113–125. [CrossRef]
43.
Shah, P.N.; Ruan, X.; van Loon, J.J.; Dicke, M. Temperature-modulated host-pathogen interactions between Hermetia illucens
L.(Diptera: Stratiomyidae) and Pseudomonas protegens Pf-5. J. Invertebr. Pathol. 2023, 198, 107934. [CrossRef] [PubMed]
44.
Eskander, S.; Saleh, H. Biodegradation: Process mechanism. Environ. Sci. Eng. 2017, 8, 1–31.
45.
Van Looveren, N.; Vandeweyer, D.; Van Campenhout, L. Impact of Heat Treatment on the Microbiological Quality of Frass
Originating from Black Soldier Fly Larvae (Hermetia illucens). Insects 2022, 13, 22. [CrossRef] [PubMed]
46.
Van Peer, M.; Coudron, C.; Alvarez, C.; Kingston-Smith, J.A.A.; Van Miert, S. Literature Review to Define Knowledge Gaps on the
Sustainable Production of Insects for Feed; European Union: Maastricht, The Netherlands, 2022.
47.
Mulu, D.; Yimer, F.; Opande, G. Characterizing quality of frass produced by black soldier fly (Hermetia illucens) larvae after
treating water hyacinth and fruit wastes in various proportions. Biomass Convers. Biorefinery 2023, 13, 15185–15196. [CrossRef]
48.
Dinnes, D.L.; Karlen, D.L.; Jaynes, D.B.; Kaspar, T.C.; Hatfield, J.L.; Colvin, T.S.; Cambardella, C.A. Nitrogen management
strategies to reduce nitrate leaching in tile-drained Midwestern soils. Agron. J. 2002, 94, 153–171. [CrossRef]
49.
Sanginga, N.; Woomer, P.L. Integrated Soil Fertility Management in Africa: Principles, Practices, and Developmental Process; CIAT:
Palmira, Colombia, 2009.

Sustainability 2024, 16, 3746
16 of 16
50.
Gebbers, R.; Adamchuk, V.I. Precision agriculture and food security. Science 2010, 327, 828–831. [CrossRef]
51.
Katchali, M.; Senagi, K. Frass Fertilizer Production. Available online: https://dmmg.icipe.org/dataportal/dataset/unveiling-
environmental-influences-on-sustainable-fertilizer-production-through-insect-farming (accessed on 1 January 2024).
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.