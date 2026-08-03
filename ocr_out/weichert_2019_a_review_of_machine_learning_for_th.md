https://doi.org/10.1007/s00170-019-03988-5
ORIGINAL ARTICLE
A review of machine learning for the optimization of production
processes
Dorina Weichert1 · Patrick Link2 · Anke Stoll2 · Stefan R¨uping1 · Steﬀen Ihlenfeldt2 · Stefan Wrobel1
Received: 14 March 2019 / Accepted: 5 June 2019
© Springer-Verlag London Ltd., part of Springer Nature 2019
Abstract
Due to the advances in the digitalization process of the manufacturing industry and the resulting available data, there is
tremendous progress and large interest in integrating machine learning and optimization methods on the shop floor in order
to improve production processes. Additionally, a shortage of resources leads to increasing acceptance of new approaches,
such as machine learning to save energy, time, and resources, and avoid waste. After describing possible occurring data types
in the manufacturing world, this study covers the majority of relevant literature from 2008 to 2018 dealing with machine
learning and optimization approaches for product quality or process improvement in the manufacturing industry. The review
shows that there is hardly any correlation between the used data, the amount of data, the machine learning algorithms, the
used optimizers, and the respective problem from the production. The detailed correlations between these criteria and the
recent progress made in this area as well as the issues that are still unsolved are discussed in this paper.
Keywords Machine learning · Optimization · Manufacturing · Production
1 Introduction
Together with the rising popularity of machine learning
research and the growth of the available data amounts, the
applications of the developed methods have found their way
into various industrial fields. In this context especially, the
exploitation of data for optimization in existing production
lines is of high relevance [35, 53]. Optimization can take
place in two different ways: on the one hand, there is the
improvement of the product quality itself; on the other hand,
the production process can be changed for the better.
The utilization of machine learning is motivated by its
additional capabilities to spare resources, machining time,
and energy and increase yield where traditional methods
These authors contributed equally to this work.
 Dorina Weichert
dorina.weichert@iais.fraunhofer.de
 Patrick Link
patrick.link@iwu.fraunhofer.de
1
Fraunhofer IAIS, Institute for Intelligent Analysis
and Information Systems, St. Augustin, Germany
2
Fraunhofer IWU, Institute for Machine Tools and Forming
Technology, Chemnitz/Dresden, Germany
such as six sigma strategies have reached their limits [53].
In the author’s eyes, the term “machine learning” describes
algorithms to identify and extract valuable patterns in the
data: from data transformation methods (e.g., PCA), over
data exploration methods (e.g., k-means clustering), and
traditional methods of supervised learning for regression
and/or classification (e.g., decision trees) to more recent
methods (e.g., Convolutional Neural Networks). These
cover a broad range of complexities, origins, and recency
of the algorithms themselves, all having in common the
extraction and use of specific features of the data useful to
improving quality.
Though an important prerequisite for the application of
machine learning for production processes, industry 4.0,
industrial analytics and high-performance computing will
not be discussed in detail in this manuscript. The initiation
of smart manufacturing systems in existing plants can be
realized by storing and processing of arising data by existing
and additionally installed sensors. Due to the continuous
development of new sensors, processing software, and
storages on low-price level as well as the small degree of
necessary interventions into a running process, the hurdles
for smart manufacturing are set low.
The aim of this study is to review machine learn-
ing applications to optimize products and production pro-
cesses in existing production environments from 2008
The International Journal of Advanced Manufacturing Technology (2019) 104:1889–1902
/Published online: 20 June 2019

to 2018. Since earlier years, the authors refer to the
extensive review of K¨oksal et al. focusing on data min-
ing applications for quality improvement in manufactur-
ing industry [53]. Additionally, there exist more general
reviews on machine learning in manufacturing that either
do not explicitly concentrate on optimization issues [10,
37, 67, 92, 118] or focus on special methods and/or
applications [15, 112].
The interest in the integration of machine learning
and optimization algorithms in production processes has
increased steadily since 2009 and has been at a consistently
high level since 2014. Thus, it remains a hot topic in
latest research, starting with the development of scientific
methods for sensor placement, going through data storage
and processing architectures, and ending with machine
learning and optimization algorithms [118].
Since the field of machine learning and optimization
in production processes is very wide, the authors have
identified three closely related topics that will not be
covered extensively in this review. The first one is
optimization with methods from the field of design of
experiments (DOE) and response surface methodology
(RSM). Even if a DOE or RSM is used in applications,
the review will not focus on the specific designs. Here,
the authors like to refer the interested reader to the
comprehensive work of Montgomery [68], as a detailed
description of methods and applications is beyond the
scope of this review. The second topic is statistical process
control (SPC), pioneered by Shewhardt in 1925, which uses
classical statistical analysis of the collected data for process
variation reduction [93]. As the majority of publications
does not fall back to the methods of “modern” machine
learning, this field of research is excluded. A third topic
to exclude is model predictive control (MPC) as a special
field of control engineering. Here, the authors would like
to refer the interested reader for example to the work of
Mayne [64] and Scattolini [87]. In general, the application
of machine learning methods for the optimization of
production processes can take place with or without an
immediate quality feedback, depending on its’ availability.
With a quality feedback, it is quite similar to closed
loop control engineering, as it is used to adapt process
parameters to improve the measured quality. But as neither
the quality feedback, the process parameters and the process
description itself are in the typical format used for closed
loop control (feedback and parameters as time series data
and the process description as a state equation), nor is
there a frequent change of the parameters during a running
production step, the authors will exclude this special field of
research from the review.
The paper is organized as follows: firstly, the occurring
data types in manufacturing are reviewed. Secondly, an
overview on applications of machine learning for quality
improvement without change of manufacturing parameters
during the process is given. Subsequently, applications
where explicit changes of manufacturing parameters are
allowed are reviewed in detail. After a detailed analysis
connecting data, machine learning, and optimization, a
conclusion is drawn and open research questions are
discussed.
2 Data in machine learning in production
The first step to solving a machine learning problem is
to identify the data that is available. There are different
types of data which will affect the type of analyses that
can be used on them. Based on their types, the amount
of information which data gives can vary considerably
[11]. Data can be structured in the following ways. Topics
such as data quality, missing data, or details about data
preprocessing will not be addressed in this work, but may
be found, for example, in [35].
2.1 Qualitative vs. quantitative data
Qualitative data can be divided into nominal data and
ordinal data. Nominal data only gives the name of a category
to which something belongs like the name of a material
for the press hardening of a component [74]. Ordinal data
indicate the order of something. For example, Neugebauer
et al. [69] divide the quality of gears, which are produced
by forming, into classes depending on the pitch accuracy.
Quantitative data can be interval data where there is no
absolute zero point such as the tool temperature in a press
hardening process; and ratio data which can be used to give
information about relative size, such as sheet thickness of a
press hardened part at a certain point [11, 74].
2.2 Time series vs. workpiece-related data
Most commonly, a time series is a sequence or continuous
signal with equally spaced points in time like the energy
consumption of a machine tool over time (see for example
[109]). Another possibility is data that is related to
a workpiece such as the workpiece temperature during
the heating of the press hardening process [74]. Such
workpiece-related data can, however, also be time series
data.
2.3 Controllable vs. uncontrollable data
As described in Oh et al. [72], data can also be divided with
regard to their controllability. Controllable parameters can
be adjusted either manually or automatically, while uncon-
trollable parameters may not be changed. An uncontrollable
Int J Adv Manuf Technol (2019) 104:1889–1902
1890

