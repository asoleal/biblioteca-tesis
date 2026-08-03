Integration of Internet-of-Things as sustainable smart farming technology
for the rearing of black soldier ﬂy to mitigate food waste
Josiah Cheng Foong Vana, Pei En Thama, Hooi Ren Lima, Kuan Shiong Khoob,
Jo-Shu Changc,d,e,*, Pau Loke Showa,*
a Department of Chemical and Environmental Engineering, Faculty of Science and Engineering, University of Nottingham Malaysia, Jalan Broga, Semenyih, Selan-
gor Darul Ehsan 43500, Malaysia
b Faculty of Applied Sciences, UCSI University Campus No. 1, Jalan Menara Gading, UCSI Heights, Cheras, Kuala Lumpur 56000, Malaysia
c Department of Chemical Engineering, National Cheng Kung University, Tainan 701, Taiwan
d Department of Chemical and Materials Engineering, Tunghai University, Taichung 407, Taiwan
e Research Center for Smart Sustainable Circular Economy, Tunghai University, Taichung 407, Taiwan
A R T I C L E
I N F O
Article History:
Received 25 November 2021
Revised 12 January 2022
Accepted 23 January 2022
Available online 10 February 2022
A B S T R A C T
Background: Throughout the world, food wastage issues continue to plague almost every country. Multiple
ideas and solutions have been conceived and are continuously being tested by scientists and government
bodies to mitigate food waste management issues. Black Soldier Fly (BSF) rearing is an up-and-coming com-
modity because of its versatility and multi-function purposes in various ﬁelds, such as food waste manage-
ment, animal feed industry and bioactive compounds industry.
Methods: This work looks at setting up an automated smart farming system to rear BSF, with the help of
implementing the Internet-of-Things (IoT) into the monitoring system. It also entails a guide on a possible
design of a home-based Black-Soldier-Fly smart farm, where the Internet-of-Things components such as sen-
sors, relays, and mobile applications are showcased. Finally, the prospects and challenges that arise with
Black-Soldier-Fly smart farming can be identiﬁed and discussed.
Signiﬁcant ﬁndings: Important growth factors such as temperature, light and pH can be monitored remotely
by Internet-of-Things technology. Through IoT implementation, the farm can be remotely controlled and
growth parameters can be adjusted with ease. Hence, this would lead to the efﬁcient production of BSF larvae
for processing food waste or conversion to bioactive compounds.
© 2022 Taiwan Institute of Chemical Engineers. Published by Elsevier B.V. All rights reserved.
Keywords:
Black soldier ﬂy
Internet-of-Things (IoT)
Food waste
Sensor
Smart farming
1. Introduction
By 2050, it is projected that 9 billion people will inhabit the planet
[1]. This means that the global food demand will rise, which requires
greater development in the agricultural ﬁeld. However recent studies
of current trends in food availability and demand show that the yield
produced will not be enough to meet the required global food
demand [2]. Also, a greater drive in agriculture would contribute to
climate change, different kinds of pollution and food waste issues.
Food waste is becoming a prevalent issue in the world due to its
implications in economic and environmental scenarios, as well as it is
related to climate change [3,4]. Hence, there is an urgency in search-
ing for suitable methods to tackle food waste issues that are environ-
mental-friendly and effective.
Conventional methods to mitigate food waste such as landﬁlls are
not ideal as they create execrable odors, leachate and landﬁll gases
which are sources for global warming, as well as the fact that eventu-
ally, landﬁlls around the world will reach maximum capacity [5,6]. It
has been found that an insect known as the black soldier ﬂy (BSF),
can reduce certain food waste types such as kitchen waste, fruits and
vegetables, and poultry feed [7]. They are also capable of valorizing
this food waste by converting them into insect biomass, which in
turn can be used as feed for livestock [8]. More recently, biofertilizers
have also been converted, leading to a more sustainable agricultural
approach [9]. These studies show that the black soldier ﬂy has great
potential to be a solution to global food waste issues.
Black soldier ﬂy (BSF), Hermetia illucens, is an insect of the order
Diptera and part of the Stratiomyidae family. The ﬂy has been known
to be native to the North American region but is now found through-
out the world [10]. However, there is an absence of its possible habi-
tation in the northwestern part of Europe due to its low cold
hardiness [11]. The BSF and its larvae are unique as compared to simi-
lar ﬂy species, they are not considered pests or vectors [12] as they do
* Corresponding authors.
E-mail addresses: changjs@mail.ncku.edu.tw (J.-S. Chang), Show@nottingham.edu.
my (P.L. Show).
https://doi.org/10.1016/j.jtice.2022.104235
1876-1070/© 2022 Taiwan Institute of Chemical Engineers. Published by Elsevier B.V. All rights reserved.
Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235
Contents lists available at ScienceDirect
Journal of the Taiwan Institute of Chemical Engineers
journal homepage: www.elsevier.com/locate/jtice

not possess mouthpieces or stingers which can cause harm to
humans [13]. Due to this, BSF has been widely utilized in many ﬁelds
such as aquaculture, waste management, and the animal feed indus-
try [14]. It is noted that the key interest of the BSF life cycle is the lar-
val stage, as the larvae carry many beneﬁts such as the roles played
in the aforementioned ﬁelds. The BSF larvae also have a high content
of protein, lipids and bioactive compounds, which have great poten-
tial to be extracted for human and animal well-being [15,16].
As the rearing of BSF larvae carries great prospects, many farmers
are turning to both small and large-scale production and breeding of
the larvae. The rearing process usually involves a lot of manual labor
and manpower, which can be seen as a tedious and troublesome pro-
cess. Site location, ﬁnancial constraints and farm design are factors
that also need to be taken into account when starting a BSF farm [17].
Large-scale designs typically use large concrete basins with one side
having a sloping ramp leading to a rain gutter to collect the larvae
[18]. BSF farms also require stringent optimum conditions to maxi-
mize the production of BSF larvae. As we are moving forward to an
era of digitalization, it is important to look at innovations and tech-
nology to solve the difﬁculties faced in manual processes [19].
The world of human beings and technological devices are con-
nected through the Internet, which allows the ease of communication
and transfer of information. Hence, the innovations and technology
mentioned above typically revolve around this relationship, which
leads to the concept of the Internet-of-Things (IoT). It is a relatively
new concept that is extremely relevant in today’s world. It has a great
potential in being implemented into the rearing of BSF larvae, which
has been traditionally a laboring industry. The conjunction of the
principles of IoT with traditional farming has led to the concept of
smart farming. When mentioning new technologies in the BSF ﬁeld,
it does not necessarily mean that all components would need to be
connected to the Internet. Recently, Jeff Tomberlin and his research
team have developed a BSF ‘bullet’ technology, which is a unit that
helps to maintain BSF larvae in a juvenile state for longer periods
before being used for any intended purpose [20]. Regardless, any
advancements in innovation and technology in the BSF ﬁeld would
tremendously be beneﬁcial to the industry.
In recent years, researchers from India have set up an electrically
controlled artiﬁcial system to manage organic waste through the
usage of BSF with IoT monitoring. The main purpose of this research
was to design a system with minimum human interaction which
allowed remote IoT monitoring from any part of the world [21].
Besides that, in Sarawak, Malaysia, researchers were successful in set-
ting up a BSF farm using IoT technology. This was done to show that
insect rearing with IoT monitoring was capable of being carried out
in rural areas, where conventionally manual farming was carried out
[22]. These examples (discussed in more detail in Section 3.4) show
the potential of IoT being used in BSF rearing.
The main objective of this review is to investigate necessary steps
needed to be taken to set up a BSF smart farm from the comforts of
one’s home and to be able to monitor the insects’ growth through IoT
means. This review primarily focuses on a small-scale approach as
compared to other reviews, which allows researchers to have a better
understanding of the growth criteria, before scaling to a larger indus-
trial scale. To understand the process of setting up a BSF smart farm,
there needs to be a clear understanding of the life cycle and growth
parameters to set up the idealized and optimized conditions for suc-
cessful growth. By setting up a BSF smart farm with IoT implementa-
tion at home, one can experience rearing insects on a small-scale,
thus this experience and knowledge can be transferred when plan-
ning to carry out a smart farm on large scale. Besides that, through
this review, researchers can set up BSF smart farms in research labo-
ratories to carry out observations or extraction to extract the vital
bioactive compounds contained within the insects, or experiment
with food waste management approaches. Through small-scale smart
farming, growth parameters can be adjusted to one’s requirements
and allow for ease of obtaining experimental subjects to carry out sci-
entiﬁc research.
2. The farming process in BSF
2.1. Rearing of BSF
BSF has a life cycle of about 45 days, which can be split into four
distinct stages: egg, larva, pupa, and adult stages [23]. Fig. 1 below
gives a visual representation of the BSF life cycle. BSF begin the life
cycle as eggs for about 4 days, then they hatch into larvae. The larvae
are omnivorous and voracious, hence they will consume food waste
Fig. 1. The life cycle of the black soldier ﬂy (Permission obtained from [28] that was modiﬁed from [29]).
2
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235

