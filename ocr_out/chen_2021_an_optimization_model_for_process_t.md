IEEE SENSORS JOURNAL, VOL. 21, NO. 22, NOVEMBER 15, 2021
25123
An Optimization Model for Process Traceability
in Case-Based Reasoning Based on Ontology
and the Genetic Algorithm
Yineng Chen
, Xinghui Zhu
, Kui Fang
, Yanbin Wu, Yuechao Deng
, Xiao He
,
Zhuoyang Zou
, and Ting Guo
Abstract—A traceability system can quickly and accurately
query product supply chain circulation information. It is dif-
ﬁcult to obtain processing information and achieve sharing
due to the big data, long duration, large amount of equip-
ment and scattered and easily lost processing information.
In tracing the application of the case-based reasoning (CBR)
to product processing, we can solve the problem of establish-
ing an accurate and complete mathematical model between
the processing information and product quality defects by
ﬁnding a target record in a large amount of historical data.
The traceability model of ontology and CBR uses the web
ontology language (OWL) for case representation to simplify
the CBR framework for big data, classiﬁes process data and
standardizesinformation storage. A joint optimization algorithm based on the genetic algorithm (GA) and CBR is proposed
to establish an optimization model of process traceability, which is applied to case retrieval and reuse. This algorithm
optimizes the genetic operator by combining the optimal preservation strategy and roulette selection method and uses
an exponential-scale transformation method to stretch the ﬁtness function. The experiments show that the optimized
traceability model can infer information from garbled codes, wrong codes and missing messages to quickly determine
the problematic products, thus effectively improving the traceability accuracy of product processing.
Index Terms— Ontology, GA, traceability optimization, CBR, processing information.
I. INTRODUCTION
T
HERE WAS a global outbreak of COVID-19 (coronavirus
disease 2019) in 2020. The virus has been detected in
cold chain fresh products, but it is unknown at which produc-
tion link the virus was introduced. Moreover, it is impossible
to accurately ﬁnd staff and consumers who have been exposed
Manuscript received January 16, 2021; revised February 15, 2021 and
March 5, 2021; accepted March 6, 2021. Date of publication March 12,
2021; date of current version November 12, 2021. This work was sup-
ported in part by the Natural Science Foundation of Hunan, China under
Grant 2019JJ40133 and Grant 2019JJ50239, in part by the Natural Sci-
ence Foundation of Guangxi, China under Grant 2017GXNSFBA198174,
and in part by the Scientiﬁc Research Fund of the Hunan Provincial Edu-
cation Department of China under Grant 20A249. The associate editor
coordinating the review of this article and approving it for publication was
Dr. Sumarga K. Sah Tyagi. (Corresponding authors: Xinghui Zhu;
Kui Fang.)
Yineng Chen, Xinghui Zhu, Kui Fang, Yuechao Deng, Xiao He,
and Zhuoyang Zou are with the College of Information and Intelli-
gence, Hunan Agricultural University, Changsha 410128, China (e-mail:
zhuxh@hunau.edu.cn; fk@hunau.edu.cn).
Yanbin Wu is with the College of Information and Intelligence, Hunan
Agricultural University, Changsha 410128, China, and also with the Net-
work Security and Information Technology Center, Changsha Commerce
and Tourism College, Changsha 410116, China.
Ting Guo is with the College of Food and Bioengineering, Hezhou
University, Hezhou 432829, China.
Digital Object Identiﬁer 10.1109/JSEN.2021.3065757
to virus-infected products, and it takes time and effort to
investigate contacts on a large scale. However, a traceability
system can accurately ﬁnd contacts and determine the links
of product infection, which plays an important role in virus
protection and product safety. CAC (Codex Alimentarius Com-
mission) and ISO (International Standardization Organization)
have deﬁned traceability, which is the ability to trace the
history of behaviors and the use or location of goods through a
registered identiﬁcation code [1]. The traceability system can
quickly and accurately query all information in the supply
chain. When product safety and quality problems occur, the
problematic products and their causes can be quickly found
through the traceable source code on the product label. This
code is speciﬁc to an origin, warehouse, distribution route,
inspection and employee. As people pay increasing attention
to food quality and safety issues, the traceability system has
not only become a part of product trade and development but
is also inseparable from people’s daily lives and the economic
development of countries. A large number of studies have
shown that the use of traceability systems in processing and
sales can achieve improved results.
In December 2019, Jiangnan University and China Food
Safety News jointly released the “China Food Safety Devel-
opment Report 2019” report in Beijing. The report noted
1558-1748 © 2021 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Universidad Nacional de Colombia (UNAL). Downloaded on August 03,2026 at 01:48:18 UTC from IEEE Xplore.  Restrictions apply.

