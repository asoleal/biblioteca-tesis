<!-- image -->

## Original papers

## Modelling and optimal control of growth, energy, and resource dynamics of Hermetia illucens in mass production environment

Murali Padmanabha, Alexander Kobelski, Arne-Jens Hempel, Stefan Streif ∗

Automatic Control and System Dynamics Lab, Technische Universität Chemnitz, Chemnitz, 09107, Germany

## A R T I C L E I N F O

Keywords: Hermetia illucens mass production Mass and energy flux modelling Energy and resource optimization Process design and control Bioreactor optimal control

## 1. Introduction

Hermetia illucens also commonly known as Black soldier fly (BSF) is widely researched for its use in animal feed production and bio waste management and recycling processes. Their rapid growth and robust bio-waste conversion capabilities have gained attention and have proven Hermetia illucens to be a suitable candidate for efficient biomass production.

Several studies have been performed to understand the requirements for both rearing of larvae for proteins and rearing of flies for reproduction (Bondari and Sheppard, 1981; Newton et al., 1977; Tomberlin et al., 2009; Barragan-Fonseca et al., 2017). Some of these works have even proposed static models describing the growth rates as a function of growing conditions (Chia et al., 2018; Gligorescu et al., 2019; Shumo et al., 2019; Palma et al., 2018; Padmanabha et al., 2020b). A significant number of publications focussing on the waste

∗

Corresponding author.

E-mail addresses: murali.padmanabha@etit.tu-chemnitz.de (M. Padmanabha), alexander.kobelski@etit.tu-chemnitz.de (A. Kobelski), arne-jens.hempel@etit.tu-chemnitz.de (A.-J. Hempel), stefan.streif@etit.tu-chemnitz.de (S. Streif).

Received 22 November 2021; Received in revised form 2 November 2022; Accepted 10 January 2023

Available online 24 January 2023

## A B S T R A C T

Mass production of Hermetia illucens insect larvae is now being adopted in many countries and is taking an industrial production approach. Despite abundant literature on factors that affect larvae growth and the optimal static parameters identified in laboratory setup, for an industrial production process it is necessary to identify the trajectories such that the growth as well as the production process is optimal. To achieve this in this work, some of the important requirements and challenges involved thereof are identified and objectives of the automation process are formulated within a model based optimal control setup. Mechanistic models necessary for the optimization framework are derived as differential equations that describe the dynamic variation of resources (feed, water, O 2 etc.), energy, and larval biomass. In addition, the elevated metabolic activity of larvae corresponding to the final instar development is identified and also modelled based on the observation from experiments. The mass and energy balance approach used in modelling enables the quantification and distinction of the mass and energy flux components in various levels (e.g. larvae body, growing medium, production environment, and external environment) while holding its applicability for both open and closed/reactor based production setups. Finally, the trajectories generated using the synthesized optimal controller are tested under different scenarios showcasing significant reduction in resource consumption compared to a constant set-point operation of the production setup. Results presented in this work not only showcase the potential of the mechanistic models and their application in identifying the relevant process parameters (e.g. reactor properties such as volume, thermal conductivity, actuator capacities), but most importantly in optimizing the process dynamically and tuning the process objectives as desired (e.g. maximize larvae mass, reduce energy).

conversion efficiencies of the BSF larvae can be found (Diener et al., 2009; Parra Paz et al., 2015; Manurung et al., 2016; Gao et al., 2019; Lalander et al., 2019). More recent literatures show the transition of biomass conversion efficiency studies performed in labs to large scale production environments (Miranda et al., 2020; Scala et al., 2020). These trends indicate that the mass production of insect larvae is now being adopted in many countries and is taking an industrial production approach. Irrespective of the application of BSF larvae to produce high quality protein rich animal feed or to simply accelerate the reduction of biological waste, there are no studies or literature on the automation and control of the processes involved.

Some of the state of the art and relevant work which provide insights to the challenges involved in the production and facilitate the development of models are presented here. The threshold temperatures and thermal requirements were highlighted by Chia et al. (2018). A

Contents lists available at ScienceDirect

## Computers and Electronics in Agriculture

journal homepage: www.elsevier.com/locate/compag

<!-- image -->

<!-- image -->

Table 1 Process v.s. model requirements.

|   # | Process                                                                                           | Model requirement                                                                                              |
|-----|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
|  1. | Dynamic temperature control regime to promote growth and development                              | Dynamic variation of temperature in substrate due to metabolic activity and heat exchange with the environment |
|  2. | Ventilation strategies for growth promoting gas concentration and low toxic gas accumulation      | Dynamic gas concentration changes due to metabolic activity and exchange with environment                      |
|  3. | Water content regulation for moist substrate during growth phase and dry substrate for extraction | Dynamic change in substrate moisture content and evaporation                                                   |
|  4. | Feeding strategies for optimal feed consumption and less waste generation                         | Dynamic change in nutrition content and accumulation of waste (faeces and exhausted feed) in substrate         |
|  5. | In-situ monitoring/estimation of larval growth and substrate properties                           | Dynamic change in individual substrate component (feed, larvae, water) masses                                  |
|  6. | Maximize larvae dry-mass production                                                               | Dynamic growth and development changes and its dependency on the influence of growing conditions               |

comparison of the development rates over different temperature ranges was presented by Shumo et al. (2019). The effect of humidity on the egg eclosion and adult emergence were studied by Holmes et al. (2012). The influence of diet, its moisture content and the temperatures were presented together to showcase its importance in the development of the larvae (Diener et al., 2009; Harnden and Tomberlin, 2016; Guo-Hui et al., 2014; Gligorescu et al., 2018). The effects of moisture content in food waste on residue separation was presented by Cheng et al. (2017) showing the importance of the moisture in post-processing. Another study by Meneguz et al. (2018), showed the effects of pH levels of the substrate (feed), in which larvae are grown, on the larval development. Despite a large number of literature on BSF production, studies on this process optimization is limited to identifying the optimal static condition such as optimal but constant set-points for temperature (Chia et al., 2018), feeding rate (Diener et al., 2009), feed components (Lee et al., 2021), etc., that result in better biomass production. In order to perform a dynamic optimization of the rearing process including the energy and resources involved, it is necessary to identify various aspects of the production process and derive dynamic models that describe these aspects.

Based on the state of the art literature and industrial practices, some of the challenges inherent to the automation and optimization of commercial production of the Hermetia illucens larvae have been identified in this work. Firstly, high substrate temperature and moisture requirements pose the problem of increased evaporation. At lower temperatures, metabolic activity and thus the growth rate is reduced. Depending on food quality and larval density, the peak metabolic activity of the larvae generate heat and result in substrate temperatures up to 45 ° C . This requires cooling down the substrate to reduce the mortality rate of the larvae. Secondly, the fast metabolic rates in larvae results in increased oxygen consumption and depending on the feed, the rates of carbon dioxide and ammonia production also increases. This requires frequent supply of fresh air which also accelerates the evaporation of water from the substrate. Thirdly, the moisture content of the substrate has to be high enough to render it edible for the young larvae. Depending on the harvesting procedure, the substrate has to be dry to reliably separate the larvae from the substrate, which conflicts with the moisture requirements for the larvae growth. Finally, for production of larvae under constrained resources, it is necessary to find the optimal growing conditions that can result in resource and/or cost savings.

In order to address the above identified challenges, the process involved and the corresponding model requirements are formulated as in Table 1.

The dynamic models presented in our previous work (Padmanabha et al., 2020b) fulfil only the requirement 6 , which is critical since the optimization depends on the larvae biomass changes. To the best knowledge of the authors, there exists no other work that satisfies the other models requirements ( 1 -5 ). This also follows that no literature has addressed the automation strategies or the application of optimal control in the context of Hermetia illucens production. This work addresses both these aspects by firstly, defining the optimal control framework to meet the process objectives defined above and secondly, deriving all the necessary detailed mechanistic models . The models derived in this work use the biomass growth and larvae development model presented in our previous work (Padmanabha et al., 2020b) to obtain the production and consumption of various energy and resource fluxes that depend on the evolving dry mass of the larvae. Also, the data necessary to analyse the process and complete the models are obtained using our previously developed laboratory scale production environment (Padmanabha and Streif, 2019). Along with the application in optimal control, the models presented in this work can also be used to perform simulation studies of the growth and production process, design of control policies for the large scale production, etc.

The following sections provide a detailed approach taken to define the control goals, develop the necessary models, analyse the experiment data sets, obtain the model parameters, and evaluate the performance of the implemented control framework. Firstly, in Section 2.1, a typical production setup is described along with a mathematical notation of its system states and the flow of various resources. Also, an optimal control problem is formulated for the production process based on the desired control objectives. This is followed by, in Section 2.3, the details on extending the models of the previous work and obtaining the resource and energy flux models for the production setup. In Section 2.4, the process used to obtain the experiment data and the mathematical tools used to solve the optimal control problem and the parameter estimation problems are described. The results of the model simulation are compared with the actual measurement data and the quality of fit is determined in Section 3.1. Finally, in Sections 3.2 and 3.3, the application of the model derived in this work for process analysis and specifically for the optimization of resources using a model based controller is showcased.

## 2. Materials and methods

In this section, an overview to a typical production setup is presented with all the state variables, control variables and disturbances or external resources. Based on this, the setup of the optimal control framework is described followed by the detailed modelling of the resource and energy fluxes between various components in the production setup. The experiments performed to study the process are described along with the setup used for the model parameter identification.

Table 2 List of symbols used to describe the states, disturbances, and inputs of the system.

| Symbol           | Description                                                                | Unit       |
|------------------|----------------------------------------------------------------------------|------------|
| State variables: |                                                                            |            |
| 𝐿 num            | number of larvae in the growing medium                                     | [-]        |
| 𝑇 Σ              | development sums used to track the developmental stage of larva            | [ h ]      |
| 𝐵 dry            | dry mass per larva                                                         | [ g ]      |
| 𝐵 wet            | wet mass per larva                                                         | [ g ]      |
| 𝐵 med            | combined mass of larvae, water, and feed                                   | [ kg ]     |
| 𝐵 tot            | total dry mass of all larvae in substrate                                  | [ g ]      |
| 𝑁 med            | total substrate (feed and excreta) dry mass in medium                      | [ kg ]     |
| 𝑁 feed           | total unused feed in substrate                                             | [ kg ]     |
| 𝑁 exc            | larvae excreta present in substrate                                        | [ kg ]     |
| 𝑊 med            | total water in the growing medium                                          | [ kg ]     |
| 𝑇 med            | temperature of growing medium                                              | [ ° C ]    |
| 𝑇 air            | temperature of air in production environment                               | [ ° C ]    |
| 𝐶 air            | CO 2 concentration of air in production unit                               | [ kgm -3 ] |
| 𝐻 air            | absolute humidity of the air in production unit                            | [ kgm -3 ] |
| 𝑂 air            | O 2 concentration of air in production unit                                | [ kgm -3 ] |
| 𝑇 chm            | temperature on surface of walls of production system/reactor               | [ ° C ]    |
| 𝑇 hx +           | temperature of the heat exchanger inside production system                 | [ ° C ]    |
| 𝑊 chm +          | total water or condensate on the inner walls of the production environment | [ kg ]     |
| 𝑊 hx +           | total water or condensate on the surface of the heat exchanger             | [ kg ]     |
| Disturbances or  | external resources:                                                        |            |
| 𝐶 out            | CO 2 concentration of external source                                      | [ kgm -3 ] |
| 𝑇 out            | temperature of outside air                                                 | [ ° C ]    |
| 𝐻 out            | absolute humidity of external source                                       | [ kgm -3 ] |
| 𝑊 out            | water in the external source                                               | [ kg ]     |
| 𝑁 out            | Nutrients or feed in the external source                                   | [ kg ]     |
| 𝐸 out            | (electrical) energy from the external source                               | [ W ]      |
| Input variables: |                                                                            |            |
| 𝑢 v              | input signal to ventilator pump                                            | [-]        |
| 𝑢 d              | input signal to opening of the door                                        | [-]        |
| 𝑢 H              | input signal to humidifier                                                 | [-]        |
| 𝑢 T              | input signal to heater/cooler                                              | [-]        |
| 𝑢 N              | input signal to feeder                                                     | [-]        |
| 𝑢 W med          | input signal to water pump for growing medium                              | [-]        |
| 𝑢 fan            | input signal to blower/fan for air flow                                    | [-]        |
| 𝑢 h              | removal/harvesting of larvae from substrate                                | [-]        |
| 𝑢 W sto +        | input signal to water pump for storage tank for humidifier                 | [-]        |
| 𝑢 W ovf +        | input signal to water pump for condensate removal                          | [-]        |
| 𝑢 I 𝑖 +          | input to LED channel number 𝑖                                              | [-]        |