with great efﬁciency, causing them to grow rapidly and leave behind
a nutrient-rich fertilizer known as frass [24,25]. After 23 weeks, the
larvae begin turning to pupae and become more inactive and immo-
bile. They will also look for a dry space to undergo metamorphosis
into ﬂies (adults) [23]. Adult ﬂies have a lifespan of about a week
before they die [26], but the lifespan can vary depending on the con-
ditions. During the adult stage, the ﬂies do not have mouthpieces and
do not feed on perishables. However, a study in Japan has shown that
when sugar and water are placed near newly emerged adults, their
longevity increases by 3 times in males and 2 times in females, as
compared to providing water alone [27]. This goes against the con-
sensus that BSF adults need not feed on food to survive for a greater
lifespan. Hence, more detailed research needs to be carried out on
the need for the consumption of food for BSF to increase adult lon-
gevity.
2.2. Growth parameters
2.2.1. Temperature
BSF tend to be very sensitive to changes in their surroundings,
hence meticulous care needs to be given when rearing them. The
development of BSF larvae can be affected by many growth parame-
ters such as temperature, diet, humidity, and light intensity. These
factors need to be in optimum condition to ensure proper growth. It
is found that the ideal temperature for BSF larvae to successfully nur-
ture is in between the range of 2430 °C [18,26,30]. Temperatures
below and above the minimum and maximum threshold of 15 °C and
40 °C, respectively are shown to be unfavourable for the growth of
BSF in all its life stages, causing complete mortality in the species
[18,31]. Temperatures that are too cold can cause the BSF larvae to
have slowed metabolism, inactiveness hence unable to develop prop-
erly. On the other hand, temperatures that are too high cause the BSF
larvae to search for cooler places to rest instead of feeding [26]. BSF
has also been shown to be greatly affected by temperature differen-
ces. BSF larvae and adults averaged survivance of 7497% when
reared at 2730 °C, but attained a survivance of only 0.1% at 36 °C
[32]. It is also found that the ideal mating and fecundity temperature
is 28 °C [33]. Hence, the Hermetia illucens can be said to be a delicate
species, as it has very speciﬁc temperature requirements to ensure
optimum growth.
2.2.2. Diets
The dietary regime of the BSF also plays a big role in the develop-
ment of the insect. amongst its life stages, it mostly consumes food
during the larval stage. BSF larva can consume a large amount of food
and grow many times bigger than their original size [34]. It has been
noted and highlighted that nutritional components such as carbohy-
drates and proteins play an important role in the growth of insect lar-
vae [3537]. Agricultural students from a Dutch agricultural college
have found the optimum diet formulation for BSF larvae. The opti-
mum diet consists of 66.96% protein, 8.93% starch, and 24.11% rough-
age to help with the digestibility of the meal [38]. Experiments were
done and showed that the best protein source were ethanol by-prod-
ucts and corn steep, which resulted in the greatest weight gain [38].
For starch sources, mashed potatoes, wheat starch and potato pulp
were options that performed the best. Finally, corn gluten meal was a
good choice for roughage to give the diet structure. Hence, a food
waste consisting of components from each of the three criteria would
result in the optimum diet for BSF larvae. Moisture on the feed also
plays a big role in nurturing the BSF larvae. A feed containing a mois-
ture content of 40% causes the larvae to unsuccessfully develop, while
a feed of moisture content of 70% helped to develop the larvae the
fastest and increased their survival rate [39]. In terms of selecting the
protein source for BSF larvae consumption, it is found that a pork diet
is inferior to a beef diet and grain-based diet, as it increased the larval
development time by about 23% and 140% more degree hours
respectively [40]. BSF larvae fed on ﬁsh waste Sardinella aurita also
proved to have a high protein content of 78.8%, while food waste con-
sisting of fruits and vegetables only yielded a protein content of 12.9%
[41]. Besides that, from personal experiences in rearing BSF larvae,
feeding a diet containing a lot of vegetable and food scrap waste, will
cause a large amount of ammonia to be produced which can prove to
be toxic in high amounts and very uncomfortable for people in the
vicinity. A study also showed that BSF larvae focused on vegetable
composting increased the concentration of ammonia in frass by about
ﬁve to six-fold as compared to conventional means [42]. There is a
prospect of adding coffee grounds into the dietary needs of BSF lar-
vae, as coffee grounds are high in protein and caffeine. In other stud-
ies, some insects that were fed coffee grounds showed greater
metabolism
and
locomotor
activities
[18,43].
However,
more
research is needed to be carried out on the effects of caffeine on the
growth of Hermetia illucens.
2.2.3. Light
Light intensity is also a factor in the life cycle of the BSF, particu-
larly during the mating and fertilization process [33,44,45]. Both nat-
ural lighting (i.e. sunlight) and artiﬁcial lighting (quartz iodine lamp,
LED lamps) promoted mating [33], but LED lamps promoted BSF egg
fertilization, whereas sunlight encouraged improved hatchability and
fertility [27]. amongst all the artiﬁcial light sources available on the
market, BSF LED lamps (specially designed lamps based on BSF adult
visual spectral sensitivity) provided to be the most energy-efﬁcient
light source and also produced the highest mating success rate based
on inseminated females [46].
2.2.4. pH
On the other hand, the effects of pH on the development of BSF
larvae were tested and experimented with. On one occasion, it was
found that even though different pH environments ranging from val-
ues of 4.09.5 were tested, however, there were no signiﬁcant differ-
ences in ﬁnal mass between the tested samples of BSF larvae [47].
Another study showed that lower pH values of 2.0 and 4.0 produced
slightly smaller masses of BSF larvae (0.16 g) as compared to neutral
and higher pH values such as 7.0 (0.20 g) and 10.0 (0.20 g) [48].
Hence it can be said that pH plays a minor factor in BSF larvae devel-
opment as compared to other more important conditions such as diet
and temperature.
2.3. Small-Scale and large-scale BSF farms
For scientiﬁc research purposes, small-scale BSF farms are more
ideal as they are easier to manage and regulate. Hence this allows the
ease of experimentation and extraction of chemical compounds con-
tained in BSF larvae. Small-scale BSF farms are set up as controlled
environments, with the type and amount of food is known, as well as
the surrounding conditions are maintained. In small-scale BSF farms,
the diet can be controlled and food choice can be selected to increase
certain nutritional components to one’s needs. There is a debate on
whether ad libitum feeding or restricted feeding is better [49], but ad
libitum feeding allows the larvae to consume more food, causing the
nutritional content to increase. In a small-scale environment, living
space is also an important criterion to ensure BSF larvae can be nur-
tured successfully. Sufﬁcient spacing helps to improve life-history
traits (such as the number and size of BSF larvae) [50] and prevent
large larval aggregation [51] which may lead to constant alloco-
prophagy and autocoprophagy in the larvae. It is also found that the
supplementation of certain types of bacteria such as Arthrobacter
AK19 in BSF larvae diets helped to enhance the growth rate and
improve nutritional assimilation functions at a small-scale level [52].
These bacteria can be cultured personally on Luria nutrient agar [52]
or acquired from third-party producers. Therefore, it can be said
there is ﬂexibility in designing small-scale BSF farms with many
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235
3

improvements being able to be integrated into the farms. However, if
looking at from a prospective business perspective, a small-scale BSF
farm is less ideal as compared to a large-scale BSF farm. A small-scale
farm does not have the necessary equipment and facilities to produce
an output of magnitudes from large-scale farms. Large-scale farms
usually have established and guaranteed markets for products and
allows for easy business partnerships with other industries that
thrive on the BSF rearing industry such as the animal feed industry
[53]. Nonetheless, large-scale BSF farms have drawbacks, in which
there needs a large capital or investment before it can be set up. A
larger farm will also result in greater difﬁculty of quality control
(which diminishes the criteria for BSF larvae research) and more
environmental pollution/hygienic issues [53]. It has been noted that
success in small-scale farms does not necessarily translate to the
same outcome in large-scale farms. It has been found that some
growth parameters from small-scale BSF farms are not scalable and
cannot be replicated linearly on an industrial scale [54]. Large-scale
farms also in actuality do not have proper frameworks and blueprints
on how to set up a successful industrial-scale farm, so it is a particular
risk venture for prospectors in this ﬁeld [55]. In summary, the suit-
ability of a small-scale BSF farm or large-scale BSF farm falls on the
sole purpose and utilization of the insect. Research or extraction pur-
poses go hand in hand with small-scale settings, while rearing and
mass production are favourable for large-scale farms.
Small-scale BSF farms have been successfully set up in the past.
They were done mainly for the technical basis of small-scale rearing
of BSF to be used as animal feed such as ﬁsh feed [17,56]. A prototype
small-scale BSF farm was designed and constructed in June 2021 for
examination and extraction of vital biochemical compounds in BSF
larvae in a laboratory. IoT elements were implemented into the BSF
farm such as sensors and relays. The design of the small-scale BSF
farm was inspired by OFERA InsectsTM, an aquaponic company that
has attempted at constructing a compact system for rearing BSF. The
IoT integration to the design had references to Sabir et al.’s BSF design
system, to ensure the correct growth parameters were observed [21].
The IoT system was based on previous experiences with IoT integra-
tion of cultivating microalgae [57]. The small-scale farm was con-
structed as a stacked system, with three boxes being connected
vertically, along with another box at the base acting as a support. The
top box is a transparent plastic box, having the dimensions of
55 £ 36 £ 40 cm. The other boxes are blue plastic boxes, with a black
lid, and have measurements of 53 £ 34 £ 25 cm. The stacked system
has an approximate height of 1.20 m. The lower box would be the
rearing area of the larval stage, where they are fed at various times
throughout the day. The lower box and the middlebox are connected
with two pipes measuring 55 mm in diameter, placed inclined on the
opposite sides of the box (as shown in Fig. 2). This is to allow BSF lar-
vae that are nearing the end of their larval stage and evolving into
the pupal stage, to crawl upwards and seek a dry place to pupate.
During this period, the larvae tend to be more mobile hence can tra-
verse longer distances as compared to the start of their larval stage.
The pipes would lead them to a drop-off into plastic containers where
the BSF larvae are collected. As the main purpose of this farm is to
collect and examine the BSF larvae, a large portion of the larvae will
be collected, and the remaining few are allowed to pupate and con-
tinue the life cycle. This is to ensure that the life cycle is self-sustain-
able and allow for more generations of BSF larvae to be produced. On
the other hand, the egg collection procedure was stopped when the
adult BSFs have died [17]. There is a difference in methodology as the
purpose of their experiment was just setting up a technical basis,
whereas the goal of this experiment is to carry out experimentation
on the rearing of BSF larvae for food waste reduction. The remaining
pupae are allowed to undergo metamorphosis and evolve into ﬂies.
The middle box’s cover is punctured with holes to allow the ﬂies to
ﬂy to the top level. The top box is transparent to allow for easy moni-
toring and tracking of the adult stages of the BSF. At the top level, its
purpose is to attract BSF for fertilization and oviposition of the eggs.
Attractants such as sugar and water, as well as corrugated cardboard,
are placed at the top level to increase the probability of success of
breeding BSF eggs. Care must be taken to maintain good housekeep-
ing and cleanliness of the top level’s surroundings, as previous stud-
ies have shown that adult BSFs have great tendencies to lay their
eggs directly on substrates (food), especially within areas with a spilt
substrate [58]. The top box is adhered to the middle box’s cover,
while the middle box adheres to the lower box’s cover. Hence the
covers can easily be separated to observe the various levels of the
farm. In the lower level, a water pipe measuring 6 mm in diameter is
circled on the sides of the box, with mist nozzles installed along the
way of the pipe. It is controlled by IoT components which will be dis-
cussed in a further section.
In actuality, many abiotic factors within the BSF small-scale farm
can be monitored through the implementation of IoT. For example, a
key factor such as temperature can be monitored through means of
IoT. As mentioned above, BSF larvae are very sensitive to temperature
and might produce adverse effects if the temperature gets too cold or
too hot [31]. Hence temperature sensors can be installed in the larval
growth area to ensure a suitable temperature for BSF larvae develop-
ment is maintained. Besides that, some temperature sensors have
built-in humidity sensors, hence both the temperature and moisture
content can be monitored through a single sensor device. Light sen-
sors can also be installed to ensure light intensity is at an optimum
condition and not too dim or bright. Light sensors play a big role in
the fertilization and oviposition of eggs [45], hence they should be
installed in the breeding area of adult BSF. Water pumps can also be
integrated into the IoT system, to ensure the feed or environment is
sufﬁciently damped for the proper growth of BSF larvae.
3. Introduction to IoT, smart farming and their implementation
3.1. Introduction to IoT
Internet-of-Things (IoT) is a relatively modern concept but has
been proven to be still relevant and important in this digital age. The
origin of the concept of IoT has been widely disputed. Some believe
that the concept of IoT and its term was ﬁrst coined in September
1985 by Peter T. Lewis, a wireless technology developer during a
speech to the Congressional Black Caucus Foundation 15th Annual Leg-
islative Weekend in Washington, D.C. [59]. His-ﬁrst deﬁnition of the
Fig. 2. PVC pipes on opposites connect the lower box to the upper box. The pipes are
adhered to the sides using Liquid Nail.
4
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235