parameter is for example the sheet thickness at the begin-
ning of a press hardening process because this parameter is
defined by the coil producer. A controllable parameter can
be the time a part remains in the press.
2.4 Present vs. historical data
Another way of subdividing data may be with respect to its
measurement date. Machine learning algorithms can learn
from historical data and then use present data to predict
future outcomes. However, it has to be taken into account
that the data acquisition can be changed and adapted over
time. Therefore, it may be necessary to clean up historical
data, as for example described in [38] or models based on
older data have to be retrained.
2.5 Measured vs. simulated data
The origin of data also plays a significant role. It is
important to verify simulated data with real data. The
use of both simulated and experimental data is also
possible (see for example [25] where new simulations are
automatically performed in order to improve the prediction
quality of a platform that incorporates experimental data,
computational simulations, and a machine learning model).
In the case of production processes, it should also be
considered that established and robust processes almost
exclusively produce good parts and very few data are
available for rejected parts. However, machine learning
models need balanced data, so simulation plays a key role
here [7].
2.6 Observable quantities vs. process state variables
In many manufacturing processes, it is not possible to
measure on-line the state variable values that describe
the system state and are essential for process control.
Instead, only quantities related to the state variables can be
observed [89]. Senn et al. [89, 90] for example describe
a deep drawing process where observable quantities are
forces, displacements, and strains while state variables are
the high-dimensional stresses in the workpiece at various
locations.
The knowledge of the structure of production data is
crucial for the right choice of machine learning models.
Most data coming from production systems equipped with
sensors can be considered as structured data which is
much easier to handle than unstructured data [85]. Another
important aspect which is not the focus of this manuscript is
the fusion of data from multiple sensors. More information
on this topic can be found in [60] or [81]. The next section
describes different approaches for a machine learning–
based optimization in production.
3 Application of machine learning
for optimization of production
Process optimization by machine learning can be struc-
tured into two main topics, distinguished by the adjust-
ment of production parameters. The first is optimiza-
tion without change of production parameters during the
manufacturing process. Examples are root cause analy-
ses to prevent from recurrent quality issues, early pre-
diction of manufacturing outcomes to spare unnecessary
process steps, and diagnostic methods to detect erroneous
behavior of products or processing units. All examples
have in common that there is no direct adjustment of
the production parameters but product quality is improved
indirectly.
A second topic is optimization with change of production
parameters.
Here, optimal production parameters are
determined using the data of an already running production
process. By adjusting the parameters to the characteristics
of the product and the specific optimization goal, a higher
quality is achieved. Implementations can be distinguished in
machine learning approaches with additional optimization
modules and self-optimizing control systems based on
analytical process models. In this paper, only machine
learning approaches are discussed.
In both (direct and indirect) approaches, the objective
for optimization can be a product- or process-specific
quantity. Product-specific quantities are for example surface
roughness, shrinkage, and processor speed, while the energy
consumption of a plant or tool wear is a process-specific
one. Optimization of both types of objectives results in
improved product quality defined in terms of cost, time,
consumption of resources, and/or the specific optimization
objective.
3.1 Optimization without parameter changes
Typical industrial applications for quality improvement
based on machine learning are found in large-scale
production such as plastic injection molding (PIM) and
the production of semiconductors. The authors assume
that this is grounded on the high amounts of usable
data points provided due to short cycle times. Especially
that in the manufacturing of micro-electronic parts exists
long-lasting tradition (see, e.g., [4, 41] for examples
for classification algorithms in industry as early as in
1993). Up to now, scientists are still challenged by
imbalanced datasets, missing data, and concept drift [16,
115]. The following section provides an overview of
three different approaches for optimization without change
of the production parameters: Root cause analysis, early
prediction of manufacturing outcomes, and diagnostic
systems.
Int J Adv Manuf Technol (2019) 104:1889–1902
1891

3.1.1 Root cause analysis
An obvious approach for quality improvement is the
analysis of existing data records to extract relevant features
and feature combinations for high or low product quality.
This might be done by feature selection at a preliminary
stage of learning a model or as specific root cause analysis.
There exists a lot of literature in these fields (see the
already mentioned reviews [10, 15, 37, 67, 92, 112, 118])
and analysts seem to be satisfied with the identification
of previously unknown patterns and important features
relevant to product quality. Reports on the consequences of
changes of production parameters drawn from the patterns
are rare.
In the sector of semiconductor manufacturing, the
research of Chien et al. on root cause analysis is quite
fundamental. In his work, he proposed k-means clustering
[24]; principal component analysis (PCA), clustering, and
decision trees [22]; stepwise batch regression algorithms
with random forests [21] and feature selection together with
logistic regression [23] to find root causes for poor quality
and finally enhance yield.
Other authors such as Kumar et al. [56] or Diao et al.
[30] apply hierarchical generalized linear models (GLM)
or improved PCA and modified support vector machines
(SVM) to identify dominant factors for quality and quality
prediction. It is also possible to apply Gibbs Sampling
for variable selection, learn multivariate adaptive regression
splines (MARS) to predict semiconductor yield, and use
decision tables to extract root causes [49].
Another method to find root causes for quality issues
is the extraction of defect patterns. For instance, Franciosa
et al. [32] analyze a multi-stage assembly system and
utilize a combination of multi-physics simulations from
first principles, measurement data and artificial neural
networks (ANN) to identify defect patterns. In the field
of semiconductor production, Wang [110] proposes the
clustering of defect patterns.
Association rule mining is a method to extract inter-
pretable relationships relevant for product quality (see
[114] in semiconductor manufacturing). In drill produc-
tion, Kamsu-Foguem et al. thoroughly describe the use of
association rules [44].
3.1.2 Early prediction of manufacturing outcomes
In optimization of manufacturing processes, not only is
product quality a highly relevant criterion, but so are
the costs of production steps. If production steps are
expensive in terms of time or price, it is useful to
predict manufacturing outcomes beforehand. With this
method, unnecessary and costly production steps can be
avoided by dropping products from the production line
before the critical steps. Alternatively, additive corrective
manufacturing actions can be initiated, for example the
correction of wafers with expected poor performance in
semiconductor production [116].
The early prediction of production outcomes differs from
traditional process identification in the size of the parameter
set. For process identification, a full set of relevant
production parameters of all processing stages is needed,
while the early prediction already works with process
parameters of an early relevant part of the production line,
allowing to introduce correcting actions before finishing the
whole production process.
But simple process identification with the full parameter
set enables the so-called virtual metrology as exemplarily
described by Kang et al. [45] and Khan et al. [50]. Here,
the quality of the out-of-sample products is predicted by a
machine learning method, saving time and costs. As this
does not optimize the production process but only means
a regression/classification of the production output, the
authors would like to refer the reader to the work mentioned
above.
The challenge of the early prediction of manufacturing
outcomes is to make a reliable prediction of the final quality
at early stages of the process and to identify relations
between process steps. Several authors proposed solutions,
e. g., the work of Lieber et al. [59] and Konrad et al.
[54] for rolling mill processes with self-organizing maps
(SOM) and k-Nearest-Neighbor (kNN) approaches or Arif
et al. [5] for decision trees in semiconductor manufacturing.
Both works have in common that no application was
reported.
More promising is the work of Weiss et al. [115,
116], who estimated the final microprocessor speed after
each manufacturing operation applying linear regression
and boosted trees: the predictions initiating corrective
manufacturing actions if necessary. The authors were
challenged by the already mentioned concept drift, missing
data, and imbalanced datasets. Special methods to overcome
these problems were developed by Chen and Boning [16],
who apply boosting and bagging of customized decision
trees to predict semiconductor yield before packaging.
3.1.3 Diagnostic systems
Another way of optimizing the final quality of a product is
the use of diagnostic systems within the production line. It is
possible to monitor the product itself (part diagnosis) and/or
the processing machines (plant diagnosis). Both approaches
lead to an alarm being raised if the condition of the part or
machine is anomalous or becoming anomalous, requesting
correction actions to be taken.
Int J Adv Manuf Technol (2019) 104:1889–1902
1892