+ Reactor specific variables.

## 2.1. Overview of the production setup and the requirements for automation and control

To provide an overview of a production setup and to transition to the model development process, an overview of all the state variables, inputs, and disturbances or external resources are listed in Table 2.

A typical production setup, as illustrated in Fig. 1, consists of several growing trays filled with substrate made of feed and water and populated with young larvae neonates. The growing trays consisting of the substrate and the larvae are referred to as growing medium. The environment where the growing mediums are placed are referred to as production environment in this work. The environment where the production setup is located and the resources are sourced is referred to as external or outside environment.

The production environment may be completely closed, partially closed, or fully open. In a completely closed setup, as in case of complex closed bioreactors, all the resources (air, heat, humidity, water) to the production environment are supplied from external sources or generated using actuators. Such closed production setup can be described as

<!-- formula-not-decoded -->

where 𝒙 is a set of all state variables, 𝒖 is a set of all input variables and 𝒅 is a set of all disturbances or external resources. In case of a partially closed setup as in case of large halls, resources available from external environment are supplied through ventilation and partly modified (heating, cooling, humidification, dehumidification) using actuators. Such production setup are easy to establish and are less complex due to the fewer number of actuator compared to the closed setup and thus can only be partly automated/controlled. Such production setups can be described as

<!-- formula-not-decoded -->

with 𝑢 ΔT and 𝑢 ΔH representing the modification (addition or removal) done to the temperature 𝑇 out and humidity 𝐻 out of the external air such that 𝑇 air = 𝑇 out + 𝑢 ΔT and 𝐻 air = 𝐻 out + 𝑢 ΔH . Finally, a completely open setup is where the external and production environment are the same and no additional actuator exist for the modification of the environment ( 𝒖 = [ 𝑢 Wmed ] ). Based on the description of the different possible production setups, the optimal control task for automation and resource optimization can be formulated specifically.

## 2.2. Model based controller synthesis for production process optimization

To apply the optimal control framework to a process, the process goals need to be formulated as an objective function. In this work we formulate the objective function and thus the optimal control problem based on the process goals listed in Table 1. Such optimal control formulation are applied in greenhouses for automation and resource optimization (van Straten et al., 2011; Padmanabha et al., 2020a). It is also widely accepted for control process optimization (Zhang et al., 2020) and also applied in aquaculture and aquaponics for optimal fish growth and resource utilization (Cacho et al., 1991; Karimanzira et al., 2017; Chahid et al., 2021).

Fig. 1. Overview of the larvae production setup and the internal resource flows. It consists of a growing medium filled with larvae and feed, placed in either a closed or an open production environment. The valves representing the rates labelled as 𝑟 resp and 𝑟 assim are internally regulated by the larvae and the substrate states. Circular valves labelled 𝑢 xyz represent the control signals that control the flow of resources (fluxes).

<!-- image -->

Given the models of the larvae dynamics, substrate dynamics, and the surrounding environment, the optimization/optimal control problem can be defined as

<!-- formula-not-decoded -->

where 𝛼 1 , 𝛼 2 , and 𝛼 3 correspond to the weights for adjusting the process goals of maximum dry-mass v.s. dry substrate v.s. minimum feed waste at harvest 𝑡 h respectively, 𝐑 is a weight matrix that defines the cost of operation of the actuators for the entire production time, ̇ 𝒖 is the derivative of 𝒖 with respect to time representing the change rate of the actuators signals, the matrix 𝐒 defines the penalization of fast or sudden changes in the values of the actuators during the entire production time, ̇ 𝒙 the derivative of 𝒙 with respect to time, 𝐩 is the model parameter vector,  ,  , and  are the sets that define the permitted values and bounds for the state variables, inputs, and input rate change respectively. The values of 𝛼 1 , 𝛼 2 , 𝛼 3 and 𝐑 selected in this work do not correspond to actual monetary value but rather normalized values for tuning the resource utilization profile. To solve the optimal control problem formulated by Eq. (3), the system dynamics are necessary and will be derived in the following section.

## 2.3. Modelling the larvae production process

The models describing the growth and development of a larva presented by Padmanabha et al. (2020b) are first used to obtain the models of the resource and energy flux generated by the larvae. Using these flux models, the detailed models representing the different energy and resource fluxes as well as the dynamic changes of the states in a typical production setup are modelled. Some of these flux terms that originate in the production environment are independent of the organism growing inside and thus allows for the reuse of models or parts of model equations for production of other organisms as well as other production setups. In this work, the model equations presented in our previous work on lettuce production (Padmanabha et al., 2020b) are reused to derive the actuator contributed fluxes (e.g. TEC heatingcooling system and LEDs). A list of all the energy and resources fluxes used for modelling are summarized in the Table A.1 in Appendix A for reference.

2.3.1. Extension of the dynamic growth and development models of larvae The equation representing the dry mass change in the larvae as presented in Padmanabha et al. (2020b) is given as

<!-- formula-not-decoded -->

where 𝜙 Bing is feed flux to larvae, 𝜙 Bexcr is the non digested feed flux back to the substrate, 𝜙 Bassim is feed spent in assimilation process, 𝜙 Bmaint is the assimilates spent for basal maintenance of existing structure, 𝜙 Bmat is the assimilates spent for generating new structure and 𝜙 Bmetab represents all the assimilates consumed for metabolic activities.

This equation (4) of Padmanabha et al. (2020b) combines both the maintenance and maturity as a single process due to data unavailability for validation. However, in this work we explicitly model maturity and maintenance process and quantify the biomass flux 𝜙 Bmat responsible for the larvae final maturity as

<!-- formula-not-decoded -->

where 𝜖 inges = (1 𝑘 𝛼 excr -𝑘 𝛼 assim ) , represents the efficiency of the feed, and 𝑟 assim , 𝑟 maint , and 𝑟 mat being the assimilation rate, maintenance rate, and maturity rate functions respectively. The rate function 𝑟 assim remains unchanged from the original work. However, the maintenance and maturity rate functions are defined in this work as two separate rate functions.

The maintenance rate function is given as

<!-- formula-not-decoded -->

where 𝑟 T ( 𝑇 med ) 𝑘 r max T , 𝑟 F grw ( 𝐵 feed ) 𝑘 r max gm , and 𝑟 A ( 𝐴 air ) 𝑘 r max A are the normalized growth regulation rate functions dependent on the substrate temperature, feed, and air concentration respectively and 𝑘 r max T , 𝑘 r max gm , and 𝑘 r max A are the maximum observed growth rates under optimum substrate temperature, feed, and air concentrations respectively. Since the larvae also undergo morphological changes during the larval phase, referred to as instars, it is necessary to know the development age at which these transitions occur. For this purpose, we introduced the concept of development sums 𝑇 Σ in our previous work (Padmanabha et al., 2020b) which is the integration of growing conditions dependent development rates that indicate how much the larvae have developed through the larval stage. However, analysis of the experiments reveal that the final transformation to prepupae, referred to as maturity in this work, results in elevated metabolic rates. The maturity process representing the transformation of the larvae to its final instar is now defined as a switching process that is activated when the larvae reach certain development sums ( 𝑇 Σ ). This is given as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where 𝑟 Bmat is the maturity process activation function that only activates when development sums is between 𝑘 T 𝛴 1 and 𝑘 T 𝛴 3 .

We also introduce a new state variable for the larvae model in this work to consider the wet body mass change. Modelling of the wet mass change of the larvae is of interest since it allows for accurate modelling of the water flux and also implementing the in-situ mass monitoring in the production process. This wet mass of the larvae can be obtained as the sum of dry mass and the water balance through assimilation and maintenance as

<!-- formula-not-decoded -->

where 𝜙 Wassim and 𝜙 Wmaint are the water assimilated into the larva and spent for the metabolic activity respectively. Finally, in this work, we consider the feed in substrate 𝐵 feed = 𝑁 feed and substrate moisture concentration 𝑊 med% = ( 𝑊 med 𝑊 med + 𝑁 med ) and air concentration 𝐴 air = 𝑂 air 𝐶 air . The remaining model equation corresponding to the larvae are used as presented by Padmanabha et al. (2020b), unchanged.

## 2.3.2. Energy and resource flux components contributed by larvae and microbiome

The resource fluxes (heat, gas, humidity/water) contributed by different processes i.e. assimilation respiration, maintenance, maturity and microbiome activity are modelled in this section.

The metabolic activities are exothermic both in the larvae and the microbiome present in the substrate and thus generate heat as a byproduct. Microbiome gets introduced into the growing medium through the feed and also the guts of the larvae. This cannot be avoided and should be considered as part of the process. The heat produced by the larvae and the microbiome in the growing medium can be described as a sum of different metabolic processes as

<!-- formula-not-decoded -->

where 𝐿 num is the number of larvae in the substrate, 𝑘 Qassim , 𝑘 Qmaint , and 𝑘 Qmat represents the heat produced due to the assimilation, maintenance and maturity of the larvae respectively and 𝑘 Qbio is the heat produced by the microbiome per gram of feed in growing medium. Net water assimilated by the larvae is modelled to be proportional to the rate of assimilation of feed and maintenance expense as

<!-- formula-not-decoded -->

where 𝑘 wassim is the specific water consumption per gram feed assimilated by the larvae. The influence of the metabolic activity on the gas flux can be modelled as

<!-- formula-not-decoded -->

where 𝑘 Cassim , 𝑘 Cmaint , and 𝑘 Cassim are specific CO 2 production rates of the assimilation, maintenance and maturity process respectively, 𝑘 Cbio is the specific CO 2 production due to the microbiome growth and 𝑘 bio C∶O is the carbon-oxygen ratio of all the processes. The feed in growing medium is mostly consumed by larvae and partly by microbiome. Ignoring the feed consumption by microbiome, the feed ingestion and excretion flux from the substrate are given respectively as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

With the resource fluxes contributed by the larvae and microbiome modelled, the resource and energy fluxes in the production environment are modelled next.

## 2.3.3. Modelling resource and energy dynamics in larvae production

