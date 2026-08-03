<!-- image -->

<!-- image -->

## OPEN ACCESS

```
EDITED BY Jun Wang, Jiangsu University of Science and Technology, China REVIEWED BY Xingliang Wang, Nanjing Agricultural University, China Elsje Pieterse, Stellenbosch University, South Africa Michael Ackah, Jiangsu University, China *CORRESPONDENCE Stefan Streif, stefan.streif@etit.tu-chemnitz.de RECEIVED 21 March 2024 ACCEPTED 26 April 2024 PUBLISHED 22 May 2024 CITATION Kobelski A, Hempel A-J, Padmanabha M, Klüber P, Wille L-C and Streif S (2024), Modelbased process optimization of black soldier fl y
```

egg production. Front. Bioeng. Biotechnol. 12:1404776. doi: 10.3389/fbioe.2024.1404776

## COPYRIGHT

©2024Kobelski, Hempel, Padmanabha, Klüber, Wille and Streif. This is an open-access article distributed under the terms of the Creative CommonsAttribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these

terms.

## [Model-based process optimization of black soldier fl y egg production](https://www.frontiersin.org/articles/10.3389/fbioe.2024.1404776/full)

Alexander Kobelski 1 , Arne-Jens Hempel 1,2 , Murali Padmanabha 1 , Patrick Klüber 3 , Luiz-Carlos Wille 1 and Stefan Streif 1,3 *

1 Automatic Control and System Dynamics Lab, Technische Universität Chemnitz, Chemnitz, Germany, 2 Lab for Digital Engineering, Staatliche Studienakademie Glauchau, Glauchau, Germany, 3 Fraunhofer Institute for Molecular Biology and Applied Ecology, Department of Bioresources, Gießen, Germany

Black soldier fl y (BSF) larvae ( Hermetia illucens ) serve as a valuable protein source for animal feed. Limiting factors in the industrial rearing of BSF are the reproduction process and egg output. Studies indicate the potential to shorten preoviposition time and increase egg output through better utilization of environmental variables, such as temperature and light, in industrial settings. Excessive stimulation, however, can lead to stress, elevated production costs, and reduced egg numbers, emphasizing the need for a delicate balance. This study addresses these challenges by investigating controlled manipulation of environmental variables to stimulate mating and enhance egg production, thereby developing a comprehensive model encompassing the adult fl y life cycle, mating, and egg production. Model parameters were fi tted using literature data, and the model ' s plausibility was tested through simulations. Using the model and optimal control methods, the calculated dynamic trajectories for environmental variables when compared to the standard approach in a constant environment demonstrated higher output and shorter production cycles at reasonable energy costs. Applications for this model-based optimization are demonstrated for various scenarios, highlighting the practical utility and versatility of the developed model. This study contributes valuable insights for improving rearing practices of BSF through environmental stimulation, offering potential advancements in egg production ef fi ciency and overall sustainability.

## KEYWORDS

black soldier fl y (BSF), insect rearing, reproduction, egg production, control, modeling, automation

## 1 Introduction

Mass production of insects is a relatively young but rapidly evolving industrial sector which shows great potential for both standalone and circular production of high value proteins (Francuski and Beukeboom, 2020; Chavez, 2021). Efforts to understand and enhance mass rearing typically focus on investigating the effects of fi xing parameters such as feed or temperature at a constant level (Nayak et al., 2024). While some aspects of automation have been investigated (Kröncke et al., 2020), there is limited work on dynamic modeling of insect rearing and subsequent dynamic process optimization and control Padmanabha et al. (2023).

Insect proteins from the black soldier fl y (BSF) Hermetia illucens are a promising alternative to conventional animal proteins. The BSF larvae can feed on a variety of substrates such as animal feed, algae, or waste (Liland et al., 2017), which makes their rearing less dependent on global trade fl uctuations. Surendra et al. (2020) hypothesized that insects can be used to achieve waste-free production cycles that enable more sustainable food production. The dried larvae are rich in protein (Spranghers et al., 2017) and can be used as supplements for animal rearing and aquaculture (Liu et al., 2017). However, the fl exibility of the feed leads to challenges in process planning -both in the larval and fl y stage -as the development speed, fl y life span, egg production potential, etc. depend on it. While substantial efforts have been directed towards understanding the rearing process of the larvae (Bava et al., 2019; Padmanabha et al., 2020; Yakti et al., 2022), it is noteworthy that the reproductive processes of matured fl ies have not received the same degree of attention.

<!-- image -->

The production of eggs and young larvae often imposes a bottleneck on the maximum rearing capacities of a production site (Klüber et al., 2023). In standard practice, the fl ies will often sit idly in their cages without mating, wasting precious resources. However, the mating and oviposition process can be in fl uenced through various controllable variables, such as light or temperature (Tomberlin and Sheppard, 2002; Zhang et al., 2010). At the same time, unnecessary movement and stress will drain the fl ies ' energy reserves, resulting in reduced life spans and fecundity (eggs per female). Optimizing egg production with minimized stress and energy costs while maximizing egg output necessitates a systematic control approach.

In this study, we present a process-control-oriented model designed to automate environment stimulation and to optimize the egg production process of the BSF. First, the fl y life cycle, the mating process, and the egg production were analyzed and abstracted into mathematical models. The impact of control variables, including temperature and light, was systematically modeled. Model parameters were fi tted to data available in literature and the model was tested for plausibility. Subsequently, a time-varying optimal control sequence for light, and temperature was computed for various scenarios. Simulation results were compared to a standard approach in which environmental conditions were kept at constant levels and the advantages of optimal control in egg production were highlighted. This work addresses issues in rearing ef fi ciency, and process automation, thus improving economic viability of insect protein production.

## 2 Materials and methods

## 2.1 Modeling fl y life cycle, mating, egg production, and death

This section introduces a comprehensive mathematical model for the adult fl ies ' life cycle from eclosion to adulthood while also considering oviposition processes. Controllable environmental variables such as light and temperature were incorporated, in recognition of their in fl uential roles in the process. Figure 1 depicts the model dynamics in a forrester diagram. The parts of the model -fl y life cycle and life stage dynamics, egg production, survival on energy reserves, and environmental impact factors -were derived individually and would be combined in Section 2.1.4. Model equations were mostly formulated in a mechanistic way to allow for physical interpretation of equations. A continuous state model that works with population averages was used since data for modeling probabilistic and discrete events (like individual fl y death) are scarce. Additionally, the chosen modeling approach greatly reduces complexity for simulation and optimization.