3.1.4 Part diagnosis
For the diagnosis of parts, two main applications are
described, namely visual inspection and the diagnosis of
part assemblies.
Automatic visual inspection, applied before, during, and
after production processes, serves to maintain good part
quality, examining images for possible faults. Various meth-
ods were developed for the production of semiconductors
and screen glasses [40, 43, 105], ceramics and tiles [47],
and miscellaneous processes relating to metal parts [42, 63,
88, 113, 121]. Additionally, generic methods for different
materials and purposes were developed [73, 80].
Methods for visual inspection vary over projection meth-
ods like independent component analysis [105] and PCA
[17]; filter-based approaches like discrete cosine trans-
form [76] and discrete wavelet transform [121]; learning-
based approaches like SVM [106], Hidden Markov Models
(HMM) [42], fuzzy clustering [43], and convolutional neu-
ral networks (CNN) [63, 73, 80, 113] for regression or
classification; and statistical methods [88].
Diagnosis of assembly processes or its results usually
uses data sources different from images, resulting in the
use of different methods. Additionally, recent authors try to
cover not only one specific processing stage but multi-stage
processes as well. This complicates the problem to be solved
due to correlations between the different process steps and
the resulting error propagation. For sheet metal assemblies,
Ceglarek and Prakash [14] show a piecewise least squares
approach for use in a state-space model. Their introduction
reviews various publications in the field of fixture diagnosis
methods. The force signature of the assembling robot arm is
used by Rodriguez et al. as input to an SVM [82]. Luo et al.
[61] extend this approach by abstracting specific behavior
representations from the force signature.
3.1.5 Plant diagnosis
Diagnosis of production plants or machines can be
realized by anomaly detection methods. In anomaly
detection of production plants, one distinguishes between
phenomenological and model-based approaches [70]. In
phenomenological approaches, measurements are classified
directly to detect anomalous behavior, while model-based
approaches compare a system model representing the
normal system behavior and the system’s measurement data.
Due to the high amount of available publications,
only a short introduction into the topic is given and the
important topic of one-class classification is being skipped.
For this, the authors would like to refer the interested
reader to the comprehensive work of Shin et al. [96].
In case of phenomenological approaches, sensor data like
time-series data is processed. To extract features from
it, transformations like wavelet transform [33], empirical
mode decomposition [39, 117], or independent component
analysis [101] are used. The features can be processed with
various algorithms like ANN, SVM, optimizers, or fuzzy
logic [127]. Typical applications are induction machines
[8], pneumatic systems [27], gear boxes [86], and bearings
[57]. Model-based approaches usually do not rely on feature
extraction from time-series and can use machine learning
algorithms like PCA or partial least squares [120] directly.
Closely related to anomaly detection methods, which are
mostly used for failure detection, is the field of maintenance
methods which aim to prevent machine failures due
to deterioration of the machine. A distinction is made
between time-based and condition-based maintenance,
called preventive and predictive maintenance [66].
Preventive maintenance tries to extract the mean useful
life of a machine and/or its parts to schedule maintenance
activities before breakdown. To the author’s knowledge, the
use of machine learning methods for this task has not been
reported to the scientific community yet, as simple statistics
leads to good results [66]. For preventive maintenance,
a mathematical formulation of the loss function to be
optimized can be found (see, e.g., the work of Cassady and
Kutanoglu [13]). If the term of preventive maintenance is
abstracted to the level of job shop scheduling, the work
of Adibi et al. shows parameter estimation by clustering
[1], reinforcement learning [91], and ANN [2]. Predictive
maintenance tries to extend the maintenance intervals by
monitoring the machine’s conditions, sparing costs for
unnecessary, time-based scheduled, maintenance activities.
In contrast to preventive maintenance, there are several
authors applying machine learning methods in this field, and
the authors like to refer the interested reader to the review
of Ahmad and Kamaruddin comparing both time-based and
condition-based maintenance for various examples [3].
3.2 Optimization with parameter changes
In order to optimize parameters of industrial processes
which were described by machine learning methods, the
typical workflow contains the following four steps [53]:
1.
Generating a database with few experiments or run
simulations with DOE methods,
2.
Modeling the physical correlations between the process
parameters and the quality criteria with statistical or
machine learning methods,
3.
Optimization of the process parameters using the
created process model,
4.
Adjusting the process parameters manually or automat-
ically.
As mentioned in Section 2, the database for modelling
the physical correlations with machine learning methods
Int J Adv Manuf Technol (2019) 104:1889–1902
1893

can consist of measured data like in [46] or of simulated
data [77, 103]. If the machine learning model is supposed
to replace a time-consuming physics-based simulation, it
is called a meta- or surrogate-model [78, 111]. With
this method, the risk of error propagation through the
different models is given. Both systematic and stochastic
errors can occur during construction of the physics-based
simulation and subsequently be adapted by the meta-model
built from its calculations, resulting in an invalid meta-
model as well. But even with valid physics- and meta-
models, approximation errors to the real process have to be
considered. However, the approaches discussed below are
based on measured data. Often, the created process models
are not simple linear regression models but complex non-
linear models as SVM or ANN. The training of these models
can be time consuming and computationally expensive, but
for a good representation of the physical correlations, the
usage of non-linear models is often indispensable.
The optimization of process parameters can be realized
by traditional approaches like Newton’s method, hill climb-
ing algorithms, or gradient descent algorithms, leading to
a local optimum. A second possibility to optimize the pro-
cess parameters is to use evolutionary algorithms, usually
leading to the global optimum of the given search domain.
The usage of evolutionary techniques received a lot of
attention in recent years [122, 123]. The approaches dis-
cussed in the following section use evolutionary algorithms
in most cases.
3.2.1 Machine learning with subsequent optimization
approaches
There exist a lot of different fields for machine learning
approaches and subsequent parameter optimization. The
following sections present examples in different specific
manufacturing fields.
Milling Especially in milling processes, a lot of research
was done on approaches including ANN and genetic
algorithms (GA). The authors of [46, 97, 107] used
these techniques to improve different quality criteria by
optimizing the cutting parameters of the milling process.
Denkena et al. [28] suggest a SVM to predict the
geometric deviation of the workpiece. To optimize the
cutting parameters, they were sampled on a grid and optimal
parameters were chosen based on the prediction of the
SVM. In [26], Coppel et al. compare ANN and SVM models
to predict quality criteria and also test different optimization
algorithms, such as GA, particle swarm optimization (PSO),
and simulated annealing (SA) algorithms, respectively,
to determine optimal cutting parameters for the milling
operation. An ANN model with subsequent PSO achieved
the best results.
Turning Turning operations were the process of interest in
[9, 36]. In Bouacha and Terrab [9], an ANN with subsequent
PSO was compared with a non-dominated sorting genetic
algorithm (NSGA-II)-based RSM model. Because of less
computation time, the ANN with PSO algorithm was the
better choice in this case. Gupta et al. [36] used different
modeling approaches like regression, RSM, SVM, and
ANN to predict the quality criteria; GA was used to find
optimal process parameters.
Gear hobbing and boring In the field of gear hobbing [12]
ANN and in boring [108] ANN and SVR were proposed
to predict the quality criteria. Cao et al. [12] optimized
their process parameters based on ANN with a differential
evolution algorithm. Venkata Rao and Murthy [108] used an
unspecified multi-response optimizer.
Electrical discharge and abrasive waterjet machining The
authors of [6, 62] have done research on parameter
optimization in electrical discharge machining (EDM)
and wire EDM [65, 79], respectively. All of them used
ANN to predict the quality criteria, except Rao and
Pawar [79], who applied a second-order regression model.
The process parameters were optimized with different
algorithms: augmented Lagrange multiplier algorithm [6],
GA, PSO and SA algorithm [62], wolf pack algorithm
based on the strategy of the leader (LWPA) [65], and
artificial bee colony (ABC) algorithm [79]. In more special
EDM, applications like wire EDM turning [55], micro-
EDM [126], or micro-clearance electrolysis-assisted laser
machining [104] parameter optimizations based on machine
learned prediction models were conducted as well. All
used more or less already mentioned combinations of ANN
and NSGA-II [55], SVM and GA [126], and ANN and
improved ant colony algorithm [104]. Zhang et al. [126]
predicted the processing time and electrode wear with a
support vector machine as a regression model. In the second
step, they performed a multi-objective optimization with a
GA. The results represent a pareto-optimal solution between
the minimum processing time and minimum electrode
wear. Srinivasu and Babu [100] and Zain et al. [124,
125] optimized the process parameters of abrasive waterjet
machining with regression models and ANN, respectively,
followed by GA.
Finishing For the parameter optimization process in roller
grinding, Chen et al. [19] used RSM for the quality
prediction and a hybrid PSO algorithm for the optimization
task. For the optimal configuration of the grinding slurry of
waterjet grinding, Liang et al. [58] used an adaptive neuro-
fuzzy inference system (ANFIS) approach. Zhao et al. [128]
optimized the parameters of the grinding and polishing
Int J Adv Manuf Technol (2019) 104:1889–1902
1894