An overview of the actuators that influence the inputs, sensors that measure certain states and the important energy and mass fluxes are visualized in Fig. 2. This represents a fully closed or reactor type production setup presented in Padmanabha and Streif (2019) and is referred to as production unit in this work. The models proposed in this work is derived for the complex reactor type setup and identifies all the flux components. These flux terms and the corresponding model parameter values can be adapted to different production setups by performing parameter calibration.

Mass fluxes (e.g. water, water vapour, CO 2 , O 2 ) and energy fluxes (e.g. heat and light) in the production unit can be mechanistically described using mass and energy balance equations. These fluxes and the influence they have on various states are presented as differential equations that describe the rate change of the states in response to the net flux changes.

Firstly, the rate of change of temperature of the air inside the production unit can be modelled as

<!-- formula-not-decoded -->

where 𝑘 Cair is the total heat capacity of the air in the production unit, 𝜙 QLED , 𝜙 Qhx-a and 𝜙 Qexch are the heat fluxes contributed by the actuators (LED, heater-cooler and ventilator pumps respectively), 𝜙 Qleak and 𝜙 Qdoor are the losses due to leakage and the door opening event respectively, 𝜙 Qm-a is the convective heat flux between the air and the growing medium and 𝜙 Qa-c is the convective flux between the air and the walls of the production environment.

Change in temperature in the growing medium can be summarized as

<!-- formula-not-decoded -->

where 𝑘 Cmed is the total heat capacity of the growing medium, 𝜙 Qbio , 𝜙 Qm-c , and 𝜙 QL , med are, respectively, the heat fluxes due to the metabolic activity of larvae and microbiome, conductive heat transfer to the walls and latent heat of evaporation and condensation taking place in the growing medium.

Chamber unit

Fig. 2. Production unit components and fluxes in larvae production. Production unit with sensors (S1-S5), air pumps (M1-M2), water pumps (M3-M4), air conditioning unit (based on thermoelectric cooler (TEC) for heating, cooling, and condensation), humidifier, and LED lighting as presented in Padmanabha and Streif (2019).

<!-- image -->

The heater-cooler system consists of a heat exchanger with mass and stores heat during operation. Therefore the heat transfer from the heat exchanger to the air depends on its current temperature which can be modelled as

<!-- formula-not-decoded -->

where 𝑘 Chx is the heat capacity of the heat exchanger, 𝜙 QTEC is the heat energy supplied by TEC, 𝜙 Qhx-a , 𝜙 Qc-hx and 𝜙 QL , hx are the convective transfer to air, conductive transfer to walls and latent heat of condensation and evaporation from the surface of the heat exchanger.

The temperature on the walls of the production unit varies depending on the air inside 𝑇 air , the air outside 𝑇 out , and its total heat capacity. This heat change is given as

<!-- formula-not-decoded -->

where 𝑘 Cchm is the heat capacity of the walls, 𝜙 Qc-o , 𝜙 Qc-TEC and 𝜙 QL , chm are the convective heat loss to the outside air, conductive heat flux from heat exchanger to the walls and the latent heat of condensation and evaporation from wall respectively.

The humidity in the production unit can be modelled as the mass transfer between different surfaces as

<!-- formula-not-decoded -->

where 𝑘 Vchm is the inner volume of the production unit, 𝜙 Hu , 𝜙 Hexch , 𝜙 Hleak , 𝜙 Hdoor are the water vapour fluxes due to the humidifier, ventilation, leakage, and door opening events respectively, 𝜙 WL , chm , 𝜙 WL , hx , and 𝜙 WL , med are evaporation-condensation on the production unit walls, heat exchanger surface and the growing medium surface respectively.

Change in water quantity in the growing medium is given by

<!-- formula-not-decoded -->

where 𝜙 Wu , 𝜙 WL , med , 𝜙 Wbio are the water fluxes due to the input water pump, evaporation-condensation from the air-growing medium surface, and the larvae and microbiome assimilation process respectively.

Due to the temperature gradients between the surfaces of the production unit inner wall, the heat exchanger, and the air, water transport takes place resulting in evaporation and condensation. Water condenses on the surfaces when temperature of walls are colder, influencing the thermal conductivity, and evaporates when temperature of walls are higher. When sufficient water is collected, the water forms droplets and flows into the respective collection tanks. Quantification of this condensate will further extend the model in completing the water flux components. These fluxes for both heat exchanger surface and the wall surface can be modelled as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where 𝜙 WL , chm , 𝜙 WL , hx are the water flux due to condensation-evaporation and 𝜙 Wchm , out , 𝜙 WTEC , out are the condensate that trickles down respectively from the surface of the walls and TEC respectively.

The gas concentration in the production unit also changes due to the larval and microbiome metabolic activities. The CO 2 and similarly O 2 variation can be modelled as

<!-- formula-not-decoded -->

where 𝜙 Cexch , 𝜙 Cleak , and 𝜙 Cbio are the CO 2 fluxes due to ventilation, leakage and the metabolic activities of the larvae and the microbiome respectively. Similarly, the O 2 flux can be either derived from Eq. (23) assuming that the O 2 production is proportional to CO 2 or as an independent state as

<!-- formula-not-decoded -->

where 𝑘 C∶O represents the number of O 2 molecules consumed for every CO 2 molecules produced.

The feed in the growing medium is consumed by the larvae and the microbiome and is converted into biomass. This massflux of the substrate dry mass can be modelled as

<!-- formula-not-decoded -->

where 𝜙 Nu represents the feed input to the growing medium, 𝜙 Ning represents the feed ingested by the larvae, 𝜙 Nexc represents the feed excreted back, and 𝜙 Nbiome represents the feed consumed by the microbiome.

In case of the batch feeding regime, feed is introduced only at the beginning of the growth process. In this case, the nutrition or quality of the feed goes down over time as the larvae ingests and excretes. This is simply modelled as an integrator integrating the excreted feed in the growing medium as

<!-- formula-not-decoded -->

Finally, the rate change of total mass of the growing medium which can be tracked during production using in-situ measurements can be modelled as

<!-- formula-not-decoded -->

where 𝐿 num is the total number of larvae present in the medium and d 𝐵 wet d 𝑡 represents the rate of change of wet mass of the larva.

The derivation of all the flux components of the production unit are presented in detail in the Appendix A.1.

## 2.4. Data, parameter estimation, and model validation

The data to perform the model validation and parameter estimation are obtained through experiments executed in the production unit described by Padmanabha and Streif (2019) and are presented in Fig. B.1 in Appendix B.1. Two different experiments, larvae growth and thermodynamics, were performed to obtain data with and without the substrate and larvae. These two data sets enable to identify and differentiate the influence of larvae and substrate containing microbiome on the energy and resource fluxes in the production environment.

Thermodynamics, heat, and water flux experiments (TD1-TD6). Tests were performed under different conditions to study the heat and humidity fluxes in the absence of any larvae and feed. The data obtained in these experiments are mainly used to characterize and obtain model parameters of the production setup. The details of these experiments and the resulting goodness of fit of the models with identified parameters are included in Appendix B.2 and B.3 respectively.

Larvae growth experiments (TG1-TG3). The influence of temperature on larval growth and the dynamic changes of resources was studied in this experiment separately under three different constant air temperatures 𝑇 air (TG1: 25 ° C , TG2: 29 ° C and TG3: 33 ° C ). For this study, young larvae aged 7-10 days with mean dry mass of 4 . 28 mg each and dry feed consisting of one part wheat bran dry matter and three parts pig feed were obtained from Hermetia Baruth GmbH. Substrate was prepared by mixing one part dry feed and three parts water. About 2000 larvae and 2.0 kg of substrate were introduced in a stainless steel tray achieving a substrate depth of about 3-5 cm in each experiment. The production units were operated with constant temperatures, periodic ventilation at a 10 min ON and 20 min OFF cycles through air pumps. The production units were opened on a mostly daily basis to collect larvae samples (about 90 larvae) and measure growing medium mass. The collected larvae wet mass were measured immediately and dry mass were measured after drying at 70 ° C for 6 h . The raw data obtained in the experiment TG2 is illustrated in Fig. B.3 in Appendix B.4 for reference.

A summary of all the experiments, measurements taken, and the corresponding parameters estimated are provided in Table 3. The constants and model parameters used in the model are listed in Table C.1 in Appendix C.

Parameter estimation and model validation. Models presented in this work are mostly nonlinear and therefore, nonlinear least squares data fitting method is used for parameter estimation. The outputs (measured variables) of the nonlinear system 𝒚 as a function of 𝒑 , the model parameter to be estimated, can be defined as

<!-- formula-not-decoded -->

where 𝒚 𝑘 = 𝒚 ( 𝑡 𝑘 ) and similarly 𝒙 𝑘 , 𝒖 𝑘 , and 𝒅 𝑘 . The parameter estimation problem is formulated as an optimization problem with the objective of finding the parameter that minimizes the sum of square of errors as

<!-- formula-not-decoded -->

where 𝑁 is the number of measurements and ̂ 𝒚 𝑘 represent the measured values. This parameter estimation problem was implemented in MATLAB using the fmincon function with direct single-shooting method with MultiStart to explore possible solutions within the specified boundary values of parameters. Simulations of dynamic models were performed using the ode15S solver in MATLAB to solve the differential equations. The ODEs representing the models are stiff due to the nonlinearities in the models (humidity and temperature change) and also the combination of slow (growth and development) and fast (evaporation, convection, etc.,) changing processes. The coefficient of determination ( 𝑅 2 ) are calculated and used as an indicator for the goodness of fit of the developed models.

## 2.5. Simulation and numerical tools

In order to evaluate the performance of the implemented controller, the partially closed production setup described by Eq. (2) and the three Scenarios (1-3) are considered as listed in the Table 4. The starting values and external environment ( 𝑇 out , 𝐶 out , and 𝐻 out ) measurements obtained from the growth experiments TG1-TG3 are used for the controller performance study. To compare the performance of the model based controller, a constant set-point controller is chosen. In a set-point operation, a controller not containing the knowledge of the model/process operates to maintain the predetermined growing conditions. Under these conditions, the time taken to reach the maximum larva biomass in set-point operation is determined and used as the target time of harvest 𝑡 h for optimal controller. Both controllers are applied in an open-loop setup and the resulting performance of the optimal controller is compared in terms of the resource consumed to achieve the same or more biomass at the harvest time.

To solve the nonlinear optimal control problem numerically, the optimization problem defined by Eq. (3) is formulated as a multiple shooting problem and solved using CasADi's (Andersson et al., 2019) MATLAB interface together with IPOPT (Wächter and Biegler, 2006). The gradients of the state constraints and objective functions with respect to the decision variables are calculated internally using CasADi's algorithmic differentiation method. The state constraints are enforced pointwise at the boundaries of the shooting in the multiple shooting problem as described in the CasADi's documentation. A step size or sampling and control interval of 𝛥𝑡 = 1h is selected for the duration of 𝑡 ∈ [0 , 192] h . The ODEs are solved using the fixed-step classic Runge-Kutta (RK4) integrator supplied with CasADi. A total of 1000 steps of step size 𝑑𝑡 = 3 . 6 s is considered for each control interval. The small integration time step is necessary to solve the stiff ODEs using the explicit method. The focus of this work is also to generate the code of the synthesized controller (executable on different computing platforms/architecture such as PLCs, etc.) and also to parallelize the execution of the OCP for faster execution. Therefore, CasADi's RK4 implementation is selected since it executes faster compared to ode15s and CVODES solvers and also supports code generation.

Table 3

Data sets for model validation and parameter estimation.