The considered reproduction setup was a breeding cage with a certain number of male and female pupae placed within. Gobbi et al.

TABLE 1 List of parameters with source of data used for parameter fi tting. Aiming for consistency across various fi ndings, data from multiple authors were used for the development sums. When using data from (Chia et al., 2018), only data in the range of 20 -37 ° C were used. Refer to Section 3.1.1 for more details.

| Category                 | Parameters         | Parameters              | Parameters              | Data from                                  |
|--------------------------|--------------------|-------------------------|-------------------------|--------------------------------------------|
| life stage dynamics      | k y2act 0.28 d - 1 | k act2fert 0.62 d - 1   | k fert2old 0.55 d - 1   | Nakamura et al. (2016)                     |
| development sums         | k T Σ min 12 ° C   | k Σ y2act 28 ◦ Cd       | k Σ ovi 56 ◦ Cd         | various                                    |
| oviposition              | k ovi 5.9 mg d - 1 |                         |                         | Nakamura et al. (2016)                     |
| μ related                | k μ 0.0183 d - 1   | k μ ,old 2.14 d - 1     | k μ ,ovi 2.5            | Nakamura et al. (2016), Chia et al. (2018) |
| light on mating chance   | a 1 0.986          | a 2 0.368 d h - 1       |                         | Hoc et al. (2019)                          |
| temperature on fecundity | k T,ovi,0 - 3.17   | k T,ovi,1 0.286 K - 1   | k T,ovi,2 - 0.005 K - 2 | Chia et al. (2018)                         |
| temperature on μ         | k T, μ ,0 3.13     | k T, μ ,1 - 0.166 K - 1 | k T, μ ,2 0.0033 K - 2  | Chia et al. (2018)                         |

(2013) reported a female bias in Hermetia ; however, male fl ies can mate with multiple females and therefore no limiting effects would be observed in such unevenly distributed populations. While a percentage of fl ies could have been infertile or have lifethreatening deformations, e.g., wing damage during emergence, such events were neglected and not included in the model. Under the previous assumptions, only the number of female fl ies N was relevant for egg production. Hence, male fl ies were not modeled, which reduced model complexity without losing plausibility (or predictive capabilities). At harvest, eggs are collected and taken out of the system; no new pupae or fl ies are introduced during a reproduction cycle. The basic structure for the adult fl y life cycle is a life-stage model. The four life stages are introduced in the following paragraph.

## 2.1.1 Fly life stages and life stage dynamics

The process starts when pupae are introduced into the breeding cage and ends either when all fl ies are dead or when the operator decides that too few eggs are produced. The four fl y life stages are ' young ' , ' active ' , ' fertilized ' , and ' old ' . Flies are categorized as ' young ' ( N y) from the time of their introduction to the system as pupae and continue to be classi fi ed as such even after hatching. This classi fi cation extends throughout the period during which they unfold their wings, and undergo exoskeleton hardening persisting until mating occurs. After the young fl y stage comes the sexually ' active ' stage N act , where fl ies actively search for mating partners. A fraction of the population then has a chance to become fertilized, N fert . Fertilized fl ies actively contribute to the egg production process, and once they have completed oviposition, they transition into the ' old ' category ( N old ).

The pupae placed in the breeding cage do not have the exact same life history, e.g., age, genetics, etc. While, for the individual fl y, transition to the next life stage happens instantaneously, for the fl y population in the breeding cage -due to their variations in life history and stochastics during mating -this is a gradual process. The rate of change was modeled as an ordinary differential equation (ODE)

<!-- formula-not-decoded -->

in which the dot notation was used to represent derivatives with respect to time. Parameter values for k y2act can be found in Table 1 and k μ ,N = 1 d -1 . The dying rate μ is introduced in the next section.

The fl ies undergo certain internal development processes which result in time delays between hatching and mating, and fertilization and oviposition (Tomberlin and Sheppard, 2002). Chia et al. (2018) have found that temperature strongly impacts the time from emergence to oviposition which suggests that both time and temperature should be considered for development and stage transitioning. For this, now introduced development sums T Σ

<!-- formula-not-decoded -->

with T as the temperature in the breeding cage and k T Σ min as a threshold temperature below which development halts. The transition rates would be only activated once a minimum amount of development sums (i.e., threshold values) had accumulated

<!-- formula-not-decoded -->

where ' sw ' is a switch function de fi ned as follows

<!-- formula-not-decoded -->

with k Σ y2act and k Σ ovi being threshold values for mating behavior and oviposition, respectively. See Section 2.3.1 and Supplementary Material for a smooth implementation of max and sw functions to improve numerics. The next sections discusses fl y dying rate and egg production.

## 2.1.2 Energy reserves, fl y survival, and egg production

The diet during the larval stage allows the fl ies to accumulate energy reserves (Gobbi et al., 2013), predominantly in the form of the so-called fat body. These energy reserves play a crucial role in determining both the remaining life span and the potential for egg production in the fl ies (Hall and Gerhardt, 2002). As the energy reserves diminish, the dying rate μ would increase at a rate of k μ

<!-- formula-not-decoded -->

When μ = 0, this means most reserves are used up, and the fl ies begin to starve, risking death. In reality, there may have been early deaths due to problems during emergence or hardening of the chitin carapace, or when trying to unfold their insect wings. However, this was unrelated to μ and the choice of environment conditions for egg production optimization.