concept of IoT is that it is the integration of people, processes, and
technology with connectable devices and sensors to enable remote
monitoring, status, manipulation and evaluation of trends of such
devices. On the other hand, some people believed it was ﬁrst intro-
duced in 1999 by MIT’s Kevin Ashton during his promotion of radio
frequency identiﬁcation (RFID) technology [60]. Regardless of the ori-
gin, the early deﬁnitions proved to be accurate and comparable to
modern deﬁnitions available today. A version of the concept of IoT is
that it is a new technology paradigm envisioned as a global network of
machines and devices capable of interacting with each other [61]. In
short, IoT is the interaction of “things” (i.e., sensors, relays, and soft-
ware) with other technological systems through the Internet. As the
popularity of IoT implementation is increasing rapidly, it is forecasted
that the installed base value of 15.4 billion devices in 2015 will
increase to 75.4 billion in 2025 [62]. IoT has constantly been integrated
into our daily lives and many systems are utilizing its technology such
as home security systems, smart farming, and connected cars.
An IoT system can be said to be composed of ﬁve major compo-
nents: sensors, gateways, cloud ecosystem, data analysis, and user
interface (UI) [63]. The ﬁrst main component is the sensors/ “things”.
These smart devices are components present in what some people
call the sensing layer or sensing domain [64,65]. Their main function
is to collect data and information from the surroundings they are
placed in and transmit the information to the succeeding compo-
nents/devices. Examples are temperature and humidity sensors that
can record the temperature and moisture content at any given time,
motion detectors, and RFID tags. To facilitate the transfer and proc-
essing of the data acquired, these sensors and smart devices can be
connected to wireless networks such as Wi-Fi, Bluetooth, ZigBee,
WPAN, and many more. Every component in IoT carries a digital
identity known as a universally unique identiﬁer (UUID) [64]. This
UUID can be used to identify objects on the Internet as everything
has a connection.
The data collected is then passed through an IoT gateway. An IoT
gateway is a physical device or virtual platform that receives the
sensed data and transmits the data towards the application platform
for cloud storage and data analysis [66,67]. It is also bidirectional,
meaning it can work both ways by receiving information from the
application platform and giving signals to the sensors or actuators to
carry out the speciﬁc task. Another key function of an IoT gateway is
that it pre-processes the data received (compiling and synchronizing
data) before passing it to the cloud. This helps reduce the burden and
load on the cloud system, hence it helps to reduce response times
and network transmission costs [66]. The IoT gateway can offer secu-
rity by transmitting data through higher-order encryption methodol-
ogies and protecting the system from possible cyberattacks [63,68].
At the IoT cloud, there is a massive network of servers that sup-
ports IoT components and applications. The IoT cloud offers the nec-
essary infrastructure, storage, and servers for large-scale and real-
time operations. This allows the cloud to process billions of IoT devi-
ces and trafﬁc management at incredibly high speeds. The scenario
where IoT smart devices are integrated with a cloud ecosystem is
known as CloudIoT [69] or Cloud of Things (CoT) [70]. Through this
integration, the advantages of cloud computing can be reaped [71].
Some of the beneﬁts of cloud computing are reducing expendable IT
costs for expensive hardware storage, the freedom and ﬂexibility of
business scalability, and allowing the ease of collaboration with other
partners through access to the cloud [72]. Hence the collected data
from the sensors in the BSF farm can be stored in the cloud easily.
The information and data stored in the cloud usually have to go
through analytics. IoT analytics is the application of data analysis
tools to analyze and interpret information collected by the sensors
which can be utilized to improve and monitor the IoT system [73]. A
major beneﬁt of having an efﬁcient IoT system with good analytical
tools is that the analysis process can be carried out in real-time which
helps technicians and engineers to identify the irregularities and
inconsistencies in the data quickly and prevent alarming issues. Now-
adays, big corporations utilize data analytics to help identify future
insights and plan out future business opportunities. In the case of the
BSF farm, info regarding the temperature or humidity can be ana-
lyzed and compared with one another to see if there is a possible
issue in the abiotic conditions or to identify random errors during the
rearing process.
The ﬁnal important aspect of an ideal IoT system should be a well-
designed and well-produced user interface (UI). UIs are the visible
and interactable part of the IoT system which can be accessed by
common users or consumers. They allow users to visually monitor
the changes in the IoT system, and can also allow the user to activate
certain actuators or sensors remotely. Good UIs are usually user
friendly and have a minimalistic control system to allow ease of com-
pleting tasks and prevent confusion. Typical UIs are applications on
mobile phones and computers, but in recent years UIs can be present
on smartwatches or virtual assistants such as Amazon Echo or Alexa
[74]. If looked at commercially, UI design is crucial in today’s compet-
itive IoT market, as the visual appearance will be what draws poten-
tial purveyors to the product. UI applications need to have a clear
logic ﬂow and creative outlook to be likened by users [75]. For the
BSF smart farm, UIs can be installed on applications on computers
and mobile phones, which can then allow users to monitor the farm
remotely through interactable widgets and controls. An example of
UI monitoring will be showcased below.
3.2. Smart farming
Smart farming is a new and emerging concept that is based upon
the management of farms using technologies such as IoT, robotics,
and artiﬁcial intelligence (AI) to increase the output and quality of
products while minimizing the manpower required for hard labor
[76]. Therefore, smart farming can be deﬁned as a management con-
cept that provides the agricultural industry with the needed infra-
structure to allow for advanced technology [77]. As smart farming
comprises the principles of IoT, it also implements the usage of sen-
sors for soil scanning and growth parameters management, telecom-
munication devices such as GPS, and data analytical tools along with
software for IoT-based problem solving and decision making [78].
Smart farming usually encompasses a cycle that is based on IoT fun-
damentals. It can be divided into 4 phases: observation, diagnostics,
decisions, and action [76]. The observation phase is where the digital
sensors record information from the crops, livestock, or surround-
ings. Proceeding to the diagnostics phase, the sensorial information is
passed through the gateway and fed to the IoT cloud. The decisions
phase is where the user utilizes machine learning-driven compo-
nents of the IoT structure to make an informed selection. Finally, the
action phase is when the action is taken and the cycle is repeated. It
is noted that even though the smart farming concept was created
based around the agricultural industry, the ideology can be trans-
ferred to the rearing of insects as they are very similar in terms of
growth needs and parameters.
Smart farming is very beneﬁcial and provides an upper hand com-
pared to the traditional manual farming methods. It helps to improve
the quantity and quality control of the products through IoT automa-
tion. With great control over the agricultural system, it brings about
better cost management and waste reduction. Hence, it can be said
that gives way to a sustainable agricultural system. IoT in smart farm-
ing allows real-time monitoring which allows for producers to alter
certain growth factors depending on the current environmental con-
ditions. This enables quicker action to be taken and prevents any det-
rimental setbacks. Smart farming has also allowed the ease of
precision farming. Precision farming is the concept of being able to
get crops or livestock the precise treatment or necessity with pin-
point accuracy [76]. It relies on satellite imagery as decisions are usu-
ally made according to the area or per commodity [79].
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235
5