| Experiment              | Measurement type                         | Measurements                                                                                                             | Parameters estimated                                                                                                                                              |
|-------------------------|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Thermodynamics: TD1-TD6 | sensors manual (starting)                | 𝐶 out , 𝐻 out , 𝑇 out , 𝐶 air , 𝐻 air , 𝑂 air , 𝑇 air , 𝑇 med 𝐵 feed , 𝑊 med , 𝐵 med                                     | 𝑘 h a-c , 𝑘 he a-m , 𝑘 hm a-m , 𝑘 h a-ah , 𝑘 h o-c , 𝑘 U hx-c , 𝑘 U m-c , 𝑘 c chm , 𝑘 h med , 𝑘 h chm , 𝑘 h hx                                                    |
| Larvae Growth: TG1-TG3  | sensors manual (daily) manual (starting) | 𝐶 out , 𝐻 out , 𝑇 out , 𝐶 air , 𝐻 air , 𝑂 air , 𝑇 air , 𝑇 med 𝐵 dry , 𝐵 wet 𝐵 med 𝐵 feed , 𝐵 tot , 𝐵 wet , 𝑊 med , 𝐵 med | 𝑘 mat , 𝑘 maint , 𝑘 𝛼 excr , 𝑘 𝛼 assim , 𝑘 Q assim , 𝑘 Q maint , 𝑘 Q mat , 𝑘 Q bio , 𝑘 W assim , 𝑘 C assim , 𝑘 C maint , 𝑘 C mat , 𝑘 C bio , 𝑘 lrv C∶O , 𝑘 c feed |

Table 4 Simulation scenarios.

|   Scenario | Growing conditions              | Set-point operation                                                      | Optimal controller                                                                                           |
|------------|---------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
|          1 | TG2                             | 𝑇 air =33 ° C 𝐻 air = 60% 𝑢 w med = 14μgs -1                             | 𝛼 1 ,𝛼 2 ,𝛼 3 = 10 𝐑 = diag (0 . 01 , 0 . 001 , 0 . 001 , 1000) 𝐒 = diag (0 . 01 , 0 . 01 , 0 . 01 , 0 . 01) |
|          2 | TG2 with 𝑇 out lowered by 8 ° C | 𝑇 air = 33 ° C 𝐻 air = 60% 𝑢 w med = 14μgs -1                            | same as Scenario 1, but 𝐑 3 , 3 = 0 . 01 (expensive 𝑢 w med )                                                |
|          3 | TG2                             | 𝑇 air = 33 ° C 𝐻 air = 𝐻 out 𝑢 w med = 28μgs -1 𝑢 ΔH = 0 (faulty/absent) | same as Scenario 1 𝑢 ΔH = 0 (faulty/absent)                                                                  |

## 3. Results and discussion

The ordinary differential Eqs. (5), (9) and (15)-(27) model the mass and energy dynamics of the entire production system. In this section, the data obtained from the experiments and the results of the parameter estimation process for the production unit model and the larvae model are discussed. The goodness of fit of the developed model is evaluated based on the data sets from the experiments. The results of the optimal control studies are presented along with its performance in reducing the resource consumption.

## 3.1. Model goodness of fit for biomass, heat, water, gases, and larvae growth

This section addresses the performance of the models in describing the fluxes contributed mainly due to the presence and the growth of the larvae. Measurements from experiment TG2, after applying moving average filter of window size 50 (for noise reduction) and resampling, are plotted and compared to the results produced by the models in Fig. 3. In addition, to further analyse the model quality, the deviation of the model from the measured data are presented in Fig. 4. The larvae wet mass, dry mass, and the growing medium mass were measured intermittently requiring the opening and closing of the doors. This causes drop in the values of temperature, humidity and CO 2 concentration as seen in Fig. 3(c), (d), and (e) respectively.

Conclusion on the quality of the models in describing the variations of biomass, energy, and resources can be made based on the following observations. Firstly, the larvae biomass changes and the development stages determined by the model reproduces the measurements with a high coefficient of determination ( 𝑅 2 &gt; 0 . 96 ) for the dry mass and slightly lower score for the wet mass (see Figs. 3(a), 4(a), and 4(b)). Secondly, the overall substrate mass 𝐵 med follows the measured value with slight deviation as shown in Fig. 3(b). Since 𝐵 med is modelled based on the dynamic changes of three other state variables 𝐵 wet , 𝑁 med , and 𝑊 med which are not measured independently (see Fig. 3(f)), deviation in any one state translates to the deviation in the overall mass. Thirdly, the evaporation and thus the humidity of the air inside the production system plotted in Fig. 3(d) is captured by the model also indicating the changes due to variation in temperature and the availability of the water in the growing medium. A slightly lower 𝑅 2 =

0 . 83 score for 𝐻 air , as also seen from Fig. 4(e), can be reasoned by the slight deviation in temperatures 𝑇 med and 𝑇 air as seen in Figs. 3(c) and 4(d).

Finally, an important aspect identified in the measurement of growing medium temperature 𝑇 med and CO 2 concentration 𝐶 air , is the presence of peaks in measurement values at 110 h , 120 h , and 138 h marked with red squares as seen in Fig. 3(c) and (e). These peaks were observed in all the growth experiments (TG1-TG3) indicating that these peaks corresponds to the high metabolic activity of the larvae undergoing instar change. Such observations are not previously presented in any other work and can be considered as a novel and significant contribution of this work towards better understanding of the production process.

The developed models are able to capture the final instar change (maturity phenomenon) around 140 h and the resulting elevated energy ( 𝑇 med =42 ° C ) and resource ( 𝐶 air =26gm -3 ) fluxes due to elevated metabolic activity. If desired, the intermediate instar changes can also be modelled by periodically repeating the appearance of maturity fluxes 𝜙 Bmat in Eq. (5) with the period depending on the development sums 𝑇 Σ . Since for the production process only the last instar change is of interest, the intermediate instar changes are ignored in this work.

With these observations and the obtained results, it can be concluded that the models satisfy all the model requirements from 1 -5 and describe the process dynamics necessary for process design, automation, and resource optimization.

## 3.2. Model based quantification of fluxes: observations for process design

Using the models developed in this work and the identified parameters, it is possible to obtain information useful for process design. Information such as magnitude and rate change of the individual fluxes; rate change of state variables; and influence of the state variables on the various process rates can be computed using the models. To provide an example, all the flux terms are computed using the model and the conditions used for TG2 (initial values of the larvae number, dry mass, wet mass, feed, and water, and the climate). These individual mass and energy flux terms and the corresponding reaction rates are presented in Fig. 5.

Firstly from Fig. 5(a), various process rates at all time steps can be visualized to analyse the rates which limits the growth at any given instant. The starting values of the feed ( 480 g dry) and water ( 1 . 5 kg ) used in the experiment TG1-TG3 provides sufficient nutrition for the growth. However, observing the temperature dependent growth rate 𝑟 T , it can be stated that the low initial temperature 𝑇 med of 27 ° C

Fig. 3. Measurement vs. simulation (entities with hat): biomass, energy, and resource changes during growth and development. Data from TG2 experiment with air temperature set to a constant 29 ° C . (a) Wet and dry mass of individual larva and the corresponding development sums. (b) Mass change of the total growing medium including the larvae mass, feed, excreta and water. (c) Temperature changes in the growing medium and production environment. (d) Humidity changes in production environment. (e) CO 2 concentration changes in production environment. (f) Substrate component changes such as water, feed, excreta, and larvae wet mass as computed by the model.

<!-- image -->

Fig. 4. Measurement vs. simulation: residuals analysis. Measured data from TG2 experiment is plotted against the model simulation data. (a)-(f) represent the deviation of the model data from the measured data of larva dry mass, larva wet mass, growing medium mass, temperature of air, temperature of growing medium, humidity, and CO 2 concentration respectively.

<!-- image -->

Fig. 5. Process rates, energy, resource, and biomass fluxes computed using the model. (a) Process rates of all biological processes modelled for larvae growth and development. (b) Biomass fluxes within the larvae. (c) Heat fluxes originating from different sources. (d) Carbon dioxide and oxygen fluxes originating due to metabolic activities and ventilation. (e) Humidity fluxes originating due to evaporation and condensation. (f) Water fluxes originating from larvae ingestion, condensation, and evaporation.

<!-- image -->

results in lower growth 𝑟 grw and development rates 𝑟 T Σ . In contrast, this temperature increases later due to metabolic activity leading to increased growth and development rates. Using this information one can design the heating strategy where the substrate is initially heated and later turned down to operate the production process at high growth rates.

Secondly, the initial feed and moisture in substrate can be reduced significantly at start since the larvae are small, and they cannot utilize all the available feed. As seen in Fig. 5(b), feed gets consumed at a higher rate only when larvae reach sufficiently large size. This strategy would reduce the feed consumed by the microbiome and the water wastage due to evaporation at the early stages. However, this strategy may be not suitable if manual effort is involved for additional feed supply. Design decisions regarding feeding systems and strategies can be made based on these observations.

Thirdly, heat and mass (CO 2 , O 2 , H 2 O) fluxes plotted in Fig. 5(c)(f) show the dynamic variation contributed by the different (physical and biological) components during the production process. The components, plotted in black, indicate the contribution of the fluxes from the growing medium due to the direct and indirect influence of metabolic activities. For the chosen growing tray size of 0 . 12 m 2 , consisting of 2000 larvae, the larvae produce 31 W at the peak development phase, out of which, 19 W is lost to the ambient air through convection and 12 W is lost through evaporation (latent heat). For the same setup, the CO 2 production and thereof O 2 consumption at peak development phase reaches a maximum of 1 . 9 mg s -1 of which 95 % is ventilated out through the ventilation system. Similarly, the larvae consume a net 1 . 5 mg s -1 water at the peak growth phase. The humidity flux caused by the evaporation from the growing medium reaches a maximum of

4 . 4 mg s -1 when the substrate temperature 𝑇 med reaches the maximum value. Due to ventilation operating at a constant rate, there exists an average vapour flux of 1 . 3 mg s -1 . Based on these values, process parameters such as actuator rates, actuator capacities, resource utilization, and resource supply rates can be computed and used to design and analyse the production systems.

Finally, another observation made using the models in this study is the optimal temperatures for growth. From Fig. 3(c) and 5(c) it can be also noted that despite the temperature inside the production reactor set to a constant 29 ° C , the temperature in the substrate increases accelerating the metabolic processes and thus the growth and development. It is therefore necessary and important to consider the substrate temperature 𝑇 med in lieu of the ambient temperature 𝑇 air to draw conclusions on the influence of the temperature on growth-contradictory to Tomberlin et al. (2009), Harnden and Tomberlin (2016), Chia et al. (2018), Shumo et al. (2019) where only 𝑇 air is considered.

The above discussed applications of model for process design can be further extended for process automation and resource optimization as discussed in the next section.

## 3.3. Optimization of resource and energy using model-based optimal control

The second application demonstrated in this work using the models together with the estimated parameters is the optimization of resources and energy consumption in the larvae production process. Scenarios 1-3 defined in Section 2.5 are executed and the performance of the synthesized controller are compared, in terms of resources consumed, with the results of set-point operation. The first scenario compares the resource consumption between the production setups operated by the two controllers (model based controller and set-point controller)

10