25124
IEEE SENSORS JOURNAL, VOL. 21, NO. 22, NOVEMBER 15, 2021
that the food safety incidents that occurred in 2018 were
mainly in production and processing, accounting for 45.16%
of the total [2]. It is very important for product quality
and safety to trace the source accurately in production and
processing. Pizzuti et al. [3] described an ontology developed
for supporting the management of meat traceability along
a whole supply chain. MESCO is able to represent all the
knowledge and information related to the meat traceability
domain in a single ontology, enabling interoperability among
different systems. This method would be better if it could make
automatic decisions. Wang et al. [4] improved the traceability
of wheat ﬂour tracking information and the efﬁciency of
hazard queries and reduced the scope of defective product
recall. However, this method is not suitable for traceable
data with high complexity and similarity. Chen [5] proposed
a traceability method based on intuition and fuzzy case-
based reasoning and adopted a sorting method to predict the
performance similarity of products. This method can distin-
guish traceable information with high similarity but cannot
quickly classify traceable products. Zhang et al. [6] proposed
a case-based reasoning method for the traceability of exhaust
gas pollution and constructed a general ontology model to
represent exhaust gas traceability cases, but the attributes of
the cases need to be optimized. Gautam et al. [7] implemented
a plant pollinator optimization algorithm to reduce the cost
of logistics, implementation and liability for fruit traceability.
This method can ﬁnd the grower or pack house that pays the
cost of examination, but it cannot determine which grower or
pack house performs the examination. Bin et al. [8] proposed
a solution to the optimization problem of batch mixing for the
traceability of fresh-cut vegetable processing, which optimized
the order and ﬁnished product processing sequence and raw
material selection sequence. However, this method does not
take the traceability information of the processing environ-
ment into account, such as processing equipment. Chen [9]
used case-based reasoning to optimize the production process,
which has strong practicability, but the case representation
method of industrial production process attributes needs to
be further studied. Khan et al. [10] proposed a model to
optimize the data of the food supply chain based on a recurrent
neural network. A genetic algorithm was used to optimize
the parameters of the model, which had a very good effect.
With the development of traceability systems, production and
processing traceability has four research phases: origin trace-
ability, quality traceability, resource optimization traceability
and precise traceability, as shown in Figure 1. In general, refer-
ences 3-6 are methods that study origin traceability and quality
traceability, references 7 and 8 are methods that study resource
optimization in processing, and references 9 and 10 are
methods that optimize processing. However, studies on precise
traceability optimization for processing are rarely reported.
To improve the traceability accuracy of the product supply
chain, a processing traceability model is constructed by CBR
for complex product processing links. A joint optimization
method based on ontology, the genetic algorithm and case
reasoning is proposed to optimize the model. This method is
based on ontology for case representation, while the improved
genetic algorithm is applied to case retrieval and case reuse.
Fig. 1. Research progress in production and processing traceability.
It effectively improves the traceability accuracy of product
processing and ensures the integrity of traceability data.
II. CASE REASONING FOR PRODUCT PROCESSING
TRACEABILITY
The traceability information of the product processing link
includes information on the raw materials, order, equipment,
ﬁnished products and other relevant information. It is not only
difﬁcult to record and collect data but also error-prone in
data acquisition, which may cause confusion in product supply
chain data and even affect the accuracy of the system traceabil-
ity information [11]. In addition, the traceability information
will change with product processing [12]. Therefore, to trace
the processing history of a product, it is necessary to trace
all the equipment and its environment in the whole process to
trace the complete information of the supply chain.
According to the time, batch, name, number and sequence
of warehousing, a new batch (material batch, MaB) will be
generated for the raw materials purchased from the processing
plant. After receiving the raw materials, the processed prod-
ucts are formed through key processing steps. However, the
processing steps are complex and uncontrollable. To solve this
problem, the processing information is based on processing
equipment in this paper. RFID technology is used to associate
the MaB with a processing batch (PiB). The generated RFID
tag is printed on the packaging bag or other transfer device
for identiﬁcation, including the equipment number, equipment
name, date, time, temperature, and pressure. After processing,
the ﬁnished product batch (PoB) is formed, which is com-
posed of the packing date, product name, product quality and
sequence. The map of the product processing information is
shown in Figure 2.
The MaB, PeiI (processing equipment information) and PoB
are recorded in sequence and closely related to each other. The
processing information to be queried can be inferred from
the relevant historical data. CBR [13] is used to solve new
problems by looking for speciﬁc knowledge in the experience
or results of similar historical cases. It has the advantages of
being a simple, fast and efﬁcient problem solving method.
This method can transform knowledge, experience and mod-
els that are difﬁcult to regularize in historical records into
intuitive understandings [14]. Product processing traceability
Authorized licensed use limited to: Universidad Nacional de Colombia (UNAL). Downloaded on August 03,2026 at 01:48:18 UTC from IEEE Xplore.  Restrictions apply.