process of integrally bladed rotors by using a regression
model and the signal to noise ratio for the optimization.
Plastic injection molding (PIM) and fused deposition mod-
eling For PIM, extensive reviews are found in [31, 48],
extending the possible methods to other meta-models and
optimization algorithms. Further, authors like Chen et al.
[18] and Xu and Yang [119] used ANN and GA or rather
ANN, gray correlation analysis, PSO, and multi-objective
PSO for the parameter optimization. Peng et al. [75]
improved fused deposition modeling by using the response
surface methodology combined with a fuzzy inference sys-
tem and a GA optimization.
Welding In the field of welding, Rong et al. [83] proposed
an extreme learning machine; Dhas and Kumanan [29],
a quadratic regression model; and Norouzi et al. [71],
an ANN, an ANFIS, and an ANN trained with PSO
for predicting quality parameters. For process parameter
optimization, Rong et al. used only PSO algorithm [83],
while the other authors used both PSO and GA.
Others The last three examples for research in parameter
optimization based on machine learning models are press
hardening [103], electroplating [34], and selective laser
sintering [84]. Stoll et al. [103] predicted their quality
criteria with a linear regression model. In the second
step, a parameter optimization based on the least squares
method was performed. Genna et al. [34] and Rong-Ji
et al. [84] predicted their quality criteria in electroplating
and selective laser sintering with ANN and optimized
the process parameters by a so-called external optimized
algorithm and GA, respectively.
3.2.2 Machine learning with other optimization approaches
The
previously
mentioned
papers
contain
various
approaches to optimize process parameters and improve
quality in many different manufacturing applications. In
general, many researchers used ANN to describe their
manufacturing process and predict the quality criterion
of interest. In the second step, a GA was applied. Alter-
natively, the model and the optimization can be realized
simultaneously by using an active DOE [94, 95], sequential
approximate optimization [51, 52], or Bayesian optimiza-
tion [20, 99, 102]. Another possibility is to inverse the
problem. Instead of building a model and optimizing the
input parameters, a model with quality parameters as inputs
and process parameters as outputs is constructed [98].
This rejects the underlying assumption used beforehand
that one specific parameter configuration will result in a
defined quality value, but different parameter configura-
tions can result in the same quality. Here, the assumption is
that different qualities can result from the same parameter
configuration. This seems counterintuitive to the authors,
but according to [98] the prediction error compared to
experimental data is less than 5%.
4 Discussion and analysis
The reviewed literature shows that the production-related
applications of machine learning with or without optimiza-
tion are manifold. In this study, we investigated which
combinations of production methods and machine learning
models are most successful and how optimization methods
for quality improvement can be integrated. Our results are
presented in the following.
4.1 Classes and origin of used data
The available data for training the machine learning models
can be classified according to the categories explained in
Section 2: Process parameters mostly are on continuous
scales, therefore most data in the mentioned papers contain
quantitative data such as water pressure or jet traverse rate
[100]. Further examples for interval and ratio data can be
found in [116]. In a few cases, also nominal qualitative data
are available, for example in [12, 16, 116].
Depending on the selected optimization goal, data can be
available in the shape of time series and product-specific
data. If the parameters are not changed during optimization
(see Section 3.1), often only product-specific data are
available, except in the area of anomaly detection [8, 27, 57,
86]. If the parameters are changed during optimization (see
Section 3.2), the data may be available both as time series
and as product-specific data. In the work of Bouacha and
Terrab [9], among other things, the process forces and the
surface roughness of the part are defined as outputs. Here,
the process forces are available as time series and the surface
roughness of the part as product-specific quantity.
For the distinction into controllable and uncontrollable
data, as well as observable quantities and process state
variables, it can be summarized that input variables are
mostly controllable and observable quantities, for example:
cutting speed [36] or electrode feed rate [104]. Input
variables can also only be controlled indirectly, for example
feed rates [26, 36]. The output variables, however, are
mostly uncontrollable or only indirectly controllable, for
example the process forces in Bouacha and Terrab [9].
Most of the data in the investigated papers was recorded
and subsequently a machine learning model was trained.
Exceptions are the work of Denkena et al. [28]; here, the
model is further trained with present data. Furthermore, they
also use simulated data to train the model. More examples
of approaches based only on simulated data can be found in
Int J Adv Manuf Technol (2019) 104:1889–1902
1895

Fig. 1 Applications, algorithms, and number of data points per input. Size and color indicate the median of the number of data points per input
dimension of the model. On the horizontal axis, the machine learning algorithms are roughly sorted by complexity
[51, 77, 103]. In the remaining articles, only measured data
have been used.
4.2 Machine learning and applications
A closer look on the reviewed papers reveals several
potentials to increase the effectiveness of machine learning
for optimization of processes.
Figure 1 gives an overview of the analyzed research
papers. Tables 1 and 2 map the different applications and
algorithms to the classes used in Figs. 1 and 2.
It is obvious that in nearly every mentioned field of
application every mentioned algorithm has been used. The
size and color of the points additionally give a feeling for the
used data. They represent the median of the number of data
points per input dimension; the median is used due to the
fact that the specific distributions are unequally distributed.
It can be seen that most entries are on the same level, but
there are upper outliers in semiconductor manufacturing and
diagnosis, where huge databases are available.
To dive deeper into the topic of the used data and the
model complexity, Fig. 2 shows the ratio of data points
Table 1 Classification of applications
Diagnosis
Machining
Plastic manufacturing
Others
Defect detection
Milling
PIM
welding
Automatic visual inspection
Welding
Fused deposition modeling
Gas forming
Assembly fault detection
Gear hobbing
Polyester film manufacturing
Press hardening
Finishing
Job shop scheduling
Drilling
Textile draping
Turning
Deep drawing
EDM
Abrasive waterjet machining
Boring
Int J Adv Manuf Technol (2019) 104:1889–1902
1896