Neglecting such premature deaths, there isa delay before the fi rst fl y deaths start occurring -depending on initial weight and breeding cage setup, e.g., temperature and availability of nourishing fl uids (Nakamura et al., 2016; Bertinetti et al., 2019; Macavei et al., 2020). One approach to model this phenomenon, similar to how changes in behavior for mating and ovipositing were handled, would be to use switch functions and development sums. However, employing such methods could have compromised the mechanistic interpretability of the model when explaining how access to water or nutrient-rich fl uids impacted fl y lifespan. Alternatively, a more interpretable method would involve working with the initial value μ ( t = 0) = μ 0. While μ was initially introduced as the dying rate, an alternative interpretation would be to view it as the proportion of energy reserves already consumed by the fl y relative to a fl y on the verge of starvation (i.e., μ = 0). Negative values of μ signify the presence of remaining energy reserves, while values greater than zero indicate that the fl ies are in a state of starvation (and consequently at risk of dying). It is important to note that μ is an abstract variable and cannot be directly measured. However, its effects can be readily observed by monitoring when and how many fl ies perish. The initial value μ 0 is in fl uenced by the wellbeing and accumulated reserves (i.e., weight) during the larval stage (see Section 2.2 for our parameter fi tting approach).

As seen in Eq. 1, fl ies die at a rate of -k μ ,N μ N . However, negative values of μ would lead to an increase of population, which cannot happen in reality. That is why the dying term -k μ ,N μ N needed be modi fi ed such that population would not increase for negative μ , i.e.,

<!-- formula-not-decoded -->

In the adult stage, due to their mouth physiology, the fl ies can only consume fl uids and no solids (Bruno et al., 2019). Consuming fl uids like water, nectar, or milk slows down decay of energy reserves and increases egg production (Bertinetti et al., 2019; Bruno et al., 2019; Klüber et al., 2023). To accommodate for feeding, Eq. 3 could be extended with a positive term that is added and therefore slows down the decay of energy reserves. However, the purpose of this model is to calculate dynamic trajectories for environmental factors. Choosing a fl uid to constantly supply the fl ies with does not require such sophisticated methods. This concludes the description of the dynamics of μ .

As previously stated, μ in fl uences the potential for egg production, which can be described with

<!-- formula-not-decoded -->

where k ovi is a constant for egg production per fertilized fl y and k μ ,ovi adjusts how the energy reserves impact egg production. It can be seen that bigger larvae and fl ies (i.e., negative μ 0 ) result in higher egg mass. This also means that the less energy fl ies spend before ovipositing, the more eggs they can produce. In a study by Tomberlin and Sheppard (2002), it was hypothesized that females may reabsorb oocytes to maintain respiration, resulting in reduced egg clutch size. Keeping stress levels and unnecessary movement to a minimum enhances production potential.

Nakamura et al. (2016) found that fl ies that do not mate lived signi fi cantly longer, suggesting that the search for a mating partner and oviposition were the biggest energy drains for the fl ies. To model the fl ies dying faster after oviposition, the dying rate was multiplied by a factor k μ ,old .

FIGURE 2

<!-- image -->

Data showing normalized egg mass from (Hoc et al., 2019). Model fi t shows response of ξ L ( u L ).

The upcoming section explores how environmental variables, including temperature and light, in fl uence fl y behavior.

## 2.1.3 Factors in fl uencing the life cycle of adult fl ies

Recall that the aim is optimization of BSF egg production by controlling certain environmental variables, as previously illustrated in Figure 1. The three most in fl uential factors during the life of the fl y are temperature, lighting, and access to nutrient rich liquids (Holmes et al., 2012; Chia et al., 2018; Bertinetti et al., 2019; Hoc et al., 2019; Nayak et al., 2024). Relative humidity of air impacts multiple life history traits, including development speed (Holmes et al., 2012). However, data on the effect of relative humidity on mating behavior were insuf fi cient for modeling. Results of (Holmes et al., 2012) suggests that relative humidity should be kept suf fi ciently high and at a constant level. Thus, dynamic trajectories of humidity do not seem to have any optimization potential and will not be modeled.

For the in fl uence of light ξ L the control variable is u L, i.e., light hours per day. Only white light was considered, and the effects of different wave lengths and light intensities were neglected. Hoc et al. (2019) found that more light hours per day increase the amount of eggs harvested. The reason is that the chance of fi nding a partner for mating is enhanced (Jones and Tomberlin, 2021). Data from (Hoc et al., 2019) were used to fi t a model of the form

<!-- formula-not-decoded -->

where a 1 and a 2 are parameters. Parameter values were determined from data (see Figure 2 and Table 1; Section 2.2).

Temperature in fl uences three properties of fl y life: lifespan, fecundity, and life stage transition speed. The concept of development sums already encompasses the transition speed, as higher temperatures contribute to the accelerated accumulation of T Σ , resulting in earlier sexual activity and oviposition.

Chia et al. (2018) found that fecundity (i.e., number of unfertilized eggs per female) is signi fi cantly affected by temperature. A 2 nd order polynomial was found to be a good fi t:

FIGURE 3 (A) Data showing normalized egg mass from (Chia et al., 2018). Model fi t shows response of ξ T,ovi ( u T). (B) Data showing normalized fl y life duration from (Chia et al., 2018). Model fi t shows response of ξ T,mu ( u T).

<!-- image -->

<!-- formula-not-decoded -->

with k T,ovi being the respective polynomial coef fi cients and u T being the controllable temperature inside the breeding cage (see Figure 3A).

Chia et al. (2018) also found that longevity is signi fi cantly affected by temperature. A 2 nd order polynomial was found to be a good fi t:

<!-- formula-not-decoded -->

Fitting results can be seen in Figure 3B.

## 2.1.4 Combined model

The combined model includes the in fl uence of u T and u L and the cross dynamics between T Σ and Ni as well as μ and m e :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.2 Parameter fi tting

Parameters were fi tted to data using functions from MATLAB (r2022a) on a standard desktop PC. Initially, development sum dependent stage transition parameters were identi fi ed using linear regression. Next, base parameters (i.e., ξ T = ξ L = 1) for life stage transition dynamics, oviposition, and dying rate were identi fi ed by minimizing the difference between simulation results and data from literature using lsqcurvefit . Polyfit was used to fi t a parabola for ξ T,ovi and lsqnonlin to fi t ξ L. Finally, similar to the base parameters, ξ T, μ was identi fi ed by minimizing the difference between simulation results and literature data. The source of data used for each identi fi cation step is described in Table 1, and fi tting results are shown in Section 3.1.1 and Figure 2 as well as 3.