CHEN et al.: OPTIMIZATION MODEL FOR PROCESS TRACEABILITY IN CBR BASED ON ONTOLOGY AND GA
25125
Fig. 2. Map of the product processing information.
Fig. 3. The process of CBR for product traceability.
determines the product processing information according to
the ﬁnished product batch number of the problematic product
and then ﬁnds the cause of the product quality defect. It is
difﬁcult to establish an accurate and complete mathematical
model between the processing information and product qual-
ity when there are a large number of historical processing
information defect records. Therefore, it is very desirable to
apply CBR to traceability in product processing. The process
of CBR for product traceability is shown in Figure 3.
However, due to the large amount of data, strong time
continuity and large amount of production equipment, the
processing information acquisition and sharing efﬁciency are
low, which brings great difﬁculty for product traceability [15].
On the other hand, raw material information, warehouse
information, and processing information will not be man-
aged in a uniﬁed manner. Recording and storage are carried
out separately, causing product processing information to be
scattered or lost, and product processing traceability cannot
be performed normally. Therefore, establishing processing
information records and storage standards to provide a basis
for management will be conducive to improving the efﬁciency
of information acquisition and sharing to improve the product
traceability accuracy from the data source. To standardize
and classify processing information recording and storage,
ontology will be applied to case representation and retrieval,
which can simplify the big data CBR framework.
III. ONTOLOGY-BASED TRACEABILITY CASE
REPRESENTATION MODEL CONSTRUCTION
Ontology can not only be suitable for the deﬁnition and
representation of product processing traceability cases but can
also be integrated into the general knowledge of the process-
ing ﬁeld. Moreover, ontology has a more mature modeling
language, query language and development tools [16]. It is
convenient to retrieve and modify the product processing
traceability cases represented by ontology.
Case representation mainly adopts eigenvectors or struc-
tures, both of which have advantages and disadvantages [17].
The advantage of an eigenvector representation is that it is
simple and effective, and the disadvantage is that the utilization
rate of processing data is not high enough to improve the
retrieval efﬁciency of cases [18]. The advantage of a structured
representation is that it makes full use of the knowledge of
the target case domain [19], such as traceability classiﬁcation
knowledge. Since a structured representation uses a seman-
tic network or framework to deﬁne the case structure and
knowledge, the two knowledge representations are nonformal
representation methods, which bring many difﬁculties for the
storage, modiﬁcation and retrieval of cases. It is not only
difﬁcult to share case knowledge and domain knowledge but
also complicated to manage and maintain the case base.
As a formal conceptual model, ontology can deﬁne both
the eigenvector and the structured representation method of
the case. In the ontology of knowledge representation logic
based on description logic (DL), DL is a decidable logi-
cal representation language that formalizes the description
of deterministic, shared knowledge within a domain [20].
According to the characteristics of product processing trace-
ability, ontology-based case representation can be deﬁned by
the following triple:
Case =< D, C, S >
where D is the deﬁnition set, C is the case set, and S is the
solution set.
A. Case Structure Deﬁnition
For the case of eigenvector representation, the OWL-DL
abstract syntax is adopted, where na represents a custom
namespace preﬁx, i ∈[1,n], and n is the dimension of the
eigenvector. In the structured case, an interfeature relationship
that is used to represent the inclusion relationship is added
based on the eigenvector approach. The case structure deﬁni-
tion steps for processing information traceability are shown in
Figure 4.
According to the deﬁnition steps of the case structure, the
feature vector of the case of processing information traceabil-
ity can be simpliﬁed as <MaB, MaN, PD, Ql, Qt, ENu, ENa,
PT, PoE>, where MaN refers to the material name, PD refers
to the processing date, Ql refers to the quality, Qt refers to the
quantity, ENu refers to the equipment number, ENa refers to
Authorized licensed use limited to: Universidad Nacional de Colombia (UNAL). Downloaded on August 03,2026 at 01:48:18 UTC from IEEE Xplore.  Restrictions apply.