Smart farming also helps to boost agricultural proﬁtability for pro-
ducers and farmers. By reducing the amount of resources needed to
be inputted, money and labor costs can be reduced [80]. Through IoT,
yield projections and disease/disaster probability maps can be con-
structed which drastically helps to reduce business risks and allow
optimal cultivation of crops and animals [80]. To further elaborate on
the sustainable agricultural system mentioned above, smart farming
can reduce the ecological footprint. Precision farming allows the alle-
viation of leaching problems and greenhouse gas emissions from the
excessive, unaccounted usage of fertilizers and pesticides in crop
growing [81].
In smart farming, agricultural drones can be implemented to
assist in the monitoring and ﬁeld analysis process [82]. They can be
both ground-based and aerial-based, depending on their deﬁned
function. They can carry out repetitive tasks for prolonged periods,
and at top-notch efﬁciency. This would greatly eliminate the reliance
on manual labor. They can also cover large grounds in a short amount
of time, thus boosting the efﬁciency of the surveying and nurturing
process. Besides that, smart greenhouses, which are greenhouses lev-
eraged with IoT, help to create a self-regulating microclimate so that
crops can grow in a conducive environment [83]. The real-time data
received by farmers allow them to make adjustments to the system
to ensure the plants have unhindered growth. Smart farming has also
opened opportunities for a more efﬁcient method in detecting and
monitoring pests and diseases in crops [84]. In India, many mobile
applications such as Kheti-Badi (social initiative app to present infor-
mation and issues to farmers in India) and Pusa Krishi (provides sim-
ple solutions to agricultural problems faced by farmers in India) as
well as Pest Management Information Systems (PMIS) have been uti-
lized to help carry out surveillance and divulge important informa-
tion to farmers [84]. This way, farmers are kept in the loop and can
add technological and IoT advances to their repertoire. It may seem
smart farming is only conﬁned to the realms of agriculture, but in
actuality, it has started to be integrated into the insect rearing ﬁeld.
Aspire Food Group has implemented IoT smart farming in rearing
insects by applying complex modelling simulations and analytical
approaches to optimize their insect farming techniques [85]. They
are trying to build an autonomous and centralized system and
implement zero-waste systems so the farms can function at high efﬁ-
ciency and sustainability.
3.3. Implementation of IoT in small-scale BSF farms
As mentioned in the above sections, the prototype small-scale BSF
farm created has IoT elements integrated into it as shown in Fig. 3,
and they can be divided into mainly three parts: sensors/devices,
software platform, and mobile application (user interface). The small
white box is where the devices and ﬁrmware are stored, and the
green container is the water storage for mist nozzle spraying. The
blue device on the water storage is the water pump motor.
3.3.1. Sensors/Devices
The ﬁrst part involves sensors, relays and moving components. As
temperature and humidity conditions are vital for the successful
growth of BSF, a temperature-humidity sensor should be used to
monitor these factors to ensure they are maintained at an optimum
range. In the prototype BSF farm, a DHT22 sensor is used. The DHT22
sensor is a 2-in-1, temperature and humidity sensor composed of a
capacitive humidity sensor and a thermistor to measure the sur-
rounding air and produce a digital signal on its data pin [86]. It is low
cost and has a basic design, making it suitable for simple data logging.
It has a voltage range of 35 V and a maximum current of 2.5 mA
while requesting data [86]. Fig. 4(a) shows the DHT22 sensor
attached to the wall of the lower box. Besides that, to regulate the
moisture content of the rearing area, water needs to be sprayed peri-
odically to ensure the humidity is at the right level. Water nozzles
with a misting setting are connected along a water pipe surrounding
the box, as shown in Fig. 4(b). The pipe is connected to a water pump
that runs on a voltage of 5 V. However, the NodeMCU ﬁrmware board
runs on 3 V. Hence, a relay connected to a breadboard is used to step
down the voltage to the suitable value of 3 V.
3.3.2. Software platform
All the sensors require a platform to send the acquired data to,
hence a NodeMCU board is used. NodeMCU is an open-source ﬁrm-
ware and development board based on the Lua scripting language
Fig. 3. The prototype BSF small-scale farm.
6
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235

[87]. It typically runs on a voltage of about 3 V. It can connect to the
Internet with a Wi-Fi SoC (System on a Chip) called ESP8266. The
NodeMCU is coded using Arduino through the C++ language to be
able to receive the sensed data and transmit data and responses to a
mobile application through the Wi-Fi SoC. The code requires the
input of the WiFi SSD as well as the WiFi password.
3.3.3. Mobile application
The mobile application used is Blynk, an IoT platform with a free
IoT Cloud network. Through this app, the sensed data can be visual-
ized and be represented in charts and graphs. Besides that, the user
interface can be customized to one’s personal preference. Moving
parts such as the pump can be controlled through in-app widgets at
one’s desire, to ensure sufﬁcient water is provided to the rearing area
of the BSF larvae. Some features of the application are shown in
Fig. 5. The temperature and humidity recorded by the DHT22 sensor
are displayed, as well as the trend in the graph of the respective
quantities for a given set of times. The button displayed controls the
motors and by activating it, water will be drawn in and sprayed
through the misting nozzles. A closer look at the graph of tempera-
ture and humidity against time is shown on the right.
3.4. Related examples
In addition to the prototype BSF smart farm attempted, there have
been multiple types of research done more thoroughly where IoT is
implemented into the designing of smart farms, as well as BSF rearing
[21,88-90]. For example, Ryu, et al. [88] has come up with a con-
nected farm based on IoT systems, which aim to provide smart farm-
ing systems for end-users. The research used similar IoT principles
and components to the prototype carried out. Mobius, an IoT service
platform was used to create virtual representations of physical IoT
devices [88]. The IoT service platform is compliant with the oneM2M
initiative, which is an initiative started in 2012 to regulate and stan-
dardize a common machine to machine (M2M) and IoT service layer
platform for an M2M service that is applicable worldwide and
access-independent [89]. Besides that, a device software platform,
such as a middleware known as &Cube was installed into the IoT
gateways. It functions as a Java program [88]. The &Cube was
installed in a Raspberry Pi, as compared to the prototype where a
NodeMCU ESP8266 was used instead. As this farm was geared to agri-
cultural purposes, more advanced sensors in addition to the tempera-
ture
and
humidity
sensor
were
used,
such
as
CO2
sensors,
Fig. 4. (a) DHT22 sensor adhered to the wall of the rearing area (b) Waterpipe with misting nozzles surrounding the rearing area.
Fig. 5. (a) Blynk User Interface for the BSF Farm IoT Project (b) Superchart graph display the temperature and humidity over time.
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235
7

photosynthetic photon ﬂux density (PPFD) sensors, and soil moisture
sensors [88]. Instead of a Wi-Fi-based network, a ZigBee-based net-
work was used. There are pros and cons to both. ZigBee consumes a
very low amount of power and has a long battery life, however, its
data transfer speed is much lower than Wi-Fi networks (maximum
speed is 250kbps) [90]. Wi-Fi on the other hand has a high bandwidth
and faster data transfer speed, however, the drawback is that the
power consumption is greater and might be an alarming issue if the
endpoints run on battery life [90]. Hence, the selection boils down to
the user’s preference on which factor to prioritize. Ryu et al. also
developed their mobile application for remote monitoring and con-
trol over the connected farm, hence they can customize the applica-
tion to one’s desire.
On the other hand, in India, a BSF containment system with IoT
monitoring was set up to tackle the organic waste issue which is a
more environmentally friendly management system [21]. The IoT
monitoring methodology done on the prototype BSF small-scale farm
was heavily inspired by the research done by Sabir et al. [21] as it
proved to be a simple and easy method to integrate IoT elements into
a manual project. The experiment used more high-tech sensors such
as MQ7 gas sensor (detects carbon dioxide), MQ135 sensor (detects
ammonia, hydrogen sulﬁde, and other harmful gases) and MS-1100
VOC formaldehyde sensor [21]. In terms of the breeding container,
used a multi-container system that was designed to utilize the BSF
larvae as a composter of organic waste. It has great potential to be
used on a large scale for better organic waste management, through
an electrically controlled artiﬁcial system.
Finally, in Sarawak, Malaysia, a prototype of a remote monitoring
system for BSF farming was set up for showcasing the possibility of
implementing an IoT remote system in an environment for rural agri-
culture [22]. The purpose of this research was to show a possible
solution to food security issues in Southeast Asia, and BSF was chosen
as the subject of rearing as there are multiple parameters to be moni-
tored [22]. Libelium Waspmote Smart Agriculture platform was used
as the IoT sensor node for the collection of data. A Raspberry Pi 3B is
selected as the IoT Gateway device as it has a low power consump-
tion, along with a MiFi Modem for an Internet connection [22]. A
Raspberry Pi is more suitable for professional projects due to it being
one of the more advanced boards, whereas the NodeMCU used for
the prototype BSF farm is more for casual projects and occasions. The
monitoring system also uses the XBee Pro 900HP, a wireless radio
module that helps to transmit data packets to the IoT gateway [22].
4. Extraction methods of biochemical compounds from BSF
As mentioned above, the main purpose of setting up the BSF
small-scale farm was to carry out extraction on the biochemical com-
pounds contained in BSF. Some of the biochemical compounds
include lipids, proteins, and chitin/chitosan. The extraction methods
will be brieﬂy discussed.
Lipids are typically the ﬁrst biochemical compound to be
extracted from BSF, as it is relatively the easiest compound to be
extracted, and would also result in easier extraction for the remain-
ing biochemical compounds. This can be seen in the procedures of
the following experiments. The most conventional method to extract
lipids from BSF larvae is to carry out Soxhlet extraction [91]. The BSF
larvae can be ground and free-dried to a powder, where Soxhlet
extraction with n-hexane and 2-methyloxolane (2-MeO) respectively
was carried out exhaustively [92]. In the same research, a three-stage
cross-current extraction was set up using the same solvents men-
tioned above comparatively, whereby in each stage fresh solvents
were added [92]. It was found that the cumulative oil yield extracted
was the same between the two conventional and industrial methods,
however, it was found that 2-MeO was overall a better lipid recovery
and enhanced bioactivity [92]. Another lipid extraction process
involved ﬁnely ground BSF prepupae that was extracted with
petroleum ether as the solvent and recovered through solvent evapo-
ration under a vacuum [93]. The process was found to have a yield of
87% [93] An extraction with enzymatic methodology was also carried
out, using enzymes such as Bacillus licheniformis protease, pepsin,
papain, and pancreatin [93]. However, after centrifugation, it was
found that the yield of lipids was only 10%, which is much lower than
the solvent extraction methods. Hence, it was deduced that to
acquire a pure lipid fraction, it is most efﬁcient to carry out extraction
with organic solvents [93].
BSF also has an attractive protein content, which has made it a
popular choice as animal feed and as a meat substitute in entomoph-
agy. A simple one-step method to extract proteins is to treat defatted
BSF pellets with NaOH in a water bath, and then neutralize and place
the supernatant acquired into a centrifuge for 15 min at 4000 RPM
[93]. Precipitation with 10% trichloroacetic acid (TCA) solution in ace-
tone was then carried out and proteins were then recovered. It is
found that the supernatant had an 84% protein fraction recovery, and
if the residual fraction was solubilized, the combined protein recov-
ery would be 96% [93]. Another way to extract proteins from insects
is to blend nitrogen-frozen insects with demineralized water and
ascorbic acid [94]. The insect suspension was then ﬁltered and centri-
fugated to produce pellets, the supernatant and fat fraction [94]. The
protein is found in the pellets and supernatant. It is also found that
defatting the insect residue beforehand and carrying out sonication
enhances the protein extraction yield by a large margin [95]. Hence,
it is advisable to carry out these procedures if the protein is the main
subject of extraction. A study has also been done to compare chemi-
cal extraction and enzymatic-assisted extraction, and it was found
that the enzymatic extraction had a greater impact on the environ-
ment as compared to the latter, due to the longer experimental time
for the enzymatic process [96]. To mitigate this issue, improvements
like biomass pretreatment procedures or enzymes that require a
shorter extraction time should be utilized.
Chitin is also an important bioactive compound present in BSF.
Chitosan, the derivative of chitin, can be produced by carrying out
deacetylation on chitin, typically using hydrochloric acid and sodium
hydroxide [97]. Chitin is not soluble in water, whereas chitosan is
sparingly soluble in water [98]. Chitin is highly sought after, due to
its versatility in many industries. It can be used as an inducer in plant
defence mechanisms against diseases [99], as an additive that func-
tions to thicken and stabilize foods and food emulsions [100], and
even to produce nanoﬁbrils, which are biopolymers that have
wound-healing properties [101] and promote cell migration and pro-
liferation [102]. Chitin is typically extracted through an initial grind-
ing of the insect in a mortar and pestle to break the exoskeleton
[103]. Then, demineralization is carried out using hydrochloric acid,
followed by deproteinization with NaOH [103,104]. The solids (chi-
tin) in the mixture are ﬁltered out and washed with demineralized
water until neutral pH is attained, and ﬁnally dried [103]. Chitin can
also be extracted through biological methods, that is microbial fer-
mentation. Bacillus lichenformis A6 is placed together with grounded
BSF shells, and is left on a rotary shaker for 10 days [97]. The fer-
mented powder was then washed, sieved and dried. The chitin resi-
due then undergoes discoloration by adding sodium bicarbonate,
then washed with water and dried to obtain chitin [97]. A beneﬁt of
using biological methods is that it eliminates the need of generating
large volumes of acid and alkaline efﬂuents in conventional chemical
methods, which need to be treated before being able to be disposed
of. Table 1 shows a comprehensive evaluation of the extraction meth-
ods discussed above.
Currently, there has not been any attempts at implementing IoT
during the BSF larvae extraction process. Through IoT integration,
certain extraction processes can be automated and done remotely,
which will result in the reduction of manpower required on-site. IoT
integration also allows monitoring of extraction parameters such as
temperature and concentration, which in turn allows errors and
8
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235