Fig. 6. Optimization of energy and resource consumption using optimal control (Scenario 1). State trajectories and control inputs from the optimal controller are indicated by ∗ . (a) Dry and wet mass of larva under constant set-point and the optimal controller case. (b) Comparison of temperature changes in substrate and air and the heat supplied. (c) Humidity modification and the additional water vapour supplied. (d) Comparison of water and feed changes in growing medium with and without optimal control.

<!-- image -->

Fig. 7. Optimization of energy and resource consumption using optimal control (Scenario 2). State trajectories and control inputs from the optimal controller are indicated by ∗ .

<!-- image -->

considered in nominal weather conditions and resource costs. Scenario 2 considers extreme conditions such as colder climate condition and expensive or limited water supply. This should increase the overall operation costs in constant set-point operation where the process knowledge is absent. Lastly, Scenario 3, showcases performance of the controller in operating either a further simplified setup or faulty setup with absence of some actuators for manipulating the growing conditions. In this case a humidity control device is considered to be either absent or faulty and therefore, the process can only be controlled through temperature control and water supply to the substrate. In all three cases it is expected that the controller with process knowledge perform better compared to the constant set-point operation.

Scenario 1:. The control signals 𝒖 ∗ generated by the synthesized controller and the resulting optimal states trajectories 𝒙 ∗ are illustrated in Fig. 6. Observing the biomass change for larva over time (see Fig. 6(a)), it can be seen that there is not a significant increase using the optimal controller. Only a 4 % increase in the biomass is noticeable. However, a significant reduction in resource consumption is observed. The setup with an optimal controller consumes only 29 % of the energy required for heating, 98 % of water and energy for humidification, and 58 % of water required to keep the substrate moist.

Fig. 8. Optimization of energy and resource consumption using optimal control (Scenario 3). State trajectories and control inputs from the optimal controller are indicated by ∗ .

<!-- image -->

From Fig. 6(b), the 𝑢 ΔT ∗ is high initially and gradually reduced by the controller taking into consideration the heat released due to the metabolic activities. Similarly, from the humidification policy 𝑢 ΔH ∗ as seen in Fig. 6(c), humidity is only compensated when losses incur due to increase in temperature. Consequently, to compensate the water loss from the substrate, water supply to growing medium only takes place when the temperature increases and the humidity drops. Also noticeable from the results are the lower substrate moisture in the optimized case. These policies/control trajectories generated can be further adapted adjusting the weights 𝛼 and 𝐑 based on the process goals.

Scenario 2:. This scenario tests the operation at a outside temperature 𝑇 out much lower ( 8 ° C ) than considered in Scenario 1 to showcase the necessity of higher heating requirements (see Fig. 7(b)). Also, the costs for water supplied to medium is set 10 times higher compared to the humidification costs. For this scenario, the setup with an optimal controller consumes 44 % of the energy required for heating, 122 % of water and energy for humidification and only 1 % of water required to keep the substrate moist. There is also a small increase ( 3 . 6 % ) in the biomass despite a much smaller overall energy and resource consumption. It can be observed that the controller increases the ambient humidity to limit evaporative losses from the substrate thus requiring little to no additional supply of water to the substrate by choosing the less expensive resource.

Scenario 3:. In this scenario it is considered that no humidity control is possible and only temperature and water supply to growing medium are controlled. For a set-point control operation, a constant higher water supply rate ( 28 μg s -1 ), twice compared to scenario 1 and 2, is required to keep the substrate moist to facilitate growth for the constant setpoint operation. In case of the optimal controller setup, only 60 % of the energy is required for heating, 84 % of water required to keep the substrate moist and resulting in about 8 % higher biomass (see Fig. 8).

In all three scenarios (1-3), it was observed that the process utilizing the optimal controller generated control signals results in a significant reduction in resource consumption while still producing the same or higher larvae biomass. It is also to be noted that the optimization is performed in these scenarios with harvest time as constant. It is possible to significantly reduce the resource consumption further by including the harvest time as an optimization variable resulting in a shorter harvesting period. Obtaining other specific control policies are possible by either changing weights 𝛼 1 , 𝛼 2 , 𝛼 3 , 𝐑 , and 𝐒 ; or modifying the objective function Eq. (3); or introducing additional control variables such as harvest time and development sums for stage specific harvest.

Although the model-based optimal control approach requires detailed models with process knowledge compared to model-free or heuristic approaches, the advantages are manifold. Most importantly, an optimal controller with a process model always produces deterministic results, which allows for a sound interpretation of even those that appear to be a counter intuitive decision. Besides that, there are several benefits in adopting the model-based optimal control framework as seen in other areas of food and biomass production (van Straten et al., 2000; Padmanabha et al., 2020a; Cacho et al., 1991; Karimanzira et al., 2017; Freitas et al., 2017; Chahid et al., 2021). However, this is the first work that implements the model-based control and highlight its benefits for the industrial mass production of the Hermetia illucens larvae.

## 4. Conclusion and outlook

Differential equations representing the dynamic changes of the resources (feed, water, larvae biomass, gas concentration, humidity, etc.) and energy in a closed production system including the interaction dynamics between the Hermetia illucens larvae and its environment are derived based on requirements established for process automation. The derived model of the production environment together with the identified model parameters validated against the datasets resulted in a high goodness of fit for all data sets. Furthermore, important and unique observations on the elevated heat and CO 2 production due to instar changes in the experiment datasets could be captured by the models. Also, the reproduction of the elevated metabolic peaks using the newly derived model Eq. (5) is also highlighted. The differential equations representing the model Eqs. (5), (9) and (15)-(27) were validated and it is shown that they satisfy all the model requirements (1-6) defined in this work for process automation and application in optimal control.

To showcase one of the several possible use cases of the models for process design, mass fluxes, energy fluxes, and process rates were generated using the flux terms and analysed to obtain crucial information pertaining to the production process. We also conclude that the temperature of the growing medium is rather more important than the air temperature for the control of the larave growth and development. In addition, conclusions for designing the feeding strategies and also designing the actuator framework could be drawn by studying the feed dynamics and fluxes of temperature, humidity, and CO 2 obtained using these models. Therefore, it can be concluded that these models are novel and also very useful in designing production systems including special closed agricultural systems such as CUBEScircles (Circle, 2018) that aim at reusing the byproducts to produce zero waste. Not only are these models useful in designing the process, but also necessary to automate the process and simultaneously optimize the resource consumption as demonstrated using the proposed optimal control framework.

The performance of the synthesized optimal controller studied under the three scenarios, showcases its potential in optimizing resources while achieving the defined automation goals of Hermetia illucens production. In all three scenarios presented in this work, the optimal controller driven production process achieves same or higher larvae biomass while consuming significantly low resources compared to a constant set-point operation. This showcases the strengths of the model based control approach which exploits the process knowledge for optimum operation. Although its adoption is seen in other areas of food and biomass production, this is the only work that addresses its adoption for Hermetia illucens larvae production and presents all the necessary tools such as models ( Eqs. (5), (9) and (15)-(27)), data (TD1-TD6, TG1-TG3), examples (Scenario 1-3) and an objective function Eq. (3) to solve the control challenges associated.

The tools presented in this work will lay the foundation for future work which will focus on exploring the variations of the objective functions; adjusting the weights for fine-tuning the process for multiple process goals; define sophisticated control policies; and develop resource aware open loop decision support infrastructure and closed loop control for safe, uninterrupted, and efficient operation of closed and interconnected production systems.

## CRediT authorship contribution statement

Murali Padmanabha: Conceptualization, Methodology, Software, Validation, Formal analysis Investigation, Data curation, Writing - original draft, Visualization. Alexander Kobelski: Investigation, Data curation, Writing - review &amp; editing. Arne-Jens Hempel: Methodology, Writing - review &amp; editing, Supervision, Project administration. Stefan Streif: Conceptualization, Methodology, Resources, Writing - review &amp; editing, Supervision, Project administration, Funding acquisition.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgements

This measure is co-financed with tax revenues on the basis of the budget passed by the Saxon state parliament, Germany (grant number SAB 100403339; project NutriCon) and of the Federal Ministry of Education and Research of Germany (BMBF, Germany; grant number 031B0733D; project CUBEScircles).

## Appendix A. Flux components

Additional information pertaining to all the individual flux components and modelling of the flux components contributed due to the physical phenomenon are presented in this section.

## A.1. Energy and resource flux components

All the flux terms introduced in the mass and energy balance equations in Section 2.3.3 are derived based on laws of physics as presented in detail here.

Temperature and heat fluxes:. The individual heat flux components represented by 𝜙 Q in Eqs. (15)-(18) are mostly results of convection, conduction, mass transfer, and latent heat of condensation and evaporation.

Firstly, the general convective heat flux between the air and the surface of consideration is given as

<!-- formula-not-decoded -->

where the area of the surface y under consideration is 𝑘 Ay and the heat transfer coefficient between the air and the surface y is 𝑘 h a-y , and the subscripts 𝑎 , 𝑐 , 𝑚 , ℎ𝑥 , and 𝑜 corresponds to air inside, walls, growing medium, heat exchanger and air outside respectively. The above equation for convective fluxes holds good when the ratio of mass and energy transfer is constant. In case of high evaporation and thus higher mass transfer, the net convective heat transfer coefficient varies proportional to the mass transfer flux (Lewis, 1922). Therefore, the convective heat transfer between the air and the growing medium is modified as

<!-- formula-not-decoded -->

where 𝑘 he a-m is the convective heat transfer only due to the energy transport and 𝑘 hm a-m is the specific mass dependent heat transfer rate.

The heat flux components due to conductive heat transfer is given as

<!-- formula-not-decoded -->

where the area of contact between the surface y and walls are given as 𝑘 Ay-c and the conductive heat transfer coefficient between them are given as 𝑘 Uy-c with the subscript 𝑚 and ℎ𝑥 corresponding to the growing medium and heat exchanger respectively.

Heat exchange due to mass transfer with the outside environment through ventilation systems (air-pumps), leakage, and opening of door is a function of the mass transfer rate modelled as

<!-- formula-not-decoded -->

where 𝑘 c air and 𝑘 𝜌 air are the specific heat capacity and density of the air and 𝑘 ̇ Vu , 𝑘 ̇ Vleak and 𝑘 ̇ Vdoor represent the maximum mass transfer rate of ventilation system, leakage, and door opening events respectively.

Table A.1 List of symbols used to describe the fluxes.