25126
IEEE SENSORS JOURNAL, VOL. 21, NO. 22, NOVEMBER 15, 2021
Fig. 4.
The case structure deﬁnition steps for processing information
traceability.
the name of the equipment, PT refers to the processing time,
and PoE refers to the processing environment. It should be
noted that the processing time refers to the time spent in the
corresponding process of the equipment processing products,
and the processing condition refers to the temperature, pressure
and other factors in the processing process. Therefore, PD,
Qt and PT are numerical properties, while MaN, Ql, ENa
and PoEare are object properties. According to the DL case
representation method, it can be expressed as:
Clacc(na: Processing traceability partial owl:Thing);
Clacc(na: MaN partial owl:Thing);
Clacc(na: Ql partial owl:Thing);
Clacc(na: ENa partial owl:Thing);
Clacc(na: PoE partial owl:Thing);
Datatype Property (na: MaB domain (ex: Processing trace-
ability));
Datatype Property (na: PD domain (ex: Processing trace-
ability));
Datatype Property (na: Qt domain (ex: Processing traceabil-
ity));
Datatype Property (na: ENu domain (ex: Processing trace-
ability));
Datatype Property (na: PT domain (ex: Processing trace-
ability));
Object Property (na: has Materialname domain (na: Process-
ing traceability) range (na: MaN));
Fig. 5. The case structure deﬁnition for processing traceability.
Object Property (na: has Quality domain (na: Processing
traceability) range (na: Ql));
Object Property (na: has Devicename domain (na: Process-
ing traceability) range (na: ENa));
Object Property (na: has processing environment domain
(na: Processing traceability) range (na: PoE));
The deﬁnition domain of the Datatype Property and Object
Property is the processing traceability, and the value domain
of the Object Property is the corresponding concept class.
For example, the value domain of ’has Materialname’ is
’raw material product name’. Figure 5 is the case structure
deﬁnition for processing traceability.
B. Representation of a Case Instance
After deﬁning the case representation and structure, the
value of the case instance is assigned to the corresponding
feature item. If it is an object-type attribute, this attribute
can only be added between two individuals in DL. Therefore,
an eigenvalue is an instance of a class, which is assigned
by attaching an attribute between the case instance and the
eigenvalue instance.
IV. CASE RETRIEVAL OPTIMIZATION MODEL
CONSTRUCTION BASED ON A GENETIC ALGORITHM
During product processing, many different products may be
produced by the MaB. However, when the processing ﬂow and
the raw material ratio are consistent, the same equipment is
used to process these different products, and their processing
environments are also similar. Therefore, there are too many
data points for product processing, and they are very similar.
In this case, it is difﬁcult to retrieve the historical case that
matches the target case with the traditional case retrieval
or ontology similarity calculation method. To improve the
accuracy of case retrieval, this paper uses the genetic algorithm
to optimize the case retrieval model. The genetic algorithm
is a kind of intelligent search algorithm that has all the
characteristics of intelligent search [21]. In addition, it is a
global random search algorithm [22]. In contrast, using the
Authorized licensed use limited to: Universidad Nacional de Colombia (UNAL). Downloaded on August 03,2026 at 01:48:18 UTC from IEEE Xplore.  Restrictions apply.

CHEN et al.: OPTIMIZATION MODEL FOR PROCESS TRACEABILITY IN CBR BASED ON ONTOLOGY AND GA
25127
TABLE I
BINARY BITS OF THE CASE ATTRIBUTE ENCODING
genetic algorithm to retrieve historical cases can effectively
improve the reasoning speed.
The genetic algorithm replaces the parameter space of the
problem with the coding space, takes the ﬁtness function as
the evaluation, and takes the coding group as the evolution
basis [23]. An iterative process is established to carry out
the selection and genetic mechanism of individual bit strings
in the population. New excellent individuals are searched
randomly in the solution space through chromosome crossing
and mutation of the individuals in the population until an
optimal or suboptimal solution that satisﬁes the condition of
convergence is found [24]. The principle and execution of the
genetic algorithm are shown in Figure 7.
A. Coding Scheme Design
The optimization solution of the genetic algorithm can
only be obtained by encoding the parameters that need to be
optimized; that is, the weights of the case attributes and cases
need to be coded. Due to the high complexity and similarity
of product processing traceability cases, the binary coding
method is adopted in this paper, which can quickly distinguish
each case by simplifying genetic operations such as crossover
and mutation.
The population in the genetic algorithm is composed of
individuals, each of whom represents a solution to a problem,
that is, a historical case. The more historical cases there are in
the population, the stronger the search ability of the algorithm,
and the more likely it is to obtain the optimal solution, but
the calculation time will be longer. The more binary digits
there are, the wider the range of attribute weights that can be
expressed, but the computational complexity of the algorithm
will increase. Therefore, this article adopts the case weight
attribute strategy, in which the attribute of each individual
includes the attribute of the case. The number of bits in the
binary code is designed separately according to the range of
each property, for a total of 76 bits. The setting of the number
of bits is shown in Table I.
In the table, the date (20201231) occupies too many binary
digits, so it can be reduced by dividing it into the year (20),
month (12) and day (31). The processing time is the speciﬁc
time based on the processing date, and the range is 00:00-
23:59. To obtain the genes of the genetic algorithm, the value
of the case attribute is converted into the corresponding binary
value. Examples of populations are shown in Table II.
B. Selection of the Fitness Function
To evaluate the ﬁtness of each individual, it is necessary to
make an inference decision regarding the accuracy of the CBR
Fig. 6. Case example of processing traceability.
system determined by the individual based on the training
sample. The speciﬁc steps are as follows:
Step 1: For the current individual, randomly select K cases
from the original case library as the training set C. The
attribute weight of each case, that is, the problem description
in set C, is used as the input of case reasoning.
Step 2: Based on the case reasoning system for the current
individual, perform reasoning operations on set C to obtain
the solution of the training case.
Step 3: Compare the solution obtained by the inference
with the real solution of the training case, and obtain the
decision accuracy of the individual for the k training cases.
The maximum value of the sum of the decision accuracy is
selected as the ﬁtness function.
To improve the computational efﬁciency and precision of
the genetic algorithm, real number coding is adopted for
each attribute. Express each group of encoded weights as an
individual case in the population, which can be expressed as
Ci = (ci1, ci2, ci3, ci4, ci5, ci6, ci7, ci8)
Through CBR reasoning, the decision accuracy of the
genetic algorithm for processing traceability cases is shown
in Table III.
In the table, cij represents the weight of individual ci
for attribute j. The higher its value, the more important the
attribute is. D is the decision accuracy of the current individual
in the training case, which can be expressed as
D=