anomalies to be identiﬁed and amended accordingly. It is noted that
for some extraction processes complete automation will be very difﬁ-
cult to achieve, however, IoT implementation will ease certain sec-
tions of the processes. Hence, there needs to be further research into
the effectiveness and feasibility of implementing IoT in BSF extraction
processes.
5. Future prospects and challenges in smart farming of BSF
BSF has proven to be analogous to a Swiss army knife, being versa-
tile and applicable to many circumstances. BSF can be used as a probi-
otic additive and are in the works of being implemented into organic
semiconductors [107]. As we are living at the apex of a technological
era, it would certainly be a waste to not take the opportunity to inte-
grate IoT into the conventional manual farming methods. Smart
farming will be relevant in helping to improve and solve issues
regarding manual labor in agricultural farming and insect rearing. As
a majority of the world begins to have easier access to smartphones
and IoT, information can easily be divulged amongst one another to
provide solutions to agricultural problems faced by farmers in devel-
oping countries. These new technologies can bridge the gap between
rural and urban farmers [108]. As mentioned previously, agricultural
mobile applications have been developed which allows for the estab-
lishment of systems and networks for smart farming learning and
information exchange.
Rearing insects on organic waste can signiﬁcantly reduce waste
odour and also pathogens [109,110]. Besides that, insect rearing on
organic waste such as food waste and human faeces has been found
to reduce organic waste in a range from 25% to 72%, on a dry matter
basis [111,112]. This was done through the manual rearing process of
BSF. Now with the huge boom in IoT, experiments have been carried
out where IoT was implemented in the rearing process of BSF. How-
ever, as this is still a developing ﬁeld in the case of BSF, there has not
been any studies done in where BSF reared through IoT implementa-
tion undergo the organic waste (food waste) reduction process quan-
titatively, which would allow an analytical and statistical comparison
between the efﬁciency of manually reared BSF versus IoT-reared BSF.
Hence, research on this ﬁeld would help to make decisions on
whether one method is superior to the other.
IoT in smart farming allows for wireless technologies and remote
devices to function with ease. Unmanned aerial vehicles (UAV) have
been used to survey and evaluate the growth of crops, as well as
observe biodiversity and ecological landscape features [113]. With
advancements in task-based control and swarm technology, drones
and robots can be equipped with various devices and work together
to improve land management capabilities [108]. A lot of these devices
are powered through wireless networks. Wireless technologies that
are suitable for long-range constraints and a large amount of data
should rely on Long Term Evolution (LTE) or 4 G networks (and its
future releases) to carry out technology-reliant agriculture [114].
They are the most suitable wireless networks as they can transfer
large amounts of data within a short amount of time. Finally, machine
learning (ML) and artiﬁcial intelligence (AI) can be implemented in
smart farming to analyse and mine data for trend analysis [108].
Through ML and AI, algorithms, valuable information about produc-
tivity and growth trends can be acquired, which allows farmers to
tailor to the changes needed.
However, with beneﬁts, smart farming also brings some chal-
lenges that could be detrimental if not taken care of. Firstly, the data
collected through ICT means on agriculture farming and insect rear-
ing can raise doubts about property rights and the use of data. It is
said that business models can create added value by converting the
data acquired into information and advice for both farmers and regu-
latory authorities who have a chance of using the data for control and
surveillance [80]. Hence, governments across the world need to
instate rigid regulations to prevent the misuse of data, which will
lead to legal and ethical issues regarding data monitoring [115].
Besides that, technology adoption to farming might pose an issue
to developing countries, as there are high costs to bear and limited
knowledge available to farmers from these regions [116]. Hence
there is a possibility that the fruits of IoT may only be savoured by
developed and industrialized countries. Hence, there needs to be an
initiative whereby this technological gap in developing countries is
closed and keep the farmers up to date. A social implication of IoT
implementation that raises doubts in farmers themselves is whether
automated and technological services will replace the existing
knowledge and experience in farmers [117]. However, farmers
should be able to collaborate and provide input on the trend develop-
ment created by IoT devices on whether such scenarios are realistic.
Finally, as there are new technological advances, there will always
be cybersecurity issues trailing behind. The increased usage of IoT in
agriculture increases the level of exposure to cybercrimes, hence
Table 1
Possible extraction methods for bioactive compounds in BSF.
Extraction methods
Targeted compound Extraction conditions
Yield (%)
Potential applications
References
n-hexane Soxhlet extraction
Lipids
3-stage cross-current extraction
32.51 § 0.39
-Biodiesel
-Animal feed
[105,106]
2-MeO Soxhlet extraction
Lipids
3-stage cross-current extraction
35.83 § 1.12
Petroleum ether extraction
Lipids
2-step method involving mixing
and evaporation
87
Enzymatic extraction
Lipids
Hydrolysis under varying condi-
tions dependant on the type of
enzyme used, followed by
centrifugation
10
NaOH extraction
Proteins
-BSF needs to be defatted
-Heated in a water bath and
centrifugated at 4000 RPM for
15 mins
84 (96 if the residual protein
fraction is further solubilized
through acid
demineralization)
-Component in processed
human food
-Animal feed (replacement of
soy and ﬁsh meal)
[15]
Demineralized water and ascor-
bic acid
Proteins
-Insects need to be frozen with
N2, then blended
-Filtered and centrifugated
6575 (as dry matter pellet frac-
tions)
5061 (as a supernatant
fraction)
Demineralization and
deproteination
Chitin
-BSF is ground, then demineral-
ized with HCl, followed by
deproteination with NaOH
824
-Plant defence mechanism
inducer
-Food additive that acts as a
thickener and stabilizer
-Nanoﬁbrils (biopolymer)
[99102]
Microbial fermentation
Chitin
-BSF is grounded and treated
with Bacillus lichenformis A6
-Discoloured, washed and
dried
12.4
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235
9

