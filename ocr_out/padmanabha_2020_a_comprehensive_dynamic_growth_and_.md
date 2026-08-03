<!-- image -->

<!-- image -->

<!-- image -->

Citation: Padmanabha M, Kobelski A, Hempel A-J, Streif S (2020) A comprehensive dynamic growth and development model of Hermetia illucens larvae. PLoS ONE 15(9): e0239084. https://doi.org/ 10.1371/journal.pone.0239084

Editor:

Ji-Zhong Wan, Qinghai University, CHINA

Received:

July 16, 2020

Accepted:

August 28, 2020

Published:

September 18, 2020

Copyright: © 2020 Padmanabha et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: All relevant data are within the paper and its Supporting Information files.

Funding: Murali Padmanabha received funds from European Social Funds (ESF) grant number 100316180. URL: https://www.sab.sachsen.de/f% C3%B6rderprogramme/sie-planen-ihremitarbeiter-oder-sich-selbst-weiterzubilden/ promotionen.jsp#program\_intro The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

RESEARCHARTICLE

## Acomprehensive dynamic growth and development model of Hermetia illucens larvae

Murali PadmanabhaID, Alexander Kobelski, Arne-Jens Hempel, Stefan Streif *

Automatic Control and System Dynamics Lab, Technische Universita ¨t Chemnitz, Chemnitz, Germany

* stefan.streif@etit.tu-chemnitz.de

## Abstract

Larvae of Hermetia illucens , also commonly known as black soldier fly (BSF) have gained significant importance in the feed industry, primarily used as feed for aquaculture and other livestock farming. Mathematical models such as the Von Bertalanffy growth model and dynamic energy budget models are available for modelling the growth of various organisms but have their demerits for their application to the growth and development of BSF. Also, such dynamic models were not yet applied to the growth of the BSF larvae despite models proven to be useful for automation of industrial production process (e.g. feeding, heating/ cooling, ventilation, harvesting, etc.). This work primarily focuses on developing a model based on the principles of the afore mentioned models from literature that can provide accurate mathematical description of the dry mass changes throughout the life cycle and the transition of development phases of the larvae. To further improve the accuracy of these models, various factors affecting the growth and development such as temperature, feed quality, feeding rate, moisture content in feed, and airflow rate are developed and integrated into the dynamic growth model. An extensive set of data was aggregated from various literature and used for the model development, parameter estimation and validation. Models describing the environmental factors were individually validated based on the data sets collected. In addition, the dynamic growth model was also validated for dry mass evolution and development stage transition of larvae reared on different substrate feeding rates. The developed models with the estimated parameters performed well, highlighting their potential application in decision-support systems and automation for large scale production.

## Introduction

Hermetia illucens , commonly known as the black soldier fly (BSF), is an insect species which is widely studied for the high nutrition value of its larvae. Studies [1-4], showcase these nutritional values and its suitability as a source for animal feed and human food. Several studies, [5] and [6-9] amongst the recent, also indicate their application for recycling food and bio waste. These studies clearly demonstrate the potential of Hermetia illucens in addressing the approaching food scarcity while reducing the resource usage for their production. Irrespective of the potential applications of Hermetia illucens , for their (mass)

Competing interests: The authors have declared that no competing interests exist.

production, it is necessary to study: (1) the underlying biological processes such as assimilation, respiration, morphological changes, etc.; (2) the fundamental resource prerequisites such as feed composition, growing environment conditions, etc.; (3) the resulting growth dynamics that exhibits the various stages of the larval growth in response to the supplied resources; and (4) the interaction between the larvae and its environment (microbiome, substrate, etc.) and biological effects that trigger certain events (e.g. fleeing from substrate due to low O 2 concentration etc.).

This insect species originates from tropical South American climate zones and thus requires a warm and humid environment. Such conditions were verified in research studies: [10] highlighted the threshold temperatures and thermal requirements; [11] compared the development rates over different temperature ranges; and [12] studied the effect of humidity on the egg eclosion and adult emergence. The influence of diet, its moisture content and the temperatures were studied together to showcase its importance in the development of the larvae [1316]. Another study [17], proposed and showed the effects of pH levels of the substrate (feed), in which larvae are grown, on the larval development. From these studies, one can conclude the importance of the environmental conditions (temperature, humidity, etc.), the substrate conditions (moisture, pH, etc.) and the feed composition for the growth and development of the larvae.

Athorough literature survey revealed only time-invariant static models that describe certain biological processes of the BSF larvae. The authors of [10] suggested a model to describe the development rate as a function of temperature and, similarly, a model for calculation of metabolic rate as a function of temperature was presented in [18]. In case of [19], a logistic model was suggested for modelling the larval growth in response to the air flow rate. Also, a more recent work [20] suggested the use of a Richards model to fit the larval growth. These models from literature are mostly static models and do not adequately describe various timedependent dynamical aspects of larvae production such as resource dynamics, environment dynamics, etc. Also, it can be observed that the motivation behind the above mentioned literature was to improve the growth and hence the large scale production of BSF larvae. In order to fully utilize such models for performing simulation studies, reactor design, process design, automation, control and resource optimization, it is also necessary to appropriately formulate them as dynamic models. The main aim of this work is to develop suitable mathematical models that adequately describe the effect of environmental conditions on the larval metabolism; the larval growth describing the evolution of its dry mass over time; and finally, the transition of development stages between larvae and pupae.

The following sections provide in detail the approach taken to develop the models, analyze the data and obtain the model parameters. Firstly, a detailed explanation of the experimental setup is provided. Then, a dynamic model describing the growth and development of the larvae is presented. The experiments performed for the estimation of parameters are described followed by the model parameter estimation. Finally, the results of the models are compared with the actual measurement data and the quality of fit is determined for the models.

## Materials and methods

In this work, data for model development, parameter estimation and model validation are mainly obtained from literature and experiments performed in this study. Details of the experiments performed and the data source are also provided. The following sections provide the details of the mathematical models developed in this work and the procedure followed for estimating the model parameters.

## Production unit

The studies on the production of larvae in an artificial controlled environment in this work are conducted in a custom built production unit [21] that can provide the necessary growing conditions and simultaneously perform measurements of various parameters (e.g. air and substrate temperature, CO2 and O2 concentrations, humidity). The controlled environment has a volume of 75 L and holds a growing tray of dimension 22 cm × 32 cm × 5.5 cm that could contain up-to 4 kg of substrate. This growing tray serves as a container for the growing medium that contains selected feed for the larvae, selected number of young larvae (neonates) and the microbiome that eventually develops and grows along with the larvae in the growing medium. The temperature, humidity, airflow/air-concentration, and day-night cycles/photo period within the unit can be regulated as required. Information related to the states inside the production unit such as temperature of air and growing medium; CO2 and O2 concentrations; and humidity in air and moisture in growing medium are recorded by the sensors integrated within. Similarly, information related to the states outside the production unit, e.g., temperature, humidity and CO2 concentration of external air source, are logged using data loggers. Further details regarding the production environment can be found in [21] (see Section 2.1.4 and 3.7).

## Experiment setup for moisture dependency

To study the dependency on substrate or feed moisture, a larval growth experiment was performed. In this experiment, ten small containers of height 8 cm and diameter 5 cm were filled with 10 g of dry feed and varying amounts of water, from 0 to 40 g, were added. Then, 20 larvae of about 8 days old with a starting weight of 2 mg were added to each container. A small net was placed over each container to prevent the larvae from escaping while allowing air exchange. All containers were then placed inside the production unit with air temperature set at 29˚C and air ventilation at a rate of 7.5 l min -1 . The weight of each container was checked daily. Any changes in container weight, considered mostly due to evaporation, was supplemented to keep the moisture constant. The final fresh and dry weight of the larvae (dried for 6 h at 70˚C in an air dryer) was measured at the end of the experiment (on 8th day).

## Modelling approach for larvae growth, development and the influence of its environment

The main focus of this work is to obtain a model that describes the evolution of dry mass over a given period in response to various environmental factors. These models should also capture the drop in larval dry mass due to the maturation process that BSF larvae undergo during their last larval instars. Furthermore, it is also necessary to obtain information related to the development phases of the larvae that can be used for streamlining the production process. This description can be assistive in determining harvesting strategies such as harvesting for maximumlarval dry weight or for obtaining pupae for rearing adults.

The most commonly used models to describe the growth of biological organism, among others, are the von Bertalanffy growth model [22] and dynamic energy budget (DEB) [23] model. The former model describes the growth empirically while the latter is based on mechanistic description using the concepts of energy reserves and volume. Despite having a simple model structure, the von Bertalanffy model can be used to model the dry weight/size change over time. However, no inference can be obtained regarding the current development phase of the larvae or the drop in dry weight during maturation. The DEB model in comparison, uses states (energy density and structural volume) that are either difficult or not directly measurable. Also, it is not evident if using this model, information pertaining to the development phases could be obtained. Therefore, in this work, a new model is developed based on the mass balance approach and uses concepts such as asymptotic maximum size proposed for use with von Bertalanffy model [24] and the concept of maturity reserves used in DEB model. The following section provides some background to the fundamentals of larval growth and an overview of the model development based on these fundamental principles. Table 1 lists all the symbols used in this work for developing the models.