1, if cij = Cij
0,
Authorized licensed use limited to: Universidad Nacional de Colombia (UNAL). Downloaded on August 03,2026 at 01:48:18 UTC from IEEE Xplore.  Restrictions apply.

25128
IEEE SENSORS JOURNAL, VOL. 21, NO. 22, NOVEMBER 15, 2021
TABLE II
EXAMPLE OF A PRODUCT PROCESSING TRACEABILITY POPULATION
TABLE III
CALCULATION OF THE DECISION ACCURACY OF THE GENETIC ALGORITHM
f(C) is the total decision-making accuracy of the current
individual on training set C, which is selected as the ﬁtness
function for judging the individual, which can be expressed as
f (C)=
k

i=1
Di
The larger the F value is, the higher the decision-making
accuracy of the case-based reasoning system determined by
the current individual, and the more likely the individual is to
be inherited by the next generation. Take the maximum value
of ﬁtness as the objective function of the genetic algorithm.
C. Genetic Algorithm Generates a New Population
The selection operation in the genetic algorithm selects
good individuals from the parent population and inherits them
in the next-generation population. The selection operation is
used to determine the recombination or crossover as well
as how many offspring will be produced by the selected
individuals [25]. The selection operation is not only used to
determine the individuals in the recombination or crossover
but also calculates how many offspring individuals to pro-
duce. Although genetic algorithms can produce an increasing
number of excellent individuals, they are likely to destroy the
most adaptive individuals in the current population due to the
randomness of the genetic operators. Of course, the efﬁciency
and convergence of the genetic algorithm are affected. This
paper adopts the best retention selection method to retain the
most adaptable individuals in the next-generation group [26].
In this method, the individual with the highest ﬁtness does not
participate in the operations of crossover and mutation, but
instead it is used to replace the lowest-ﬁtness individual after
crossover and mutation in the current generation population.
Combining the optimal preservation strategy with the conven-
tional roulette selection method will make the optimization
process of the genetic algorithm efﬁcient and accurate. The
realization process is shown in Figure 8.
For an individual Ci (i = 1,2,3, . . ., N), the individual’s
selection probability pi is
pi =
f (Ci)
N
a=1
f (Ca)
where
N
a=1
f (Ca) is the sum of probabilities in the population.
To avoid precocity and low diversity in the multigeneration
evolution algorithm, the ﬁtness function is stretched by the
exponential scale transformation method. In the initial stage
of evolution, it narrows the difference in ﬁtness between
individuals to maintain diversity in the population. In the later
stage of evolution, it enlarges the difference in ﬁtness to make
the performance of the good individuals more prominent. The
selection probability Pi of individual Ci is improved to
p′
i =
e
0.5gf (Ci )
G
N
a=1
e
0.5gf (Ca )
G
Authorized licensed use limited to: Universidad Nacional de Colombia (UNAL). Downloaded on August 03,2026 at 01:48:18 UTC from IEEE Xplore.  Restrictions apply.

CHEN et al.: OPTIMIZATION MODEL FOR PROCESS TRACEABILITY IN CBR BASED ON ONTOLOGY AND GA
25129
Fig. 7. The principle and execution of the genetic algorithm.
where g is the current evolutionary generation and G
is the total number of evolutionary generations of the
population.
To select a good individual and ensure that it is outstanding
in each generation of evolution, we not only consider its
contemporary selection probability but also consider the evo-
lutionary historical selection probability. The worst individual
Min( ¯pi (h + 1)) is replaced in the next generation with the best
contemporary Max( ¯pi (h)). The historical selection probability
Pi(h) of an individual Ci is deﬁned as
¯pi (h) =
g
h=1
pih
g
h=1
h
where pih is the selection probability of Ci in generation h.
V. EXPERIMENTAL RESULTS AND DISCUSSION
A. Experimental Design
We collected 1000 sets of processing data from a beverage
processing factory. Based on these data, the case structure set,
case set and solution set are established on Protégé. Then,
we used Jena to save the OWL ﬁle of the beverage ontology
to the MySQL database to establish a traceability case and
designed a genetic algorithm in Jena. Additionally, the genetic
algorithm was designed in Jena to complete the reasoning
Fig. 8.
The process of optimizing the genetic algorithm based on the
optimal preservation strategy and the roulette selection method.
Fig. 9. Average accuracy of traceability of the 3 methods.
of the traceability case. Table IV shows an example of some
traceability cases of beverage processing.
To verify the performance of the method, the following
three groups of comparative experiments were used to trace
the beverage processing information:
1) The ontology model was used to represent the case, and
the K-nearest neighbors (KNN) algorithm was used to
perform case retrieval, which was called OCBR.
2) A genetic algorithm was used to optimize the weight of
the CBR attributes and to reduce the case base, which
was called GA-CBR.
Authorized licensed use limited to: Universidad Nacional de Colombia (UNAL). Downloaded on August 03,2026 at 01:48:18 UTC from IEEE Xplore.  Restrictions apply.