Table 2 Classification of algorithms
Clustering
Projections
Decision tree
Special neural
Other classification
Other regression
ensembles
networks
algorithms
algorithms
kNN
PCA
Boosted trees
ANFIS
HMM
GLM
k-means
ICA
RF
CNN
Logistic regression
MARS
Gabor filter
RBF-NN
Association rule mining
Regression tree
SOM
Decision tree
Gaussian process
Fuzzy classification
Extreme learning machine
Statistical image processing
per input dimension for different algorithms, sorted roughly
by their complexity. Some really high ratios occurring in
diagnosis via projections are skipped for a better scaling.
Two important points can be recognized from this figure.
Firstly, the values of the data points per input dimension;
secondly, the missing relationship of this ratio to the used
algorithms.
The number of data points per input dimension varies
between 1 and some thousand, and the authors like to
state that ratios below 10 might be critical. To learn
an appropriate model, the data has to represent the full
complexity of the given process. For example, if the process
is linear and assuming no noise, at least two data points
Fig. 2 Point-dimension ratio for used algorithms. The image was
created using a swarm plot to make points with the same values
distinguishable. The gray area indicates a critical amount of points per
dimensions
per dimension are necessary to map this relationship from
the data. With increasing noise and the potential of outliers,
the ratio has to increase as well to learn an appropriate
model. As the industrial processes are assumed to have
a higher complexity, it might be possible that even with
a sophisticated DOE not all relevant relationships are
represented by the data.
Relating the ratio to the algorithms, the authors expected
them to be correlated, as a more complex algorithm that
is able to map more complex relationships typically needs
more representative data. But this expectation was not
fulfilled, as there is no correlation visible. All algorithms
are used with all possible ratios. In the opinion of the
authors, this is considered critical. To stay with the example
mentioned beforehand, an ANN can be used for a linear
mapping as well as a simple linear regression, but the
less complex model has several advantages over the ANN.
On the one hand, it provides a better interpretability, so
the mapped relationships can be understood and possible
failures (of the data and the model) can be detected. On the
other hand, a complex model needs more time for training,
split into the actual training time, the feature engineering,
and the tuning of the hyperparameters. If training time is an
issue, this fact should not be ignored.
At the end of this paragraph, the authors want to point
out that process complexity, the number of data points per
input dimension to the model, and the model complexity are
highly related. To learn an appropriate model, the data has to
represent the process complexity and the model complexity
has to fit both the process complexity and the number of
data points available.
4.3 Optimization algorithms
If optimization is used to find the best process parameters as
stated in Section 3.2, an appropriate optimization algorithm
has to be selected. As the loss function is assumed to be
complex with different local optima, global optimization
algorithms are used. In the meantime, GA is just as popular
as PSO, while both approaches can provide similar results
as comparisons like [29, 62, 71] show.
Int J Adv Manuf Technol (2019) 104:1889–1902
1897

4.4 Applicability in the real process
In this section, the authors want to discuss the applicability
of the different approaches in real production processes.
For root cause analysis, the early prediction of manu-
facturing outcomes, and diagnostic systems, approaches are
assumed to work in real life (see e. g. [40, 44, 116]).
If process parameters are changed, the application is
more critical, due to several reasons. Firstly, as the used
data originates from simulations and experiments, it is not
certain that it truly represents the real production process.
Secondly, for a running process, optimization results have
to be robust. They should be valid for different machines
and products and should be able to tolerate measurement
outliers like a crashed sensor. Thirdly, for process chains,
certain parameter changes that are valid for a single
machine might be inconvertible due to the relationship
to previous and subsequent process steps. Processing
times cannot change if the process chain shall not get out
of step.
A more general problem seems to be the amount of
available data, as the analysis in Section 4.2 shows. If that
is the case, the authors propose to add additional, better
available data such as simulation data or to inject knowledge
using a gray box approach. Both possibilities can result
in higher model accuracy and higher acceptance of the
model. More data generally provides the ability to map more
complex processes and to reduce the model’s variance. With
respect to the acceptance issue, the authors think that the
opportunity to improve the model by domain knowledge can
lower the hurdle to use it. Together with an interpretable
model like the rule mining approach by Kamsu-Foguem
et al. [44], this can help establish appropriate data mining
approaches for optimization in production.
5 Conclusion and further aspects
5.1 Summary
The advent of smart manufacturing simplifies the exploita-
tion of data provided by whole production plants, individual
machines, or single sensors, enabling machine learning at
different stages of complexity. Simultaneously, a shortage
of resources and the struggle of manufacturers to stay com-
petitive makes machine learning necessary to spare energy,
time, and resources and to reduce waste. As data often
already exists in various storages or is cheap to create, the
step to its beneficial use is a small one.
In this review, the available data types and the use of
the data for machine learning in different applications were
described. The applications vary from the simple setting of
learning a valid machine learning model to the combination
of machine learning with optimization. If only a model
is learned, it can be used for root cause analysis, the
early prediction of manufacturing outcomes, and diagnostic
systems to optimize product quality or process efficiency.
Else, if a model is combined with optimization algorithms,
it is possible to find production parameters optimal for
a specified loss function. This function can include the
mentioned constraints on energy, time, and resources and
waste or describe a specific measure of the part’s quality.
The optimized parameters and their introduction into the
machine make the whole production process more flexible
and adaptive to the different requirements occurring in the
process.
5.2 Conclusion
Given these potentials of optimization, the closer analysis
of the overall process of data collection, model training,
and optimization revealed a critical aspect: the connection
between the process complexity, the stored data amount,
and the model complexity. In the inspected papers, quite
often, this connection was not respected, leading to complex
models being trained on low amounts of data, risking
overfitting and/or a lack of interpretability. This aspect can
gain skepticism toward the application of machine learning
in the manufacturing industry. To face this challenge, the
authors recommend being careful in every step of building
the optimization chain and to question the data, the used
machine learning methods, and optimizers. Other critical
aspects hindering the optimization of processes via machine
learning might be a lack of relevant data or difficulties
in getting access to the machine’s control systems. All
these problems might vanish with time passing to gain
expertise, fill storages, and lower hurdles by hard- and
software.
5.3 Future research directions
In the author’s eyes, machine learning in production is not
limited to the before-mentioned improvements. It has the
specific chance to improve product quality enormously if
applied for open-loop control for multi-stage production
processes, as already proposed by Konrad et al. [54],
Lieber et al. [59], and Arif et al. [5]. As product quality
can already be predicted at early production stages as
done by Weiss et al. [116], one could optimize for the
best subsequent machine parameter set to achieve the best
possible product quality, given the limits of the raw material,
the production parameters, and the previous processing
results. Thinking bigger, this approach could be extended
from the product-specific stage to machine- and plant-
specific stages, improving the overall efficiency taking
resource, energy, and time restrictions into account.
Int J Adv Manuf Technol (2019) 104:1889–1902
1898