| Symbol           | Description                                                                                                                                        | Unit                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 𝜙 B ing          | flux of feed from substrate into the larva                                                                                                         | [ g s -1 ]            |
| 𝜙 B excr         | flux of non digested feed back to substrate                                                                                                        | [ g s -1 ]            |
| 𝜙 B assim        | feed converted into energy and spent to digest the ingested feed                                                                                   | [ g s -1 ]            |
| 𝜙 B eff          | effective assimilates available from the ingested feed for growth and maintenance                                                                  | [ g s -1 ]            |
| 𝜙 B mat          | assimilates spent towards building of new structure                                                                                                | [ g s -1 ]            |
| 𝜙 B maint        | assimilates spent for maintenance of existing structure                                                                                            | [ g s -1 ]            |
| 𝜙 W assim        | flux of water from substrate into the larva                                                                                                        | [ g s -1 ]            |
| 𝜙 W maint        | water spent for maintenance respiration                                                                                                            | [ g s -1 ]            |
| 𝜙 Q bio          | heat production in growing medium                                                                                                                  | [ J s -1 ]            |
| 𝜙 C bio          | CO 2 production in growing medium                                                                                                                  | [ kgs -1 ]            |
| 𝜙 O bio          | O 2 consumption in growing medium                                                                                                                  | [ kgs -1 ]            |
| 𝜙 N ing          | net feed consumption by all larvae                                                                                                                 | [ g s -1 ]            |
| 𝜙 N exc          | net digested feed excretion by all larvae                                                                                                          | [ g s -1 ]            |
| 𝜙 N biome        | feed consumed by microbiome                                                                                                                        | [ g s -1 ]            |
| 𝜙 Q LED          | heat produced by LED lighting system                                                                                                               | [ J s -1 ]            |
| 𝜙 Q hx-a         | convective flux between air and heat exchanger                                                                                                     | [ J s -1 ]            |
| 𝜙 Q exch         | heat flux through ventilation pumps                                                                                                                | [ J s -1 ]            |
| 𝜙 Q leak         | heat flux through leakage                                                                                                                          | [ J s -1 ]            |
| 𝜙 Q leak         | heat flux through door                                                                                                                             | [ J s -1 ]            |
| 𝜙 Q m-a          | convective heat flux between growing medium and air                                                                                                | [ J s -1 ]            |
| 𝜙 Q a-c          | convective heat flux between air and walls of production system                                                                                    | [ J s -1 ]            |
| 𝜙 Q m-c          | conductive heat flux between growing medium and walls of production system                                                                         | [ J s -1 ]            |
| 𝜙 Q TEC          | heat generated or removed by the heating-cooling system                                                                                            | [ J s -1 ]            |
| 𝜙 Q c-hx         | conductive heat flux between heat exchanger and walls of production system                                                                         | [ J s -1 ]            |
| 𝜙 Q L , med      | and external environment heat flux in growing medium due to latent heat of evaporation                                                             | [ J s -1 ]            |
| 𝜙 hx             | and condensation                                                                                                                                   |                       |
| Q L ,            | heat flux in heat exchanger due to latent heat of evaporation and condensation                                                                     | [ J s -1 ]            |
| 𝜙 Q L , chm 𝜙    | heat flux in walls of production system due to latent heat of evaporation and condensation water vapour provided to or removed from the production | [ J s ] -1            |
| H u              | system through (de)humidifier                                                                                                                      | [ kgs ]               |
| H exch 𝜙 H leak  | water vapour loss due to air exchange through leakage                                                                                              | [ kgs -1 ]            |
| 𝜙 H              | water vapour change due to air exchange during door                                                                                                | [ kgs -1 ]            |
| door             | opening events                                                                                                                                     |                       |
| 𝜙 W L , chm      | net water movement between the air and walls (condensation and evaporation) net water movement between the air and heat exchanger                  | [ kgs -1 ]            |
| 𝜙 W L , hx       | (condensation and evaporation)                                                                                                                     | [ kgs -1 ]            |
| 𝜙 W L , med      | net water movement between the air and growing medium (condensation and evaporation)                                                               | [ kgs -1 ]            |
| 𝜙 W u            | water provided to the growing medium through pumps                                                                                                 | [ kgs -1 ]            |
| 𝜙 W bio          | water consumed by the larvae from the growing medium                                                                                               | [ kgs -1 ]            |
| 𝜙 W chm , out    | condensate flow from the walls of the production system to collection tank                                                                         | [ kgs -1 ]            |
| 𝜙 W hx , out 𝜙 C | condensate flow from the heat exchanger to collection tank active exchange of CO 2 through pumps                                                   | [ kgs -1 ] [ kgs -1 ] |
| 𝜙 C leak         | passive exchange of CO 2 through leakage                                                                                                           | [ kgs -1 ]            |
| 𝜙                | active exchange of O 2 through pumps                                                                                                               | [ kgs -1 ]            |
| O exch 𝜙         | passive exchange of O 2 through leakage                                                                                                            | [ kgs -1 ]            |
| O leak 𝜙 N u     | feed supplied to substrate as input                                                                                                                | [ kgs -1 ]            |
| 𝜙 ̇ V u          | air exchange taking place through ventilator pumps                                                                                                 | [ m 3 s -1 ]          |

The heat inside the production unit is supplied and removed by the TEC based heating-cooling system. This heat flux term contributed by the TEC module can be modelled as presented in Rowe (1995)

<!-- formula-not-decoded -->

where 𝑘 𝛼, q , 𝑘 R , q , and 𝑘 TEC are the Seebeck coefficient, series resistance and thermal conductivity of the TEC module respectively, 𝑢 T is the input to the TEC driver and 𝑘 Vmax is the maximum voltage that can be applied. This flux component can be replaced by the corresponding model of the heat-exchanging system in use.

The LED panel inside the production unit also produces heat and can be modelled as

<!-- formula-not-decoded -->

where 𝑖 represents the narrow and wide-band wavelengths (LED channels) supported by the light panel and 𝑘 heat 𝑖 is the maximum heat dissipated by the respective LED channel.

The growing medium containing high concentration of water contributes to evaporation resulting in the loss of heat through latent heat of evaporation. This can be described as the heat required to raise the water at temperature 𝑇 med to 100 ° C plus the additional latent heat for converting water from liquid to vapour state as

(

)

<!-- formula-not-decoded -->

where 𝑘 h ew latent heat of vaporization of water at 100 ° C , 𝑘 Cwater is the specific heat capacity of water, and 𝜙 WL , med is the rate of transport of water between the air and the surface of the medium. Eq. (A.7) can be applied to obtain the latent heat for walls 𝜙 QL , chm and heat exchanger 𝜙 QL , hx surface by replacing the temperature 𝑇 med with 𝑇 chm and 𝑇 hx respectively.

The heat capacity 𝑘 Cair of the air in production environment and 𝑘 Cmed for the growing medium varies due to changes due to mass fluxes. Therefore, these parameters are not constants but are dependent on the state variables given as

<!-- formula-not-decoded -->

where 𝑘 c tray , 𝑘 c feed , 𝑘 c water , 𝑘 c air , 𝑘 c vap are the specific heat capacities of growing tray, feed, water, production unit internal parts, air, and water vapour respectively, 𝑘 Vchm is the volume inside the production unit, 𝑘 mtray , and 𝑘 mchm are the mass of the growing trey and the inner components and walls of production unit.

Water and humidity fluxes:. Water fluxes in the production unit take place in both liquid and vapour forms. Evaporation of water from the growing medium has twofold effect: cooling of the growing medium resulting in lower temperatures for larval growth and loss of moisture resulting in reduced ingestion rate. It is therefore important to accurately model the phenomenon that captures both water loss and temperature drop. The maximum rate of evaporation or condensation from any surface is defined as (Monteith, 1981),

<!-- formula-not-decoded -->

where 𝑘 Asurf , 𝑘 h surf , and 𝑇 surf are the area, vapour transport coefficient and temperature of the given surface. The saturation concentration of water vapour, 𝐻 sat , for any given reference temperature 𝑇 ref , can be calculated using the Magnus-Tetens equation (Murray, 1967; Alduchov and Eskridge, 1996) as

<!-- formula-not-decoded -->

where 𝑘 Wmmol is molar mass of water and 𝑘 Rg is the gas constant.

In order to obtain actual condensation and evaporation rate from the above Eq. (A.9) as separate flux terms, it is necessary to split the components and consider the actual quantity of water available for this process.

<!-- formula-not-decoded -->

where 𝜖 evap is the evaporation coefficient modelled here as a function of water content available on the surface. For evaporation from the surface of the growing medium, this is modelled in this work as

<!-- formula-not-decoded -->

where 𝑘 GW is the conductivity offered by the feed for transport of water to the growing medium surface and 𝑘 Wper is the moisture percentage above which the growing medium is moist enough to allow maximum evaporation.

From above Eq. (A.11) replacing the terms 𝑘 Asurf , 𝑘 h surf , 𝑇 surf and 𝑊 med% with the terms corresponding to actual surfaces, in this case the growing medium, walls and the heat-exchanger, gives the corresponding water flux terms 𝜙 WL , chm , 𝜙 WL , TEC and 𝜙 WL , med .

Water vapour transport due to the air exchange through ventilation, leakage, and door opening events similar to heat exchange through ventilation, is given by

<!-- formula-not-decoded -->

Finally, the water influx to the growing medium (in liquid form) is through pumps and depend on the actuator properties given as

<!-- formula-not-decoded -->

where 𝑘 Wu is the water transport rate of the pumps.

Air composition:. Metabolic activity of larvae consumes O 2 and feed, producing CO 2 as a result. The concentration of the two gases O 2 and CO 2 change relative to each other and modelling both these concentrations may not be necessary when air is supplied from natural source with fixed O 2 to CO 2 ratio. The gas concentration changes and the flux due to ventilation, leakage, and door opening events are given respectively as

<!-- formula-not-decoded -->

## Appendix B. Experiment setup and experiments

The production setup used, raw data obtained using the setup, and the additional experiments performed to identify the characteristics of the production setup are described in this section.

## B.1. Production unit

The controlled environment (see Fig. B.1) has a volume of 75 L and holds a growing tray of dimension 22 cm × 32cm × 5 . 5 cm and can contain up-to 4 kg of substrate. This growing tray serves as a container for the growing medium that contains selected feed for the larvae, selected number of young larvae (neonates) and the microbiome that eventually develops and grows along with the larvae in the growing medium. The temperature, humidity, airflow/air-concentration, light intensity and day-night cycles within the unit can be regulated as required. Information related to the states inside the production unit such as temperature of air and growing medium; CO 2 and O 2 concentrations; and humidity in air and moisture and temperature in growing medium are recorded by the sensors integrated within. Similarly, information related to the states outside the production unit, e.g., temperature, humidity and CO 2 concentration of external air source, are logged using a data logger. Further details regarding the production environment can be found in our previous work (Padmanabha and Streif, 2019) (see Section 2.1.4 and 3.7).

## B.2. Thermodynamic experiments for characterizing the production setup

The production unit is operated in different modes under different conditions as listed in Table B.1. In passive mode, the contents (air or growing medium) are pre heated and the variations in temperature and humidity are observed. In active automated mode, the actuators execute pre-programmed sequence to generate specific temperature and ventilation profiles and the resulting temperature and humidity changes are logged.

Fig. B.1. Experiment Setup. Three independent production units, with individual climate control and integrated sensors.

<!-- image -->

Fig. B.2. Measurement vs. simulation (entities with hat): dynamic temperature changes under different conditions. (a) TD1: convective losses between 𝑇 air and 𝑇 out . (b) TD2: convective transfer between 𝑇 air and 𝑇 med only through heat transfer. (c) TD3: actuator influenced convective transfer between 𝑇 hx , 𝑇 air and 𝑇 out . (d) TD4: actuator influenced convective transfer between 𝑇 hx , 𝑇 air and 𝑇 med only through heat transfer. (e) TD5: same as TD4 but through simultaneous heat and mass transfer with heat loss due to latent heat of evaporation. (f) TD6: same as TD5 but also additional mass flux between production unit and external environment through ventilation.

<!-- image -->

Table B.1

## Thermodynamics experiment configurations.

| ID   | Growing medium                         | Mode                               | TEC           | Ventilator   |
|------|----------------------------------------|------------------------------------|---------------|--------------|
| TD1  | none                                   | passive, pre heated air            | OFF           | OFF          |
| TD2  | 1kg water covered with conductive film | passive, pre heated growing medium | OFF           | OFF          |
| TD3  | none                                   | active, automated                  | 100% to -100% | OFF          |
| TD4  | 1kg water covered with conductive film | active, automated                  | 100% to -100% | OFF          |
| TD5  | 1kg water without conductive film      | active, automated                  | 100% to -100% | OFF          |
| TD6  | 1kg water without conductive film      | active, automated                  | 100% to -100% | ON           |