25130
IEEE SENSORS JOURNAL, VOL. 21, NO. 22, NOVEMBER 15, 2021
TABLE IV
SOME EXAMPLES OF TRACEABILITY CASES IN BEVERAGE PROCESSING
3) The ontological model was used to represent the case.
Additionally, the optimal historical selection improved
genetic algorithm was used to optimize the weight of
the CBR attributes and to reduce the case base, which
was called HGA-OCBR.
The experimental parameter settings were as follows: There
were 1000 cases in the traceability case library for beverage
processing, with 1 bit of binary code for each case. The
case had eight feature attributes, with a 10-bit binary code
representing one feature attribute weight. Thus, the individual
chromosome length was 1080 digits. For the current individ-
ual, 50 cases were selected from the case base species as the
training set. The ﬁve parameters of the genetic algorithm were
as follows: the initial population size N was 100, the maximum
iteration number G was 300, the crossover probability Pc was
0.7, the variation probability Pd was 0.05 and the K value
was 3.
B. Experimental Results
To verify the accuracy and traceability speed of the opti-
mization model, OCBR, GA-CBR and HGA-OCBR were
used to conduct comparative experiments on 200 sets of
selected data, and the average accuracy rate, accuracy error,
accuracy stability, average traceability time, and traceability
speed stability were recorded.
Figure 9 is a comparison chart of the average accuracy of
HGA-OCBR, OCBR and GA-CBR. The average accuracy of
HGA-OCBR is higher than OCBR and GA-CBR. OCBR has
the lowest average accuracy of traceability. As the number
of traceability experiments increases, the average accuracy of
HGA-OCB stabilizes at approximately 96%-98%.
Figure 10 shows the error rates of the three methods. The
error of HGA-OCBR is much lower than that of OCBR and
GA-CBR. OCBR and GA-CBR have similar errors, but the
error rate of GA-CBR is slightly lower than that of OCBR.
As the number of traceability experiments increases, the error
of HGA-OCBR decreases by approximately 2%-4%, which
also shows that the average accuracy of HGA-OCBR is the
highest.
Fig. 10. Error rate of the 3 methods.
Fig. 11. Accuracy stability of the 3 methods.
The stability of the accuracy is calculated by the slope.
The more extreme the peaks and valleys of the line are, the
more unstable, and the straighter the line is, the more stable
the accuracy. With the increase in the number of traceability
experiments, GA-CBR showed only a regular and steady rise
and fall, indicating high stability, while OCBR ﬂuctuates
greatly and often, indicating general stability. HGA-OCBR has
the stability of GA-CBR; there are ups and downs, but they
are not extreme.
Figure 12 compares the average traceability times of the
three methods. The average traceability time of HGA-OCBR
Authorized licensed use limited to: Universidad Nacional de Colombia (UNAL). Downloaded on August 03,2026 at 01:48:18 UTC from IEEE Xplore.  Restrictions apply.