The starting value for dying rate μ 0 could not be determined through measurements but instead had to be chosen in accordance with model assumptions and boundary conditions. As was explained during modeling, μ 0 is negative because there is a delay between emergence and fi rst death. Next, we know that -neglecting deaths due to accidents during emergence -fi rst fl ies start dying after ≈ 7 days (Nakamura et al., 2016). Lastly, data from (Nakamura et al., 2016) indicated that the dying rate after 14 days should be μ ≈ 0.15 days -1 . With these three conditions, the starting value was chosen to be -0.1, and parameters were fi t accordingly.

## 2.3 Simulation and optimization of egg production

In this section, the framework for simulation and optimization of the egg production process is described. This includes explanation of the method, process constraints, and other criteria. Simulations, parameter fi tting, and optimization were all performed in MATLAB (r2022a) (The MathWorks, 2022).

## 2.3.1 Simulation framework

Eqs 9 -15 describe a system of (non-stiff ordinary) differential equations. Integrator cvodes from CasADi Matlab toolbox (Andersson et al., 2019) was used for numeric integration using the backward differentiation formula (BDF). Step size was 1 h, and simulation time was 14 d to re fl ect typical production times. The sw and max functions used in, e.g., Eqs 2, 4, respectively, caused numerical dif fi culties during optimization, which is why they were instead implemented through a tangent hyperbole function ( 1 2 + 1 2 tanh ( kx )) , where x is a state variable and k was chosen to be large enough to make the tanh steep (see Supplementary Figures S1, S2).

For the population Ni , all states except N y were zero, since pupae are only introduced to the system in the beginning. The number of young fl ies at the beginning was set to 50 to ensure simulation results were comparable with data from (Nakamura et al., 2016). Egg mass in the beginning was zero. Development sums were zero as well, since, after emergence, a new life stage starts, and it was assumed that temperature history during pupae stage would not in fl uence the life of the fl y. The starting value for dying rate was μ 0 = -0.1 as explained in Section 2.2. Standard environment conditions were taken from Nakamura et al. (2016) with u T = 25 ° C and u L = 16 h d -1 .

## 2.3.2 Optimization approach, framework, and variables

The model detailed in the preceding sections was formulated with the objective of optimizing egg production. This was achieved through the manipulation of environmental process parameters, speci fi cally temperature and daily light exposure hours. A model-based optimization approach was used to fi nd optimal trajectories for u T and u L. The CasADi Matlab toolbox was used for the implementation of the optimization algorithm (Andersson et al., 2019). Lower and upper bounds for u T were chosen as 20 ° C and 37 ° C, respectively, under consideration of data from (Chia et al., 2018). The upper bound for u L was 24 h d -1 , and the lower bound was chosen as 2 h d -1 as the minimum stimulus required to keep fl ies alive (Nakamura et al., 2016; Hoc et al., 2019). Interior point optimizer ( ipopt ) was used as the solver, which utilizes gradients and Hessians obtained through symbolic and automatic differentiation (Wächter and Biegler, 2006). Input trajectories were discretized into 1 hour intervals. Time horizon for optimization was t end = 14 d to re fl ect typical production times.

## 2.3.3 Optimization aim

To maximize egg output m e with minimal effort, i.e., minimize input u ∈ { u T, u L}, the optimization problem was formulated as follows

<!-- formula-not-decoded -->

with weights R and Q . Acommon approach for choosing the weights is to abstract them into money, i.e., costs per kilo watt hour and pro fi t per milligram egg mass. However, since those prices vary vastly by countries, a different approach was chosen here. Note that the optimization method and cost function were formulated in a generalized manner, allowing for easy adaptation if economic parameters are available. Instead, weights were chosen such that both m e and u have similar importance. From simulations, we know the expected value of m e ( t end ) ≈ 300 mg, while u ranges between low single to double digits. Thus, for equal weighing, the ratio should be R / Q ≈ ! 10. Based on systematic testing, we chose Q = 12 mg -1 and R = 100 I 2 (units omitted).

The cost function awarded egg mass at every time step instead of only fi nal mass at the end of production cycle t end. That way, the optimization calculated a trajectory that balances maximum output and production speed.

## 3 Results and discussion

Parameter fi tting results are explained, and the plausibility of the theoretical model is assessed. Afterwards, optimization is evaluated in various scenarios.

## 3.1 Simulation studies and comparison to literature data

Model performance was evaluated by comparing simulation results with data from literature. However, the scarcity of available data and substantial variations in experimental setups among different authors posed challenges for parameter identi fi cation and model validation. Differences during the larval rearing stage can especially in fl uence adult fl y performance, including longevity and fecundity. However, we assumed that, regardless of life history before pupation, the fl ies ' responses to environmental variables are the same. Thus, computed control trajectories would improve egg production even under parameter uncertainties.

## 3.1.1 Plausibility of environment impact

Data from Hoc et al. (2019) were utilized to calibrate the light impact component from Eq. 6 (see Figure 4A). The model predicted that egg production would be reduced by 19% when u L is decreased from 16 to 6 h d -1 and by 53% from 16 to 2 h d -1 . These predictions aligned well with the provided data and were consistent with observations reported by Liu et al. (2021).

For the impact of temperature on fecundity, Eq. 7, data from (Chia et al., 2018) were used (see Figure 4B). The model predicted highest fecundity at 28.6 ° C and a signi fi cant drop for temperatures above 35 ° C, which agreed well with (Chia et al., 2018; Shumo et al., 2019).

No data were found that describe the impact of temperature on the time period from emergence until fi rst mating behavior occurs, but (Tomberlin and Sheppard, 2002) reported this to be approximately 2 days. Due to the lack of data, parameter k Σ y2act was decided to be half of k Σ ovi (preoviposition period). Chia et al. (2018) investigated the in fl uence of temperature on the preoviposition period; however, their fi ndings con fl icted with other authors. While Chia et al. (2018) found mean preoviposition time to be above 9 days at both 25 and 30 ° C, other authors report periods of 3 -5 days (Tomberlin and Sheppard, 2002; Nakamura et al., 2016; Heussler et al., 2018; Hoc et al., 2019; Liu et al., 2021). We chose the parameters in such a way that the model produced plausible results. Little data was found on the exact minimum required temperature k T Σ min for development, but (Chia et al., 2018) reported that development still occurred at 15 ° C. The parameter k T Σ min was chosen as 12 ° C such that the model produced plausible results.

