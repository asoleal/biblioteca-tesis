Computers and Electrical Engineering 113 (2024) 109052
Available online 18 December 2023
0045-7906/© 2023 Elsevier Ltd. All rights reserved.
Studies on energy efficient techniques for agricultural monitoring 
by wireless sensor networks 
Kapil Aggarwal a,*, G. Sreenivasula Reddy b, Ramesh Makala c, T. Srihari d, 
Neetu Sharma e, Charanjeet Singh f 
a Department of Computer Science & Engineering, Koneru Lakshmaiah Education Foundation, Vaddeswaram, Guntur, Andhra Pradesh 522302, 
India 
b Department of Computer Science and Engineering, Chaitanya Bharathi Institute of Technology, Proddatur, India 
c Computer Science and Engineering, Hindu College of Engineering and Technology, Guntur, Andhra Pradesh, India 
d Department of Electrical and Electronic Engineering, Saveetha School of Engineering, Saveetha Institute of Medical and Technical Sciences 
(SIMATS), Saveetha Universit, Chennai, Tamil Nadu, India 
e Department of Computer Science and Engineering, Galgotias University Greater Noida, Uttar Pradesh, India 
f Electronics and Communication Department, Deenbandhu Chhotu Ram University of Science and Technology, Murthal, Sonipat, Haryana, India   
A R T I C L E I N F O  
Keywords: 
IoT 
Healthcare 
Agriculture 
Wireless sensor networks 
Artificial Intelligence 
Wireless biomedical sensors 
A B S T R A C T  
Wireless Sensor Networks (WSN) are pivotal for real-time monitoring in diverse sectors through 
the Internet of Things (IoT). However, current wireless communication protocols face challenges 
in integrating Precision Agriculture (PA) management systems with Artificial Intelligence (AI). PA 
optimizes nutrient supply and pesticide use, enhancing crop yield and product quality. Despite 
these advantages, structural changes in WSNs, including deployment, coverage, scalability, and 
energy consumption, hinder their potential. This paper conducts a comparative study of WSNs in 
agriculture, focusing on wireless protocols, energy harvesting, and efficiency procedures. The 
research delves into challenges faced by WSNs in agriculture, emphasizing the need for power- 
saving agricultural management strategies to ensure sustained, effective long-term monitoring. 
The study addresses integration issues, explores agricultural benefits, and proposes solutions to 
enhance WSN performance in dynamic field environments.   
1. Introduction 
Owing to the advancements in computer networking and wireless communication technology, wireless sensor networks (WSNs) are 
one of the fastest growing technologies today. WSNs have potential applications in a wide range of industries, including health care, 
surveillance, safety, border control, environmental monitoring, etc. This has piqued the interests of a lot of people in these networks. 
WSNs can detect and keep an eye on the environment around them- thanks to the employment of autonomous low-energy sensors! 
Each sensor normally consists of a power unit, a microprocessor, a device for wireless communication, and a variety of environmental 
sensors (i.e. units for sensing temperature, pressure and humidity). 
WSNs for the internet of things (IoT) may develop even more advanced, integrated infrastructure that can capture and analyse 
massive volumes of data by getting updated with the most current advancements in information and communications technology [1]. 
* Corresponding author. 
E-mail address: kapil594@gmail.com (K. Aggarwal).  
Contents lists available at ScienceDirect 
Computers and Electrical Engineering 
journal homepage: www.elsevier.com/locate/compeleceng 
https://doi.org/10.1016/j.compeleceng.2023.109052 
Received 8 September 2023; Received in revised form 28 November 2023; Accepted 4 December 2023