causing the industry to be more vulnerable to cyberattacks on infra-
structures and production facilities [118]. As the data collected usu-
ally are stored on the Internet, security and privacy issues will arise
regarding smart farming threats. Cyber espionage can be rampant as
countries around the world will make illegal efforts to get informa-
tion and schematics regarding other nations’ agricultural technology
[119]. The use of GPS systems in smart farming can pose a threat by
allowing cybercriminals to gain vital information regarding the farm
and crops being reared [120]. This gives rise to agroterrorism, a term
to describe cyber terrorism in the agriculture industry. Also, cloud
computing attacks are frequent in IoT, as a lot of information is stored
in the cloud. If a large number of vulnerable machines get infected
with malware, there is a huge possibility that distributed denial-of-
service (DDoS) attacks can occur and hinder the usage of the cloud
[121]. DDoS attacks can cause major operational (interruption of
services, new training for farm operators) and ﬁnancial damages
[122]. Luckily, some steps have been taken to safeguard the safety of
smart farming. A lightweight device authentication solution in which
session keys and public keys in Peer to Peer (P2P) network are com-
bined to expedite encryption/decryption tasks. This helps to give rise
to a safer smart farming communication system [123].
6. Conclusion
As we pivot into a new decade, food wastage is still a serious issue
that has plagued all parts of the world. Even though the beginning of
the COVID-19 pandemic had caused a 12% increase in household food
waste generation, many initiatives have been taken by scientists to
mitigate food waste problems [124]. This work serves as an attempt
to showcase the potential of using IoT in BSF rearing to tackle food
waste issues. This work allows for remote monitoring of a BSF farm,
along with real-time monitoring of growth parameters and amend-
ments which can be done conveniently off-site, in the case of contin-
gencies. This work also showcases the potential of smart farming,
which if implemented on BSF on a large scale, can prove to be very
lucrative and efﬁcient in terms of producing BSF larvae for various
purposes, including organic waste management and also as a sub-
stance to be extracted. Besides that, this work has shown BSF larvae
to be a good source of bioactive compounds with wide availability of
applications in various ﬁelds. Through the implementation of IoT in
these processes, the reliance on technology will help to ease the pro-
cedures of carrying out the necessary activity.
Credit Author Statement
Josiah Cheng Foong Van: Conceptualization, Josiah Cheng Foong
Van: Writing  Original Draft, Josiah Cheng Foong Van, Pei En Tham,
Hooi Ren Lim, Kuan Shiong Khoo, Jo-Shu Chang, Pau Loke Show:
Writing  Review & Editing, Josiah Cheng, Foong Van: Visualization,
Kuan Shiong Khoo, Jo-Shu Chang, Pau Loke Show: Supervision.
Declaration of Competing Interest
The authors declare that they have no known competing ﬁnancial
interests or personal relationships that could have appeared to inﬂu-
ence the work reported in this paper.
Acknowledgment
This work was supported by the Fundamental Research Grant
Scheme,
Malaysia
[FRGS/1/2019/STG05/
UNIM/02/2],
MyPAIR-
PHCHibiscus Grant [MyPAIR/1/2020/STG05/UNIM/1] and Kurita
Water and Environment Foundation (KWEF) [21Pmy00421R]. The
authors also gratefully acknowledge the ﬁnancial support by Tai-
wan’s Ministry of Science and Technology (MOST) under grant nos.
108-2218-E-029-022-MY3,
1102221-E-029
004
-MY3,
1102621-M-029 001, and 1092622-E-110 011.
References
[1] Chapagain AK, James K. Chapter 12 - Accounting for the Impact of Food Waste on
Water Resources and Climate Change. In: Kosseva MR, Webb C, editors. Food
Industry Wastes. San Diego: Academic Press; 2013. p. 217–36.
[2] Bajzelj B, Richards KS, Allwood JM, Smith P, Dennis JS, Curmi E, CA Gilligan.
Importance of food-demand management for climate mitigation. Nat Clim
Change 2014;4(10):924–9.
[3] Abeliotis K, Lasaridi K, Costarelli V, Chroni C. The implications of food waste gen-
eration on climate change: The case of Greece. Sustain Prod Consum 2015;3:8–
14.
[4] Jeon Y-S, Yang J-S, Park E-R, Yang J-W, Baek K. Continuous electrochemical
removal
of
salts
from
Korean
food
wastes.
J
Taiwan
Inst
Chem
Eng
2016;64:142–5.
[5] Cameron M, Marshall J, Wang J, Elliot A. Solid waste in Canada. Human Activity
and the Environment, Annual Statistics. Statistics Canada 2005.
[6] Tejera J, Hermosilla D, Gasco A, Miranda R, Alonso V, Negro C, Blanco A. Treat-
ment of mature landﬁll leachate by electrocoagulation followed by Fenton or
UVA-LED photo-Fenton processes. J Taiwan Inst Chem Eng 2021;119:33–44.
[7] Nguyen TTX, Tomberlin JK, Vanlaerhoven S. Ability of Black Soldier Fly (Diptera:
Stratiomyidae) Larvae to Recycle Food Waste. Environ Entomol 2015;44
(2):406–10.
[8] Shelomi M, Wu M-K, Chen S-M, Huang J-J, CG Burke. Microbes Associated With
Black Soldier Fly (Diptera: Stratiomiidae) Degradation of Food Waste. Environ
Entomol 2020;49(2):405–11.
[9] Liu T, Awasthi MK, Awasthi SK, Duan Y, Zhang Z. Effects of black soldier ﬂy larvae
(Diptera: Stratiomyidae) on food waste and sewage sludge composting. J Envi-
ron Manage 2020;256:109967.
[10] Craig Sheppard D, Larry Newton G, Thompson SA, Savage S. A value added
manure management system using the black soldier ﬂy. Bioresour Technol
1994;50(3):275–9.
[11] Spranghers T, Noyez A, Schildermans K, De Clercq P. Cold Hardiness of the Black
Soldier Fly (Diptera: Stratiomyidae). J Econ Entomol 2017;110(4):1501–7.
[12] Newton L, Sheppard C, Watson D, Burtle G, Dove R. Using the Black Soldier Fly,
Hermetia Illucens, as a Value-Added Tool for the Management of Swine Manure
2005;17 Animal and Poultry Waste Management Center.
[13] Park HH. "Black Soldier Fly Larvae Manual." https://scholarworks.umass.edu/cgi/
viewcontent.cgi?article=1015&context=sustainableumass_studentshowcase
(accessed 15 July, 2021).
[14] Diener S, Zurbr€ugg C, Tockner K. Conversion of organic material by black soldier
ﬂy larvae: establishing optimal feeding rates. Waste Manag Res 2009;27
(6):603–10.
[15] M€uller A, Wolf D, HO Gutzeit. The black soldier ﬂy, Hermetia illucens  a prom-
ising source for sustainable production of proteins, lipids and bioactive substan-
ces. Naturforsch C 2017;72(9-10):351–63.
[16] Mohd-Noor S, Wong C-Y, Lim J-W, Mah-Hussin M-T-A, Uemura Y, Lam M, Ramli
A, Bashir M, Tham L. Optimization of self-fermented period of waste coconut
endosperm destined to feed black soldier ﬂy larvae in enhancing the lipid and
protein yields. Renew Energy 2017;111:646–54.
[17] Gougbedji A, Agbohessou P, Laleye PA, Francis F, Caparros Megido R. Technical
basis for the small-scale production of black soldier ﬂy, Hermetia illucens (L.
1758), meal as ﬁsh feed in Benin. J Agric Food Res 2021;4:100153.
[18] Bullock N, Chapin E, Evans A, Elder B, Givens M, Jeffay N, Pierce B, Robinson W.
The Black Soldier Fly How-to-Guide 2013:12.
[19] Wang K, Khoo KS, Leong HY, Nagarajan D, Chew KW, Ting HY, Selvarajoo A,
Chang J-S, Show PL. How does the Internet of Things (IoT) help in microalgae
bioreﬁnery? Biotechnol Adv 2021:107819.
[20] Einstein-Curtis A. "Black soldier ﬂy tech aims to simplify, specialize production."
https://www.feednavigator.com/Article/2019/08/29/Black-soldier-ﬂy-tech-
aims-to-simplify-specialize-production (accessed 3 August, 2021).
[21] Sabir MO, Verma P, Maduri PK, and Kushagra K, "Electrically controlled artiﬁcial
system for organic waste management using Black Soldier Flies with IOT moni-
toring," in 2nd International Conference on Advances in Computing, Communica-
tion Control and Networking (ICACCCN), Greater Noida, India, 2020, December
2020, pp. 871-875, doi:10.1109/ICACCCN51052.2020.9362816.
[22] Chew KT, Jo RS, Lu M, Raman V, and Then PHH, "Organic Black Soldier Flies (BSF)
Farming in Rural Area using Libelium Waspmote Smart Agriculture and Inter-
net-of-Things Technologies," in 11th IEEE Symposium on Computer Applications &
Industrial Electronics (ISCAIE), Penang, Malaysia, 2021, April 2021, pp. 228-232,
doi:10.1109/ISCAIE51753.2021.9431801.
[23] Ferrarezi R, Cannella L, Nassef A, and Bailey D, UVI/AES Annual Report 2016 -
Alternative Sources of Food for Aquaponics in the U.S. Virgin Islands: A Case Study
with Black Soldier Flies. 2016.
[24] Insectta. "The BSF Life Cycle." https://www.insectta.com/learn-more (accessed
14 July, 2021).
[25] Libal A. "The Difference Between Soldier Fly Larvae & Maggots." https://animals.
mom.com/difference-between-soldier-ﬂy-larvae-maggots-8917.html (accessed
14 July, 2021).
[26] Dortmans B, Diener S, Verstappen B, Zurbr€ugg C. Black Soldier Fly Biowaste Proc-
essing - A Step-by-Step Guide. Eawag  Swiss Federal Institute of Aquatic
10
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235