Fitting parameters for Eq. 8 was challenging since μ cannot be directly measured. The parameters had to be indirectly inferred by observing longevity at different temperatures. Experiments conducted by Chia et al. (2018) provided relevant data; however, their fi ndings con fl icted with observations from other authors. For instance, while Nakamura et al. (2016) reported longevity to be around 18 d at 25 ° C (with distilled water provided to fl ies), data from Chia et al. (2018) indicated a longevity of around 14 days at the same temperature (with sugar water provided) -a notable discrepancy. It is important to note that mating behavior and oviposition also indirectly in fl uence longevity. Higher temperatures accelerated the development time, causing fl ies to lay eggs earlier -a highly energy-consuming process that can reduce the overall lifespan. Nakamura et al. (2016) reported that female fl ies in separated colonies lived up to 47.6 d when provided with sugar water. It cannot be distinguished if decreases in longevity at higher temperatures were due to earlier oviposition or due to increased energy consumption from higher fl y activity. Experiment setups between authors differed greatly; feeding during larval rearing stage, fi nal pupae weight, population genetics, liquid feed provided during adult stage, etc. all impact longevity, which made fi nding general parameters that robustly predict longevity impossible. Parameters were chosen again for plausibility (see Figures 4C,D).

FIGURE 4 Change in fl y performance in dependence of environment parameters. (A) Egg production is reduced by 10% when going from 16 to 6 h d -1 . However, at 2 h d -1 , egg production is reduced to 51% of maximum value. (B) Fly fecundity peaks at 28.6 ° C and is reduced by 23% at 35 ° C. (C) Longevity (i.e., when population reaches 5% of its starting value). is longest at 24 ° C and is reduced by 3.5 d ( ≈ 29%) at 35 ° C. (D) Fly dying rate increases most slowly at 24 ° C, but grows 42% faster at 35 ° C.

<!-- image -->

## 3.1.2 Simulation studies 3.1.2.1 Standard conditions

Figure 5 shows simulation results of the model under standard conditions. For N and m e, root mean squared errors were 1.1 and 8.6 mg, respectively. Furthermore, a visual comparison of both total fl y population and egg production to data from (Nakamura et al., 2016)

indicated a reasonably good fi t. Our model did not predict individual fl ies dying after only 3 days; it is possible that individual pupae in the experiments of Nakamura et al. (2016) suffered from malnutrition, were sick, or damaged themselves during emergence. Final egg mass of the simulation overshot data by 0.15%. Egg production in the beginning seemed to be delayed in comparison to the data; the reason might be because the model for preoviposition time ( k Σ ,ovi ) was fi tted to data from a multitude of authors. This delay can also explain why egg mass in experimental data reached its peak faster than model predictions and why model predictions of N were slightly off around day 7 (earlier oviposition results earlier deaths). Overall, the simulation results indicated a plausible model for standard conditions.

## 3.1.2.2 Non-standard environment conditions

The model was controlled dynamically through environment variables u L and u T. To better understand how the model behaved in response to different inputs, see simulation results in Figure 6 or Supplementary Figure S3. Egg production and longevity were investigated at three different light input levels and over a range of temperatures.

<!-- image -->

<!-- image -->

Highest longevity was found at 22 ° C. At u L = 2 h d -1 , longevity decreased by 25% (12.4 d -9.3 d) from u T = 22 ° C to 37 ° C. At u T = 22 ° C longevity decreased by 2% (12.4 d -12.1 d) from u L = 2 h d -1 to 16 h d -1 . Impact of u L on longevity was negligible. This agreed with (Liu et al., 2021), who found that the survival rate after 10 d did not differ signi fi cantly with changes in light regime.

Highest egg production occurred at u L = 16 h d -1 and u T = 28 ° C with 348 mg. It decreased by 52% (167 mg) and 54% (157 mg) at 37 ° C and 20 ° C, respectively. At u T = 28 ° C, egg production decreased by 2% (348 mg -341 mg) from u L = 16 h d -1 to 6 h d -1 and by 17% (348 mg -298 mg) from u L = 16 h d -1 to 2 h d -1 . Results were compatible with the fi ndings of (Hoc et al., 2019).

First oviposition occurred after 2.46 d at 35 ° C, while at 30 and 25 ° C it occurred after 3.1 and 4.3 d, respectively. This agreed well with data from (Bertinetti et al., 2019; Binsin et al., 2023).

In the range of reasonable inputs, the model delivered plausible predictions and was sensitive to changes in control variables. Note how longevity, fecundity, and development speed all have their maximum at different temperatures. These differences were the reason why temperature trajectories have high potential for egg production optimization compared to constant temperatures. The optimization potential is explored in the following section.

## 3.2 Results of optimal control

## 3.2.1 Optimization potential

Higher temperature increased the development speed of the fl ies, i.e., oviposition occurs sooner, which is bene fi cial in industrial production. Simultaneously, increased fecundity is observed at higher temperatures. This came at the price of higher operation costs and accelerated dying rate. However, keeping dying rate μ low increased egg production. This resulted in con fl icting requirements for T Σ , ξ T,mu, and ξ T,ovi with concern to u T.

<!-- image -->

TABLE 2 Accumulated inputs and fi nal egg mass when abort criterium of m egg &gt; 0.9 m e ( t end) was violated.

|              | Σ u T    |   Σ u L (h) |   Time (d) |   m e (mg) |
|--------------|----------|-------------|------------|------------|
| benchmark    | 270 ◦ Cd |         173 |       10.9 |        284 |
| optimization | 281 ◦ Cd |         101 |        9.9 |        311 |

Changing u L did nothing while there were no active fl ies, and, therefore, light hours should be kept short at the beginning of the reproduction cycle.

Certain assumptions and simpli fi cations were made while modeling. As previously mentioned, relative humidity, choice of liquid food supplements, population density, and light quality parameters such as wave length spectrum and intensity can impact the egg production process (Klüber et al., 2020; Nayak et al., 2024). However, there are -to our knowledge -no dynamic effects to these process parameters. It thus suf fi ced to make a choice at the beginning and to keep those parameters constant.