Yet another future research topic could be the simplifica-
tion of machines and the use of larger tolerances of the raw
material. Machine learning–based optimization techniques
might face the higher requirements of the processing steps,
ensuring unvarying quality, and simultaneously reducing the
costs of machines and the raw material.
Acknowledgments This work was supported by Fraunhofer Cluster of
Excellence “Cognitive Internet Technologies.”
Funding information This work is part of the Fraunhofer Lighthouse
Project ML4P (Machine Learning for Production).
References
1. Adibi MA, Shahrabi J (2014) A clustering-based modified
variable neighborhood search algorithm for a dynamic job shop
scheduling problem. Int J Adv Manuf Technol 70(9):1955–1961
2. Adibi
MA,
Zandieh
M,
Amiri
M
(2010)
Multi-objective
scheduling of dynamic job shop using variable neighborhood
search. Expert Syst Appl 37(1):282–287
3. Ahmad R, Kamaruddin S (2012) An overview of time-based and
condition-based maintenance in industrial application. Comput
Ind Eng 63(1):135–149
4. Apte C, Weiss S, Grout G Predicting defects in disk drive
manufacturing: a case study in high-dimensional classification. in:
CAIA. IEEE Computer Society Press, Los Alamitos, pp 212–218
5. Arif F, Suryana N, Hussin B (2013) Cascade quality prediction
method using multiple pca+id3 for multi-stage manufacturing
system. IERI Procedia 4:201–207
6. Assarzadeh S, Ghoreishi M (2008) Neural-network-based model-
ing and optimization of the electro-discharge machining process.
Int J Adv Manuf Technol 39(5-6):488–500
7. Batista G, Prati R, Monard M (2004) A study of the behavior
of several methods for balancing machine learning training data.
ACM SIGKDD Explor Newslett 6(1):20–29
8. Bellini A, Filippetti F, Tassoni C, Capolino GA (2008) Advances
in diagnostic techniques for induction machines. IEEE Trans Ind
Electron 55(12):4109–4126
9. Bouacha K, Terrab A (2016) Hard turning behavior improvement
using nsga-ii and pso-nn hybrid model. Int J Adv Manuf Technol
86(9-12):3527–3546
10. Braha D (2001) Data mining for design and manufacturing:
Methods and applications massive computing, vol 3. Springer,
Boston
11. Calder J, Sapsford R (2006) Statistical techniques. In: Sapsford R,
Jupp V (eds) Data collection and analysis. Sage Publications Ltd,
London, pp 208–242
12. Cao WD, Yan CP, Ding L, Ma Y (2016) A continuous
optimization decision making of process parameters in high-speed
gear hobbing using ibpnn/de algorithm. Int J Adv Manuf Technol
85(9-12):2657–2667
13. Cassady CR, Kutanoglu E (2005) Integrating preventive mainte-
nance planning and production scheduling for a single machine.
IEEE Trans Reliab 54(2):304–309
14. Ceglarek D, Prakash PK (2012) Enhanced piecewise least squares
approach for diagnosis of ill-conditioned multistation assembly
with compliant parts. Proc Inst Mech Eng Part B: J Eng Manuf
226(3):485–502
15. Chandrasekaran M, Muralidhar M, Krishna CM, Dixit US
(2010) Application of soft computing techniques in machining
performance prediction and optimization: a literature review. Int J
Adv Manuf Technol 46(5):445–464
16. Chen H, Boning D (2017) Online and incremental machine learn-
ing approaches for ic yield improvement. In: 2017 IEEE/ACM
International conference on computer-aided design (ICCAD),
Irvine, pp pp 786–793
17. Chen SH, Perng DB (2011) Directional textures auto-inspection
using principal component analysis. Int J Adv Manuf Technol
55(9):1099–1110
18. Chen WC, Fu GL, Tai PH, Deng WJ (2009) Process parameter
optimization for mimo plastic injection molding via soft
computing. Expert Syst Appl 36(2):1114–1122
19. Chen Z, Li X, Wang L, Zhang S, Cao Y, Jiang S, Rong Y (2018)
Development of a hybrid particle swarm optimization algorithm
for multi-pass roller grinding process optimization. Int J Adv
Manuf Technol 99(1-4):97–112
20. Cheng H, Chen H (2014) Online parameter optimization in robotic
force controlled assembly processes. In: 2014 IEEE International
conference on robotics and automation (ICRA). Piscataway, pp
3465–3470
21. Chien CF, Chuang SC (2014) A framework for root cause
detection of sub-batch processing system for semiconductor
manufacturing big data analytics. IEEE Trans Semicond Manuf
27(4):475–488
22. Chien CF, Hsu CY, Chen PN (2013) Semiconductor fault detec-
tion and classification for yield enhancement and manufacturing
intelligence. Flex Serv Manuf J 25(3):367–388
23. Chien CF, Liu CW, Chuang SC (2017) Analysing semiconductor
manufacturing big data for root cause detection of excursion for
yield enhancement. Int J Prod Res 55(17):5095–5107
24. Chien CF, Wang WC, Cheng J (2007) Data mining for yield
enhancement in semiconductor manufacturing and an empirical
study. Expert Syst Appl 33(1):192–198
25. Colosimo BM, Pagani L, Strano M (2015) Reduction of
calibration effort in fem-based optimization via numerical and
experimental data fusion. Struct Multidiscip Optim 51(2):463–478
26. Coppel R, Abellan-Nebot JV, Siller HR, Rodriguez CA, Guedea
F (2016) Adaptive control optimization in micro-milling of
hardened steels—evaluation of optimization approaches. Int J Adv
Manuf Technol 84(9-12):2219–2238
27. Demetgul M, Tansel IN, Taskin S (2009) Fault diagnosis of
pneumatic systems with artificial neural network algorithms.
Expert Syst Appl 36(7):10,512–10,519
28. Denkena B, Dittrich MA, Uhlich F (2016) Self-optimizing cutting
process using learning process models. Procedia Technol 26:221–
226
29. Dhas JER, Kumanan S (2011) Optimization of parameters of
submerged arc weld using non conventional techniques. Appl Soft
Comput 11(8):5198–5204
30. Diao G, Zhao L, Yao Y (2015) A dynamic quality control
approach by improving dominant factors based on improved
principal component analysis. Int J Prod Res 53(14):4287–4303
31. Fernandes C, Pontes AJ, Viana JC, Gaspar-Cunha A (2018)
Modeling and optimization of the injection-molding process: a
review. Adv Polym Technol 37(2):429–449
32. Franciosa P, Palit A, Vitolo F, Ceglarek D (2017) Rapid response
diagnosis of multi-stage assembly process with compliant non-
ideal parts using self-evolving measurement system. Procedia
CIRP 60:38–43
33. Gao RX, Yan R (2011) Wavelets. Springer, Boston
34. Genna S, Simoncini A, Tagliaferri V, Ucciardello N (2017) Opti-
mization of the sandblasting process for a better electrodeposition
of copper thin films on aluminum substrate by feedforward neural
network. Procedia CIRP 62:435–439
35. Grzegorzewski P, Kocha´nski A, Kacprzyk J (2019) Soft Modeling
in Industrial Manufacturing. Springer, Berlin
Int J Adv Manuf Technol (2019) 104:1889–1902
1899