Computers and Electrical Engineering 113 (2024) 109052
2
WSNs are the building blocks of the IOT. This year, it is predicted that over 50 billion different devices will connect to the network; 
and most of these devices will consist of sensors. WSNs are capable of operating in inhospitable and desolate environments, like war 
zones, highlands, deserts, etc., where the deployment of sensors and the manual monitoring of networks is either dangerous or 
impossible. 
However, this form of deployment results in higher pricing and maybe a higher overall consumption of energy throughout the 
network as compared to manual deployment. That is because it is necessary to set up a significant number of sensor nodes to make 
efficient use of this technology. 
In addition to having batteries that cannot be swapped out, the sensor nodes’ sensing, processing, and communication capabilities 
are severely limited. Besides, these nodes also do not have removable power sources. In some applications, it is not practical to replace 
sensor nodes if they become inoperable due to environmental conditions or if their batteries run out of power. Yet, the unequal use of 
energy does have an influence on the efficiency with which the sensor performs its function [2]. 
This research does a literature review, focusing on wireless networking challenges with the goal of reducing energy consumption in 
IoT applications. It gives a fundamental grasp of the designs of IoT devices and the topologies of IoT networks and a wide variety of 
applications. It also discusses some possible issues that might limit the lifetime of IoT networks and devices. This study’s objective is to 
find the cost-saving potential of environmentally responsible networking. 
Recent studies have produced a variety of energy-efficient WSN schemes, some of which are precise and hierarchical, but they have 
not investigated how the components are ordered in relation to an energy-efficient IoT. The authors show that this approach is not only 
more agile and successful than the traditional ways used for designing WSNs, but also that it includes an energy efficient IoT. 
In addition, the authors investigate the existing body of research literature for the problems identified therein and the solutions 
proposed thereof. This is done to provide a comprehensive evaluation of the current efforts being made to address the difficulties 
associated with energy conservation in limited-resource IoT devices [3]. 
United Nations estimated in 2010 that the number of people living on our planet will hit 10 billion by 2050. Consequently, there is a 
consistent and steady rise in the demand for agricultural products. Nevertheless, the depletion of natural resources, the loss of agri­
cultural land, and the occurrence of natural calamities like global warming, salinization, and floods, have raised the food security issue 
to the top of the global priority list. 
In the agricultural sector, during the last several years, new strategies and technical breakthroughs have been adopted with the 
intention of increasing productivity to meet the current demand. The application of large amounts of data to the IoT represents a 
significant new development in this domain. There have been a lot of research done, and a significant amount of attention has been 
placed on investigating, testing, and applying the findings. Cisco anticipates 500 billion plus IoT devices being linked to the web by 
2030 [4]. 
The IoT and big data will make practising intelligent agriculture feasible, and this in turn, would result in an improvement in both 
productivity and efficiency. Over the years, the agricultural sector has made extensive use of WSNs, which has enabled the 
Fig. 1. IoT tools for efficient agriculture.  
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
3
development of smart agriculture via providing the essential infrastructure. The distinct abilities of WSNs, such as their capability to 
self-establish, self-configure, self-organize, and self-recover, would be of use to the field of intelligent agriculture [5]. 
The IoT proliferation has been primarily spurred by the growth of science and technology and the increasing need for new ap­
proaches and instruments to boost agricultural efficiency and productivity. The breakthrough developments in smart agriculture and 
the industry’s unavoidable role as the future of intelligent and sustainable environmental management are the primary reasons 
pushing its acceptance. The IoT tools for efficient agriculture are shown in Fig. 1. 
The IoT makes use of a diverse assortment of items and technologies that are now on the market. These systems are made up of 
components including cloud computing, end-user application software, ad hoc networks, cognitive radio, and WSNs. Smart agriculture 
includes all the mechanical equipment, information, software, services, and decision-making tools. And all work together to support 
farmers in improving their output, product quality, and profitability [6]. 
This paper is organized as follows: Section 2 presents a literature review on agriculture-based Wireless Sensor Networks (WSN). 
Section 3 discusses the IoT layout for intelligent agriculture. In Section 4, we detail an Energy Efficient and Secure IoT-Based WSN 
Framework. The experimental analysis is covered in Section 5, exploring remnant energy attributes, route selection based on Er value, 
and data reduction strategies. Finally, Section 6 concludes the paper, summarizing key findings and their implications for enhancing 
WSN applications in intelligent agriculture. 
2. Review of literature 
WSNs have a wide range of potential applications in day-to-day living including the monitoring of animals, environment, 
healthcare, and other areas. Yet, one of the most significant challenges faced by WSNs is the limitation of available energy. So, pre­
serving energy is essential to the efficient running and continued viability of WSNs. In a network of nodes with varying amounts of 
energy, our objective is to locate energy-aware disjoint dominant sets (DSs) that may act as data collecting nodes in each round of the 
algorithm. For, this will enable the extension of the WSN’s lifetime. 
To accomplish this, a technique of intelligent data collection that consists of two phases was proposed. The first phase is the se­
lection of the collector nodes, and the second phase is the development and collection of the nodes involved in the data-gathering 
route. During the phase of selection of the collector nodes, an energy-aware swarm intelligence technique was employed to 
construct disjoint dominating sets that will act as collector nodes in each round. 
During the second phase, the data gathering paths were selected in such a way that there is optimized efficiency in data collection 
and reduction in energy consumption. The viability of this approach had been shown, both conceptually and practically [7]. 
The IoT has lately attracted a lot of interest because of its many applications, including smart cities, home automation, smart 
healthcare, and transportation, etc. These IoT-based systems make extensive use of WSNs to capture the data that is necessary for smart 
environments. 
Nevertheless, IoT-enabled WSNs have several challenges as a result of the enormous quantity of heterogeneous data produced by 
numerous sensing devices. These challenges include lengthy connection delays, restricted throughput, and limited network lifespan. 
A research study proposed an intelligent routing strategy for IoT–enabled WSNs that makes use of deep reinforcement learning 
(DRL) to reduce network latency and increase its lifetime. The method divides the whole network into many unequal groups depending 
on the data load of the sensor node. As a result, the proposed method significantly reduced the risk of premature network failing. An 
extensive evaluation of the strategy was carried out with the help of ns3. The proposed system’s efficiency with regards to the number 
of live nodes, energy efficiency, delivery of packets, and communication latency in the network were compared with that of existing 
approaches [8]. 
Another study first outlined the physical elements of the sensor nodes. It went on to discuss a transmission model that may be used 
to determine the amount of energy that is lost at the unit for communication. Then, it presented a comprehensive review of the energy- 
efficient algorithms and techniques, with a particular emphasis on Medium Access Control (MAC) routing techniques. 
It also gave a taxonomy consisting of five subcategories, including topology management, duty cycling, data minimization, energy- 
efficient routing, etc. The study investigated the many potential causes of energy loss and offered various interpretations for the 
network’s lifetime. Then, each strategy was analysed in-depth for its energy conserving potential. Thus, the study came up with 
additional subcategories, if any, and presented the causes of energy loss linked with each strategy [9]. 
Another study provided a comprehensive review and analysis of the energy-saving measures applicable to hardware. The focus 
particularly was on several physical-level strategies that could further lessen the energy consumption. A few of these methods are 
energy harvesting, dynamic voltage-frequency scaling, power gating, and wake-up radio receivers. The objective was to decrease the 
amount of electricity used while maintaining an acceptable cost. 
The study investigated the low-power standards that were already in place for WSNs to determine the primary application areas for 
WSNs, the needs of each of those application area, and so on. Next, a new taxonomy, which consists of low-level subdivisions was 
freshly developed. Evaluations and analyses of five major areas including battery depletion, energy-efficient routing, sleep/awake 
schemes, data reduction, and radio-optimization were also done. The authors largely focused their efforts on developing responses that 
satisfied their aim of both reducing the amount of energy used and the satisfying the specific requirements of each application [10]. 
"Smart city" is a term that indicates a group of concepts and pieces of technologies that have been compiled with the intention of 
making cities more efficient, technologically advanced, ecologically sustainable, and socially inclusive. Among these concepts are 
advancements in the areas of technology, economics, and society. The term “smart city” has been used often in the 2000s by a range of 
actors in politics, business, administration, and urban planning to characterize technical improvements and progresses in cities. 
In the beginning of this century, post-industrial countries were confronted with several economic, social, and political issues. As a 
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
4
reaction, digital technology and the concept of smart cities started emerging to address these challenges. The primary focus is on 
tackling difficulties such as a lack of resources, environmental destruction, population growth, demographic shifts, and healthcare 
provisioning that urban society confronts. 
The term also refers, in a broader sense, to non-technical improvements that increase the environmental friendliness of urban life. 
Using sensor networks that are based on healthcare IoT applications has the potential to eliminate inefficiencies present in the current 
infrastructure. 
Since there are loads of data to be handled in an intelligent manner, an approach known as machine learning is needed for the 
successful deployment of IoT-powered WSNs. A study discussed the use of AI-enabled IoT and WSNs in the medical field. It intended to 
serve as a basis for future research initiatives aiming to understand the role played by IoT in smart cities, specifically in the healthcare 
sector [11]. 
The agricultural industry that already has access to cutting-edge technologies for various types of information systems to facilitate 
efficient farming, is a strong candidate for the implementation of smart farming. To farm successfully, farmers need the right soil, 
climate, crops, and a whole host of other factors. 
The amount of crop that may be harvested is directly influenced by the kind of the soil in which the plants are grown. Nitrogen (N), 
phosphorus (P), and potassium (K) are the topmost vital nutrients found in soil. Other soil related factors include minor nutrients, 
humidity, temperature, and pH level. Besides, every organism on the farm is essential in some way to the process of crop production. 
The advances in technology enable an intelligent farming. The concept of “smart farming” refers to the use of computers and 
information technology to oversee agricultural operations. The utilization of IoT linked equipment, WSNs, machine learning, deep 
learning, and an agile strategy can transform a conventional farming practice into smart farming. 
A study analysed the challenges that farmers face in farming, including how the condition of the soil may impact the amount of food 
that can be harvested from a crop. It offered an exhaustive literature review on computer-based smart farming. It discussed the 
technologies and techniques used grouped by year. It has a table format that presented not just the findings but also the recom­
mendations for moving forward. In addition, significant gaps in research were also discussed in the paper [12]. 
3. IoT layout for intelligent agriculture 
The authors propose a common base for an IoT ecosystem for intelligent agriculture by using three primary elements: solutions for 
data processing and storage, communication technologies, and IoT devices. These components make an ecosystem for intelligent 
agriculture that the IoT provides.  
v IoT devices 
A typical design for an IoT device includes actuators that can move objects via wired or wireless connections, sensors that collect 
data from the surrounding environment, and an embedded system that includes a central processing unit (CPU), battery power, 
memory, communication modules, and input-output interfaces. To detect and capture environmental data including the temperature, 
Fig. 2. The primary attributes of IoT devices.  
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
5
humidity, and soil nutrients that might influence production, the sensor devices are constructed to function in open areas, nature, soil, 
water, and air. 
These hardware components of intelligent agricultural systems need to possess several special attributes including the capacity to 
endure the impacts of temperature, humidity, and weather instability during their service lives. Agricultural practises falling under the 
category of “smart farming” are those that are often carried out on huge tracts of land. Devices that are part of the IoT are well-suited 
for usage in intelligent agriculture solutions due to the IoT’s primary characteristics, which are shown in Fig. 2 [13]. 
Depending on the nature of the specific task at hand, the sophisticated agricultural sector makes use of a wide variety of standard 
sensors. The most fundamental sensors used are air flow sensors, optical sensors, location sensors, electrochemical sensors, and me­
chanical sensors. These sensors can monitor different environmental factors like solar radiation, wind direction, barometric pressure, 
air temperature, soil moisture, leaf moisture, soil temperature, wind speed, air humidity, precipitation, and many more.  
v Communication technology 
For the IoT technology to be included into the smart agriculture business, IoT devices must continue to advance, suggests recent 
research on IoT communication technologies. That is because these are necessary for the development of infrastructure for IoT 
communications. Protocol, spectrum, and topology are the three categories of communication solutions that are now accessible to 
users. 
The components that make up a smart agricultural system can share information, interact with one another, and make decisions 
depending on the protocols that are in place. As a result, the system can monitor and regulate the agricultural environment, and 
improve production efficiency, and increase yields. The common low-power communication technologies employed in intelligent 
agriculture are classified into short-range and long-range communication methods. What differentiates the two categories is the 
distance that the transmitted information must travel [14]. 
Short-range technologies include things like near field communication (NFMI- Near-Field Magnetic Induction), radio frequency 
identification (RFI), Bluetooth, ZigBee, and terahertz (Z-Wave). As it is seen in Table 1, the transmission range of short-range 
communication technologies is less than 20 metres. 
These technologies have a low data transfer rate and excel in optimising their energy efficiency. Also, these technologies have a low 
data transfer rate. Although the transmission range of long-range communication techniques can be up to many tens of kilometres, 
these use more energy, and are intended for backhaul device-to-device connections. These approaches are frequently used in sensor 
networks. 
Spectrum: Different radio instruments rely on specific frequency bands for communicating with one another. The Federal Com­
munications Commission (FCC) has created unlicensed spectrum bands to accommodate operations in the domains of research, 
business, and medicine. 
Applications that need minimal power and operate at a close range often make use of these spectrum bands. Consequently, several 
technologies that are widely used in the smart agricultural industry make use of unlicensed spectrum bands. Examples of technologies 
include unmanned aerial vehicles, wireless control of machinery, and various forms of wireless and wired communication such as 
Bluetooth and Wi-Fi. 
Nonetheless, there are a few downsides associated with the use of unlicensed spectrum. The most significant ones are poor service 
quality, high initial expenses for infrastructural establishment, and interference caused by the increasing number of devices connected 
to the IoT. 
Mobile network companies often have access to licensed airwaves. It makes the network more reliable, boosts service quality, 
provides security, provides wide coverage, and reduces the upfront expenses of infrastructure for clients. In addition, it results in a 
more productive traffic on the network. Two factors that have contributed to the restricted use of authorized frequency bands are the 
Table 1 
Common communication methods for intelligent agriculture.  
Type 
Spectrum 
Transmission Distance 
Type of Network 
“802.11a/b/g/n/ac” 
Unapproved 
95 m 
WLAN 
“802.11ah” 
Unapproved 
1020 m 
WLAN 
“802.11p” 
Approved 
1.2 km 
WLAN 
“802.11af” 
Approved 
1.3 km 
WLAN 
“Sigfox” 
Approved 
Rural: 50 km 
LPWA   
Urban:10 km  
“Lora WAN” 
Approved 
25 km 
LPWA 
“NB-IoT” 
Approved 
40 km 
LPWA 
“LTE-3GPP” 
Approved 
4 km 
WWAN 
“EC-GPRS” 
Approved 
5 m 
WWAN 
“WiMAX” 
Hybrid 
51–80 km 
WWAN 
“Bluetooth” 
Unapproved 
100 m 
WPAN 
“ZigBee” 
Unapproved 
1 km 
WHAN 
“Z-Wave” 
Unapproved 
110 m 
WHAN 
6LoWPAN 
Unapproved 
35 m 
WHAN 
NFC 
Unapproved 
25cm 
D2D  
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
6
Table 2 
A description of the uses of WSNs for widespread healthcare monitoring.  
Category 
Name 
Hard ware design 
Software design 
GUI design 
Sensing modality 
Routing 
Obtrusive 
Context aware 
Machine learning 
Loc. track. 
RFID use 
Activity monitoring 
AICO 
Yes 
Yes 
Yes 
Multi. 
Single 
Low 
High 
Yes 
yes 
Passive  
Caregiver’s Ast. 
No 
Yes 
Yes 
Single 
Single 
Low 
Medium 
No 
No 
Passive 
At-home Healthcare 
ITALH 
Yes 
No 
Yes 
Multi. 
Single 
High 
Medium 
Yes 
GPS 
No  
HipGuard 
Yes 
No 
No 
Multi. 
Single 
High 
High 
No 
No 
No 
Physiological monitoring 
CodeBlue 
Yes 
Yes 
Yes 
Multi. 
Multi. 
High 
High 
No 
RF 
No  
MEDiSN 
Yes 
Yes 
Yes 
Multi. 
Multi. 
High 
High 
No 
RF 
No  
PATHS [ 
Yes 
No 
Yes 
Multi. 
Single 
High 
Low 
No 
No 
No  
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
7
low energy efficiency of devices connected to the IoT and the high cost of data transmission.  
v IoT applications 
3.1. Agriculture 
The IoT is used by smart farms to monitor the condition of soil, cultivate healthy crops, and eliminate weeds. Sensors connected to 
the IoT may be used to aid in the collection of crucial data on temperature, acidity, nutrients, and moisture content of the soil. When 
this information is taken into consideration, irrigation and ensuring soil fertility may be properly regulated. The IoT also makes it 
easier for farmers to make educated choices on when to sow seeds, how to diagnose plant diseases, and what kind of fertiliser to use 
[15]. 
3.2. Health care 
Wearable technology and sensors allow medical professionals to monitor their patients more closely. The IoT may be used to set up 
continuous monitoring of crucial metrics. The installation of smart beds might potentially shorten the time duration that patients have 
to wait for to access available hospital beds. Sensors connected to the IoT might potentially be used to monitor and manage the repair, 
maintenance, and malfunction of medical devices. The use of IoT technology also results in a more pleasant treatment for older pa­
tients. Besides, the real-time patient monitoring enabled by the IoT sensors makes it possible to determine whether a patient’s con­
dition is getting better or remaining the same [16]. 
3.3. Industry 
The industrial IoT was a contributory factor to industrial revolution in the beginning of its fourth wave. Sensors enabled by the IoT 
have the potential to lengthen the usable period of machinery. And the IoT in industry makes it possible to ensure a greater level of 
availability and reliability. So, factories are increasingly adopting computerised management systems for maintaining and managing 
enterprise assets for including IoT applications to their resource and maintenance management. 
Industrial IoT applications enable the best possible state of machine health via the use of predictive maintenance. These appli­
cations also reduce costs associated with the implementation of condition-based maintenance in commercial and industrial settings 
[17]. 
4. Research methodology  
v Healthcare 
WSNs are successfully used in many general health monitoring prototypes and commercial applications, including those for 
monitoring the health of children, the elderly, and individuals who suffer from chronic conditions. A few of the most common forms of 
health applications are location tracking, medical condition monitoring, drug use monitoring, activity monitoring, etc. Table 2 shows a 
summary of the WSN apps that are current used and also presents some prospective ideas. 
Wireless Body Area Networks (WBANs), are one-of-a-kind wireless technologies, used in many medical environments. WBANs 
monitor the patient’s physical condition, and then, use connectivity to convey their findings to either the patient themselves or to 
medical specialists. WBANs are often used for the purpose of monitoring physiological variables such as the user’s heart rate, levels of 
stress, levels of oxygen, body temperature, and levels of blood sugar. 
Diabetes may lead to a variety of serious health complications such as blindness, high blood pressure, kidney failure, amputations, 
stroke, heart disease, etc. The use of wireless biomedical sensors (WBS) for glucose level monitoring could be an example of a more 
proactive, reliable, and accurate approach to diabetes treatment. 
The biosensor subgroups can also serve as valuable elements in a variety of circumstances, including medical business, competi­
tiveness of sports events, and other fields of endeavour. The rapid development of wearable biosensors has resulted in numerous 
advantages, including accessibility, user-friendliness, and a provision for reliable information in real time for satisfying all the pre­
requisites of clinical practise. 
Wearable biosensors use wireless sensors and are found in a wide variety of wearable products such as bandages, bracelets, etc. The 
information obtained using these technologies is analysed for identifying trends suggesting that a patient’s clinical status will worsen, 
and is sent to the concerned patient or clinicians over a wireless network. 
Using PA with sensors, actuators, processors, wireless transceivers, and other information technologies, site-specific management 
can be computerised for automated agriculture. Precision in the agricultural sector has increased as a direct result of research into 
wireless protocols designed specifically for use in agricultural applications. 
It is widely agreed that precision irrigation improves irrigation accuracy because of its capability to control both the appropriate 
amount of water and the duration for which it should be applied. Studies have shown that precision irrigation systems use 90 % (based 
on Bluetooth), 33 % (based on ZigBee), 90 % (based on ZigBee), and 50 % (based on Bluetooth) less water than conventional irrigation 
systems. This is shown in Fig. 3. The power demands of a number of wireless technologies and their respective communication ranges 
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
8
are shown in Table 3. 
Using the ZigBee wireless protocol, researchers were able to monitor several kinds of animal behaviour like walking, grazing, 
standing, laying down, sitting, and more. The researchers hypothesise that grazing and laying down will result in an improvement in 
performance that is approximately 83.5 % higher than that of earlier experiments. 
Another study that used an algorithm based on the ZigBee wireless protocol found that the accuracy rate in monitoring honeybees 
as well as agricultural and environmental aspects was 95.4 %. The strategy recommended to track honeybee had forecasted that the 
algorithm would need this level of precision to monitor honeybees along with agricultural and environmental indicators. 
The ZigBee-based irrigation system automation resulted in system cost reductions ranging from 1.24 % to 6.72 % lower than the 
overall cost of the water user groups. These cost reductions were a direct consequence of using the system. A 2.05 to 8.21 % reduction 
in the amount of energy consumed, and 0.71 to 6.46 % reduction in the quantity of water used was necessary to achieve this. The model 
included support for three distinct types of irrigation systems and operated on a platform designed specifically for mobile devices 
[based on Bluetooth and Global System for Mobile (GSM) technologies]. 
The efficiency factors for subterranean drip types was increased by 90 percent to account for drift and evaporation occurring before 
the water droplets reached the ground. The efficiency factors for both high-pressure and low-pressure varieties of overhead sprinklers 
saw increases of 85 % and 75 %, respectively, over their previous versions. 
To keep an eye on the grapes in Northwest Spain, Libelium used 3 G technology that was based on wireless sensor devices man­
ufactured by Waspmote. The growth yields climbed by 15 % while phytosanitary treatments such as fungicides and fertilisers saw a 20 
% decline. It was believed that agricultural conditions were being monitored with the help of the Long Rage (LoRa) wireless protocol, 
which has a power consumption efficiency of 90 %. The implementation of the Sigfox wireless protocol led to a thirty percent reduction 
in the amount of money spent on pumping water for precise irrigation system in the green regions. 
4.1. Network assumptions 
The proposed Energy Efficient and Secure Internet of Things-Based Wireless Sensor Network Framework for Intelligent Agriculture, 
makes the following network assumptions:  
i. There are N agricultural sensors dispersed evenly over the observation square.  
ii. The installation of the nodes does not affect the functionality of any of the agricultural sensors or base stations.  
iii. There is an evidence of the presence of symmetric transmission connections.  
iv. Agricultural sensors draw their power from a variety of energy sources.  
v. Base Station (BS) is the owner of the most powerful node in the network, which has an infinite supply of resources.  
vi. The Global Positioning System (GPS) is employed for precisely locating agricultural sensors. 
4.2. Energy and link efficient routing 
In this section, the authors talk about the architecture of the recommended energy-and-link efficient channelling, which is made up 
of two major layers. These layers are stacked one upon the other. At the first level, choosing the best cluster heads (CHs) is based on an 
outcome function that considers many factors. After that, the nodes that use the least amount of energy are clustered together into 
Fig. 3. Wireless technologies in terms of their communication distance and power consumption.  
Table 3 
The power demands of a number of wireless technologies and their respective communication ranges.  
Name 
BLE 
ZigBee 
LoRa 
Classic BT 
SigFox 
LTE 
GPRS 
Wi-Fi 
Power consumption 
9 
37.7 
100 
150 
280 
400 
590 
845 
Communication distance 
9 
99 
4500 
10,000 
60 
4800 
10,000 
93  
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
9
numerous groups. 
The second stage in the recommended energy-and-link-efficient routing involves strengthening the stability of the routing channel 
over a longer time duration. This decreases the likelihood of wireless connections behaving in an abnormal manner when cluster heads 
interact with their BS. 
As stated in Eq. (1), for choosing cluster heads, multiple criteria including the BS; signal-to-noise ratio (SNR), SNRi; node energy, ei; 
and distance to BS, di, are used by the proposed framework as a decision-making function f (n). The proposed methodology includes 
the use of SNR to evaluate the signal strength for successfully improving delivery performance. 
SNR refers to the ratio of the Received Signal Strength Indicator (RSSI) to the setting noise (I). Assuming that RSSIi is the signal 
strength indicator obtained, and Bni is the link, the assessment of SNRi may be calculated by dividing RSSIi by Bni. The connection that 
displays the lowest SNRi value is chosen for data transfer. 
f(n) = ei +
(
1
/
di,BS
)
+ (1 / SNRi)
(1) 
The value of f (n) is normalized in the range of [0...1] using 1 −
f (n). 
With the architecture that has been proposed, BS makes use of a worldwide database to maintain info on agricultural sensors. The 
SNR, the node’s location, the residual energy, and the distance from the BS comprise the hop info. BS performs an evaluation of f(n) 
and generates a normalised score by using the stored data. 
Following that, BS will choose the sensor node with the highest score in the agricultural sector to serve as the primary cluster head. 
Consequently, depending on the value of f, BS maps the entries to the nodes that are picked to serve as cluster heads (n). The remaining 
nodes, which do not have the role of cluster heads, are called normal nodes. After that, BS will update the global database by making its 
members contain the one-hop nodes that originate from every cluster head. 
All the agricultural sensors included in the proposed design gather the required information and send it to their respective cluster 
heads. A single-hop approach is then used to transmit the data from the cluster heads to the BS, which is linked to the internet. BS is also 
the location from where end users may get information on agricultural land for evaluation. 
4.3. Data transmission to BS from agriculture sensors in a secure manner 
According to the suggested design, the data is sent from the farm sensors to the cluster heads, and then, on to the BS via a safe and 
dependable network. For the scope of this discussion, the BS generates secret keys by iteratively solving the linear congruential Eq. (2). 
Yn+1 = (αYn + β)modm
(2) 
Yi are the hidden random values generated for the sensor node ni, m is the modulus parameter (which should be higher than 0), …. 
is the multiplier parameter (which should also be higher than zero and lower than the modulus m), …. is the increment parameter 
(which should also be higher than zero and lower than the modulus m), and Y0 is the seed value. 
All of these parameters must be less than the modulus m. Eq. (2) is used to provide the top-secret keys to all the sensor nodes. After 
that, Eq. (3) is used to encrypt the data transferred by the sensor node ni to the cluster head CHj. Encryption is done to make the data 
unreadable for unauthorised parties. 
Ej(mi) = mi ⊕Yi
(3) 
Yi are the top-secret random values generated for node ni of the sensor network, where m is the modulus parameter (which should 
be higher than 0), …. is the multiplier parameter (which should also be higher than zero and lower than the modulus m), …. is the 
increment parameter (which should also be higher than zero and lower than the modulus m), and Y0 is the seed value. Thus, Eq. (2) is 
used to provide the secret keys to all the sensor nodes. Eq. (4) is then used to encrypt the data sent to the cluster head CHj from the 
sensor node ni. 
Dj(mi) = Ej(mi) ⊕Yi
(4) 
Table 4 
The simulation parameters.  
Parameter 
Value 
Simulation area 
200 m x 200m 
Deployment 
Random 
Sensor nodes 
100 
Malicious nodes 
15 
Packet size, k 
64 bits 
Energy level 
2j to 4j 
Payload size 
256 bytes 
MAC layer 
IEEE 802.11b 
Control message 
25 bits 
Transmission range 
20m 
Simulation rounds 
0 to 1000 
Traffic flows 
CBR 
Simulation tool 
NS2.35  
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
10
5. Experimental setup and results 
The default simulation settings utilized in the experimental comparison of the suggested approach with the existing approaches 
viz., Particle Swarm Optimization based Energy efficient Cluster Head Selection algorithm (PSO-ECHS) and energy efficient centroid- 
based routing protocol (EECRP), is presented in this section. A popular, open-source simulation program called Network Simulator2 
(NS2), which is used for examining network routing and communication, is used to carry out the simulation tests. 
The outcomes of the simulation are assessed for varied numbers of rounds. A single simulation round lasts for 20 s. In addition, 
there are 100 farm sensors and 15 anonymous nodes. All of the agricultural sensors are dispersed at random. These include the 
anonymous nodes and the sensors used for capturing temperature, light, soil moisture, position, and airflow. 
100 agricultural sensors are now available. There will always be 15 malicious nodes. The payload size (256 bytes) and packet size 
(k) are both set to 64 bits. Agriculture sensors have a non-uniform residual energy range of 2j to 4j. Constant Bit Rate (CBR) data flow is 
used between the sensor nodes, and the transmission range for these is set at 20 m. These simulation parameters along with their 
respective values are given in Table 4. 
The average execution times consumed by each of the four techniques for encrypting and decrypting data was measured on an 
Atmel ATmega 128 L, and are given in milliseconds. For determining the duration taken for different tasks, the authors used the MICAz 
(Atmel ATmega 128 L) mote and Microchip Studio. Five iterations of each scenario was performed, with each iteration duplicating the 
primary criterion sets of the encryption function, encryption key schedule, decryption function, and decryption key schedule. 
Camellia has the longest running duration across all message loads for both graphs, while RECTANGLE has the lowest running 
duration across all message loads. RECTANGLE has a higher performance level while executing software. That is because it makes use 
of the bit-slice method, which is a helpful technique for implementing software. 
It is notable that the running duration for encryption and decryption operations using RECTANGLE and Fantomas are comparable 
for all payloads. That is because both algorithms use the S-Box of Fantomas’ method, which is also executed in a bit slice form. 
Fantom’s internal LS-design earned it the position of being in second place for running duration. After every six rounds, the 
Camellia cypher includes an extra round for logical operations and key whitening processes, while AES only requires one and a half 
rounds for encryption and decryption. 
Encryption Throughput (MICAz) = NB
Te
(5)  
Decryption Throughput (MICAz) = NB
Td
(6)  
Throughput (Network) = ND∗P
T
(7) 
The amount of time that each of the four methods takes to carry out encryption and decryption operations on an Atmel ATmega 
128 L are recorded. To determine the execution times of the four basic criteria sets viz., the encryption function, encryption key 
schedule, decryption function, and decryption key schedule, the authors performed five repetitions of each scenario utilizing the 
MICAz (Atmel ATmega 128 L) mote and Microchip Studio. 
Each scenario was replicated using the MICAz (Atmel ATmega 128 L) mote. RECTANGLE has the quickest running duration for all 
message loads as seen from the two graphs. And Camellia takes the longest since it uses the bit-slice approach, which is particularly 
suitable for implementations. 
RECTANGLE works better when executing software. As both RECTANGLE and Fantomas employ the S-Box, which is executed in a 
bit slice form, their running duration for encryption and decryption functions are comparable for all payloads. 
In the second place for running duration, stands the Fantom’s internal LS-design. While the Camellia cypher requires an additional 
round after every six rounds for logical operations and key whitening procedures, Advanced Encryption Standard (AES) needs only one 
and a half rounds to encrypt and decode data. 
The throughput statistics spanning across 50 nodes, 256-byte sample enciphered data transmission, and average throughput figures 
based on the number of nodes were generated. The simulations were executed in both a secure (as ciphertext) and insecure (as 
plaintext) manner. The modeller generates cipher text by first reading the plaintext from a text file, and then, converting it. 
I ∗t = Q
(8)  
Q ∗V = E
(9) 
The typical energy use is shown. A multimeter is employed to monitor voltage and amperage to quantify the energy usage over the 
MICAz (Powered by two AA batteries) mote. The following formulae are used to determine the energy used by a certain MICAz. 
In Eq. (4), “I” stands for the current stream, “t” for time, and “Q” for charge. In Eq. (5), Voltage is represented by “V” and energy 
consumption by “E” in Joules. As noticed previously, the running duration and energy use are closely related. 
On the network side, the open-ZB simulation model’s battery may monitor the spent and residual energy levels of nodes. By 
comparing of the bar charts’ heights (over MICAz mote), it is observed that RECTANGLE uses the least quantity of energy than other 
methods for both encryption and decryption processes for all payloads. 
As predicted, Camellia uses more energy, notably after 512 bytes, and peaks at 1024 bytes. This is observed from the operating time 
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
11
graphs, which show the typical amount of energy used while delivering plaintext across a network. It is discovered that up to 256 bytes, 
the energy usage of all nodes significantly increases. Energy usage increases faster for 512-byte data than for 1024-byte data. 
5.1. Energy efficient algorithm 
The remnant energy attributes are used for data aggregation at base stations. This is accomplished in an energy-efficient manner. 
For estimating the remnant energy, the approach makes use of not one but two different criteria- one for the network and the other for 
the route. 
Establish an energy-efficient network G/ 
Initialize EE = 1; 
During the time interval EE, EEA is put in the inactive state 
IF (event) 
Choose the route with the fewest hops and send it back to commence data transmission from S to T at a time interval EE+1 
Put the sensor nodes to sleep EE+1 
END IF 
Wake up the EEA at the scheduled time EE+2 
Send the data obtained to the sink 
At each time interval, check the status of the sensor nodes EE++
IF (Φi< σ1) 
select additional node, then sleep the EEA 
ELSE 
Continue to be awake the EEA 
END IF 
IF finished sending data 
sleep EEA 
END IF 
5.2. Route selection based on Er value at the target node 
The path used by the Ad hoc On-Demand Distance Vector (AODV) approach is determined by the node that represents the 
destination. The destination node, upon receiving a route request, immediately discards the other route requests, and then, sends the 
route replay back to the source. Fig. 4 is a depiction of the strategy that is used in an IoT environment to choose the energy-efficient 
path for the destination node. The proposed approach takes into consideration the amount of energy that is still available in the IoT 
device to enhance energy efficiency. 
The IoT device’s residual energy (Er) is taken into consideration at the route selection step at the destination node. It chooses the 
node that has the highest Er value. Once the Route Replay (RREP) timer is begun, the destination node will transmit an RREP packet as 
a reply to each RREQ packet that has been stored in cache. When the data transfer is complete, every cache entry will be removed. The 
IoT refers to networks that are powered by low-power smart devices. The two most important aspects of an IoT network are the 
installation of appropriate intelligent devices for a given application and the ongoing maintenance of the network. Using resources in 
an effective and economical manner is the primary goal of the IoT network. 
5.3. Energy monitoring of IoT 
Individual buildings may differ substantially from one another, which is why it is essential to pinpoint the “thing” or pattern of 
Fig. 4. Flowchart of Er path.  
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
12
energy-efficiency that is common to all of them. Therefore, as part of our project, the study looked into the fundamental architecture of 
these buildings and thoroughly addressed their building maintenance with some specialists working on it on-site. 
The authors came to the conclusion that the utilization of networking technologies to control or modify an energy strategy is 
significantly less complicated and more straightforward for small commercial and residential constructions. Since it is harder to make 
changes to huge buildings like the one that serves as our testbed, our investigation focuses mostly on very large office complexes. In 
case of more buildings, whether they are of similar or dissimilar type, the system should be adapted and modified based on the findings 
of the testbed [18]. 
5.3.1. System model 
Gaining an understanding of the IoT is harder than understanding WSNs. This is due to the higher level of complexity and a greater 
number of independent components of the former. When it comes to WSNs, dynamic routing is not suitable for application over vast 
geographic areas. Expansive networking projects like the IoTs might pose difficulty during implementing during their dynamic routing 
in a WSN environment. 
Besides, it may be difficult to get accurate results using dynamic routing. This is because of the high sensitivity of sensor trans­
mission to ambient factors such as temperature, air, interference, and humidity. So, using dynamic routing may be somewhat 
challenging. 
If a stable topology is apt for the IoT with massive networks, static routing, rather than dynamic routing, would facilitate energy- 
efficient communication. For, it consumes less amount of energy comparatively. Since the proposed framework does not make use of 
the relay layer, a tier-based architecture, quite like existing frameworks, with the absence of that layer could be developed. It illustrates 
a hierarchical network design in which the only static objects that adhere to static routing-based transmission are Cluster Heads (CH), 
Cluster Brokers (CB), Relay Nodes (N relay), and End Nodes (EN). 
The lowest layers consist of sensor nodes, cluster coordinators, relay nodes, and cluster heads. The very top layer, which is referred 
to as the convergence layer, is positioned there. The nodes that comprise this level are mostly comprised of internet-accessible base 
stations. It is the responsibility of the lower-level nodes to recognise an object or entity and relay that information to the higher-level 
nodes. 
Using Nrelay, data is sent to the CHs. To distribute the load fairly over all the CHs and CBs, data is sent from the CHs to the higher 
layer CB, which in turn sends it to CB above it, and so on. This is done until the data is sent to the highest layer BS. 
It would not be easy to attain an energy efficiency level that will allow IoT devices to run on a single battery for years together 
without replacement. More efficient components that use less energy and power distribution systems are needed. So, the authors 
propose a lower energy consumption algorithm for the IoT. 
The current efforts focus on exploring cutting-edge methodologies and transistor technologies for boosting energy efficiency. Using 
a segmented energy protocol for the IoT, which would dynamically move from one phase to the next based on whether an IoT device is 
switched on, is recommended. This is done for assisting the sensor network in using less energy. By carefully analysing the real data on 
the IoT devices’ energy usage for the many different types of buildings, the study was able to find the major factors and trends. 
5.3.2. Residual energy 
Energy is viewed as an essential resource since the vast majority of WSN applications are managed by devices that run on battery 
power. The quantity of energy that is used will be the primary factor that decides how long the network will continue to function. For, 
this determines how quickly the node’s battery will run down and how erratic the distribution of energy consumption will be. 
While developing a solution for this problem in a WSN-based IoT system, one option is to ensure that the route finding takes into 
consideration the energy level of each node. The nodes in the network that are considered to have high energy levels are those that are 
considered to be in between the source and the destination nodes. The units for the node’s residual energy, abbreviated Er, are given as 
below- 
Er = Er/Emax 
Er is the node’s remaining energy, while Emax is the node’s maximum amount of energy. 
5.4. Transmitted data reduction 
The amount of data that is carried in a WSN has a considerable impact on the amount of energy that is required by the sensor node. 
This is especially true when the data is delivered across a greater distance. So, to effectively limit the quantity of transmission energy 
that is spent by the node, it is necessary to lessen the number of bits that are included within each packet or the number of packets that 
are contained within each message. This will help the device to make use of a more appropriate amount of transmission energy. To 
accomplish this objective, a wide variety of strategies, such as data aggregation, data compression, etc. are used. 
Despite the fact that data reduction techniques need a little increase in the amount of energy, they result in a significant decrease in 
the number of traversal flows. Because of this, the quantity of additional energy that is needed by the communication unit is reduced, 
which in turn lengthens the battery’s life. Nonetheless, there are certain circumstances in which such methods ought to utilise less 
power than what would be saved by delivering the smaller data packets. 
In some situations, it may be important to consider the pros and cons of various options. The communication unit in the sensor node 
is the one that consumes the most energy since it is responsible for both transmitting and receiving of data. For instance, the volume of 
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
13
data that is being transferred and the distance that separates the sender and the destination are the two most critical aspects that 
impact the process of transmission. There is a one-to-one relationship between the distance between the nodes sending and receiving 
information and the amount of energy that is lost. This is shown in Fig. 5. 
For travelling a longer distance, a higher quantity of energy is required, but when travelling a shorter distance, a lower amount of 
energy is required. The next section identifies several techniques with the potential to lower the energy required. 
6. Conclusion 
This study significantly contributes to the field of precision agriculture, shedding light on the crucial aspects of wireless sensor 
networks (WSN) in crop production applications. Our investigation highlights the capability of precision agriculture to accurately 
estimate, monitor, and evaluate vital signs of nutrient deficiency. However, the widespread usage of wireless IoT devices in controlling 
crop growing conditions raises concerns about energy efficiency. The observed massive energy wastage necessitates the exploration of 
cutting-edge methods to enhance the sustainability of battery-operated gadgets. Our focused examination on agriculture based WSNs, 
specifically addressing wireless protocols, energy harvesting, and efficiency procedures, unveils critical challenges. The proposed 
investigation not only identifies these challenges but also puts forth solutions to mitigate them. The study introduces a novel taxonomy 
of energy-saving approaches for both traditional WSNs and IoT-based systems. The summarized insights cover crop healthcare 
methods, integrated agriculture technologies, and various IoT applications. Furthermore, the study underscores the potential of IoT 
applications in precision agriculture, providing real-time monitoring, health status updates, and prompt treatment responses for crops. 
It emphasizes the transformative impact of integrated agriculture technologies in addressing water shortages, improving irrigation, 
reducing costs, and effectively managing field variability. As we explore these advancements, this research advocates for overcoming 
existing challenges to establish WSNs that meet IoT standards, particularly in the context of medical and agricultural applications. In 
essence, the study offers a roadmap for future technology integration, emphasizing the need for continued research in WSNs for IoT 
technologies. 
Ethics approval and consent to participate 
This article does not contain any studies with human participants or animals performed by any of the authors. 
Declaration of Competing Interest 
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to 
influence the work reported in this paper. 
Data availability 
Data sharing not applicable to this article as no datasets were generated or analyzed during the current study. 
Fig. 5. Methods for reducing the amount of data sent.  
K. Aggarwal et al.

Computers and Electrical Engineering 113 (2024) 109052
14
References 
[1] Dong Y, Xu F, Liu L, Du X, Ren B, Guo A, Geng Y, Ruan C, Ye H, Huang W, et al. Automatic system for crop pest and disease dynamic monitoring and early 
forecasting. IEEE J Sel Top Appl Earth Obs Remote Sens 2020;13:4410–8. 
[2] de Carvalho Silva J, Rodrigues JJPC, Alberti AM, Solic P, Aquino ALL. LoRaWAN - a low power WAN protocol for internet of things: a review and opportunities. 
In: Proceedings of the 2nd international multidisciplinary conference on computer and energy science (SpliTech); 2017. p. 1–6. 
[3] Ghandar A, Ahmed A, Zulfiqar S, Hua Z, Hanai M, Theodoropoulos G. A decision support system for urban agriculture using digital twin: a case study with 
aquaponics. IEEE Access 2021;9:35691–708. 
[4] Pasha AK, Mulyana E, Hidayat C, Ramdhani MA, Kurahman OT, Adhipradana M. System design of controlling and monitoring on aquaponic based on internet of 
things. In: Proceedings of the 4th international conference on wireless and telematics (ICWT); 2018. p. 1–5. 
[5] Lavanya S, Prasanth A, Jayachitra S, Shenbagarajan A. A Tuned classification approach for efficient heterogeneous fault diagnosis in IoT-enabled WSN 
applications. Measurement 2021;183:109771. 
[6] Prasad A, Chawda P. Power management factors and techniques for IoT design devices. In: Proceedings of the 19th international symposium on quality 
electronic design (ISQED); 2018. p. 364–9. 
[7] Wei Y, Li W, An D, Li D, Jiao Y, Wei Q. Equipment and intelligent control system in aquaponics: a review. IEEE Access 2019;7:169306–26. 
[8] Kandavalli SR, Khan AM, Iqbal A, et al. Application of sophisticated sensors to advance the monitoring of machining processes: analysis and holistic review. Int J 
Adv Manuf Technol 2023;125:989–1014. 
[9] Rao Y, Jiang ZH, Lazarovitch N. Investigating signal propagation and strength distribution characteristics of wireless sensor networks in date palm orchards. 
Comput Electron Agric 2016;124:107–20. 
[10] Iso-Ketola P, Karinsalo T, Vanhala J. HipGuard: a wearable measurement system for patients recovering from a hip operation. In: Proceedings of the 2nd 
international conference on pervasive computing technologies for healthcare. Pervasive Health; 2008. https://doi.org/10.1109/PCTHEALTH.2008.4571068. 
[11] Kachhoria R, Varma S, Radhakrishna M. A case study of a remote sensing using WSN. In: Proceedings of the IEEE recent advances in geoscience & remote 
sensing: technologies, standards and applications (TENGRASS); 2019. https://doi.org/10.1109/TENGARSS48957.2019.8976047. 
[12] Markkandan S, Narayanan L, Robert Theivadas J, Suresh P. Edge based interpolation with refinement algorithm using EDGE strength filter for digital camera 
images. Turk J Physiother Rehabil 2021;32(2):981–93. 
[13] Firouzi F, et al. Internet-of-Things and big data for smarter healthcare: from device to architecture, applications and analytics. Future Gener Comput Syst 2018. 
https://doi.org/10.1016/j.future.2017.09.016. 
[14] Tao F, Zuo Y, Xu LD, Zhang L. IoT-based intelligent perception and access of manufacturing resource toward cloud manufacturing. IEEE Trans Ind Inform 2014; 
10(2):1547–57. 
[15] Cho SC, Kwak HE, Chung KS. An energy efficient cluster management method based on autonomous learning in a server cluster environment. J KIPS Trans 
Comput Commun Syst 2015;4(6):185–96. 
[16] Cho YB, Lee SH, Woo SH. An adaptive clustering algorithm of wireless sensor networks for energy efficiency. J Inst Internet Broadcast Commun (IIBC) 2017;17 
(1):99–106. 
[17] Lee HB, Kwon KH. Implementation of a DB-based virtual file system for lightweight IoT clouds. J KIPS Trans Comput Commun Syst 2014;3(10):311–22. 
[18] Lee JY, Choi HS, Rhee WS. Development of the web-based participation IoT service brokering platform. J Korea Contents Assoc 2015;15(2):40–57. 
Kapil Aggarwal is an Associate Professor in Computer Science & Engineering at Koneru Lakshmaiah Education Foundation, Vaddeswaram, Guntur, Andhra Pradesh. 
With over 20 years in teaching and 5 years in research, he holds a Bachelor’s from Nagpur University (1994), a Master’s from IETE, New Delhi (2001), and a Ph.D. from 
Shri JJT University, Rajasthan (2021). He has published over 30 papers and serves as a reviewer for respected journals. 
G. Sreenivasula Reddy is currently a Professor, Department of Computer Science and Engineering at Chaitanya Bharathi Institute of Technology, Proddatur, Andhra 
Pradesh. His Bachelor’s degree in Mechanical Engineering, in the year 1996 and he received his Master’s Degree in Computer Science in the year 2007. He was awarded 
Ph.D in the year 2013. His research area is Networking, Cloud Computing and IoT. 
Ramesh Makala is a Professor in Computer Science and Engineering at HINDU College of Engineering and Technology, Guntur, Andhra Pradesh. He completed his Ph. 
D. from Acharya Nagarjuna University in 2013 and M.Tech. from Andhra University in 2004. Specializing in Image Processing, Software Engineering, Information 
Security, and Machine Learning, his research stands out in security and data compression fields. 
T. Srihari is a distinguished academic and researcher in the field of Electrical and Electronics Engineering. He holds a Bachelor’s degree from Thiagarajar College of 
Engineering, Madurai, and a Master’s degree from PSG College of Technology, Coimbatore. Dr. Srihari earned his Doctorate from Anna University, Chennai, marking a 
significant milestone in his academic journey. Currently serving as an Associate Professor in the Department of Electrical and Electronics Engineering at Saveetha School 
of Engineering, SIMATS University, Chennai, 
Neetu Sharma is a Professor in Computer Science & Engineering at Galgotias University, Greater Noida, with over 23 years of teaching experience. She earned her Ph.D. 
(2016) from Mewar University, Rajasthan, an M.E. (2010) from NITTTR, Chandigarh (Panjab University), and a B.E. (1996) from Chhotu Ram State College of En­
gineering, Murthal, Sonepat. She has published over 50 research papers and is a reviewer for renowned journals. 
Charanjeet Singh is working as an Assistant Professor in the Department of Electronics and Communication at Deenbandhu Chhotu Ram University of Science and 
Technology, Murthal, Sonipat. His area of interests is Wireless Communication, Wireless Sensor Network, Internet of Things, Artificial Intelligence Machine Learning, 
Deep Learning, Antenna Design, MIMO Technology. He has 11 years of teaching experience. 
K. Aggarwal et al.