Another simpli fi cation was that, while fecundity (number of eggs laid per female) was modeled, fertility (number of fertilized eggs) and hatchability (portion of fertilized eggs that survive and become larvae) were neglected. It is important to recognize that an increase in fecundity might not necessarily lead to a proportional increase in the number of hatched larvae if optimal temperatures for fecundity, fertility, and hatchability differ. This implies that optimizing the process solely based on fecundity may yield suboptimal results for the reproduction of larvae.

Another necessary simpli fi cation was that dynamic effects (i.e., long term effects) had to be neglected due to lack of information. For instance, exposure to high temperatures during the early stage (for accelerated development) might in fl uence fecundity in the fertile stage. Additionally, there is a question of de fi ning temperature in this context -whether it refers to the currently measured temperature, the average temperature, or the highest temperature since emergence.

## 3.2.2 Standard scenario

The benchmark scenario was chosen similar to (Nakamura et al., 2016) with 16 h d -1 and constant 25 ° C. Process optimization was performed according to Eq. 16. Resulting state trajectories can be seen in Figure 7.

Comparison of states shows that, while fl y population declined faster, the amount of eggs per cycle increased by 9.4% after 14 d (benchmark 315.2 mg versus optimized 345.2 mg). The shorter life cycle was a result of faster transition between life stages due to higher temperature at early stages. Flies reached sexual maturity faster but also burn their energy reserves faster. Shorter life cycles, however, mean that breeding cages can be re fi lled more often, resulting in more cycles and consequently higher egg production per time.

A production cycle abort criteria of 90% of predicted maximum egg mass was de fi ned. With that, Table 2 shows results on how much production could be improved through optimization. While the total energy invested into heating was 3.7% higher, light input was reduced by 41.4%, cycle time was reduced by 1 d and egg production was increased by 9.4%.

<!-- image -->

<!-- image -->

<!-- image -->

## 3.2.3 High penality for inputs

The benchmark scenario was chosen similarly as before with 16 h d -1 and constant 25 ° C. However, input weights were set to R 11 = R 22 = 1000. The reasoning was that light and heating can be rather costly and leave high CO2 footprints; a reduction of inputs u is of interest. Figure 8 shows the results. Egg mass after abort criteria in the benchmark was 284.2 mg versus 289 mg, an increase of 1.7%. Heat input was decreased by -7.33% and light input by -66.6%. Production time was decreased by 1.3 d.

## 3.2.4 Light control only

Egg production facilities may not allow for precise control of temperature, or breeding may happen in big halls with multiple unsynchronized breeding cages. In such cases, dynamic control of temperature is no longer an option, but optimization of light stimulation still is. Simulations showed that, while impact on egg output and time related performance parameters was negligible, light input could be reduced by -44% when compared to the benchmark scenario (see Figure 9).

## 3.2.5 Delay production to avoid weekends and holidays

Another plausible scenario, especially in batch setups, involved intentionally delaying oviposition. The process of egg collection typically involves manual labor. If the initiation of the oviposition phase aligns with weekends and holidays, there might be up to 4 days during which eggs are not collected. The designated areas for oviposition, usually specialized units designed for easy egg extraction, may become full, prompting the fl ies to avoid these areas and instead lay eggs in locations where collection is less convenient.

To address this issue, we utilized our model-based control to formulate a strategy capable of intentionally delaying oviposition by 2 days. This action aimed to potentially minimize the overlap between the egg collection window and labor-free days. For that, we introduced a constraint that ensured T Σ ( t = 6) ≤ k Σ ovi . Optimization results can be seen in Figure 10. While the standard approach seemingly produced 4.5% more egg mass, not all of them could be harvested, as previously described. Assuming that one-third of the eggs oviposited before day 6 could not be collected, amount of eggs harvested using optimal control was actually 10.6% higher.

## 4 Conclusion and outlook

Wehave developed a dynamic control model that describes the life cycle and oviposition processes of Hermetia fl ies as a function of environmental factors. Dynamic models are in general useful tools for life cycle assessment and process monitoring, where comparison of measurements to model prediction may help in detecting possible faults. Other uses are process analysis through simulation studies and -as was showcased in this work -process optimization and control. During the review of literature, one thing became clear: there is a lack of information on dynamic effects of u L and u T on Hermetia fl ies. Most experiments in literature are conducted at near constant parameters. One, however, wants to dynamically control the environment which leads to the question of whether certain effects have a ' memory ' . For example, high temperatures during the young stage results in faster life stage transition to the active stage. However, fecundity is impaired by too high of a temperature, so temperature is reduced when fi rst ovipositing occurs. According to the model, no problems would arise and one could bene fi t from fast development and high egg output simultaneously. But in reality, temperature might already affect fecundity during the time between becoming fertilized and oviposition. If the fl ies ' life processes have something similar to a ' memory ' in regards to environmental parameters, it raises the question on just what the meaning of parameters such as temperature is: the current temperature, highest temperature since emergence, or some average temperature? Due to lack of data, such effects could not be considered during modeling. The absence of proper modeling for longterm effects raises concerns regarding the optimization algorithm potentially generating trajectories that appear optimal within the model but could be detrimental in real-world application. Approaches to address this challenge are the incorporation of process knowledge not only into the model itself but also into the process constraints during optimization or the extension of the model.

Possible extensions of the model may involve the identi fi cation of additional process control variables. For instance, studies may explore how airborne time of fl ies could be in fl uenced, as this potentially increases the chances of fi nding a mating partner. Inputs such as sound, light fl ashes, or air jets represent potential variables for investigation. Environmental factors such as temperature and humidity have an effect on fertility and hatchability -processes which could also be included in the model.

The plausibility of the model was examined and tested against literature data, reaf fi rming that the model dynamics evolve in a realistic and plausible manner. We then used the model to calculate input trajectories to optimize the egg production process in various scenarios. Compared to a benchmark scenario, in our simulation study, the optimized process was able to generate more egg mass (9.4%) in less time (1 day faster) at reasonable costs ( -41% u L and +3.7% u T). Overall, we could show the versatility and usefulness of the model and optimal control in various scenarios. A possible extension to the optimization is to parameterize weights Q and R based on economic factors -allowing for direct economical evaluation of the optimization.