CHEN et al.: OPTIMIZATION MODEL FOR PROCESS TRACEABILITY IN CBR BASED ON ONTOLOGY AND GA
25131
Fig. 12. Average traceability time of the 3 methods.
Fig. 13. Traceability speed stability of the 3 methods.
is approximately 0.08 s, which is shorter than the average
traceability times of OCBR and GA-CBR.
Figure 13 shows that the traceability speed of GA-CBR
ﬂuctuates greatly, indicating that the traceability speed is
unstable; OCBR has smaller ﬂuctuations than GA-CBR, but
it is also denser and more stable. The traceability speed of
HGA-OCBR has little ﬂuctuation and is relatively stable.
In comparison, HGA-OCBR combines the advantages of
OCBR and GA-CBR. The case representation through the
ontological classiﬁcation case structure effectively improves
the traceability speed and stability, and the GA algorithm is
used to improve the case retrieval to improve the traceability
accuracy and stability. HGA-OCBR has the best traceability
accuracy and traceability speed.
VI. CONCLUSION
By tracing the source code on a product label, the prod-
uct’s origin information, storage, distribution and transporta-
tion route, detection time and staff information data can be
quickly acquired, but processing link information traceability
is rarely involved. Aiming to address the problems of complex
product processing and procedures, the high difﬁculty of
collecting and recording information, and error-prone data
acquisition, a joint optimization algorithm based on GA and
CBR is proposed to establish a process traceability optimiza-
tion model. This method is meaningful for improving the
traceability accuracy of product processing and ensures the
integrity of traceability data, which is achieved in three main
ways.
1) Using an ontology for case representation and an
improved GA to optimize case retrieval and reuse, a case
reasoning traceability model is constructed to trace all
equipment and environmental information in the overall
processing in order to trace the complete historical
information of the product supply chain.
2) OWL-DL syntax is adopted to represent traceability
cases and to classify and process information, which
facilitates the storage, modiﬁcation and retrieval of cases
and the sharing of case knowledge and domain knowl-
edge, thus simplifying the management and maintenance
of the case database.
3) This paper not only optimizes the genetic operator by
combining the optimal preservation strategy and roulette
selection method but also uses the exponential scale
transformation method to stretch the ﬁtness function.
A joint optimization algorithm is proposed based on GA
and CBR, which is used in case retrieval and case reuse.
REFERENCES
[1] Y. Zhang, W. Wang, L. Yan, B. Glamuzina, and X. Zhang, “Development
and evaluation of an intelligent traceability system for waterless live ﬁsh
transportation,” Food Control, vol. 95, pp. 283–297, Jan. 2019.
[2] L. Wu and S. Yin, China Food Safety Development Report 2018. Beijing,
China: Peking Univ. Press, Dec. 2018.
[3] T. Pizzuti, G. Mirabelli, G. Grasso, and G. Paldino, “MESCO (MEat
supply chain Ontology): An ontology for supporting traceability in the
meat supply chain,” Food Control, vol. 72, pp. 123–133, Feb. 2017.
[4] S. Wang, C. Zhao, J. Qian, B. Wu, D. Chen, and Y. Song, “Bill of
lots combined with Petri tracing model improving traceability of wheat
ﬂour processing,” Trans. Chin. Soc. Agricult. Eng., vol. 34, no. 14,
pp. 263–271, 2018.
[5] R.-Y. Chen, “Intelligent predictive food traceability cyber physical
system in agriculture food supply chain,” in Proc. J. Phys., Conf.,
vol. 1026, May 2018, Art. no. 012017.
[6] C. Zhang, Y. Jia, X. Li, and C. Wang, “Research on the method of tracing
the source of waste gas pollution in industrial park based on case-based
reasoning,” J. Test Meas. Technol., vol. 32, no. 6, pp. 526–534, 2018.
[7] R. Gautam, A. Singh, K. Karthik, S. Pandey, F. Scrimgeour, and
M. K. Tiwari, “Traceability using RFID and its formulation for a
kiwifruit supply chain,” Comput. Ind. Eng., vol. 103, pp. 46–58,
Jan. 2017.
[8] X. Bin, X. Liu, J. Qian, J. Wang, and X. Wu, “Establishment of materials
batch mixing optimization model for traceability of fresh-cuts fruits and
vegetables processing,” Trans. Chin. Soc. Agricult. Eng., vol. 31, no. 10,
pp. 309–314, 2015.
[9] Z. Chen, “Research on industrial production process optimization
method based on case-based,” Ph.D. dissertation, Dept. Inf. Sci. Eng.,
Northeastern Univ., Shenyang, China, Jun. 2014.
[10] P. W. Khan, Y.-C. Byun, and N. Park, “IoT-blockchain enabled optimized
provenance system for food industry 4.0 using advanced deep learning,”
Sensors, vol. 20, no. 10, p. 2990, May 2020.
[11] K. Fang, Y. Chen, X. Zhu, and Y. Yang, “Research for improving rice
traceability precision based on organic RFID,” J. Investigative Med.,
vol. 63, no. 8, pp. 21–23, 2015.
[12] Z. Jiang, Y. Jiang, Y. Wang, H. Zhang, H. Cao, and G. Tian, “A hybrid
approach of rough set and case-based reasoning to remanufacturing
process planning,” J. Intell. Manuf., vol. 30, no. 1, pp. 19–32, Jan. 2019.
[13] S. Wan, D. Li, J. Gao, and J. Li, “A knowledge based machine tool
maintenance planning system using case-based reasoning techniques,”
Robot. Comput.-Integr. Manuf., vol. 58, pp. 80–96, Aug. 2019.
[14] C. Ke, Z. Jiang, H. Zhang, Y. Wang, and S. Zhu, “An intelligent design
for remanufacturing method based on vector space model and case-based
reasoning,” J. Cleaner Prod., vol. 277, Dec. 2020, Art. no. 123269.
[15] Y. Chen, K. Fang, X. Zhu, and T. Guo, “Research on improving method
of traceability accuracy based on organic RFID,” Jiangsu Agricult. Sci.,
vol. 6, pp. 426–429, Jun. 2016.
[16] M. M. Mabkhot, A. M. Al-Samhan, and L. Hidri, “An ontology-enabled
case-based reasoning decision support system for manufacturing process
selection,” Adv. Mater. Sci. Eng., vol. 2019, pp. 1–18, Aug. 2019.
Authorized licensed use limited to: Universidad Nacional de Colombia (UNAL). Downloaded on August 03,2026 at 01:48:18 UTC from IEEE Xplore.  Restrictions apply.