In the active automated tests, the TEC based heating-cooling system is set to +100% and allowed to heat for 1 h to reach temperature saturation. The power is then reduced in steps of 5% and allowed to saturate for 20 min until the power reaches -100% and then turned OFF to allow the temperatures to reach the outside temperatures passively. These tests cover a wide range of temperatures, transport mechanisms, and flux directions for the heat and water transport.

Fig. B.3. Temperature dependant larvae growth experiment TG2. Temperature set point of 29 ° C and tracking the development of larvae and resource changes in production unit using sensors and manual measurements. (a) Average wet and dry mass of larva samples. (b) Total mass of the growing medium including larvae, substrate and water. (c),(d),(e) and (f) are temperature, humidity, CO 2 concentration, and O 2 concentration measurements respectively.

<!-- image -->

## B.3. Models goodness of fit for heat and water fluxes without larvae

The thermodynamic properties of the production unit along with the heat and water fluxes are identified using the data from TD1-TD6 experiments based on the developed models. This step is important to obtain accurate convective and conductive heat transfer properties of the production unit and necessary to separate the resource and energy flux contributed due to the larvae growth and interaction with its environment. This identification enables to distinguish between the heat produced by the biological component and the latent heat of evaporation.

Models are simulated using the starting values, actuator signals, and disturbance signals as logged in the experiments. The simulation results compared to the actual measurements are illustrated in Fig. B.2. The convective heat transfer parameters obtained using TD1 and TD2 successfully describe the heat transfer between the production environment, growing medium and external environment (see Fig. B.2(a) and (b)). Parameters obtained using TD3 describe the dynamics of the heating-cooling system and the heat exchange between the heat exchanger 𝑇 hx and the air 𝑇 air . Comparing the temperature 𝑇 med and 𝑇 air in Fig. B.2(d), (e), and (f) in the time period 4 h -12 h , it can be observed that the heat transfer between the ambient air and the growing medium is higher in the experiments TD5 and TD6. The higher transfer rate is due to increase in convective transfer coefficient due to the vapour transport (evaporation) taking place in TD5 and TD6. Evaporation of water from the growing medium causes additional loss of heat. This loss of heat is proportional to the latent heat of evaporation and results in cooling of the growing medium. This can be inferred from the increasing temperatures difference 𝑇 air 𝑇 med in TD4-TD6 observed from 0 h -3 h in Fig. B.2(d), (e), and (f).

In conclusion, the derived model of the production environment together with the identified model parameters, accurately describe the functioning of the individual components of the production system with 𝑅 2 &gt; 0 . 97 . The only slight deviation observed (see Fig. B.2(c)) is due to the difference in the construction of the sensor housing, where the sensor measuring 𝑇 air has slightly lower sensitivity compared to the sensor measuring 𝑇 med . With these results, it can be stated that the model requirements 1 and 3 for the production environment are satisfied.

## B.4. Raw data obtained in larvae growth experiments TG2

The sensor data appears to be jittery as seen in Fig. B.3 and this is simply due to the periodic air exchange represented by 𝑢 v . Significant drop in sensor values for a short time period can be observed which is due to the opening of the production unit for extracting samples. Despite the temperature set to 29 ° C , increase in substrate temperature can be seen in (c) . This increase in temperature and also the CO 2 production are the byproducts of the metabolic activities of the larvae and the microbiome.

## Appendix C. Model parameters

The Table C.1 lists all the constants and model parameters identified for both the larvae growth dynamics model and the resource and energy flux models.

## References

- [Alduchov, O.A., Eskridge, R.E., 1996. Improved magnus form approximation of saturation vapor pressure. J. Appl. Meteorol. 35 (4), 601-609.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb1)
- Andersson, J.A.E., Gillis, J., Horn, G., Rawlings, J.B., Diehl, M., 2019. CasADi: a software framework for nonlinear optimization and optimal control. Math. Program. Comput. (ISSN: 1867-2957) 11 (1), 1-36. http://dx.doi.org/10.1007/s12532-0180139-4.

Table C.1

List of all constants and parameters.

| Symbol                                    | Description                                                                                                 | Value         | Unit             |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------|------------------|
| 𝑘 inges                                   | specific ingestion rate per larva                                                                           | 37 × 10 -6    | [ g g -1 s -1 ]  |
| 𝑘 mat                                     | specific maturity rate per larva                                                                            | 17 × 10 -6    | [ g g -1 s -1 ]  |
| 𝑘 maint                                   | specific maintenance rate per larva                                                                         | 2 . 2 × 10 -6 | [ g g -1 s -1 ]  |
| 𝑘 𝛼                                       | fraction of ingested feed excreted out                                                                      | 0.25          | [-]              |
| excr 𝑘 𝛼                                  | fraction of ingested feed spent for digestion                                                               | 0.1843        | [-]              |
| assim 𝑘 T Σ 1                             | development sum at which the assimilation starts to cease and                                               | 261           | [ h ]            |
|                                           | maturity starts                                                                                             |               |                  |
| 𝑘 T 2                                     | development sum at which the assimilation process ends                                                      | 272           | [ h ]            |
| Σ 𝑘 T 3                                   | development sum at which the maturity process end                                                           | 286           | [ h ]            |
| Σ 𝑘 Q assim                               | specific heat production through assimilation respiration                                                   | 14 × 10 3     | [ J g -1 ]       |
| 𝑘 Q mat                                   | specific heat production through maturity respiration                                                       | 28 × 10 3     | [ J g -1 ]       |
| 𝑘 Q miant                                 | specific heat production through maintenance respiration                                                    | 28 × 10 3     | [ J g -1 ]       |
| 𝑘 Q bio                                   | specific heat production through microbiome respiration                                                     | 3 . 1 × 10 3  | [ J g -1 ]       |
| 𝑘 W assim                                 | specific water consumption per gram feed assimilated by the                                                 | 2 . 9         | [ g g -1 ]       |
| larvae                                    | larvae                                                                                                      |               |                  |
| 𝑘 C assim                                 | specific CO 2 production through assimilation respiration                                                   | 1 . 6         | [ g g -1 ]       |
| 𝑘 C mat                                   | specific CO 2 production through maturity respiration                                                       | 1 . 6         | [ g g -1 ]       |
| 𝑘 C miant                                 | specific CO 2 production through maintenance respiration                                                    | 1 . 6         | [ g g -1 ]       |
| 𝑘 C bio                                   | specific CO 2 production through microbiome respiration                                                     | 120 × 10 -6   | [ g g -1 ]       |
| 𝑘 bio C∶O                                 | O 2 consumed for every CO 2 produced                                                                        | 1             | [-]              |
| Production unit specific model parameters | Production unit specific model parameters                                                                   |               |                  |
| 𝑘 V chm                                   | total volume inside the production unit                                                                     | 64 × 10 -3    | [ m 3 ]          |
| 𝑘 A c                                     | total surface area of the production unit                                                                   | 1 . 1         | [ m 2 ]          |
| 𝑘 A m                                     | total surface area of the growing medium                                                                    | 120 × 10 -3   | [ m 2 ]          |
| 𝑘 A hx                                    | total surface area of the heat exchanger unit                                                               | 290 × 10 -3   | [ m 2 ]          |
| 𝑘 h a-c                                   | convective heat transfer coefficient for air-wall interface                                                 | 27            | [ Wm -2 K -1 ]   |
| 𝑘 h                                       | convective heat transfer coefficient for air-growing medium                                                 | 13            | [ Wm -2 K -1 ]   |
| a-m interface                             | a-m interface                                                                                               |               |                  |
| 𝑘 h a-hx                                  | convective heat transfer coefficient for air-heat exchanger interface                                       | 26            | [ Wm -2 K -1 ]   |
| 𝑘 h a-o                                   | convective heat transfer coefficient for wall-outside air interface                                         | 8 . 5         | [ Wm -2 K -1 ]   |
| 𝑘 he a-m                                  | mass flow absent convective heat transfer coefficient for                                                   | 12            | [ Wm -2 K -1 ]   |
|                                           | air-growing medium interface                                                                                |               |                  |
| 𝑘 hm a-m                                  | mass flow influenced additional convective heat transfer                                                    | 1 . 3         | [ Wm -2 K -1 ]   |
| 𝑘 A                                       | coefficient for air-growing medium interface total surface area of contact at heat exchanger-wall interface | 0             | [ m 2 ]          |
| hx-c 𝑘 A                                  | total surface area of contact at growing medium-wall interface                                              | 0             | [ m 2 ]          |
| m-c 𝑘 U hx-c                              | conductive heat transfer coefficient for heat exchanger-wall                                                | 0             | [ Wm -2 K -1 ]   |
| 𝑘 U m-c                                   | interface conductive heat transfer coefficient for growing medium-wall interface                            | 0             | [ Wm -2 K -1 ]   |
| 𝑘                                         | of air                                                                                                      | 3             |                  |
| c air                                     | specific heat capacity                                                                                      | 1 . 0 × 10    | [ JK -1 kg -1 ]  |
| 𝑘 𝜌 air                                   | density of air                                                                                              | 1 . 2         | [ kgm -3 ]       |
| 𝑘 ̇ V u                                   | mass transfer rate through ventilation pumps                                                                | 250 × 10 -6   | [ m 3 s -1 ]     |
| 𝑘 ̇ V leak                                | mass transfer rate through leakage in the production unit                                                   | 580 × 10 -9   | [ m 3 s -1 ]     |
| 𝑘 ̇ V door                                | mass transfer rate through door in the production unit                                                      | 150 × 10 -6   | [ m 3 s -1 ]     |
| 𝑘 a , q                                   | Seebeck coefficient of the TEC element                                                                      | 46 × 10 -3    | [ VK -1 ]        |
| 𝑘 V max                                   | maximum applicable voltage to TEC                                                                           | 12            | [ V ]            |
| 𝑘 R q                                     | Internal resistance of the TEC element                                                                      | 1 . 7         | [ Ω ]            |
| 𝑘 TEC                                     | Thermal conductivity of the TEC element                                                                     | 420 × 10 -3   | [ WK -1 ]        |
| 𝑘 c water                                 | specific heat capacity of water                                                                             | 4 . 2 × 10 3  | [ JK -1 kg -1 ]  |
| 𝑘 h ew                                    | latent heat of vaporization of water                                                                        | 2 . 3 × 10 6  | [ kJkg -1 ]      |
| 𝑘 c tray                                  | specific heat capacity of growing tray                                                                      | 500           | [ JK -1 kg -1 ]  |
| 𝑘 m                                       | mass of growing tray                                                                                        | 850 × 10 -3   | [ kg ]           |
| tray 𝑘 c                                  | specific heat capacity of feed (dry mass)                                                                   | 20 × 10 3     | [ JK -1 kg -1 ]  |
| feed 𝑘 c vap                              | specific heat capacity of water vapour                                                                      | 4 . 2 × 10 3  | [ JK -1 kg -1 ]  |
| 𝑘 c                                       | specific heat capacity of chamber internal parts                                                            | 1 . 9 × 10 3  | [ JK -1 kg -1 ]  |
| chm 𝑘 W                                   | molar mass of water                                                                                         | 610           | [ gmol -1 ]      |
| mmol 𝑘 R g                                | gas constant                                                                                                | 460           | [ JK -1 mol -1 ] |
| 𝑘 G W                                     | conductivity of the feed for transport of water to the surface                                              | 1             | [-]              |
| 𝑘 W per                                   | moisture percentage above which maximum evaporation is possible                                             | 0.6           | [-] -1           |
| 𝑘 W u                                     | water transport rate of the pumps                                                                           | 3 . 8 × 10 -3 | [ kgs ]          |