In our forthcoming work, we aim to address a critical aspect -parameter uncertainties, with a speci fi c focus on μ 0 . Since μ cannot be measured, the starting condition μ 0 was chosen without a strong data basis. It was tested how the model reacts to a parameter uncertainty of 50% -which can also be interpreted as very well fed larvae/pupae (see Supplementary Figure S4). A change of 50% in the initial value results in a 46% increase in time until the fi rst fl y dies and in an increase of 24% in produced egg mass. Georgescu et al. (2020) have found that female weight impacts fl y egg output. This shows that the reactions of the model to parameter changes in μ 0 are plausible. However, it also shows that the model is rather sensitive to this parameter and a fi tting choice for μ 0 (which cannot be directly measured) is crucial and subject to future experimental work.

## Data availability statement

Publicly available datasets were analyzed in this study. This data can be found here: https://doi.org/10.1371/journal.pone.0216160. s001 -Hoc et al. (2019) light on mating https://doi.org/10.1007/ s13355-015-0376-1 -Nakamura et al. (2016) data on population survival https://doi.pangaea.de/10.1594/PANGAEA.895274 -Chia et al. (2018) on temperature related data.

## Ethics statement

The manuscript presents research on animals that do not require ethical approval for their study.

## Author contributions

AK: Conceptualization, Investigation, Software, Writing -original draft. A-JH: Software, Writing -review and editing, Conceptualization. MP: Methodology, Software, Writing -review and editing. PK: Investigation, Writing -review and editing. L-CW: Software, Investigation, Writing -review and editing. SS: Funding acquisition, Methodology, Writing -review and editing.

## Funding

The author(s) declare that fi nancial support was received for the research, authorship, and/or publication of this article. This measure is co- fi nanced with tax revenues on the basis of the budget passed by the Federal Ministry of Education and Research of Germany (BMBF, Germany; grant number 031B0733D; project CUBEScircles) and grant FKZ 031B1291B (InA) within the BioBall innovation space. The publication of this article was funded by Chemnitz University of Technology.

## Acknowledgments

We thank Morgan Uland for proof reading and her help in improving readability of this work. A previous preprint version of the manuscript has been been published on arXiv (Kobelski et al., 2022).

## Confl ict of interest

The authors declare that the research was conducted in the absence of any commercial or fi nancial relationships that could be construed as a potential con fl ict of interest.

## Publisher ' s note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their af fi liated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fbioe.2024.1404776/ full#supplementary-material

## References

Andersson, J. A. E., Gillis, J., Horn, G., Rawlings, J. B., and Diehl, M. (2019). CasADi -a software framework for nonlinear optimization and optimal control. Math. Program. Comput. 11, 1 -36. doi:10.1007/s12532-018-0139-4

Bava, L., Jucker, C., Gislon, G., Lupi, D., Savoldelli, S., Zucali, M., et al. (2019). Rearing of Hermetia illucens on different organic by-products: in fl uence on growth, waste reduction, and environmental impact. Animals 9, 289. doi:10.3390/ani9060289

Bertinetti, C., Samayoa, A. C., and Hwang, S.-Y. (2019). Effects of feeding adults of Hermetia illucens (Diptera: stratiomyidae) on longevity, oviposition, and egg hatchability: insights into optimizing egg production. J. Insect Sci. 19, 19. doi:10. 1093/jisesa/iez001

Binsin, C., Ahmad, H., and Abu Hasan, H. (2023). Age-stage, two-sex life table analysis of black soldier fl y, hermetia illucens (diptera: stratiomyidae), reared on different organic wastes. J. Asia-Pacific Entomology 26, 102108. doi:10.1016/j.aspen.2023.102108

Bruno, D., Bonelli, M., Cadamuro, A., Reguzzoni, M., Grimaldi, A., Casartelli, M., et al. (2019). The digestive system of the adult Hermetia illucens (diptera: stratiomyidae): morphological features and functional properties. Cell Tissue Res. 378, 221 -238. doi:10.1007/s00441-019-03025-7

Chavez, M. (2021). The sustainability of industrial insect mass rearing for food and feed production: zero waste goals through by-product utilization. Curr. Opin. Insect Sci. 48, 44 -49. doi:10.1016/j.cois.2021.09.003

Chia, S. Y., Tanga, C. M., Khamis, F. M., Mohamed, S. A., Salifu, D., Sevgan, S., et al. (2018). Threshold temperatures and thermal requirements of black soldier fl y Hermetia illucens : implications for mass production. PLOS ONE 13, 02060977 -e206126. doi:10. 1371/journal.pone.0206097

Francuski, L., and Beukeboom, L. W. (2020). Insects in production -an introduction. Entomologia Exp. Appl. 168, 422 -431. doi:10.1111/eea.12935

Georgescu, B., Struti, D., P ă puc, T., Ladosi, D., and Boaru, A. (2020). Body weight loss of black soldier fl y Hermetia illucens (diptera: stratiomyidae) during development in non-feeding stages: implications for egg clutch parameters. Eur. J. Entomology 117, 216 -225. doi:10.14411/eje.2020.023

Gobbi, P., Martinez-Sanchez, A., and Rojo, S. (2013). The effects of larval diet on adult life-history traits of the black soldier fl y, Hermetia illucens (diptera: stratiomyidae). Eur. J. Entomology 110, 461 -468. doi:10.14411/eje.2013.061

Hall, R. D., and Gerhardt, R. R. (2002). ' 8 - fl ies (diptera), ' in Medical and veterinary entomology . Editors G. Mullen and L. Durden (San Diego: Academic Press), 127 -145. doi:10.1016/B978-012510451-7/50010-4

Heussler, C. D., Walter, A., Oberko fl er, H., Insam, H., Arthofer, W., Schlick-Steiner, B. C., et al. (2018). In fl uence of three arti fi cial light sources on oviposition and half-life of the black soldier fl y, Hermetia illucens (diptera: stratiomyidae): improving small-scale indoor rearing. PLOS ONE 13, 01978966 -e197910. doi:10.1371/journal.pone.0197896

Hoc, B., Noël, G., Carpentier, J., Francis, F., and Caparros Megido, R. (2019). Optimization of black soldier fl y ( Hermetia illucens ) arti fi cial reproduction. PLOS ONE 14, 02161600 -e216213. doi:10.1371/journal.pone.0216160