Science and Technology Department of Sanitation, Water and Solid Waste for
Development (Sandec) 2017:100.
[27] Nakamura S, Ichiki RT, Shimoda M, Morioka S. Small-scale rearing of the black
soldier ﬂy, Hermetia illucens (Diptera: Stratiomyidae), in the laboratory: low-
cost and year-round rearing. Appl Entomol Zool 2016;51(1):161–6.
[28] Lievens S, Poma G, Smet J, Van Campenhout L, Covaci A, Van Der Borght M.
Chemical safety of black soldier ﬂy larvae (Hermetia illucens), knowledge gaps
and recommendations for future research: a critical review. J Insects as Food
Feed 2021;7:1–14.
[29] Smet JD, Wynants E, Cos P, Campenhout LV, HL Drake. Microbial Community
Dynamics during Rearing of Black Soldier Fly Larvae (Hermetia illucens) and
Impact on Exploitation Potential. Appl Environ Microbiol 2018;84(9):e02722-
17.
[30] Shumo M, Khamis FM, Tanga CM, Fiaboe KKM, Subramanian S, Ekesi S, van Huis
A, Borgemeister C. Inﬂuence of Temperature on Selected Life-History Traits of
Black Soldier Fly (Hermetia illucens) Reared on Two Common Urban Organic
Waste Streams in Kenya. Animals : an open access journal from MDPI 2019;9
(3):79.
[31] Chia S, Tanga C, Khamis F, Mohamed S, Salifu D, Subramanian S, Fiaboe K, Niassy
S, van Loon J, Dicke M, Ekesi S. Threshold temperatures and thermal require-
ments of black soldier ﬂy Hermetia illucens: Implications for mass production.
PLoS One 2018;13:e0206097.
[32] Tomberlin JK, Adler PH, Myers HM. Development of the Black Soldier Fly (Dip-
tera: Stratiomyidae) in Relation to Temperature. Environ Entomol 2009;38
(3):930–4.
[33] Zhang J, Huang L, He J, Tomberlin JK, Li J, Lei C, Sun M, Liu Z, Yu Z. An artiﬁcial
light source inﬂuences mating and oviposition of black soldier ﬂies, Hermetia
illucens. J Insect Sci 2010;10:202.
[34] Zenyr Garden. "Food Amount for 1 KG of BSF Larvae & The Larvae Yield." https://
zenyrgarden.com/how-much-food-to-feed-one-kilo-of-black-soldier-ﬂy-larvae-
the-larvae-yield/ (accessed 16 July, 2021).
[35] Nijhout HF. The control of body size in insects. Dev Biol 2003;261(1):1–9.
[36] Simpson SJ, Sword GA, Lorch PD, ID Couzin. Cannibal crickets on a forced march
for protein and salt. Proc Natl Acad Sci U.S.A. 2006;103(11):4152.
[37] Lee KP, Simpson SJ, Raubenheimer D. A comparison of nutrient regulation
between solitarious and gregarious phases of the specialist caterpillar, Spodop-
tera exempta (Walker). J Insect Physiol 2004;50(12):1171–80.
[38] Koeleman E. "What to feed the Black Soldier ﬂy larvae?" https://www.allabout-
feed.net/all-about/new-proteins/what-to-feed-the-black-soldier-ﬂy-larvae/
(accessed 16 July, 2021).
[39] Cammack JA, Tomberlin JK. The Impact of Diet Protein and Carbohydrate on
Select Life-History Traits of The Black Soldier Fly Hermetia illucens (L.) (Diptera:
Stratiomyidae). Insects 2017;8(2).
[40] Harnden LM, Tomberlin JK. Effects of temperature and diet on black soldier ﬂy,
Hermetia illucens (L.) (Diptera: Stratiomyidae), development. Forensic Sci Int
2016;266:109–16.
[41] Hopkins I, Newman LP, Gill H, Danaher J. The Inﬂuence of Food Waste Rearing
Substrates on Black Soldier Fly Larvae Protein Composition: A Systematic
Review. Insects 2021;12(7):608.
[42] Green TR, Popa R. Enhanced Ammonia Content in Compost Leachate Processed
by Black Soldier Fly Larvae. Appl Biochem Biotechnol 2012;166(6):1381–7.
[43] Mustard JA. The buzz on caffeine in invertebrates: effects on behavior and
molecular mechanisms. Cell Mol Life Sci 2014;71(8):1375–82.
[44] Tingle FC, Mitchell E, WW Copeland. The soldier ﬂy, Hermetia illucens in poultry
houses in north central Florida [Insect pests]. J Ga Entomol Soc 1975.
[45] Tomberlin J, Sheppard D. Factors Inﬂuencing Mating and Oviposition of Black
Soldier Flies (Diptera: Stratiomyidae) in a Colony. J Entomol Sci 2002;37:345–
52.
[46] Liu Z, Najar-Rodriguez AJ, Minor MA, Hedderley DI, Morel PCH. Mating success
of the black soldier ﬂy, Hermetia illucens (Diptera: Stratiomyidae), under four
artiﬁcial light sources. J Photochem Photobiol B 2020;205:111815.
[47] Meneguz M, Gasco L, Tomberlin JK. Impact of pH and feeding system on black
soldier ﬂy (Hermetia illucens, L; Diptera: Stratiomyidae) larval development.
PLoS One 2018;13(8):e0202591.
[48] Ma J, Lei Y, Ku Rehman, Yu Z, Zhang J, Li W, Li Q, Tomberlin JK, Zheng L. Dynamic
Effects of Initial pH of Substrate on Biological Growth and Metamorphosis of
Black Soldier Fly (Diptera: Stratiomyidae). Environ Entomol 2018;47(1):159–65.
[49] Ruhnke I, Normant C, Campbell DLM, Iqbal Z, Lee C, Hinch GN, Roberts J. Impact
of on-range choice feeding with black soldier ﬂy larvae (Hermetia illucens) on
ﬂock performance, egg quality, and range use of free-range laying hens. Anim
Nutr 2018;4(4):452–60.
[50] Yang F, Tomberlin JK. Comparing Selected Life-History Traits of Black Soldier Fly
(Diptera: Stratiomyidae) Larvae Produced in Industrial and Bench-Top-Sized
Containers. J Insect Sci 2020;20(5).
[51] Barragan-Fonseca KB, Dicke M, JJAv Loon. Nutritional value of the black soldier
ﬂy (Hermetia illucens L.) and its suitability as animal feed - a review. J Insects as
Food Feed 2017;3(2):105–20.
[52] Kooienga EM, Baugher C, Currin M, Tomberlin JK, HR Jordan. Effects of Bacterial
Supplementation on Black Soldier Fly Growth and Development at Benchtop
and Industrial Scale. Front Microbiol 2020;11(2907).
[53] Diener S, Lalander C, Zurbr€ugg C, and Vinnera
 s B, Opportunities and constraints
for medium-scale organic waste treatment with ﬂy larvae composting. 2015.
[54] Miranda CD, Cammack JA, Tomberlin JK. Mass Production of the Black Soldier
Fly, Hermetia illucens (L.), (Diptera: Stratiomyidae) Reared on Three Manure
Types. Animals : an open access journal from MDPI 2020;10(7):1243.
[55] Green T. DipTerra LLC, editor. Modular Farming of BSF Scaling Up - Schematic
Overview 2016;2021.
[56] Kenis M, Bouwassi B, Boafo H, Devic E, Han R, Koko G, Kone NG, Maciel G,
Nacambo S, Pomalegni SCB, Roffeis M, Wakeﬁeld M, Zhu F, Fitches E. Small-Scale
Fly Larvae Production for Animal Feed 2018:239–61.
[57] Tham PE, Ng YJ, Vadivelu N, Lim HR, Khoo KS, Chew KW, Show PL. Sustainable
smart photobioreactor for continuous cultivation of microalgae embedded with
Internet of Things. Bioresour Technol 2022;346:126558.
[58] Fisher H and Romano N, Black soldier ﬂy larval production in a stacked production
system. 2020.
[59] Sharma C. "Correcting the IoT History." http://www.chetansharma.com/correct-
ing-the-iot-history/ (accessed 22 July, 2021).
[60] Zhang WE, Sheng QZ, Mahmood A, Tran DH, Zaib M, Hamad SA, Aljubairy A,
Alhazmi AAF, Sagar S, Ma C. The 10 Research Topics in the Internet of Things.
IEEE 6th International Conference on Collaboration and Internet Computing (CIC),
Atlanta,
GA,
USA,
2020;
December
2020.
p.
34–43.
doi:
10.1109/
CIC50333.2020.00015.
[61] Lee I, Lee K. The Internet of Things (IoT): Applications, investments, and chal-
lenges for enterprises. Bus Horiz 2015;58(4):431–40.
[62] Lucero S. IoT platforms: enabling the Internet of Things. IHS Technology 2016
Accessed:
22/7/2021.
[Online].
Available:
https://cdn.ihs.com/www/pdf/
enabling-IOT.pdf.
[63] Rajiv. "What are the major components of Internet of Things." https://www.
rfpage.com/what-are-the-major-components-of-internet-of-things/
(accessed
24 July, 2021).
[64] Gokhale P, Bhat O, Bhat S. Introduction to IOT 2018;5:41–4.
[65] Hao C, Xueqin J, Heng L. A brief introduction to IoT gateway. IET International
Conference on Communication Technology and Application (ICCTA 2011), Beijing,
China, 2011; October 2011. p. 610–3. doi: 10.1049/cp.2011.0740.
[66] Thales. "Bridge the Gap with IoT Gateways." https://www.thalesgroup.com/en/
markets/digital-identity-and-security/iot/inspired/iot-gateway
(accessed
24
July, 2021).
[67] Zhu Q, Wang R, Chen Q, Liu Y, Qin W. IOT Gateway: BridgingWireless Sensor
Networks into Internet of Things. IEEE/IFIP International Conference on Embedded
and Ubiquitous Computing, NW Washington, DC, United States, 2010; December
2010. p. 347–52. doi: 10.1109/EUC.2010.58.
[68] Deuskar P. "Internet of Things—a new world and a huge business opportunity."
https://www.moneycontrol.com/news/trends/expert-columns/internet-of-
things-a-new-world-and-a-huge-business-opportunity-7089921.html
(accessed 24 July, 2021).
[69] Botta A, de Donato W, Persico V, Pescape A. Integration of Cloud computing and
Internet of Things: A survey. Future Gener Comput Syst 2016;56:684–700.
[70] Aazam M, Khan I, Alsaffar AA, Huh E. Cloud of Things: Integrating Internet of
Things and cloud computing and the issues involved. In: Proceedings of 2014
11th International Bhurban Conference on Applied Sciences & Technology (IBCAST),
Islamabad,
Pakistan,
2014;
January
2014.
p.
414–9.
doi:
10.1109/
IBCAST.2014.6778179.
[71] Elazhary H. Internet of Things (IoT), mobile cloud, cloudlet, mobile IoT, IoT cloud,
fog, mobile edge, and edge emerging computing paradigms: Disambiguation
and research directions. J Netw Comput Appl 2019;128:105–40.
[72] Queensland B. "Beneﬁts of cloud computing." https://www.business.qld.gov.au/
running-business/it/cloud-computing/beneﬁts (accessed 24 July, 2021).
[73] Wigmore I. "IoT analytics (Internet of Things analytics)." https://whatis.techtar-
get.com/deﬁnition/IoT-analytics-Internet-of-Things-analytics (accessed 26 July,
2021).
[74] Leverege. "Introduction to UIs and UX in IoT." https://www.leverege.com/iot-e-
book/ui-and-ux-design-iot (accessed 26 July, 2021).
[75] Maiman M. "How the User Interface on IoT Hardware Can Make or Break the
User’s Experience." https://www.electronicdesign.com/technologies/iot/article/
21808679/how-the-user-interface-on-iot-hardware-can-make-or-break-the-
users-experience (accessed 26 July, 2021).
[76] Sciforce. "Smart Farming: The Future of Agriculture." https://www.iotforall.com/
smart-farming-future-of-agriculture (accessed 5 August, 2021).
[77] Bernstein C. "smart farming." https://internetofthingsagenda.techtarget.com/
deﬁnition/smart-farming (accessed 5 August 2021).
[78] Zhu J, Yao Y, Li D, Gao F. Monitoring big process data of industrial plants with
multiple operating modes based on Hadoop. J Taiwan Inst Chem Eng
2018;91:10–21.
[79] McBratney A, Whelan B, Ancev T, Bouma J. Future Directions of Precision Agri-
culture. Precis Agric 2005;6(1):7–23.
[80] Walter A, Finger R, Huber R, Buchmann N. Opinion: Smart farming is key to
developing sustainable agriculture. Proc Natl Acad Sci U.S.A 2017;114(24):6148.
[81] Schulze ED, Luyssaert S, Ciais P, Freibauer A, Janssens IA, Soussana JF, Smith P,
Grace J, Levin I, Thiruchittampalam B, Heimann M, Dolman AJ, Valentini R, Bous-
quet P, Peylin P, Peters W, R€odenbeck C, Etiope G, Vuichard N, Wattenbach M,
Nabuurs GJ, Poussi Z, Nieschulze J, Gash JH, the CarboEurope T. Importance of
methane and nitrous oxide for Europe's terrestrial greenhouse-gas balance. Nat
Geosci 2009;2(12):842–50.
[82] s Ahirwar, S Swarnkar, Srinivas B, Namwade G. Application of Drone in Agricul-
ture. Int J Curr Microbiol Appl Sci 2019;8:2500–5.
[83] Meola A. "Smart Farming in 2020: How IoT sensors are creating a more efﬁcient
precision agriculture industry." https://www.businessinsider.com/smart-farm-
ing-iot-agriculture (accessed 5 August, 2021).
[84] Dutta J, Dutta J, Gogoi S. Smart farming: An opportunity for efﬁcient monitoring
and detection of pests and diseases. J Entomol Zool Stud 2020;8:2352–9.
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235
11