25132
IEEE SENSORS JOURNAL, VOL. 21, NO. 22, NOVEMBER 15, 2021
[17] S. Chen, J. Yi, H. Jiang, and X. Zhu, “Ontology and CBR based
automated decision-making method for the disassembly of mechanical
products,” Adv. Eng. Informat., vol. 30, no. 3, pp. 564–584, Aug. 2016.
[18] S. El Kadiri and D. Kiritsis, “Ontologies in the context of product
lifecycle management: State of the art literature review,” Int. J. Prod.
Res., vol. 53, no. 18, pp. 5657–5668, Sep. 2015.
[19] N. Bayar, S. Darmoul, S. Hajri-Gabouj, and H. Pierreval, “Using immune
designed ontologies to monitor disruptions in manufacturing systems,”
Comput. Ind., vol. 81, pp. 67–81, Sep. 2016.
[20] P. Chhim, R. B. Chinnam, and N. Sadawi, “Product design and manu-
facturing process based ontology for manufacturing knowledge reuse,”
J. Intell. Manuf., vol. 30, no. 2, pp. 905–916, Feb. 2019.
[21] M. B. Vivek, N. Manju, and M. B. Vijay, “Machine learning based food
recipe recommendation system,” in Proc. Int. Conf. Cognition Recognit.,
2018, pp. 11–19.
[22] S. Guo, G. Pan, L. Zhao, and Y. Guo, “Recommendation system based
on fuzzy ontology and genetic algorithm,” Comput. Eng. Des., vol. 3,
no. 40, pp. 834–838, 2019.
[23] L. D. C. Martins and G. P. Silva, “A genetic algorithm for the mass
transit crew rostering problem,” in Proc. IEEE 19th Int. Conf. Intell.
Transp. Syst. (ITSC), Nov. 2016, pp. 2424–2429.
[24] H. Ibrahim, R. O. Aburukba, and K. El-Fakih, “An integer linear pro-
gramming model and adaptive genetic algorithm approach to minimize
energy consumption of cloud computing data centers,” Comput. Elect.
Eng., vol. 67, pp. 551–565, Apr. 2018.
[25] R. Meena and K. K. Bharadwaj, “A genetic algorithm approach for
group recommender system based on partial rankings,” J. Intell. Syst.,
vol. 29, no. 1, pp. 653–663, Jun. 2018.
[26] C. Yang, Q. Qian, F. Wang, and M. Sun, “Application of improved
adaptive genetic algorithm in function optimization,” Appl. Res. Com-
put., vol. 35, no. 4, pp. 1042–1045, 2018.
Yineng Chen received the M.S. degree from the
College of Information and Intelligence, Hunan
Agricultural University, China, where he is cur-
rently pursuing the Ph.D. degree in agricultural
information engineering. He is a Lecturer in 2016.
He has published more than 11 articles in various
journals. His major research interests include the
Internet of Things and artiﬁcial intelligence.
Xinghui Zhu received the M.S. degree in com-
puter science and technology from the National
University of Defense Technology in 2004, and
the Ph.D. degree from Hunan Agricultural Uni-
versity, China, in 2018. He is a Professor with
Hunan Agricultural University. His research inter-
ests include agricultural information, the Internet
of Things, and distributed computing.
Kui Fang was born in 1963. He received the M.S.
degree in computational mathematics from Xi’an
Jiaotong University, China, in 1985, and the Ph.D.
degree in computer science and technology from
the National University of Defense Technology,
China, in 2000. He is a Professor of Computer
Science and Technology with Hunan Agricultural
University. His major research interests include
image processing and machine learning.
Yanbin Wu, photograph and biography not available at the time of
publication.
Yuechao Deng, photograph and biography not available at the time of
publication.
Xiao He, photograph and biography not available at the time of publica-
tion.
Zhuoyang Zou, photograph and biography not available at the time of
publication.
Ting Guo, photograph and biography not available at the time of
publication.
Authorized licensed use limited to: Universidad Nacional de Colombia (UNAL). Downloaded on August 03,2026 at 01:48:18 UTC from IEEE Xplore.  Restrictions apply.