Larvae growth and dry mass partitioning. The collective processes that define the growth and development of an organism are known to be the metabolism. The important processes of the metabolism in an organism-here abstracted-are assimilation, maintenance, growth, maturity. Using the mass/energy balance approach, these abstracted metabolic processes can be used to describe the growth and development rate of an organism. General consideration in this approach is that the afore mentioned abstract processes can either use energy or mass for developing the model. Since mass is easy to measure in-situ both in laboratory and in production compared to measuring energy, in this work models are derived based on the mass.

Growth, which describes the increase in structural volume or mass in an organism, requires ingestion of feed. This feed ingested by larva is converted into assimilates through the process of assimilation consuming a portion of the assimilates for this process. The assimilates are converted into structural mass towards growth and maturity. Maturity, which is an indicator for larval development, consumes assimilates throughout the larval stage. Maintenance respiration that keeps the organism alive also consumes some of the assimilates. Using a Forrester diagram, the flow and partitioning of biomass and energy through the afore mentioned processes are presented in Fig 1.

With this context and background, growth or the rate change of the larval dry mass is represented using mass balance model as

<!-- formula-not-decoded -->

where � B ing is feed flux from substrate into the larvae, � B excr is the flux of non digested feed back to the substrate, � B assim is the feed converted into energy necessary for assimilation of the ingested feed, � B maint is the assimilates converted into energy for basal maintenance of existing structure, � B mat is the assimilates spent for growth and maturity (responsible for accumulating new structure) and � B metab represents all the assimilates consumed for metabolic activities.

The effective assimilates available for growth and maintenance � B eff can be expressed as

<!-- formula-not-decoded -->

where k a excr and k a assim are respectively the fractions of feed excreted and spent in the process respectively and � inges corresponds to the efficiency of the digested feed and provides information related to the quality of the feed.

Furthermore, maturity and maintenance expenses ( � B mat and � B maint ) cannot be distinguished since these two processes are active during the entire development phase of the larvae [16]. Due to this reason as well as the terms being difficult to separately measure, they are combined into one flux term. These flux components corresponding to the assimilation and maintenance are considered proportional to the weight/size of the organism [22]. Therefore substituting Eq (2) in Eq (1), replacing � B ing with k inges B dry, and replacing � B mat þ � B maint with

Table 1. List of symbols used in the description of the models.