[85] Aspire
Food
Group.
"Technology."
https://aspirefg.com/technology.aspx
(accessed 7 August, 2021).
[86] Ada L. "DHT11, DHT22 and AM2302 Sensors." https://learn.adafruit.com/dht
(accessed 7 August, 2021).
[87] Components 101. "NodeMCU ESP8266." https://components101.com/develop-
ment-boards/nodemcu-esp8266-pinout-features-and-datasheet
(accessed
7
August, 2021).
[88] Ryu M, Yun J, Miao T, Ahn I, Choi S, Kim J. Design and implementation of a con-
nected farm for smart farming system. IEEE SENSORS, Busan, Korea (South),
2015; November 2015. p. 1–4. doi: 10.1109/ICSENS.2015.7370624.
[89] Swetina J, Lu G, Jacobs P, Ennesser F, Song J. Toward a standardized common
M2M service layer platform: Introduction to oneM2M. IEEE Wirel Commun
2014;21(3):20–6.
[90] Ray B. "The ZigBee Vs WiFi Battle For M2M Communication." https://www.link-
labs.com/blog/zigbee-vs-wiﬁ-802-11ah (accessed 8 August, 2021).
[91] Wu J, Alam MA, Pan Y, Huang D, Wang Z, Wang T. Enhanced extraction of lipids
from microalgae with eco-friendly mixture of methanol and ethyl acetate for
biodiesel production. J Taiwan Inst Chem Eng 2017;71:323–9.
[92] Ravi HK, Vian MA, Tao Y, Degrou A, Costil J, Trespeuch C, Chemat F. Alternative
solvents for lipid extraction and their effect on protein quality in black soldier
ﬂy (Hermetia illucens) larvae. J Clean Prod 2019;238:117861.
[93] Caligiani A, Marseglia A, Leni G, Baldassarre S, Maistrello L, Dossena A, Sforza S.
Composition of black soldier ﬂy prepupae and systematic approaches for extrac-
tion and fractionation of proteins, lipids and chitin. Food Res Int 2018;105:812–
20.
[94] Yi L, Lakemond CMM, Sagis LMC, Eisner-Schadler V, van Huis A, van Boekel
MAJS. Extraction and characterisation of protein fractions from ﬁve insect spe-
cies. Food Chem 2013;141(4):3341–8.
[95] Choi BD, Wong NAK, Auh J-H. Defatting and Sonication Enhances Protein Extrac-
tion from Edible Insects. Korean J Food Sci Anim Resour 2017;37(6):955–61.
[96] Rosa R, Spinelli R, Neri P, Pini M, Barbi S, Montorsi M, Maistrello L, Marseglia A,
Caligiani A, Ferrari AM. Life Cycle Assessment of Chemical vs Enzymatic-Assisted
Extraction of Proteins from Black Soldier Fly Prepupae for the Preparation of Bio-
materials for Potential Agricultural Use. ACS Sustain Chem Eng 2020;8
(39):14752–64.
[97] Lin Y-S, Liang S-H, Lai W-L, Lee J-X, Wang Y-P, Liu Y-T, Wang S-H, Lee M-H. Sus-
tainable Extraction of Chitin from Spent Pupal Shell of Black Soldier Fly. Pro-
cesses 2021;9(6):976.
[98] Bedian L, Villalba-Rodríguez AM, Hernandez-Vargas G, Parra-Saldivar R, Iqbal
HMN. Bio-based materials with novel characteristics for tissue engineering
applications  A review. Int J Biol Macromol 2017;98:837–46.
[99] El Hadrami A, Adam LR, El Hadrami I, Daayf F. Chitosan in Plant Protection. Mar
Drugs 2010;8(4).
[100] Shahidi F, Arachchi JKV, Jeon Y-J. Food applications of chitin and chitosans.
Trends Food Sci Technol 1999;10(2):37–51.
[101] Jeffryes C, Agathos SN, Rorrer G. Biogenic nanomaterials from photosynthetic
microorganisms. Curr Opin Biotechnol 2015;33:23–31.
[102] Jayakumar R, Prabaharan M, Nair SV, Tamura H. Novel chitin and chitosan nano-
ﬁbers in biomedical applications. Biotechnol Adv 2010;28(1):142–50.
[103] Soetemans L, Uyttebroek M, Bastiaens L. Characteristics of chitin extracted from
black soldier ﬂy in different life stages. Int J Biol Macromol 2020;165:3206–14.
[104] Sagheer FAA, Al-Sughayer MA, Muslim S, MZ Elsabee. Extraction and characteri-
zation of chitin and chitosan from marine sources in Arabian Gulf. Carbohydr
Polym 2009;77(2):410–9.
[105] Franco A, Scieuzo C, Salvia R, Petrone AM, TaﬁE, Moretta A, Schmitt E, Falabella
P. Lipids from Hermetia illucens, an Innovative and Sustainable Source. Sustain-
ability 2021;13(18):10198.
[106] Nguyen HC, Liang S-H, Li S-Y, Su C-H, Chien C-C, Chen Y-J, DTM Huong. Direct
transesteriﬁcation of black soldier ﬂy larvae (Hermetia illucens) for biodiesel
production. J Taiwan Inst Chem Eng 2018;85:165–9.
[107] Insectta. "Biomaterials." https://www.insectta.com/biomaterials (accessed 27
August, 2021).
[108] Khan N, Ray RL, Sargani GR, Ihtisham M, Khayyam M, Ismail S. Current Progress
and Future Prospects of Agriculture Technology: Gateway to Sustainable Agri-
culture. Sustainability 2021;13(9):4883.
[109] Beskin KV, Holcomb CD, Cammack JA, Crippen TL, Knap AH, Sweet ST, Tomberlin
JK. Larval digestion of different manure types by the black soldier ﬂy (Diptera:
Stratiomyidae)
impacts
associated
volatile
emissions.
Waste
Manage
2018;74:213–20.
[110] Erickson MC, Islam M, Sheppard C, Liao J, MP Doyle. Reduction of Escherichia coli
O157:H7 and Salmonella enterica Serovar Enteritidis in Chicken Manure by Lar-
vae of the Black Soldier Fly. J Food Prot 2004;67(4):685–90.
[111] Surendra KC, Tomberlin JK, van Huis A, Cammack JA, Heckmann L-HL, Khanal SK.
Rethinking organic wastes bioconversion: Evaluating the potential of the black
soldier ﬂy (Hermetia illucens (L.)) (Diptera: Stratiomyidae) (BSF). Waste Manage
2020;117:58–80.
[112] Diener S, Studt Solano NM, Roa Gutierrez F, Zurbr€ugg C, Tockner K. Biological
Treatment of Municipal Organic Waste using Black Soldier Fly Larvae. Waste
Biomass Valorization 2011;2(4):357–63.
[113] FAO, E-Agriculture Strategy Guide: Piloted in Asia-Paciﬁc Countries: Food and Agri-
culture Organization of the United Nations, International Telecommunication
Union, 2016, p. 222. [Online]. Available: http://www.fao.org/3/i5564e/i5564e.
pdf.
[114] Bacco M, Berton A, Ferro E, Gennaro C, Gotta A, Matteoli S, Paonessa F, Ruggeri M,
Virone G, Zanella A. Smart farming: Opportunities, challenges and technology ena-
blers. IoT Vertical and Topical Summit on Agriculture - Tuscany (IOT Tuscany), Tus-
cany, Italy, 2018; May 2018. p. 1–6. doi: 10.1109/IOT-TUSCANY.2018.8373043.
[115] Charo RA. Yellow lights for emerging technologies. Science 2015;349(6246):384.
[116] Kutter T, Tiemann S, Siebert R, Fountas S. The role of communication and co-
operation in the adoption of precision farming. Precis Agric 2011;12(1):2–17.
[117] Hoeren T and Kolany-Raiser B, Big Data in Context: Legal, Social and Technological
Insights. 2018.
[118] Cyberterrorism Weimann G. The Sum of All Fears? Stud ConﬂTerror, 28; 2005. p.
2005129–49.
[119] Barreto L, Amaral A. Smart Farming: Cyber Security Challenges. International
Conference on Intelligent Systems (IS), Funchal, Portugal, 2018; September 2018.
p. 870–6. doi: 10.1109/IS.2018.8710531.
[120] Elmaghraby AS, Losavio MM. Cyber security challenges in Smart Cities: Safety,
security and privacy. J Adv Res 2014;5(4):491–7.
[121] Gupta M, Abdelsalam M, Khorsandroo S, Mittal S. Security and Privacy in Smart
Farming: Challenges and Opportunities. IEEE Access 2020;8:34564–84.
[122] Schreier F. On Cyberwarfare. 2012;(DCAF Horizon Working Paper): pp. 1-133.
[123] Chae C-J and Cho H-J. Enhanced secure device authentication algorithm in P2P-
based smart farm system. Peer-to-Peer Netw Appl 2018; 11(6): 1230-1239.
[124] Aldaco R, Hoehn D, Laso J, Margallo M, Ruiz-Salmon J, Cristobal J, Kahhat R, Villa-
nueva-Rey P, Bala A, Batlle-Bayer L, Fullana-i-Palmer P, Irabien A, Vazquez-Rowe
I. Food waste management during the COVID-19 outbreak: a holistic climate,
economic and nutritional approach. Sci Total Environ 2020;742:140524.
12
J.C.F. Van et al. / Journal of the Taiwan Institute of Chemical Engineers 137 (2022) 104235