- Barragan-Fonseca, K., Dicke, M., van Loon, J., 2017. Nutritional value of the black soldier fly (Hermetia illucens L.) and its suitability as animal feed - a review. J. Insects As Food Feed 3 (2), 105-120. http://dx.doi.org/10.3920/JIFF2016.0055.
- [Bondari, K., Sheppard, D., 1981. Soldier fly larvae as feed in commercial fish production. Aquaculture 24, 103-109.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb4)
- Cacho, O.J., Kinnucan, H., Hatch, U., 1991. Optimal control of fish growth. Am. J. Agric. Econ. 73 (1), 174-183. http://dx.doi.org/10.2307/1242893.
- [Chahid, A., N'Doye, I., Majoris, J., Berumen, M., Laleg-Kirati, T.-M., 2021. Model predictive control paradigms for fish growth reference tracking in precision aquaculture.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb6)

- Cheng, J.Y., Chiu, S.L., Lo, I.M., 2017. Effects of moisture content of food waste on residue separation, larval growth and larval survival in black soldier fly bioconversion. Waste Manag. (ISSN: 0956-053X) 67, 315-323. http://dx.doi.org/ 10.1016/j.wasman.2017.05.046.
- Chia, S.Y., Tanga, C.M., Khamis, F.M., Mohamed, S.A., Salifu, D., Sevgan, S., Fiaboe, K.K.M., Niassy, S., van Loon, J.J.A., Dicke, M., Ekesi, S., 2018. Threshold temperatures and thermal requirements of black soldier fly Hermetia illucens: Implications for mass production. PLoS One 13 (11), 1-26. http://dx.doi.org/10. 1371/journal.pone.0206097.
- Circle, C., 2018. CUBES cirlce: Future food production. URL https://www.cubescircle. de/en/home/project.
- Diener, S., Zurbrügg, C., Tockner, K., 2009. Conversion of organic material by black soldier fly larvae: Establishing optimal feeding rates. Waste Manag. Res. J. Int. Solid Wastes Public Clean. Assoc., ISWA 27, 603-610. http://dx.doi.org/10.1177/ 0734242X09103838.
- Freitas, H.F.S.d., Olivo, J.E., Andrade, C.M.G., 2017. Optimization of bioethanol in silico production process in a fed-batch bioreactor using non-linear model predictive control and evolutionary computation techniques. Energies (ISSN: 1996-1073) 10 (11), http://dx.doi.org/10.3390/en10111763, URL https://www.mdpi.com/19961073/10/11/1763.
- Gao, Z., Wang, W., Lu, X., Zhu, F., Liu, W., Wang, X., Lei, C., 2019. Bioconversion performance and life table of black soldier fly (Hermetia illucens) on fermented maize straw. J. Clean. Prod. (ISSN: 0959-6526) 230, 974-980. http://dx.doi.org/ 10.1016/j.jclepro.2019.05.074.
- [Gligorescu, A., Toft, S., Hauggaard-Nielsen, H., Axelsen, J., Nielsen, S.A., 2018. Development, metabolism and nutrient composition of black soldier fly larvae (Hermetia illucens; Diptera: Stratiomyidae) in relation to temperature and diet. J. Insects As Food Feed 4 (2), 123-133.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb13)
- Gligorescu, A., Toft, S., Hauggaard-Nielsen, H., Axelsen, J.A., Nielsen, S.A., 2019. Development, growth and metabolic rate of Hermetia illucens larvae. J. Appl. Entomol. 143 (8), 875-881. http://dx.doi.org/10.1111/jen.12653, arXiv:https:// onlinelibrary.wiley.com/doi/pdf/10.1111/jen.12653.
- [Guo-Hui, Y., Yi-Ping, L., Yu-Huan, Y., Qiang, X., 2014. Effects of the artificial diet with low water content on the growth and development of the black soldier fly, Hermetia illucens (Diptera: Stratiomyidae). Acta Entomologica Sinica 57 (8), 943.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb15)
- [Harnden, L.M., Tomberlin, J.K., 2016. Effects of temperature and diet on black soldier fly, Hermetia illucens (L.) (Diptera: Stratiomyidae), development. Forensic Sci. Int. 266, 109-116.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb16)
- Holmes, L.A., Vanlaerhoven, S.L., Tomberlin, J.K., 2012. Relative Humidity Effects on the Life History of Hermetia illucens (Diptera: Stratiomyidae). Environ. Entomol. (ISSN: 0046-225X) 41 (4), 971-978. http://dx.doi.org/10.1603/EN12054, arXiv: http://oup.prod.sis.lan/ee/article-pdf/41/4/971/18313264/ee41-0971.pdf.
- Karimanzira, D., Keesman, K., Kloas, W., Baganz, D., Rauschenbach, T., 2017. Efficient and economical way of operating a recirculation aquaculture system in an aquaponics farm. Aquac. Econ. Manag. 21 (4), 470-486. http://dx.doi.org/10. 1080/13657305.2016.1259368.
- Lalander, C., Diener, S., Zurbrügg, C., Vinnerås, B., 2019. Effects of feedstock on larval development and process efficiency in waste treatment with black soldier fly (Hermetia illucens). J. Clean. Prod. (ISSN: 0959-6526) 208, 211-219. http: //dx.doi.org/10.1016/j.jclepro.2018.10.017.
- Lee, K.-S., Yun, E.-Y., Goo, T.-W., 2021. Optimization of feed components to improve Hermetia illucens growth and development of oil extractor to produce biodiesel. Animals (ISSN: 2076-2615) 11 (9), http://dx.doi.org/10.3390/ani11092573.
- [Lewis, W.K., 1922. The evaporation of a liquid into a gas. Trans. ASME. 44, 325-340. Manurung, R., Supriatna, A., Esyanthi, R.R., Putra, R.E., 2016. Bioconversion of rice straw waste by black soldier fly larvae (Hermetia illucens L.): optimal feed rate for biomass production. J. Entomol. Zool Stud. 4 (4), 1036-1041.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb22)
- Meneguz, M., Gasco, L., Tomberlin, J.K., 2018. Impact of pH and feeding system on black soldier fly (Hermetia illucens, L; Diptera: Stratiomyidae) larval development. PLoS One 13 (8), 1-15. http://dx.doi.org/10.1371/journal.pone.0202591.
- Miranda, C.D., Cammack, J.A., Tomberlin, J.K., 2020. Mass production of the black soldier fly, Hermetia illucens (L.), (Diptera: Stratiomyidae) reared on three manure types. Animals (ISSN: 2076-2615) 10 (7), http://dx.doi.org/10.3390/ani10071243. Monteith, J.L., 1981. Evaporation and surface temperature. Q. J. R. Meteorol. Soc. 107 (451), 1-27.
- [Murray, F.W., 1967. On the computation of saturation vapor pressure. J. Appl. Meteorol. 6 (1), 203-204.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb26)
- [Newton, G.L., Booram, C.V., Barker, R.W., Hale, O.M., 1977. Dried hermetia illucens larvae meal as a supplement for swine. J. Anim. Sci. 44 (3), 395-400.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb27)
- [Padmanabha, M., Beckenbach, L., Streif, S., 2020a. Model predictive control of a food production unit: a case study for lettuce production. In: 21 𝑆𝑡 IFAC World Congress 2020.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb28)
- Padmanabha, M., Kobelski, A., Hempel, A.-J., Streif, S., 2020b. A comprehensive dynamic growth and development model of Hermetia illucens larvae. PLoS One 15 (9), 1-25. http://dx.doi.org/10.1371/journal.pone.0239084.
- Padmanabha, M., Streif, S., 2019. Design and validation of a low cost programmable controlled environment for study and production of plants, mushroom, and insect larvae. Appl. Sci. (ISSN: 2076-3417) 9 (23), http://dx.doi.org/10.3390/ app9235166.
- Palma, L., Ceballos, S.J., Johnson, P.C., Niemeier, D., Pitesky, M., VanderGheynst, J.S., 2018. Cultivation of black soldier fly larvae on almond byproducts: impacts of aeration and moisture on larvae growth and composition. J. Sci. Food Agric. 98 (15), 5893-5900. http://dx.doi.org/10.1002/jsfa.9252, arXiv:https://onlinelibrary. wiley.com/doi/pdf/10.1002/jsfa.9252.
- [Parra Paz, A.S., Carrejo, N.S., Gómez Rodríguez, C.H., 2015. Effects of larval density and feeding rates on the bioconversion of vegetable waste using black soldier fly larvae Hermetia illucens (L.), (Diptera: Stratiomyidae). Waste Biomass Valoriz. 6 (6), 1059-1065.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb32)
- [Rowe, D.M., 1995. CRC Handbook of Thermoelectrics. CRC Press, Boca Raton, FL. sition of Hermetia illucens (L.) (Diptera: Stratiomyidae) larvae produced at](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb34)
- [Scala, A., Cammack, J.A., Salvia, R., Scieuzo, C., Franco, A., Bufo, S.A., Tomberlin, J.K., Falabella, P., 2020. Rearing substrate impacts growth and macronutrient compoan industrial scale. Sci. Rep. (ISSN: 2045-2322) 10 (1), 19448.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb34)
- Shumo, M., Khamis, F.M., Tanga, C.M., Fiaboe, K.K.M., Subramanian, S., Ekesi, S., van Huis, A., Borgemeister, C., 2019. Influence of temperature on selected lifehistory traits of black soldier fly (Hermetia illucens) reared on two common urban organic waste streams in Kenya. Animals (ISSN: 2076-2615) 9 (3), http: //dx.doi.org/10.3390/ani9030079.
- van Straten, G., Challa, H., Buwalda, F., 2000. Towards user accepted optimal control of greenhouse climate. Comput. Electron. Agric. (ISSN: 0168-1699) 26 (3), 221-238. http://dx.doi.org/10.1016/S0168-1699(00)00077-6.
- Tomberlin, J.K., Adler, P.H., Myers, H.M., 2009. Development of the Black Soldier Fly (Diptera: Stratiomyidae) in Relation to Temperature. Environ. Entomol. (ISSN: 0046-225X) 38 (3), 930-934. http://dx.doi.org/10.1603/022.038.0347, arXiv:https: //academic.oup.com/ee/article-pdf/38/3/930/18308048/ee38-0930.pdf.
- [van Straten, G., van Willigenburg, L., van Henten, E., van Ooteghem, R., 2011. Optimal Control of Greenhouse Cultivation. CRC Press, ISBN: 9781420059618.](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb38)
- [Wächter, A., Biegler, L.T., 2006. On the implementation of a primal-dual interior point filter line search algorithm for large-scale nonlinear programming. Math. Program. 106 (1).](http://refhub.elsevier.com/S0168-1699(23)00037-6/sb39)
- Zhang, S., Guo, Y., Zhao, H., Wang, Y., Chow, D., Fang, Y., 2020. Methodologies of control strategies for improving energy efficiency in agricultural greenhouses. J. Clean. Prod. (ISSN: 0959-6526) 274, 122695. http://dx.doi.org/10.1016/j.jclepro. 2020.122695.