36. Gupta AK, Guntuku SC, Desu RK, Balu A (2015) Optimisation of
turning parameters by integrating genetic algorithm with support
vector regression and artificial neural networks. Int J Adv Manuf
Technol 77(1-4):331–339
37. Harding JA, Shahbaz M, Kusiak A (2006) Data mining in
manufacturing: a review. J Manuf Sci Eng 128(4):969–976
38. He QP, Qin SJ, Wang J (2005) A new fault diagnosis method
using fault directions in fisher discriminant analysis. AIChE J
51(2):555–571
39. Huang NE, Shen Z, Long SR, Wu MC, Shih HH, Zheng Q, Yen
NC, Tung CC, Liu HH (1998) The empirical mode decomposition
and the hilbert spectrum for nonlinear and non-stationary time
series analysis. Proc R Soc A: Math Phys Eng Sci 454(1971):903–
995
40. Huang SH, Pan YC (2015) Automated visual inspection in the
semiconductor industry: a survey. Comput Ind 66:1–10
41. Irani KB, Cheng J, Fayyad UM, Qian Z (1993) Applying machine
learning to semiconductor manufacturing. IEEE Expert 8(1):41–
47
42. J¨ager M, Knoll C, Hamprecht FA (2008) Weakly supervised
learning of a classifier for unusual event detection. IEEE Trans
Image Process: Publ IEEE Signal Process Soc 17(9):1700–1708
43. Jian C, Gao J, Ao Y (2017) Automatic surface defect detection
for mobile phone screen glass based on machine vision. Appl Soft
Comput 52:348–358
44. Kamsu-Foguem B, Rigal F, Mauget F (2013) Mining association
rules for the quality improvement of the production process.
Expert Syst Appl 40(4):1034–1045
45. Kang P, Lee H. j, Cho S, Kim D, Park J, Park CK, Doh S (2009)
A virtual metrology system for semiconductor manufacturing.
Expert Syst Appl 36(10):12,554–12,561
46. Kant G, Sangwan KS (2015) Predictive modelling and optimiza-
tion of machining parameters to minimize surface roughness using
artificial neural network coupled with genetic algorithm. Procedia
CIRP 31:453–458
47. Karimi MH, Asemani D (2014) Surface defect detection in tiling
industries using digital image processing methods: analysis and
evaluation. ISA Trans 53(3):834–844
48. Kashyap S, Datta D (2015) Process parameter optimization of
plastic injection molding: a review. Int J Plast Technol 19(1):1–18
49. Khakifirooz M, Chien CF, Chen YJ (2018) Bayesian inference
for mining semiconductor manufacturing big data for yield
enhancement and smart production to empower industry 4.0. Appl
Soft Comput 68:990–999
50. Khan AA, Moyne JR, Tilbury DM (2008) Virtual metrology
and feedback control for semiconductor manufacturing pro-
cesses using recursive partial least squares. J Process Control
18(10):961–974
51. Kitayama S, Natsume S (2014) Multi-objective optimization of
volume shrinkage and clamping force for plastic injection molding
via sequential approximate optimization. Simul Modell Pract
Theory 48:35–44
52. Kitayama S, Onuki R, Yamazaki K (2014) Warpage reduction
with variable pressure profile in plastic injection molding via
sequential approximate optimization. Int J Adv Manuf Technol
72(5):827–838
53. K¨oksal G, Batmaz ˙I, Testik MC (2011) A review of data mining
applications for quality improvement in manufacturing industry.
Expert Syst Appl 38(10):13,448–13,467
54. Konrad B, Lieber D, Deuse J (2013) Striving for zero defect
production: Intelligent manufacturing control through data mining
in continuous rolling mill processes. In: Windt K (ed) Robust
manufacturing control, lecture notes in production engineering.
Springer, Berlin, pp 215–229
55. Krishnan SA, Samuel GL (2013) Multi-objective optimization of
material removal rate and surface roughness in wire electrical
discharge turning. Int J Adv Manuf Technol 67(9-12):2021–2032
56. Kumar N, Mastrangelo C, Montgomery D (2011) Hierarchical
modeling using generalized linear models. Qual Reliab Eng Int
27(6):835–842
57. Lei Y, He Z, Zi Y (2008) A new approach to intelligent fault diag-
nosis of rotating machinery. Expert Syst Appl 35(4):1593–1600
58. Liang Z, Liao S, Wen Y, Liu X (2017) Component parameter
optimization of strengthen waterjet grinding slurry with the
orthogonal-experiment-design-based anfis. Int J Adv Manuf
Technol 90(1-4):831–855
59. Lieber D, Stolpe M, Konrad B, Deuse J, Morik K (2013)
Quality prediction in interlinked manufacturing processes based
on supervised & unsupervised machine learning. Procedia CIRP
7:193–198
60. Liggins II M, Hall D, Llinas J (2017) Handbook of multisensor
data fusion: theory and practice. CRC Press, Boca Raton
61. Luo W, Rojas J, Guan T, Harada K, Nagata K (2014) Cantilever
snap assemblies failure detection using svms and the rcbht.
In: 2014 IEEE International conference on mechatronics and
automation (ICMA), Piscataway, pp 384–389
62. Majumder A (2015) Comparative study of three evolutionary
algorithms coupled with neural network model for optimization of
electric discharge machining process parameters. Proc Inst Mech
Eng Part B: J Eng Manuf 229(9):1504–1516
63. Masci J, Meier U, Ciresan D, Schmidhuber J, Fricout G (2012)
Steel defect classification with max-pooling convolutional neural
networks. In: The 2012 international joint conference on neural
networks (IJCNN). IEEE, Piscataway, pp 1–6
64. Mayne DQ (2014) Model predictive control: Recent developments
and future promise. Automatica 50(12):2967–2986
65. Ming W, Hou J, Zhang Z, Huang H, Xu Z, Zhang G, Huang Y
(2015) Integrated ann-lwpa for cutting parameter optimization in
wedm. Int J Adv Manuf Technol 120(1):109
66. Mobley RK (2002) An introduction to predictive maintenance,
2nd edn. Butterworth-Heinemann, Amsterdam
67. Monostori L (1996) Machine learning approaches to manufactur-
ing. CIRP Ann Manuf Technol 45(Nr.2):675–712
68. Montgomery DC (2013) Design and analysis of experiments, 8th
edn. Wiley, Hoboken
69. Neugebauer R, Putz M, Hellfritzsch U (2007) Improved process
design and quality for gear manufacturing with flat and round
rolling. CIRP Ann-Manuf Technol 56(1):307–312
70. Niggemann O, Lohweg V (2015) On the diagnosis of cyber-
physical production systems - state-of-the-art and research agenda.
In: AAAI’15 Proceedings of the Twenty-Ninth AAAI Conference
on Artificial Intelligence. AAAI Press, pp 4119–4126
71. Norouzi A, Hamedi M, Adineh VR (2012) Strength modeling and
optimizing ultrasonic welded parts of abs-pmma using artificial
intelligence methods. Int J Adv Manuf Technol 61(1-4):135–
147
72. Oh S, Han J, Cho H (2001) Intelligent process control system for
quality improvement by data mining in the process industry. In:
Braha D (ed) Data mining for design and manufacturing, vol 3.
Springer, Boston, pp 289–309
73. Park JK, Kwon BK, Park JH, Kang DJ (2016) Machine learning-
based imaging system for surface defect inspection. Int J Precis
Eng Manuf-Green Technol 3(3):303–310
74. Paul A, Strano M (2016) The influence of process variables on the
gas forming and press hardening of steel tubes. J Mater Process
Technol 228:160–169
75. Peng A, Xiao X, Yue R (2014) Process parameter optimization for
fused deposition modeling using response surface methodology
Int J Adv Manuf Technol (2019) 104:1889–1902
1900