| Symbol     | Description                                                                             | Unit         |
|------------|-----------------------------------------------------------------------------------------|--------------|
| B dry      | dry mass per larva                                                                      | [g]          |
| B wet      | wet mass per larva                                                                      | [g]          |
| B eff      | non structural assimilates in larva                                                     | [g]          |
| B str      | structural mass of the larva body                                                       | [g]          |
| T S        | development sum of larvae from neonates to prepupa                                      | [h]          |
| B feed     | total feed (dry mass) available in the growing medium                                   | [g]          |
| T med      | temperature of growing medium in production unit                                        | [˚C]         |
| W med      | total water in the growing medium                                                       | [kg]         |
| W med%     | moisture concentration of substrate                                                     | [kg kg -1 ]  |
| C air      | CO 2 concentration of air in production unit                                            | [kgm -3 ]    |
| O air      | O 2 concentration of air in production unit                                             | [kgm -3 ]    |
| H air      | absolute humidity of the air in production unit                                         | [kgm -3 ]    |
| A air      | air flow rate to the larvae production unit                                             | [l min -1 ]  |
| � B ing    | flux of feed from substrate into the larva                                              | [g s -1 ]    |
| � B excr   | flux of non digested feed back to substrate                                             | [g s -1 ]    |
| � B assim  | feed converted into energy and spent to digest the ingested feed                        | [g s -1 ]    |
| � B mat    | assimilates spent towards building of new structure                                     | [g s -1 ]    |
| � B maint  | assimilates spent for maintenance of existing structure                                 | [g s -1 ]    |
| � B eff    | effective assimilates available from the ingested feed for growth and maintenance       | [g s -1 ]    |
| � B metab  | total assimilates spent for metabolic activities                                        | [g s -1 ]    |
| k a excr   | fraction of ingested feed excreted out                                                  | [-]          |
| k a assim  | fraction of ingested spent for digestion                                                | [-]          |
| � inges    | efficiency of the ingested feed                                                         | [-]          |
| k inges    | specific ingestion rate of larva                                                        | [g g -1 s -1 |
| k maint    | specific rate of maintenance and maturity of larva                                      | [g g -1 s -1 |
| k dev ts   | conversion factor to obtain development sum in hours                                    | [s -1 ]      |
| k T S 1    | development point at which the assimilation process starts to cease                     | [h]          |
| k T S 2    | development point at which the assimilation process ends                                | [h]          |
| k T S 3    | development point at which the larval development phase ends                            | [h]          |
| k B asy    | asymptotic size of the larvae in dry mass                                               | [g]          |
| k T L      | lower boundary temperature for Arrhenius equation                                       | [K]          |
| k T ref    | reference temperature for Arrhenius equation                                            | [K]          |
| k T H      | upper boundary temperature for Arrhenius equation                                       | [K]          |
| k T AL     | Arrhenius temperature for the lower boundary temperature k T L                          | [K]          |
| k T A      | Arrhenius temperature for the reference temperature k T ref                             | [K]          |
| k T AH     | Arrhenius temperature for the upper boundary temperature k T H                          | [K]          |
| k r ref T  | development rate observed at the known reference temperature k T ref                    | [s -1 ]      |
| k r max T  | maximum observed development rate in response to temperature (Logan-10 model)           | [s -1 ]      |
| k r base T | minimum development rate observed above the lower temperature boundary (Logan-10 model) | [s -1 ]      |
| k ρ T      | development rate change per degree change in temperature (Logan-10 model)               | [˚C -1 ]     |
| k T base   | lower temperature boundary above which the development is observed (Logan-10 model)     | [˚C]         |
| k T max    | lethal maximum temperature for larval survival (modified Logan-10 model)                | [˚C]         |

( Continued )

Table 1. (Continued)

| Symbol       | Description                                                                                 | Unit           |
|--------------|---------------------------------------------------------------------------------------------|----------------|
| k Δ T        | width of the high temperature boundary (modified Logan-10 model)                            | [˚C]           |
| k r max dm   | maximum development rate of the larvae in response to feed density/availability             | [s -1 ]        |
| k B half dm  | feed density/feeding rate fow which the development rate is half                            | [g g -1 d -1 ] |
| k r max gm   | maximum growth rate of the larvae in response to feed density/availability                  | [g s -1 ]      |
| k B half gm  | feed density/feeding rate for which the development rate is half                            | [g g -1 d -1 ] |
| k r max w    | maximum growth rate in response to feed moisture concentration                              | [g d -1 ]      |
| k W med C1   | lowest feed moisture below which the growth ceases                                          | [g g -1 ]      |
| k W med C2   | feed moisture above which the ingestion rate can reach maximum                              | [g g -1 ]      |
| k W med C3   | feed moisture above which the diffusion of oxygen/air exchange starts to cease              | [g g -1 ]      |
| k W med crit | feed moisture above which the larvae begins to die                                          | [g g -1 ]      |
| k A inf A    | infliction point for logistic model at which the growth rate is half for given airflow rate | [l min -1 g -1 |
| k A trans A  | airflow rate influenced growth rate transition range for logistic model                     | [l min -1 g -1 |
| k r max A    | maximum observed growth rate in response to airflow rate                                    | [g s -1 ]      |
| k A half     | air flow rate for which the growth rate is reduced to half                                  | [l min -1 ]    |
| r assim      | regulation of assimilation rate in response to internal and external factors                | [-]            |
| r mat        | regulation of maturity-maintenance rate in response to internal and external factors        | [-]            |
| r dev        | regulation of development rate in response to external factors                              | [-]            |
| r T          | larva development rate in response to substrate temperature                                 | [s -1 ]        |
| r F          | larva development rate in response to feed density                                          | [s -1 ]        |
| r F grw      | larva growth rate in response to feed density                                               | [g s -1 ]      |
| r W          | larva growth rate in response to substrate moisture                                         | [g s -1 ]      |
| r W assim    | larva assimilation rate change in response to substrate moisture                            | [-]            |
| r W resp     | larva respiration rate change in response to substrate moisture                             | [-]            |
| r A          | larva growth rate in response to air flow rate                                              | [g s -1 ]      |
| r B assim    | change of assimilation rate in larva over its development period                            | [-]            |
| r assim max  | change of ingestion potential of larva with its dry mass                                    | [g g -1 ]      |
| r B mat      | change of maturity-maintenance rate in larva over development period                        | [-]            |

[https://doi.org/10.1371/journal.pone.0239084.t001](https://doi.org/10.1371/journal.pone.0239084.t001)

k maint B dry , Eq (1) can be rewritten in terms of dry weight as

<!-- formula-not-decoded -->

where k inges and k maint are the specific maximum ingestion rate and specific maximum maturity and maintenance rate respectively (g feed g -1 larvae s -1 in dry matter). The Eq (3) is of the form similar to the general form of von Bertalanffy model given in Eq (5) of [22] with m = 1 for insects as suggested in [25]. This model given by Eq (3) is rudimentary, describing only partitioning of the biomass across different biological processes. To achieve the model goals described previously, it is also necessary to model different factors such as temperature, feed quality, current larval instar, etc., that regulate the rate of flow of the mass and energy fluxes across different processes. Introducing the factors influencing the growth, Eq (3) can be reformulated as

<!-- formula-not-decoded -->

Fig 1. Mass and energy flow between the larva, substrate and the growing environment. The rectangles represent the different states and the arrows indicate the flow of mass and energy (fluxes) between these states. Biomass and water in the substrate enters and exits larvae by ingestion and excretion. Gas exchange as a result of metabolic respiration takes place between the larva and the environment. Assimilated biomass and reserves B eff is further converted into structure towards the larval maturity B str and energy B maint necessary for maintenance of the structure. The states represented in dashed lines indicate that they are not directly measurable unlike the larva wet and dry mass B wet and B dry respectively. A part of the B maint is converted to heat, a byproduct of metabolism, and is lost to the substrate increasing its temperature T med.

<!-- image -->

[https://doi.org/10.1371/journal.pone.0239084.g001](https://doi.org/10.1371/journal.pone.0239084.g001)

where the functions r assim and r mat regulate the rate of assimilation and maturity-maintenance respectively in response to the current development stage and the available growing conditions. Deriving these regulation functions and identification of the factors affecting the growth and development is necessary. However, it is first necessary to identify a mechanism to model the development process using which the development phases of the larvae can be tracked.

Larvae development. Growth process in larvae takes place in stages which are commonly known as instars with the Hermetia illucens larvae undergoing a total of 6-7 instars [26, 27]. This development, however, seems to be not dependent on the size of the larvae. This can be inferred from the data presented in [13], where the larvae completed their development despite not reaching nearly half their maximum size. Therefore, an alternate mechanism is required to model the developmental stages of the larvae. Using this mechanism the last two larval instar stages, which have significant influence on the growth process, can be tracked.

The use of temperature sums or degree days to track the developmental stages and growth of an organism, including plants and insects, can be seen in literature [28-30]. For organisms growing in open fields where mostly only temperature vary, it was possible to estimate the actual development stage by tracking the total suitable heat the organism received during its lifetime. This concept of temperature sums serves as a unit to calculate the apparent age of the organism [31] that is different from the real age which is the time since the larva is hatched. However, this might only work for cases where the resources such as food, air concentration and heat are not limited. Therefore, as also suggested in [31], not only temperature but also other environmental conditions such as feed density, air concentration etc., need to be considered to obtain the apparent age that serves as an indicator to the total energy received by the larvae in its lifetime. In this work, such indicator for total energy is obtained from the total number of hours that the larva receives suitable growing conditions (apparent age) in its lifetime (real age).

Similar to integrating the temperatures over time as in degree days, here the instantaneous development rates determined by the environmental conditions are integrated. This integrated sum of development rates-referred to as development sum T S -is introduced. This development sum can therefore be written as a function of all factors that affect the development rate as

<!-- formula-not-decoded -->

where r dev is the function regulating the development rate for the available given growing conditions such as temperature in substrate T med, feed availability B feed , moisture in substrate W med, air flow rate A air and k dev ts is the maximum rate at which the apparent age (in h) changes in relation to the real age. This Eq (5) now provides a new unit of measure for apparent age to identify the current development stage.

Effect of external factors on larval growth and development. Factors that affect the growth and development of the larvae considered in this work include temperature, feed density, feed quality, moisture and air concentration. Each of these parameters influence the larval development through various biological processes. An attempt is made to model these influences through mechanistic and analytical models both from literature and developed based on the analysis of aggregated literature and experiment data. The factors affecting the growth and development are studied and modelled independently by varying only one factor and keeping the other factors constant.

Temperature . Temperature has a direct effect on all the biochemical reactions that take place in the larvae and thus affecting its growth and development rate. The effect of temperature on the growth of larvae can be modeled using Arrhenius equation [32]. Corrections to the metabolic rates for the temperatures beyond the upper and lower boundaries can be applied as

<!-- formula-not-decoded -->

with T K = T med in K, where k T ref is the reference temperature for which the development rate is known, k T A , k T AL and k T AH are Arrhenius temperatures at reference k T A , lower boundary k T L , and upper boundary k T H temperatures respectively, and k rrefT is the known reference development rate.

Another analytical model proposed in [33] (see Eq (10) of [33]), referred to in this work as Logan-10, also describes the growth rate in response to the temperature as well considering the effects of denaturation and desiccation at high temperatures. The Logan-10 model was modified such that for temperatures beyond the upper threshold, the resulting growth is zero instead of a negative growth. The resulting modified Logan-10 model is given as

<!-- formula-not-decoded -->

with k g ¼ k r max T k r base T k r base T � � , where k rmaxT is the maximum observed rate (s -1 ), k rbaseT is the minimum rate at the temperature above the lower threshold, kρ T rate change in response to the temperature, k T max is the lethal maximum temperature and k Δ T is the width of the high temperature boundary layer. The Logan-10 model has one less parameter compared to Arrhenius model presented in Eq (6) and can be intuitively approximated from the available data. In this work, both these models will be evaluated and the corresponding parameters will be estimated.

Feed density . The feed flux assimilated by the larvae is effected by few factors, considered important in this work due to its application, such as feed availability and change in feeding behavior due to the modifications to the mouth parts of the larvae in its final instars. It is common in literature to model the change in ingestion rate due to substrate availability using a type II function. Monod presented an adaptation of this function to model the growth of bacterial cultures in [34]. This Monod equation is adapted in this work as

<!-- formula-not-decoded -->

where B feed is the feed density in the substrate/growing medium, k rmaxdm is the maximum development rate (s -1 ) at highest feed density and k Bhalf dm is the feed density resulting in half of the maximum rate.

Similarly, Eq (8) can be rewritten to also model the growth rate of the larvae as

<!-- formula-not-decoded -->

where k rmaxgm is the maximum growth rate (g s -1 ) of the larvae and k Bhalf gm is the feed density resulting in half of the maximum growth rate.

Feed moisture . Based on the data presented in [19], the authors suggest that the moisture of the feed (kg water in kg wet feed) has a first order effect. However, in that study, data was only available for the moisture content of 48-68%. Another early work studied the development of different flies, including Hermetia illucens , under different substrate moisture conditions [35]. In this work, the authors concluded that the development increased with increase in moisture content between 30-70%, while, at 20, 80 and 90% there was no development observed. The moisture experiment performed as part of this work, covered the feed moisture in the very low and high concentrations. Based on these results, the feed moisture has different influences on the larval growth. Firstly, with lower moisture, the feed may not be ingestible and thus result in slower growth and high mortality rate at very low moisture levels. Secondly, with increasing moisture, feed could be assimilated better resulting in better growth. Finally, at higher moisture concentrations, intake of oxygen might be reduced resulting in slower growth and higher larval mortality.

Based on these observations, the influence of water content in feed on the larval growth can be modelled as

<!-- formula-not-decoded -->

where k rmaxWis the maximum growth rate, and the influence of moisture content on the assimilation rate and respiration rate r Wassim and r Wresp respectively are modelled as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where k WmedC1 is the lowest water content in the feed below which growth ceases due to reduced feed ingestion rate, k Wmed C2 is the moisture concentration above which the ingestion rate is maximum, k WmedC3 is the water concentration above which diffusion of air into substrate and thus the larvae drops, and k Wmedcrit is the highest water concentration above which oxygen diffusion ceases.

Air flow rate and O2 concentration . Effect of aeration in the growing environment influences the larval growth through the availability of O2 necessary for respiration. A study performed in [19] that compared the larval growth at different air flow rates and thus the available O2 concentration used a logistic model to describe the data.

<!-- formula-not-decoded -->

where k rmaxA is the maximum rate, k Ainf is the infliction point and k Atrans is the slope. However, in [36] the authors despite highlighting the logistic model, have used a type II function to model the development rate based on the O2 concentration. In this work, the influence of O 2 concentration is considered as a resource necessary for the underlying biological processes and therefore the growth rate in response to the airflow rate can be modeled as

<!-- formula-not-decoded -->

where k rmaxA is the maximum growth rate under certain high Air flow rate and k Ahalf is the airflow rate for which the growth rate is reduced by half.

Other factors affecting the underlying biological processes. In previous sections, models describing growth, dry mass partitioning, and external factors influencing the growth and development rate were presented. It is also necessary to establish the relation between the development stage of the larvae and how it influences the underlying biological processes such as assimilation, maturity and maintenance. Here, the regulation function describing the relation between the assimilation and maintenance rates due and the current development stage of the larvae is presented.

Feeding and growth stage . Larval structural growth is a result of constant assimilation-the main function of the larvae is to accumulate enough assimilates and mass-lasting up-to the 6th instar [26]. According to the results published in [18], the larvae assimilates the feed at highest rates during the 1st to 4th instar. This gradually drops from 4th to 6th instar and assimilation finally ceases before 7th instar. It is also observed in the works of [18], that the mouth parts of the larvae undergo morphological changes suggesting changes in feeding behavior.

With respect to the model considered in this work, this transition into non-feeding stage indicate that the assimilation is highest in the early larval stages, gradually decreases with increase in mass, and finally ceases when the feeding stage is completed. These variations of the assimilation process over the development stages, indicated by T S , can be described as

<!-- formula-not-decoded -->

with r assim max ð B dry Þ ¼ 1 B dry k B asy , where k B asy is the maximum asymptotic mass of the larvae, k T S 1 is the transition point until which the larvae feeds at a maximum rate and k T S 2 is the point beyond which the feeding comes to a halt. The function r assim max represents the ingestion/feeding potential of the larvae in relation to it its current size and the maximum size it can reach when infinitely fed. With this Eq (17), a relation between the development sum and the size dependent ingestion is established.

Maturation stage . In the final larval instar stage, the accumulated assimilates and reserves (e.g. fats) are further spent in developing the parts necessary to reach the maturity and transform into a pupae. This maturity process was studied in [37] which indicates a drop in the dry mass and, in specific, the crude fats during the transition from prepupae to pupae. However, maturation ceases at the end of this transformation and then the pupal stage begins. This maturity allocation, can be modeled as a rate that allocates the assimilates and reserves to the maturation process. Allocation to maturity can be also seen in the modeling approaches of DEB [38] (see Section 2.4). In this work, such scheduling of assimilates to maturation is done such that the maturity process continues further after the feeding phase and until the larvae turn into pupae. This continued allocation describes the drop in mass and indicates the change in body composition. Therefore, the variation in maturity allocation is described as

<!-- formula-not-decoded -->

where k T S 3 indicates the end of prepupal or beginning of pupal stage. For the model to track pupal development, the maturity allocation shall be replaced with a non zero value since the pupae undergo further metamorphosis consuming reserves.

Combining growth, development and external factors. The factors considered to be affecting the growth of larvae and the movement of mass and energy between larva, growing medium and the environment is summarized in Fig 2 using Forrester diagram. The B str , representing the structural mass of the larva, has its influences on most of the rate flows as seen in Fig 2.

From Fig 2, it can be seen that the rate or regulatory functions r assim and r mat acts as valves that regulate the underlying process by controlling the flow of necessary resources. From this context, these regulatory functions can be, in simple way, modelled to vary from to 0-1 such that for best conditions the valves are set to attain the maximum rate possible for the underlying processes. In case of deficiencies in any of the required growing conditions, the rate goes down reducing the rate of the underlying processes. Therefore, the regulatory function for assimilation can be modelled as a product of all rate functions responsible. This can be https://doi.org/10.1371/journal.pone.0239084.g002

Fig 2. Mass and energy transfer. The flow of mass and energy between the substrate or growing medium, larva body and the environment in response to various states and environment conditions are represented using the valves that regulate this flow. Influence of the states on the rate are indicated using dashed lines. Influence of the states on the rates are not explicitly indicated when the flow takes place between those corresponding states. Valves r assim , r mat , and r resp, represent the assimilation, maturity-maintenance and respiration as a function of various states that influence the flow of biomass and energy.

<!-- image -->

written as

<!-- formula-not-decoded -->

Similarly the processes underlying maturity-maintenance is affected by temperature for metabolic activities, air concentration for respiration, available reserves indirectly represented by the feed density, and finally the development state of the larvae. Therefore, this can be modelled as

<!-- formula-not-decoded -->

Finally, the regulation function for development rate r dev can be modelled similarly to Eq (17), a function of all factors affecting development, as

<!-- formula-not-decoded -->

Regulation functions Eqs (17) to (19) play a significant role is describing the dynamic interaction between the larvae and its environment.

## Implementation of switching functions

The functions that are modelled in this work as cases or switching functions, Eqs (11), (12), (17) and (18), are realized as logistic functions in the actual implementation of the model in MATLAB to allow for a smooth transitioning between the cases. This is especially done, firstly, to replicate the behavior in biology where the transition is gradual and not a sudden change and, secondly, to allow for the numerical solvers to converge to the solution.

Alogistic function modelling the transitions from 0-1 (sigmoid curve) can be written as

<!-- formula-not-decoded -->

where k defines the slope for the transition between 0 and 1, and x 0 defines the mid point of the transition where the function reaches half of its maximum value. The two parameters for the Eq (20) can be calculated and substituted back to obtain a smooth transitioning version of the function free of kinks. An example for Eq (17) is provided here as

<!-- formula-not-decoded -->

with k T S inf = k T S 1 + 0.5( k T S 2 -k T S 1 ).

## Model validation and parameter estimation

Models presented in this work are mostly nonlinear and therefore, nonlinear least squares data fitting method was used for parameter estimation. This was formulated as an optimization problem with the objective of finding the parameter that minimizes the sum of square of errors as

<!-- formula-not-decoded -->

where p represents the parameters to be estimated, f ( p , X ) represents the model, Y is the measured data and i represents the measurement samples. This parameter estimation problem was implemented in MATLAB using the lsqcurvefit function in a multi-search framework to explore possible solutions within the specified boundary values of parameters. Simulation of dynamic model was performed using the ode 45 solver in MATLAB to solve the differential equations.

The data sets obtained from different literature sources, as presented in Table 2, were used in this work for the purpose of parameter estimation and validation. Steps followed in preparing the data, estimating the parameters of the static models Eqs (6) to (10), (13) and (14), and using them in the final models are described as below:

1. Identify the datasets for the constant and variable factors. For example, for data set T1, temperature is variable but feed type and other factors are constant. Similarly, T2-T4 have variable temperatures but other factors are constant within the data sets. Therefore, T1-T4 from common data sets serving the same purpose (Temperature dependency).
2. Group together the data sets serving common purpose and normalize the measurement values. This converts the data sets to a common scale and remove any dependency due to other variables between the data sets. For example, feed type used in the data set T1 is different from T2, T3 and T4. Therefore, dividing the development and growth rates by the observed maximum value will transform the measurement of all data sets (T1-T4) to a common scale (0-1).
3. Perform the parameter estimation using the individual normalized data sets and also the normalized data sets grouped together.

Table 2. Data sets and their source used for model validation and parameter estimation.

| Dataset ID   | Source                 | Description                                                                                       | Application                                                    |
|--------------|------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| T1, T2       | Fig 3 of [10]          | Development time of BSF on different diets at different temperatures                              | Validation and parameter estimation for Eqs (6) and (7)        |
| T3, T4       | Table 1 of [11]        | Development time of BSF on different diets at different temperatures                              | Validation and parameter estimation for Eqs (6) and (7)        |
| F1           | Table 2, 3 of [13]     | Development time and dry weight respectively of BSF larvae under different feeding rates          | Validation and parameter estimation for Eqs (8) and (9)        |
| F2-F4        | Table 2, Fig 1 of [39] | Development time and dry weight respectively of BSF larvae under different feed and feeding rates | Validation and parameter estimation for Eqs (8) and (9)        |
| M1           | Fig 4 of [19]          | Larvae growth/dry weight change under different substrate moisture content                        | Validation and parameter estimation for Eqs (10) and (12)      |
| M2           | This work              | Larvae growth/dry weight change under different substrate moisture content                        | Validation and parameter estimation for Eqs (10) and (12)      |
| M3           | Table 2 [35]           | Larvae growth/dry weight change under different substrate moisture content                        | Validation and parameter estimation for Eqs (10) and (12)      |
| A1           | Fig 2 of [19]          | Larvae growth/dry weight change under different aeration rate                                     | Validation and parameter estimation for Eqs (13) and (14)      |
| G1           | Fig 1 of [37]          | Larvae growth/dry weight change over the developmental phases                                     | Validation and parameter estimation for Eqs (4), (17) and (18) |
| D1, D5       | Fig 2 of [13]          | Larvae growth/dry weight change over the developmental phases under different feeding rates       | Validation and parameter estimation for Eqs (4), (17) and (18) |
| D2-D4        | Fig 2 of [13]          | Larvae growth/dry weight change over the developmental phases under different feeding rates       | Validation of Eq (4)                                           |

https://doi.org/10.1371/journal.pone.0239084.t002

4. Parameters estimated using the grouped data sets, later labelled as average data, are used as final parameters for the model.
5. Finally, to transform the result (growth and development rates) back to the actual scale (s -1 or g s -1 ), the results are multiplied by the maximum rate observed in the data sets. These maximum rates observed, corresponds to the parameter k rmaxXYZ where XYZ represents individual static models.

Parameters corresponding to the dynamic model Eqs (4) and (5) are estimated using measurement data that contains larvae dry mass change over time and the corresponding growing conditions maintained during the entire time. Some of the parameters obtained from the static models were re-estimated in order to accommodate the dynamics and any changing growing conditions. Once re-estimated for one data set, the parameters should be valid for all the data sets from the data sets grouped together. This step calibrates the dynamic model for the new data sets. For example, in this work, parameter values for k Bhalfgm and k Bhalfdm were re-estimated to calibrate the dynamic model for the new datasets D1-D5, since the feed type changed. However, this re-estimation was only performed using a subset of the available data sets (D1 and D5). The calibrated models, using the new estimated parameter value, shall be now valid for all data sets D1-D5. Results obtained using the above described procedure and the resulting quality of fit for each data set is presented in the following section.

## Results

In this section, firstly, the performance of the individual rate functions Eqs (6) to (10), (13) and (14) describing the influence of external factors on growth and development are presented. Secondly, performance of the combined dynamic model representing the growth Eq (4) and development Eq (5) are presented, highlighting the validity of the rate functions Eqs (17) and (18) for assimilation and maturation respectively. Finally, the dynamic growth and development model are validated using additional datasets.

Fig 3. Temperature influence on development rate using Arrhenius model. (a) Parameters estimation using Arrhenius model (6) and normalized data. (b) Development rate estimation using the parameters estimated for data set obtained by averaging all (T1-T4) data sets. Model fit represented as avg shows the performance of the final model.

<!-- image -->

[https://doi.org/10.1371/journal.pone.0239084.g003](https://doi.org/10.1371/journal.pone.0239084.g003)

## Temperature influence

Atotal of four data sets (T1-T4) representing the influence of temperature on larvae development was obtained from [10, 11]. These four data sets represent the temperature dependency under four different feed types and was used to obtain the parameters for models Eqs (6) and (7). Fig 3 shows the results of the parameter estimation using the Arrhenius model (6) and Fig 4 for the modified Logan-10 model Eq (7).

Both models perform well in describing the data with good quality of fit ( R 2 &gt; 0.91). The model parameter obtained from the average data set was used to explain the data sets T1-T4 as shown in Figs 3(b) and 4(b). The results of the model with the estimated parameters from the average data, performed well in explaining all data sets with the only exception for T3 where both models could not explain the peak at 30˚C. Modified Logan-10 model has overall better

Fig 4. Temperature influence on development rate using modified Logan-10 model. (a) Parameters estimation using modified Logan-10 model (7) and normalized data. (b) Development rate estimation using the parameters estimated for data set obtained by averaging all (T1-T4) data sets. Model fit represented as avg shows the performance of the final model.

<!-- image -->

[https://doi.org/10.1371/journal.pone.0239084.g004](https://doi.org/10.1371/journal.pone.0239084.g004)

Fig 5. Feed availability on development and growth. (a) Larvae development rates at varying feed availability. (b) Larvae growth rates at varying feed availability. Model fit avg represents the results of the average model scaled to the maximum observed development rate from the 4 data sets.

<!-- image -->

[https://doi.org/10.1371/journal.pone.0239084.g005](https://doi.org/10.1371/journal.pone.0239084.g005)

quality of fit for both normalized and actual data sets. For temperatures below 15˚C, Eq 6 provides a better fit at the expense of one additional parameter.

## Feed density

Results published in [13] was used to obtain data set F1 and [39] for data sets (F2-F4) representing the development and growth rate under different feeding densities and feed types. The feed density defined in these works use gram dry mass of feed available/provided per larvae per day (g d -1 per larva) during the feeding periods. These data sets were used to obtain the development rates and growth rates using the model Eqs (8) and (9) as shown in Figs 5 and 6.

The models describe accurately ( R 2 = 0.97) for the data set F1 due to the availability of measurement for uniformly distributed feed densities. In case of F2-F4, the data set also includes both batch fed and continuous fed experiment measurements resulting in scattered measurements and thus lower quality of fit. Growth rate model, on the contrary, performs

<!-- image -->

4-

Fig 6. Feed availability on development and growth (Normalized). (a) Larvae development rates at varying feed availability. (b) Larvae growth rates at varying feed availability. Mode fit avg represents the results of the average model for the combined data sets.

[https://doi.org/10.1371/journal.pone.0239084.g006](https://doi.org/10.1371/journal.pone.0239084.g006)

better in describing all data sets F1-F4 with R 2 &gt; 0.92. The parameters for these models are obtained by combining the normalized data sets F1-F4. The resulting model from this combined data is shown with the dashed line (indicated as avg) as in Fig 6. From these results it could be concluded that these models can be used to compute the growth and development rates under different feeding rates.

## Moisture effect on growth

To evaluate the model presented in Eq (10), for influence of moisture on the growth, a total of three data sets M1-M3 were obtained. M1 and M3 are results published in [19] and [35] respectively. Data sets M1 and M2 does not contain measurements for the entire moisture concentration range but M3 provides data for the range from 20% to 90% as seen in Fig 7(a). The proposed model is capable of describing the growth for the considered data sets and also the observations from the moisture experiment coincides with [35] for the higher moisture concentration. On the contrary, higher development rate was observed for moisture at 80% in [40]. Further investigation with complementary data sets may be necessary to identify the boundaries for higher moisture concentrations.

## Airflow rate

Only one literature was found that included the effect of airflow on the growth of the larvae in [19]. In that work, closed 750 mL bioreactors with different aeration rates were used to study the larval growth rates. As expected, in closed environment, growth was slow at lower aeration rates and increased gradually with increasing aeration rates and finally saturates. Model Eqs (14) and (13) were evaluated and the results are presented in Fig 7(b). From these results, one can see that both models can describe the growth under various aeration rates. However, Eq (14) provides better results for the available data sets. Further studies might be necessary to obtain the growth response to different flow rates under varying moisture concentrations to identify correlation between them.

## Larvae growth and development

The larvae growth model presented in Eq (4), describing the evolution of dry mass of the larvae, and the development model presented in Eq (5) was validated based on the dry weight

Fig 7. Moisture and airflow on growth rate. (a) Effect of substrate/feed moisture on the growth rate. (b) Effect of airflow rate on the growth rate in closed production. Model-1 represents the Monod model Eq (14) and Model-2 represents the logistic model Eq (13).

<!-- image -->

https://doi.org/10.1371/journal.pone.0239084.g007

Fig 8. Larvae growth, development and biomass partitioning. (a) Larvae dry mass evolution over time (b) Partitioning of assimilates and dry mass over development phases. The development sum where the assimilation and maturity transition, are indicated by the horizontal markers labelled k T S 1 , k T S 2 , and k T S 3 .

<!-- image -->

[https://doi.org/10.1371/journal.pone.0239084.g008](https://doi.org/10.1371/journal.pone.0239084.g008)

measurements presented in literature [13] and [37]. Dry mass of the Hermetia illucens from eggs to adult, presented in [37], was used to obtain estimates of the parameters marking the important stages k T S 1 , k T S 1, and k T S 3. Based on the biomass conversion efficiency for chicken feed provided in [8, 13], parameters for dry mass distribution to metabolism, excretion and growth are also estimated to 0.24%, 0.62%, and 0.11% respectively. The performance of the model based on the estimated parameters is presented in Fig 8.

Initially, the change of larval dry mass from the 1st larval instar to the 5th instar is regulated by the asymptotic size of the larva (in dry mass) as seen between 0-320 h marked by k T S 1 . As the larvae approaches its last instar, ceasing of the ingestion process marked by the morphological changes such as modification of mouth parts and darkening of the skin are identified by the k T S 2 and k T S 3. The final transition from prepupae to pupae is marked at the end of k T S 3 , indicating the end of larval growth and start of pupal stage.

Furthermore to validate the model for different data sets, data set from [13] was used. Using the data sets D1 and D5, model parameters were further adjusted for the new setup and using these new parameters the performance of the model was validated for all data sets D1-D5. The results as seen in Fig 9, highlights the performance of the model by providing the dry weight evolution as well as the indication of the different Larval development stages.

As seen from Fig 9, the R 2 for the data sets D1,D2 and D5 are &gt; 0.91 but comparatively lower for D3 and D4. This is purely due to the variance in the final recorded weight for D3 and D4. To support this inference, we can also observe that for D3, D4 and D5 there were larvae with higher mass on the same day when 50% prepupae were observed. The Eq (4) also models higher assimilates allocation to maturity for higher feed density, indicating that more reserves are available in larvae growing in higher feed density. This can be seen in the drop in dry mass when larvae transforms to prepupae. This drop, as explained by the model and also as observed from the data is highest for D5 and lowest for D1.

## Summary

From these observation one can conclude that the dynamic model developed in this work serves the two main intended goals: (1) model the larval growth through change of dry mass B dry over its development stages under different growing conditions; and (2) model the transition of larval development through the development sum T S under different growing https://doi.org/10.1371/journal.pone.0239084.g009

Fig 9. Validation of larvae growth and development model. Models are validated based on the data sets D1-D5 as published in [13]. The vertical line indicates the time point where about 50% of the larvae are transformed into prepupae. The circle on the corresponding model fit indicate the k T S 3 time point when development of larvae are completed.

<!-- image -->

conditions. These results were achieved using simple model structures which plausibly and consistently explained various data from the literature. Finally, the model parameters estimated in this work are summarized in Table 3. Data set used for parameter identification of the moisture influence and the matlab implementaion of the model are included as supplementary information (see S1 Dataset and S1 File).

## Discussion

Growth and development of H . illucens larvae depend on several internal and external factors. Quantitative study of these factors and their influence is necessary for a better understanding of the growth dynamics and eventually its application for solving some of the real-world

Table 3. Estimated model parameter values.

| Parameter        | Est. value               | Parameter        | Est. value                 | Parameter         | Est. value      |
|------------------|--------------------------|------------------|----------------------------|-------------------|-----------------|
| k r ref T (6)    | 0.7195 �                 | k T A (6)        | 8450 K                     | k T AL (6)        | 60000 K         |
| k T AH (6)       | 40667.275K               | k T ref (6)      | 298.92 K                   | k T L (6)         | 285 K           |
| k T H (6)        | 308.96 K                 | k r max T (7)    | 1.0 �                      | k r base T (7)    | 0.215 �         |
| k r T (7)        | 0.2487˚C -1 d -1         | k T max (7)      | 39.769˚C                   | k D T (7)         | 3.0˚C           |
| k T base (7)     | 15.95˚C                  | k B half dm (8)  | 0.0049 g d -1              | k r max dm (8)    | 0.9758 �        |
| k B half gm (9)  | 0.00532 g d -1           | k r max gm (9)   | 2 �                        | k W med C 1 (10)  | 0.329 kg kg -1  |
| k W med C 2 (10) | 0.69 kg kg -1            | k W med C 3 (10) | 0.76 kg kg -1              | k W med crit (10) | 0.833 kg kg -1  |
| k r max A (14)   | 1.128 �                  | k A half (14)    | 0.1877 l min -1 kg -1      | k B half dm (8)   | 0.0137 g d -1 + |
| k r max dm (8)   | 1 � +                    | k B half gm (9)  | 0.0717 g d -1 +            | k r max gm (9)    | 1 � +           |
| k a excr (2)     | 0.5762                   | k a assim (2)    | 0.2135                     | � inges (2)       | 0.79            |
| k inges (4)      | 1.61 × 10 -4 g g -1 s -1 | k maint (4)      | 5.6779 × 10 -6 g g -1 s -1 | k T S 1 (15)      | 234.35 h        |
| k T S 2 (15)     | 265.5 h                  | k T S 3 (15)     | 297.5 h                    | k B asy (15)      | 0.115 g         |

[https://doi.org/10.1371/journal.pone.0239084.t003](https://doi.org/10.1371/journal.pone.0239084.t003)

problems (e.g. rearing for feed, waste processing etc.). There have been several studies that explore the application of H . illucens larvae to recycle food waste [6-8, 13, 41-47] and also in production of alternative animal feed [1, 2, 4, 48-50]. Such exploration for suitable application have also led to studies to understand the various factors affecting the growth and identifying the suitable conditions for larvae rearing [9-16, 20, 39-42, 51-57]. However, quantification of these interaction between the larvae and their growing conditions using models can only be seen in few literatures with studies limited to temperature and diet quality [10, 13, 20, 42].

This study has extended the scope of mathematical models to not only temperature but also other factors such as moisture in feed, feed density and air flow rates. Using Arrhenius and modified Logan10 model, the influence of temperature on the metabolic rates driving the growth process over a wide temperature ranges were shown. It could be seen from Figs 3 and 4 that the larvae have highest growth rates between 30-35˚C. Despite showing the variation of the growth rates over the temperature ranges, the models also captures the death of the larvae under extreme temperatures (12˚C &gt; T med &gt; 40˚C).

It is shown in [13, 39, 40] that the larvae grow faster with increase in feed availability and moisture. Growth rate, however, saturated with higher feed availability but significantly dropped at higher moisture concentration indicating larvae death. This interaction indicates that larvae ingest moist feed faster and the ingestion rate is limited by the size of the larvae mouth parts. Therefore, growth rate saturated despite excess feed being available. This is explained well by the model Eq (9) as shown in Fig 5 indicating that the feeding rate saturates despite increase in feed availability. The dependency of feed moisture modeled by the Eq (11), describes increasing ingestion rate with increasing moisture (0.25 g g -1 &gt; W med% &gt; 0.75 g g -1 ). This relationship between the larvae, feed availability and feed moisture is explained by the model presented in this work as seen in Fig 7(a).

Similar to any other resources consumed by the larvae for its growth, O2 concentration in the growing medium also plays as significant role as show in [19]. Since larvae grows in moist feed, factors such as depth and water concentration of the feed plays an important role in gas exchange. Similar to feed availability, growth rate increases with increase in air-flow rate but saturates at higher flow rate despite an increase in the flow rate as show in Fig 7(b). Also, as shown in [35], increasing the water concentration in feed could causes the larvae to drown and result in death due to decreased gas exchange. These dependencies between, water concentration, gas exchange, respiration and air-flow rate are captured in Eqs (12) and (14). From the results presented in Fig 7(a), it can be seen that the growth rate drops when moisture is &gt; 0.75 g g -1 indicating mortality at higher moisture concentrations.

Finally, the main focus of this work, to track the growth and development of the larvae over its lifetime (from neonate to pupae), dynamic model Eqs (4) and (5) are presented. The static model presented in [20] used a black-box modelling approach and only showed the larvae growth based on a single factor (i.e. diet quality). However, as shown in this work, it is important to consider other factors affecting the growth and development. Also, it is important to consider a dynamic modelling approach since it allows for accommodating the changes that take place within the larvae and their growing environment over the entire growth phase. These dynamics, as described using the regulation functions Eqs (17) to (19), explain the variation in the internal metabolic processes in response to the growing environment and the development stages. Results presented in Fig 8 show that the model proposed in this work describes the dynamic changes in larval dry mass over its growing phases, highlighting the conversion of feed into biomass. In addition, as shown in Fig 9, the model is also capable of accurately describing the growth, development time, and transition phases under different growing conditions aligning with the results presented in [13].

The models presented in this work have a broad application potential. All static models presented in this work can be used to compute certain static information that can be useful in planning the rearing process and designing the rearing environment. For example, temperature and air-flow rate dependency model, Eqs (6), (7) and (14), could be very useful in determining the heating, cooling, and air-flow requirements. Such information could be used to deduce requirements, in mass production context, for designing suitable reactors. Similarly, feed density and moisture models, Eqs (9) and (10), could be useful in preparing the feeding regimes and feed recipes for either better growth rate and reduced larval mortality or for better waste processing. The dynamic model, Eqs (4) and (5), serve as tools to compute dynamic information pertaining to the larvae growth and development. With these models, for any given sequence of growing conditions (changing over time) and initial larvae weight, it is possible to estimate/simulate the evolution of the larval dry mass and the resources consumed during the growth. Such simulations provide better understanding of the underlying process dynamics that are useful in designing algorithms that can control the reactors. Such models could also be used together with the dynamic models of the reactors to perform static and dynamic optimization of the growing process. Such optimization could be specifically designed for improved energy and resource efficiencies, in mass production context, as shown in [58].

## Conclusion

Based on comprehensive data sets aggregated from literature, various factors that affect the growth and development of larvae were analysed. Models were developed based on literature and based on the analysis of data to accurately and plausibly describe the influence of different environmental conditions such as temperature, feed density, feed moisture, and airflow rate on growth and development rates of BSF larvae. Building on the principles of mass balance, von Bertalanffy and DEB models, a novel dynamic model describing the growth and development of Hermetia illucens larvae was developed. Concept of development sum was proposed to establish a relationship between growth and development. The comprehensive dynamic model was obtained consisting of two differential equations, larval dry mass B dry and development sum T S , and combining the different rate equations. Model parameters were estimated for all the proposed models based on extensive data sets from different literature and the models were validated with R 2 &gt; 0.90 with only few exceptions. The resulting dynamic model describing the growth and development of the Hermetia illucens larvae was validated, using parameters obtained from only a subset of data, on all available data sets. The dynamic model, proposed and validated in this work, consistently explained: the change of larval dry mass over time; transition of development phase and its effect on growth; and influence of external factors on the larval growth and development. Performance of the model could be further improved with newer and larger data sets that could reveal other mechanisms or biological processes not explored in this work. Extension of this work with considerations for energy and resource efficient production of Hermetia illucens larvae in large scale production environments will be the future goal.

## Supporting information

S1 Dataset. Experiment data. This file contains the data for the moisture dependency experiment executed in this work. (XLSX)

S1 File. MATLAB files for model. The package contains MATLAB implementation of the dynamic model presented in this work. (ZIP)

## Acknowledgments

The authors acknowledge the inputs provided by the three anonymous reviewers for improving this manuscript. The authors would like to thank Wolf-Ju ¨rgen Trompke for his support in setting up the experiment facility used in this work.

## Author Contributions

Conceptualization: Arne-Jens Hempel, Stefan Streif.

Data curation: Murali Padmanabha.

Formal analysis: Murali Padmanabha, Alexander Kobelski.

Funding acquisition: Arne-Jens Hempel, Stefan Streif.

Investigation: Murali Padmanabha, Alexander Kobelski, Arne-Jens Hempel, Stefan Streif.

Methodology: Murali Padmanabha, Alexander Kobelski, Arne-Jens Hempel, Stefan Streif.

Project administration: Arne-Jens Hempel, Stefan Streif.

Resources: Stefan Streif.

Software: Murali Padmanabha.

Supervision: Arne-Jens Hempel, Stefan Streif.

Validation: Murali Padmanabha, Alexander Kobelski, Arne-Jens Hempel.

Visualization: Murali Padmanabha.

Writing - original draft: Murali Padmanabha.

- Writing - review &amp; editing: Murali Padmanabha, Alexander Kobelski, Arne-Jens Hempel, Stefan Streif.

## References

1. Newton GL, Booram CV, Barker RW, Hale OM. Dried Hermetia Illucens Larvae Meal as a Supplement for Swine. Journal of Animal Science. 1977; 44(3):395-400. https://doi.org/10.2527/jas1977.443395x
2. Barragan-Fonseca KB, Dicke M, van Loon JJA. Nutritional value of the black soldier fly (Hermetia illucens L.) and its suitability as animal feed-a review. Journal of Insects as Food and Feed. 2017; 3 (2):105-120. https://doi.org/10.3920/JIFF2016.0055
3. WangYS, Shelomi M. Review of Black Soldier Fly (Hermetia illucens) as Animal Feed and Human Food. Foods. 2017; 6(10). https://doi.org/10.3390/foods6100091 PMID: 29057841
4. Smetana S, Schmitt E, Mathys A. Sustainable use of Hermetia illucens insect biomass for feed and food: Attributional and consequential life cycle assessment. Resources, Conservation and Recycling. 2019; 144:285-296. https://doi.org/10.1016/j.resconrec.2019.01.042
5. Newton L, Sheppard D C, Watson D W, Burtle G, Dove C R, Tomberlin J, et al. The black soldier fly, Hermetia illucens , as a manure management/resource recovery tool. Symposium on the State of the Science of Animal Manure and Waste Management San Antonio, Texas, USA. 2005;.
6. Nguyen TTX, Tomberlin JK, Vanlaerhoven S. Ability of Black Soldier Fly (Diptera: Stratiomyidae) Larvae to Recycle Food Waste. Environmental Entomology. 2015; 44(2):406-410. https://doi.org/10.1093/ ee/nvv002 PMID: 26313195

7. Salomone R, Saija G, Mondello G, Giannetto A, Fasulo S, Savastano D. Environmental impact of food waste bioconversion by insects: Application of Life Cycle Assessment to process using Hermetia illucens. Journal of Cleaner Production. 2017; 140:890-905. https://doi.org/10.1016/j.jclepro.2016.06.154
8. Bava L, Jucker C, Gislon G, Lupi D, Savoldelli S, Zucali M, et al. Rearing of Hermetia Illucens on Different Organic By-Products: Influence on Growth, Waste Reduction, and Environmental Impact. Animals. 2019; 9(6). https://doi.org/10.3390/ani9060289 PMID: 31146401
9. Spranghers T, Ottoboni M, Klootwijk C, Ovyn A, Deboosere S, De Meulenaer B, et al. Nutritional composition of black soldier fly (Hermetia illucens) prepupae reared on different organic waste substrates. Journal of the Science of Food and Agriculture. 2017; 97(8):2594-2600. https://doi.org/10.1002/jsfa. 8081 PMID: 27734508
10. Chia SY, Tanga CM, Khamis FM, Mohamed SA, Salifu D, Sevgan S, et al. Threshold temperatures and thermal requirements of black soldier fly Hermetia illucens: Implications for mass production. PLOS ONE. 2018; 13(11):1-26. https://doi.org/10.1371/journal.pone.0206097 PMID: 30383771
11. Shumo M, Khamis FM, Tanga CM, Fiaboe KKM, Subramanian S, Ekesi S, et al. Influence of Temperature on Selected Life-History Traits of Black Soldier Fly (Hermetia illucens) Reared on Two Common Urban Organic Waste Streams in Kenya. Animals. 2019; 9(3). https://doi.org/10.3390/ani9030079 PMID: 30832335
12. Holmes LA, Vanlaerhoven SL, Tomberlin JK. Relative Humidity Effects on the Life History of Hermetia illucens (Diptera: Stratiomyidae). Environmental Entomology. 2012; 41(4):971-978. https://doi.org/10. 1603/EN12054
13. Diener S, Zurbru ¨gg C, Tockner K. Conversion of organic material by black soldier fly larvae: Establishing optimal feeding rates. Waste management &amp; research: the journal of the International Solid Wastes and Public Cleansing Association, ISWA. 2009; 27:603-10. https://doi.org/10.1177/ 0734242X09103838 PMID: 19502252
14. Harnden LM, Tomberlin JK. Effects of temperature and diet on black soldier fly, Hermetia illucens (L.) (Diptera: Stratiomyidae), development. Forensic Science International. 2016; 266:109-116. https://doi. org/10.1016/j.forsciint.2016.05.007 PMID: 27236368
15. Guo-Hui Y, Yi-Ping L, Yu-Huan Y, Qiang X. Effects of the artificial diet with low water content on the growth and development of the black soldier fly, Hermetia illucens (Diptera: Stratiomyidae). Acta Entomologica Sinica. 2014; 57(8):943.
16. Gligorescu A, Toft S, Hauggaard-Nielsen H, Axelsen JA, Nielsen SA. Development, metabolism and nutrient composition of black soldier fly larvae (Hermetia illucens; Diptera: Stratiomyidae) in relation to temperature and diet. Journal of Insects as Food and Feed. 2018; 4(2):123-133. https://doi.org/10. 3920/JIFF2017.0080
17. Meneguz M, Gasco L, Tomberlin JK. Impact of pH and feeding system on black soldier fly (Hermetia illucens, L; Diptera: Stratiomyidae) larval development. PLOS ONE. 2018; 13(8):1-15. https://doi.org/10. 1371/journal.pone.0202591 PMID: 30148867
18. Gligorescu A, Toft S, Hauggaard-Nielsen H, Axelsen JA, Nielsen SA. Development, growth and metabolic rate of Hermetia illucens larvae. Journal of Applied Entomology. 2019; 143(8):875-881. https:// doi.org/10.1111/jen.12653
19. Palma L, Ceballos SJ, Johnson PC, Niemeier D, Pitesky M, VanderGheynst JS. Cultivation of black soldier fly larvae on almond byproducts: impacts of aeration and moisture on larvae growth and composition. Journal of the Science of Food and Agriculture. 2018; 98(15):5893-5900. https://doi.org/10.1002/ jsfa.9252 PMID: 29999178
20. Sripontan Y, Chiu CI, Tanansathaporn S, Leasen K, Manlong K. Modeling the Growth of Black Soldier Fly Hermetia illucens (Diptera: Stratiomyidae): An Approach to Evaluate Diet Quality. Journal of Economic Entomology. 2019; 113(2):742-751. https://doi.org/10.1093/jee/toz337 PMID: 31836886
21. Padmanabha M, Streif S. Design and Validation of a Low Cost Programmable Controlled Environment for Study and Production of Plants, Mushroom, and Insect Larvae. Applied Sciences. 2019; 9(23). https://doi.org/10.3390/app9235166
22. von Bertalanffy L. Quantitative Laws in Metabolism and Growth. The Quarterly Review of Biology. 1957; 32(3):217-231. https://doi.org/10.1086/401873 PMID: 13485376
23. Kooijman SALM, Sousa T, Pecquerie L, Van Der Meer J, Jager T. From food-dependent statistics to metabolic parameters, a practical guide to the use of dynamic energy budget theory. Biological Reviews. 2008; 83(4):533-552. https://doi.org/10.1111/j.1469-185X.2008.00053.x PMID: 19016672
24. Banavar JR, Damuth J, Maritan A, Rinaldo A. Modelling universality and scaling. Nature. 2002; 420 (6916):626-626. https://doi.org/10.1038/420626a PMID: 12478280
25. Shi PJ, Ishikawa T, Sandhu HS, Hui C, Chakraborty A, Jin XS, et al. On the 3/4-exponent von Bertalanffy equation for ontogenetic growth. Ecological Modelling. 2014; 276:23-28. https://doi.org/10.1016/ j.ecolmodel.2013.12.020

26. Schremmer F. Die polymetabole Larval-Entwicklung der Waffenfliegenart Hermetia illucens.-Ein Beitrag zur Metamorphose der Stratiomyidae) / The polymetabol development of the soldier fly larva Hermetia illucens.-A contribution to the Metamorphosis of the Stratiomyidae. Annalen des Naturhistorischen Museums in Wien Serie B fu ¨r Botanik und Zoologie. 1984; 88/89:405-429.
27. Kim WT, Bae SW, Park HC, Park KH, Lee SB, Choi YC, et al. The larval age and mouth morphology of the black soldier fly, Hermetia illucens (Diptera: Stratiomyidae). International Journal of Industrial Entomology. 2010; 21(2):185-187.
28. Akers RC, Nielsen DG. Predicting Agrilus anxius Gory (Coleoptera: Buprestidae) Adult Emergence by Heat Unit Accumulation. Journal of Economic Entomology. 1984; 77(6):1459-1463. https://doi.org/10. 1093/jee/77.6.1459
29. Pruess KP. Day-Degree Methods for Pest Management1. Environmental Entomology. 1983; 12 (3):613-619. https://doi.org/10.1093/ee/12.3.613
30. Russelle MP, Wilhelm WW, Olson RA, Power JF. Growth Analysis Based on Degree Days1. Crop Science. 1984; 24(1). https://doi.org/10.2135/cropsci1984.0011183X002400010007x
31. McMaster GS, Wilhelm WW. Growing degree-days: one equation, two interpretations. Agricultural and Forest Meteorology. 1997; 87(4):291-300. https://doi.org/10.1016/S0168-1923(97)00027-0
32. Glasstone S, Laidler KJ, Eyring H. The Theory of Rate Processes. London: MacGraw-Hill Book Company; 1941.
33. Logan JA, Wollkind DJ, Hoyt SC, Tanigoshi LK. An Analytic Model for Description of Temperature Dependent Rate Phenomena in Arthropods 1. Environmental Entomology. 1976; 5(6):1133-1140. https://doi.org/10.1093/ee/5.6.1133
34. Monod J. THE GROWTH OF BACTERIAL CULTURES. Annual Review of Microbiology. 1949; 3 (1):371-394. https://doi.org/10.1146/annurev.mi.03.100149.002103
35. Fatchurochim S, Geden CJ, Axtell RC. FILTH FLY (DIPTERA) OVIPOSITION AND LARVAL DEVELOPMENTINPOULTRYMANUREOFVARIOUSMOISTURELEVELS.JournalofEntomological Science. 1989; 24(2):224-231. https://doi.org/10.18474/0749-8004-24.2.224
36. Richard TL, Walker LP, Gossett JM. Effects of Oxygen on Aerobic Solid-State Biodegradation Kinetics. Biotechnology Progress. 2006; 22(1):60-69. https://doi.org/10.1021/bp050171d PMID: 16454493
37. Liu X, Chen X, Wang H, Yang Q, ur Rehman K, Li W, et al. Dynamic changes of nutrient composition throughout the entire life cycle of black soldier fly. PLOS ONE. 2017; 12(8):1-21. https://doi.org/10. 1371/journal.pone.0182601 PMID: 28796830
38. Kooijman B, Kooijman S. Dynamic energy budget theory for metabolic organisation. Cambridge university press; 2010.
39. Barragan-Fonseca KB, Dicke M, van Loon JJA. Influence of larval density and dietary nutrient concentration on performance, body protein, and fat contents of black soldier fly larvae (Hermetia illucens). Entomologia Experimentalis et Applicata. 2018; 166(9):761-770. https://doi.org/10.1111/eea.12716 PMID: 30449896
40. Cheng JYK, Chiu SLH, Lo IMC. Effects of moisture content of food waste on residue separation, larval growth and larval survival in black soldier fly bioconversion. Waste Management. 2017; 67:315-323. https://doi.org/10.1016/j.wasman.2017.05.046 PMID: 29040452
41. Jucker C, Erba D, Leonardi MG, Lupi D, Savoldelli S. Assessment of Vegetable and Fruit Substrates as Potential Rearing Media for Hermetia illucens (Diptera: Stratiomyidae) Larvae. Environmental Entomology. 2017; 46(6):1415-1423. https://doi.org/10.1093/ee/nvx154 PMID: 29040452
42. Manurung R, Supriatna A, Esyanthi RR, Putra RE. Bioconversion of rice straw waste by black soldier fly larvae (Hermetia illucens L.): optimal feed rate for biomass production. J Entomol Zool Stud. 2016; 4 (4):1036-1041.
43. Gao Z, Wang W, Lu X, Zhu F, Liu W, Wang X, et al. Bioconversion performance and life table of black soldier fly (Hermetia illucens) on fermented maize straw. Journal of Cleaner Production. 2019; 230:974-980. https://doi.org/10.1016/j.jclepro.2019.05.074
44. Diener S, Zurbru ¨gg C, Gutie ´ rrez FR, Nguyen DH, Morel A, Koottatep T, et al. Black soldier fly larvae for organic waste treatment-prospects and constraints. In: 2nd International Conference on Solid Waste Management in Developing Countries; 2011.
45. Joly G, Nikiema J. Global experiences on waste processing with black soldier fly (Hermetia illucens): from technology to business. vol. 16. IWMI; 2019.
46. Permana A, Putra J. Growth of Black Soldier Fly (Hermetia illucens) Larvae Fed on Spent Coffee Ground. IOP Conference Series: Earth and Environmental Science. 2018; 187:012070. https://doi.org/ 10.1088/1755-1315/187/1/012070
47. Larde ´ G. Recycling of coffee pulp by Hermetia illucens (Diptera: Stratiomyidae) larvae. Biological Wastes. 1990; 33(4):307-310. https://doi.org/10.1016/0269-7483(90)90134-E

48. Bondari K, Sheppard DC. Soldier fly larvae as feed in commercial fish production. Aquaculture. 1981; 24:103-109. https://doi.org/10.1016/0044-8486(81)90047-8
49. Ferrarezi R, Cannella L, Nassef A, Bailey D. UVI/AES Annual Report 2016-Alternative Sources of Food for Aquaponics in the U.S. Virgin Islands: A Case Study with Black Soldier Flies; 2016.
50. Kroeckel S, Harjes AGE, Roth I, Katz H, Wuertz S, Susenbeth A, et al. When a turbot catches a fly: Evaluation of a pre-pupae meal of the Black Soldier Fly (Hermetia illucens) as fish meal substitute Growth performance and chitin degradation in juvenile turbot (Psetta maxima). Aquaculture. 2012; 364-365:345-352.
51. Tomberlin JK, Adler PH, Myers HM. Development of the Black Soldier Fly (Diptera: Stratiomyidae) in Relation to Temperature. Environmental Entomology. 2009; 38(3):930-934. https://doi.org/10.1603/ 022.038.0347 PMID: 19508804
52. Meneguz M, Schiavone A, Gai F, Dama A, Lussiana C, Renna M, et al. Effect of rearing substrate on growth performance, waste reduction efficiency and chemical composition of black soldier fly (Hermetia illucens) larvae. Journal of the Science of Food and Agriculture. 2018; 98(15):5776-5784. https://doi. org/10.1002/jsfa.9127 PMID: 29752718
53. Lalander C, Diener S, Zurbru ¨gg C, Vinner å s B. Effects of feedstock on larval development and process efficiency in waste treatment with black soldier fly (Hermetia illucens). Journal of Cleaner Production. 2019; 208:211-219. https://doi.org/10.1016/j.jclepro.2018.10.017
54. Parra Paz AS, Carrejo NS, Go ´mez Rodrı ´guez CH. Effects of Larval Density and Feeding Rates on the Bioconversion of Vegetable Waste Using Black Soldier Fly Larvae Hermetia illucens (L.), (Diptera: Stratiomyidae). Waste and Biomass Valorization. 2015; 6(6):1059-1065. https://doi.org/10.1007/s12649015-9418-8
55. Nguyen TTX, Tomberlin JK, Vanlaerhoven S. Influence of Resources on Hermetia illucens (Diptera: Stratiomyidae) Larval Development. Journal of Medical Entomology. 2013; 50(4):898-906. https://doi. org/10.1603/ME12260 PMID: 23926790
56. Holmes L, Vanlaerhoven S, Tomberlin J. Lower temperature threshold of black soldier fly (Diptera: Stratiomyidae) development. Journal of Insects as Food and Feed. 2016; 2:1-8.
57. Tomberlin JK, Sheppard DC, Joyce JA. Selected Life-History Traits of Black Soldier Flies (Diptera: Stratiomyidae) Reared on Three Artificial Diets. Annals of the Entomological Society of America. 2002; 95 (3):379-386. https://doi.org/10.1603/0013-8746(2002)095%5B0379:SLHTOB%5D2.0.CO;2
58. Padmanabha M, Beckenbach L, Streif S. Model predictive control of a food production unit: a case study for lettuce production. In: 21st IFAC World Congress 2020; 2020.