Holmes, L. A., Vanlaerhoven, S. L., and Tomberlin, J. K. (2012). Relative humidity effects on the life history of Hermetia illucens (Diptera: stratiomyidae). Environ. Entomol. 41, 971 -978. doi:10.1603/EN12054

Jones, B., and Tomberlin, J. (2021). Effects of adult body size on mating success of the black soldier fl y, Hermetia illucens (l.) (diptera: stratiomyidae). J. Insects as Food Feed 7, 5 -20. doi:10.3920/JIFF2020.0001

Klüber, P., Arous, E., Zorn, H., and Rühl, M. (2023). Protein- and carbohydrate-rich supplements in feeding adult black soldier fl ies ( Hermetia illucens ) affect life history traits and egg productivity. Life 13, 355. doi:10.3390/life13020355

Klüber, P., Bakonyi, D., Zorn, H., and Rühl, M. (2020). Does light color temperature in fl uence aspects of oviposition by the black soldier fl y (Diptera: stratiomyidae)? J. Econ. Entomology 113, 2549 -2552. doi:10.1093/jee/toaa182

Kobelski, A., Hempel, A.-J., Padmanabha, M., Wille, L.-C., and Streif, S. (2022) Process optimization of black soldier fly egg production via model based control . ArXiv preprint. doi:10.48550/arXiv.2212.05776

Kröncke, N., Baur, A., Böschen, V., Demtröder, S., Benning, R., and Delgado, A. (2020) Automation of insect mass rearing and processing technologies of mealworms ( Tenebrio molitor ) . Cham: Springer International Publishing, 123 -139. doi:10.1007/ 978-3-030-32952-5\_8

Liland, N. S., Biancarosa, I., Araujo, P., Biemans, D., Bruckner, C. G., Waagbø, R., et al. (2017). Modulation of nutrient composition of black soldier fl y ( Hermetia illucens ) larvae by feeding seaweed-enriched media. PLOS ONE 12, 01831888 -e183223. doi:10. 1371/journal.pone.0183188

Liu, X., Chen, X., Wang, H., Yang, Q., ur Rehman, K., Li, W., et al. (2017). Dynamic changes of nutrient composition throughout the entire life cycle of black soldier fl y. PLOS ONE 12, e0182601 -e0182621. doi:10.1371/journal.pone.0182601

Liu, Z., Najar-Rodriguez, A. J., Morel, P. C. H., and Minor, M. A. (2021). Reproduction of black soldier fl y (Diptera: stratiomyidae) under different adult densities and light regimes. J. Econ. Entomology 115, 37 -45. doi:10.1093/jee/ toab225

Macavei, L. I., Benassi, G., Stoian, V., and Maistrello, L. (2020). Optimization of hermetia illucens (l.) egg laying under different nutrition and light conditions. PLOS ONE 15, 02321444 -e232218. doi:10.1371/journal.pone.0232144

Nakamura, S., Ichiki, R. T., Shimoda, M., and Morioka, S. (2016). Small-scale rearing of the black soldier fl y, Hermetia illucens (diptera: stratiomyidae), in the laboratory: lowcost and year-round rearing. Appl. entomology zoology 51, 161 -166. doi:10.1007/ s13355-015-0376-1

Nayak, A., Rühl, M., and Klüber, P. (2024). Hermetia illucens (diptera: stratiomyidae): need, potentiality, and performance measures. Agriculture 14, 8. doi:10.3390/ agriculture14010008

Padmanabha, M., Kobelski, A., Hempel, A.-J., and Streif, S. (2020). A comprehensive dynamic growth and development model of Hermetia illucens larvae. PLOS ONE 15, 02390844 -e239125. doi:10.1371/journal.pone.0239084

Padmanabha, M., Kobelski, A., Hempel, A.-J., and Streif, S. (2023). Modelling and optimal control of growth, energy, and resource dynamics of Hermetia illucens in mass production environment. Comput. Electron. Agric. 206, 107649. doi:10.1016/j.compag. 2023.107649

Shumo, M., Khamis, F. M., Tanga, C. M., Fiaboe, K. K. M., Subramanian, S., Ekesi, S., et al. (2019). In fl uence of temperature on selected life-history traits of black soldier fl y ( Hermetia illucens ) reared on two common urban organic waste streams in Kenya. Animals 9, 79. doi:10.3390/ani9030079

Spranghers, T., Ottoboni, M., Klootwijk, C., Ovyn, A., Deboosere, S., De Meulenaer, B., et al. (2017). Nutritional composition of black soldier fl y ( Hermetia illucens ) prepupae reared on different organic waste substrates. J. Sci. Food Agric. 97, 2594 -2600. doi:10.1002/jsfa.8081

Surendra, K., Tomberlin, J. K., van Huis, A., Cammack, J. A., Heckmann, L.-H. L., and Khanal, S. K. (2020). Rethinking organic wastes bioconversion: evaluating the potential of the black soldier fl y ( Hermetia illucens (l.)) (diptera: stratiomyidae) (bsf). Waste Manag. 117, 58 -80. doi:10.1016/j.wasman.2020.07.050

The MathWorks (2022) Matlab version: 9.12.0 (r2022a) . United States: MathWorks.

Tomberlin, J. K., and Sheppard, D. C. (2002). Factors in fl uencing mating and oviposition of black soldier fl ies (Diptera: stratiomyidae) in a colony. J. Entomological Sci. 37, 345 -352. doi:10.18474/0749-8004-37.4.345

Wächter, A., and Biegler, L. T. (2006). On the implementation of an interior-point fi lter line-search algorithm for large-scale nonlinear programming. Math. Program. 106, 25 -57. doi:10.1007/s10107-004-0559-y

Yakti, W., Schulz, S., Marten, V., Mewis, I., Padmanabha, M., Hempel, A.-J., et al. (2022). The effect of rearing scale and density on the growth and nutrient composition of Hermetia illucens (l.) (diptera: stratiomyidae) larvae. Sustainability 14, 1772. doi:10. 3390/su14031772

Zhang, J., Huang, L., He, J., Tomberlin, J. K., Li, J., Lei, C., et al. (2010). An arti fi cial light source in fl uences mating and oviposition of black soldier fl ies, Hermetia illucens . J. Insect Sci. 10, 1 -7. doi:10.1673/031.010.20201