combined with fuzzy inference system. Int J Adv Manuf Technol
73(1-4):87–100
76. Perng DB, Chen SH (2011) Directional textures auto-inspection
using discrete cosine transform. Int J Prod Res 49(23):7171–
7187
77. Pfrommer J, Zimmerling C, Liu J, K¨arger L, Henning F, Beyerer
J (2018) Optimisation of manufacturing process parameters using
deep neural networks as surrogate models. Procedia CIRP 72:426–
431
78. Queipo NV, Haftka RT, Shyy W, Goel T, Vaidyanathan R, Kevin
Tucker P (2005) Surrogate-based analysis and optimization. Prog
Aerosp Sci 41(1):1–28
79. Rao RV, Pawar PJ (2009) Modelling and optimization of process
parameters of wire electrical discharge machining. Proc Inst Mech
Eng Part B: J Eng Manuf 223(11):1431–1440
80. Ren R, Hung T, Tan KC (2018) A generic deep-learning-based
approach for automated surface inspection. IEEE Trans Cybern
48(3):929–940
81. Rodger JA (2018) Advances in multisensor information fusion: a
markov–kalman viscosity fuzzy statistical predictor for analysis
of oxygen flow, diffusion, speed, temperature, and time metrics in
cpap. Expert Syst 35(4):e12,270
82. Rodriguez A, Bourne D, Mason M, Rossano GF, Wang J (2010)
Failure detection in assembly: Force signature analysis. In: 2010
IEEE Conference on automation science and engineering (CASE).
Piscataway, NJ
83. Rong Y, Zhang G, Chang Y, Huang Y (2016) Integrated
optimization model of laser brazing by extreme learning machine
and genetic algorithm. Int J Adv Manuf Technol 87(9):2943–2950
84. Rong-Ji W, Xin-hua L, Qing-ding W, Lingling W (2009)
Optimizing process parameters for selective laser sintering based
on neural network and genetic algorithm. Int J Adv Manuf Technol
42(11-12):1035–1042
85. Sagiroglu S, Sinanc D (2013) Big data: a review. In: 2013 Inter-
national conference on collaboration technologies and systems
(CTS). IEEE, pp 42–47
86. Saravanan N, Ramachandran KI (2010) Incipient gear box fault
diagnosis using discrete wavelet transform (dwt) for feature
extraction and classification using artificial neural network (ann).
Expert Syst Appl 37(6):4168–4181
87. Scattolini R (2009) Architectures for distributed and hierarchical
model predictive control – a review. J Process Control 19(5):723–
731
88. Scholz-Reiter B, Weimer D, Thamer H (2012) Automated surface
inspection of cold-formed micro-parts. CIRP Ann 61(1):531–534
89. Senn M, Link N (2012) A universal model for hidden state
observation in adaptive process controls. Int J Adv Intell Syst
4(3-4):245–255
90. Senn M, Link N, Gumbsch P (2013) Optimal process control
through feature-based state tracking along process chains.
In: Proceedings of the 2nd World Congress on Integrated
Computational Materials Engineering (ICME), pp 69–74
91. Shahrabi J, Adibi MA, Mahootchi M (2017) A reinforcement
learning approach to parameter estimation in dynamic job shop
scheduling. Comput Ind Eng 110:75–82
92. Sharp M, Ak R, Hedberg T (2018) A survey of the advancing use
and development of machine learning in smart manufacturing. J
Manuf Syst 48:170–179
93. Shewhart WA (1925) The application of statistics as an aid in
maintaining quality of a manufactured product. J Am Stat Assoc
20(152):546
94. Shi H, Gao Y, Wang X (2010) Optimization of injection molding
process parameters using integrated artificial neural network
model and expected improvement function method. Int J Adv
Manuf Technol 48(9):955–962
95. Shi H, Xie S, Wang X (2013) A warpage optimization method for
injection molding using artificial neural network with parametric
sampling evaluation strategy. Int J Adv Manuf Technol 65(1):343–
353
96. Shin HJ, Eom DH, Kim SS (2005) One-class support vector
machines—an application in machine fault detection and classifi-
cation. Comput Ind Eng 48(2):395–408
97. Silva JA, Abell´an-Nebot JV, Siller HR, Guedea-Elizalde F (2014)
Adaptive control optimisation system for minimising production
cost in hard milling operations. Int J Comput Integr Manuf
27(4):348–360
98. Sivanaga Malleswara Rao S, Venkata Rao K, Hemachandra Reddy
K, Parameswara Rao CVS (2017) Prediction and optimization of
process parameters in wire cut electric discharge machining for
high-speed steel (hss). Int J Comput Appl 39(3):140–147
99. Sorensen LC, Andersen RS, Schou C, Kraft D (2018) Automatic
parameter learning for easy instruction of industrial collaborative
robots. In: 2018 IEEE International conference on industrial
technology (ICIT), Piscataway, pp 87–92
100. Srinivasu DS, Babu NR (2008) An adaptive control strategy for
the abrasive waterjet cutting process with the integration of vision-
based monitoring and a neuro-genetic control strategy. Int J Adv
Manuf Technol 38(5-6):514–523
101. Stefatos G, Ben hamza A (2010) Dynamic independent
component analysis approach for fault detection and diagnosis.
Expert Syst Appl 37(12):8606–8617
102. Sterling D, Sterling T, Zhang Y, Chen H (2015) Welding
parameter optimization based on gaussian process regression
bayesian optimization algorithm. In: 2015 IEEE International
conference on automation science and engineering (CASE),
Piscataway, pp 1490–1496
103. Stoll A, Pierschel N, Wenzel K, Langer T (2019) Process control
in a press hardening production line with numerous process
variables and quality criteria. In: Machine learning for cyber
physical systems. Springer, pp 77–86
104. Sun A, Jin X, Chang Y (2017) Research on the process
optimization model of micro-clearance electrolysis-assisted laser
machining based on bp neural network and ant colony. Int J Adv
Manuf Technol 88(9-12):3485–3498
105. Tsai DM, Lai SC (2008) Defect detection in periodically
patterned surfaces using independent component analysis. Pattern
Recogn 41(9):2812–2832
106. Valavanis I, Kosmopoulos D (2010) Multiclass defect detection
and classification in weld radiographic images using geometric
and texture features. Expert Syst Appl 37(12):7606–7614
107. Vallejo AJ, Morales-Menendez R (2010) Cost-effective supervi-
sory control system in peripheral milling using hsm. Annu Rev
Control 34(1):155–162
108. Venkata Rao K, Murthy PBGSN (2018) Modeling and optimiza-
tion of tool vibration and surface roughness in boring of steel using
rsm, ann and svm. J Intell Manuf 29(7):1533–1543
109. Vijayaraghavan A, Dornfeld D (2010) Automated energy
monitoring of machine tools. CIRP Ann 59(1):21–24
110. Wang CH (2008) Recognition of semiconductor defect patterns
using spatial filtering and spectral clustering. Expert Syst Appl
34(3):1914–1923
111. Wang GG, Shan S (2007) Review of metamodeling techniques
in support of engineering design optimization. J Mech Des
129(4):370
112. Wang J, Ma Y, Zhang L, Gao RX, Wu D (2018) Deep learning
for smart manufacturing: Methods and applications. J Manuf Syst
48:144–156
113. Weimer D, Scholz-Reiter B, Shpitalni M (2016) Design of deep
convolutional neural network architectures for automated feature
extraction in industrial inspection. CIRP Ann 65(1):417–420
Int J Adv Manuf Technol (2019) 104:1889–1902
1901

114. Weiss SM, Baseman RJ, Tipu F, Collins CN, Davies WA,
Singh R, Hopkins JW (2010) Rule-based data mining for
yield improvement in semiconductor manufacturing. Appl Intell
33(3):318–329
115. Weiss SM, Dhurandhar A, Baseman RJ (2013) Improving
quality control by early prediction of manufacturing outcomes. In:
Proceedings of the 19th ACM SIGKDD international conference
on Knowledge discovery and data mining. ACM, pp 1258–1266
116. Weiss SM, Dhurandhar A, Baseman RJ, White BF, Logan
R, Winslow JK, Poindexter D (2016) Continuous prediction of
manufacturing performance throughout the production lifecycle. J
Intell Manuf 27(4):751–763
117. Wu Z, Huang NE (2009) Ensemble empirical mode decomposi-
tion: a noise-assisted data analysis method. Adv Adapt Data Anal
01(01):1–41
118. Wuest T, Weimer D, Irgens C, Thoben KD (2016) Machine learn-
ing in manufacturing: advantages, challenges, and applications.
Prod Manuf Res 4(1):23–45
119. Xu G, Yang Z (2015) Multiobjective optimization of process
parameters for plastic injection molding via soft computing and
grey correlation analysis. Int J Adv Manuf Technol 78(1-4):525–
536
120. Yin S, Ding SX, Xie X, Luo H (2014) A review on basic data-
driven approaches for industrial process monitoring. IEEE Trans
Ind Electron 61(11):6418–6428
121. Yun JP, Choi DC, Jeon YJ, Park C, Kim SW (2014) Defect
inspection system for steel wire rods produced by hot rolling
process. Int J Adv Manuf Technol 70(9-12):1625–1634
122. Yusup N, Zain AM, Hashim SZM (2012) Evolutionary tech-
niques in optimizing machining parameters: Review and recent
applications (2007–2011). Expert Syst Appl 39(10):9909–9927
123. Zain AM, Haron H, Sharif S (2008) An overview of ga technique
for surface roughness optimization in milling process. 2008 Int
Sympos Inf Technol 4:1–6
124. Zain AM, Haron H, Sharif S (2011) Optimization of process
parameters in the abrasive waterjet machining using integrated
sa–ga. Appl Soft Comput 11(8):5350–5359
125. Zain AM, Haron H, Sharif S (2012) Integrated ann–ga for
estimating the minimum value for machining performance. Int J
Prod Res 50(1):191–213
126. Zhang L, Jia Z, Wang F, Liu W (2010) A hybrid model using
supporting vector machine and multi-objective genetic algorithm
for processing parameters optimization in micro-edm. Int J Adv
Manuf Technol 51(5-8):575–586
127. Zhang W, Jia MP, Zhu L, Yan XA (2017) Comprehensive
overview on computational intelligence techniques for machinery
condition monitoring and fault diagnosis. Chin J Mech Eng
30(4):782–795
128. Zhao T, Shi Y, Lin X, Duan J, Sun P, Zhang J (2014) Surface
roughness prediction and parameters optimization in grinding and
polishing process for ibr of aero-engine. Int J Adv Manuf Technol
74(5-8):653–663
Publisher’s note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional affiliations.
Int J Adv Manuf Technol (2019) 104:1889–1902
1902