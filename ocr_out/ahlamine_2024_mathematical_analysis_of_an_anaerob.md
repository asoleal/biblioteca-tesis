## scientific reports

## OPEN

<!-- image -->

## Mathematical analysis of an anaerobic digestion model for biogas production from solid waste

Iliyass Ahlamine 1  , Abdellah Alla 1,2 &amp; Noha El Khattabi 1,2

Municipal solid waste is one of the most significant sources of gas emissions. In a context of renewable energy production and greenhouse gas emission reduction, we focus on the amount of biogas produced by the anaerobic digestion of organic matter in a controlled landfill environment. We present a mathematical model describing this process from a microbiological and biochemical point of view, including the dynamics of the methane and carbon dioxide produced. A qualitative analysis of the dynamic system shows the existence of an infinite number of non-hyperbolic equilibria inducing an attractor that has been identified. Through numerical tests, we explore how the non-connectivity of the attractor resulting from the choice of growth functions can entirely transform the performance of the process, and highlight critical initial stock values that influence the amount of biogas produced.

Keywords Biogas production, Anaerobic digestion, Dynamical systems theory, Stable manifold theorem, Optimal initial stock

## List of symbols

Ss Total concentration of biodegradable organic substrate (g/l)

Sdc Dissolved organic substrate concentration (g/l)

Xa Acidogenic biomass concentration (g/l)

Sac Acetate substrate concentration (g/l)

Xm Methanogenic biomass concentration (g/l)

CH 4 Methane concentration (g/l)

CO 2 Carbon dioxide concentration (g/l)

Y

V ector of variables

ya Mass conversion rate of dissolved organic substrate into acidogenic biomass

ym Mass conversion rate of acetate substrate into methanogenic biomass

yac Acetate substrate conversion yield yCH 4 Methane conversion yield

Kd Half-saturation constant of dissolved organic substrate (g/l)

Ka Half-saturation constant of acetate substrate (g/l)

Kid Inhibition constant of dissolved organic substrate (g/l)

Kia Inhibition constant of acetate substrate (g/l)

da Death rate of acidogenic bacteria ( day -1 )

kh Hydrolysis constant of biodegradable organic substrate ( day -1 )

dm Death rate of methanogenic bacteria ( day -1 )

µ max m Maximum growth rate of methanogenic bacteria ( day -1 )

µ max a Maximum growth rate of acidogenic bacteria ( day -1 )

t Time ( day )

S ∗ ac Limit concentration of acetate substrate (g/l)

S ∗ dc Limit concentration of dissolved organic substrate (g/l)

̂

Limit concentration of methane (g/l)

̂

CH

4

CO

2

µa

(

.

)

Limit concentration of carbon dioxide (g/l)

Growth function of acidogenic bacteria

µm ( . ) Growth function of methanogenic bacteria

The  bio-degradation  process  of  municipal  waste  in  landfills  consists  of  a  succession  of  chemical  reactions catalyzed by bacteria, which transform slowly the organic matter contained in the waste into mineral or gaseous

1 LAMA Laboratory, Department of Mathematics, Faculty of Sciences, Mohammed V University in Rabat, Rabat, Morocco. 2 these authors contributed equally to this work.  email: iliyass.ahlamine@um5r.ac.ma elements. This transformation of organic matter can be decomposed in many steps, which differ depending on the environment being under aerobic or anaerobic conditions. The aerobic digestion lasts only a few days after the waste is deposited in the landfill, where oxygen is present in the void spaces. During this period, the biogas produced is mainly carbon dioxide. The anaerobic digestion operates within a closed environment where, in the absence of oxygen, organic matter is gradually converted into biogas, primarily composed of carbon dioxide and methane 1,2 . This process unfolds in four major stages: first, hydrolysis breaks down insoluble organic polymers into soluble derivatives that become accessible to other bacteria. Next, during acidogenesis, acidogenic bacteria convert  these  sugars  and  amino  acids  into  carbon  dioxide,  hydrogen,  ammonia,  and  organic  acids.  In  the acetogenesis stage, these organic acids are further processed by bacteria into acetic acid, along with additional ammonia, hydrogen, and carbon dioxide. Finally, methanogens convert these end products into methane and carbon dioxide, completing the biogas production process 3,4 .

The  mathematical  modeling  of  the  anaerobic  digestion  process  in  landfills  holds  significant  importance for multiple reasons. It's a fundamental tool for optimizing, and managing the generation of biogas, offering essential prospects for environmental sustainability and energy recovery.

In the literature, various models have been developed to describe the anaerobic digestion process and the associated microbial dynamics, aiming to better understand and optimize digester performance under varying microbial conditions 5-13 .The Anaerobic Digestion Model No. 1 (ADM1) is a structural model that outlines the four main stages of anaerobic digestion leading to biogas production 5 . However, its complexity, due to a large number of equations, makes difficult its analysis.  To  overcome  this,  simplified  models  have  been  proposed. Rouez's model 6 uses a two-step process (hydrolysis/acidogenesis and methanogenesis), and was mathematically analysed later by Ouchtout et al. 14 highlighting the impact of the selected bacterial growth functions. In the context of wastewater treatment, the (AM2) model by Bernard et al. 7 is notable, incorporating Monod growth for acidogenesis and Haldane growth for methanogenesis. This choice is well-suited for control and optimization, as demonstrated by the stability analysis conducted by Benyahia et al. 15 Furthermore, in the context of co-digestion, where multiple types of substrates are mixed, Berga et al. 16 have provided a mathematical analysis of Rakmak et al. ' s two-step model (hydrolysis/acidogenesis and methanogenesis) 8 , and highlighting the influence of the chosen bacterial growth functions. However, the Halvadakis model 9 , which captures the natural process of anaerobic digestion, is of particular interest for our study. This model provides a comprehensive description of the three main stages: hydrolysis, acidogenesis, and methanogenesis. The model considers biodegradable organic matter (easily, intermediate, and slowly), which is hydrolyzed into a dissolved organic substrate. This substrate is then transformed into acetate substrate and carbon dioxide by the acidogenic biomass. The methanogenic biomass uses the acetate substrate to produce methane and additional carbon dioxide. The substrate utilization by biomass is determined by the Monod bacterial growth function. The model also takes into account the decomposition of dead acidogenic bacteria, which is converted to acetate and carbon dioxide, and the decomposition of dead methanogenic bacteria, which is converted to methane and carbon dioxide.

In this study, we perform a mathematical analysis of the Halvadakis dynamical system, incorporating bacterial growth functions µa ( . ) and µm ( . ) ,  which can be of either the Monod or Haldane type 17,18 .  Regardless of the growth function selected, our analysis confirms the existence of an infinite number of non-hyperbolic equilibria toward which the system's trajectories converge. By employing Barbalat's lemma and the stable manifold theorem, we identify the attractor of the dynamical system and derive an expression for the biogas produced based on initial substrate concentrations and their limiting values. Through numerical simulation, we demonstrate how the process performance is influenced by the connectivity of the attractor when the Monod growth function is chosen, and by its non-connectivity when the Haldane growth function is applied. Furthermore, we demonstrate that biogas production, as a function of the initial stock concentration, exhibits five changes in monotonicity. These changes are driven by the four regions of convergence of substrate concentrations that result from the selection of the Haldane growth function. We also analyze the impact of bacterial mortality rates on biogas production, highlighting their significant role in the overall process.

## Description of the model

In  this  section,  we  introduce  the  mathematical  model  for  anaerobic  digestion,  inspired  by  the  Halvadakis model. Initially, the biodegradable organic substrate present in the waste, with easily, intermediate, and slowly degradable  components,  breakdown  into  dissolved  organic  substrate  with  an  hydrolysis  constant kh .  The dissolved organic substrate is then consumed by acidogenic biomass at a rate of 1 ya µa ( Sdc ) .  A portion of this consumption supports the growth of the acidogenic biomass, which is modeled as a natality rate µa ( Sdc ) minus a mortality rate da . The remainder of the consumed substrate, expressed as 1 -ya ya µa ( Sdc ) , is partially converted to acetate substrate with a yield yac , while the rest is transformed into carbon dioxide with a yield of (1 -yac ) . A similar process applies to the acetate substrate and methanogenic biomass. The acetate substrate is consumed by methanogenic biomass at a rate of 1 ym µm ( Sac ) . Part of this consumption is used for the growth of methanogenic biomass, described by a natality rate µm ( Sac ) minus a mortality rate dm . The remaining portion, expressed as 1 -ym ym µm ( Sac ) ,  leads to the production of methane with a yield yCH 4 ,  while the remainder produces carbon dioxide with a yield of (1 -yCH 4 ) . The model also emphasizes the significant role of mortality rates in biogas production. These rates are included in the equations for biogas production because they account for the natural decrease in biomass. This decrease influences substrate availability, which in turn affects the rates of methane and carbon dioxide production.The mathematical model of the process described in Fig. 1 is formulated through a system of differential equations. This system is represented as follows:

<!-- formula-not-decoded -->

The bacterial growth functions denoted as µa and µm , are two C 1 -functions defined on R by:

- Monod law:

·

- Haldane law:

<!-- formula-not-decoded -->

Fig. 1 .  Schematic representation of anaerobic digestion process in landfill.

<!-- image -->

<!-- formula-not-decoded -->

- Haldane's law includes inhibition effects, providing a more realistic representation of bacterial growth at high substrate concentrations. Monod's growth function is appropriate for simpler systems with lower substrate concentrations and minimal inhibition effects, while the Haldane function is better suited for complex scenarios involving significant substrate inhibition, although it can affect biogas production. In the model, we have:

## Variables:

- Ss : Total concentration of biodegradable organic substrate (g/l),
- Sdc : Dissolved organic substrate concentration (g/l),

Xa : Acidogenic biomass concentration (g/l),

Sac : Acetate substrate concentration (g/l),

Xm : Methanogenic biomass concentration (g/l),

CH 4 : Methane concentration (g/l),

CO 2 : Carbon dioxide concentration (g/l).

## Parameters:

ya : mass conversion rate of dissolved organic substrate into acidogenic biomass,

ym : mass conversion rate of acetate substrate into methanogenic biomass,

yac

: acetate substrate conversion yield,

yCH 4 : methane conversion yield.

Kd : half-saturation constant of dissolved organic substrate (g/l),

Ka : half-saturation constant of acetate substrate (g/l),

Kid : inhibition constant of dissolved organic substrate (g/l),

Kia : inhibition constant of acetate substrate (g/l),

da : death rate of acidogenic bacteria ( day -1 ) ,

kh : hydrolysis constant of biodegradable organic substrate ( day -1 ) ,

dm : death rate of methanogenic bacteria ( day -1 ) .

µ max m : maximum growth rate of methanogenic bacteria ( day -1 ) .

µ max a : maximum growth rate of acidogenic bacteria ( day -1 ) ,

The model parameters satisfy the following conditions.

H1 . The substrate-biomass yields are strictly positives and:

<!-- formula-not-decoded -->

- H2 . The hydrolysis, half saturation and inhibition constants are strictly positives:

<!-- formula-not-decoded -->

- H3 . The bacterial death rates are strictly positives and less than the maximum growth rates:

<!-- formula-not-decoded -->

We define the non-empty sets:

<!-- formula-not-decoded -->

For the Monod expression, we have:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For the Haldane expression, we have:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and

and

where

<!-- formula-not-decoded -->

## Study of the asymptotic behavior

As our system (1)-(2) satisfies the conditions of Cauchy-Lipschitz theorem, the existence and uniqueness of the solution with a given initial value is guaranteed. We begin with a result on the non-negativity and boundedness of the solution.

Proposition  1 Under  hypothesis  ( H1 -H3 ),  for  any  non-negative  initial  condition ( S 0 s , S 0 dc , X 0 a , S 0 ac , X 0 m, CH 0 4 , CO 0 2 ) , the solution

( Ss ( . ) , S dc ( . ) , Xa ( . ) , S ac ( . ) , Xm ( . ) , CH 4 ( . ) , CO 2 ( . )) of (1)-(2) is non-negative and bounded.

Proof We will demonstrate the non-negativity of each component of the solution.

- For the component Ss ,  we  have dSs dt = -khSs with Ss (0) = S 0 s ,  which implies Ss ( t ) = S 0 s e -k h t .  If S 0 s ≥ 0 , then for all t 0 , we have Ss ( t ) 0 .
- ≥ ≥ · For  the  component Sdc ,  we  have dSdc dt = khSs -1 ya µa ( Sdc ) Xa with Sdc (0) = S 0 dc .  We  have dSdc dt ≥ -1 ya µa ( Sdc ) Xa for all t ≥ 0 . According to the comparison theorem 19 , if S 0 dc &gt; S 0 , then Sdc ( t ) &gt; S ( t ) , such that S ( t ) is a solution of the differential equation:

<!-- formula-not-decoded -->

If S 0 = 0 , then S ≡ 0 is the only solution of (7), thus S ( t ) &gt; 0 when S 0 &gt; 0 for all t ≥ 0 . Then, if S 0 dc &gt; 0 , we have Sdc ( t ) &gt; 0 for all t ≥ 0 .

- For the component Xa , we have dXa dt = ( µa ( Sdc ) -da ) Xa with Xa (0) = X 0 a . The term ( µa ( Sdc ) -da ) Xa is linear with respect to Xa , thus if X 0 a ≥ 0 , we have Xa ( t ) ≥ 0 for all t ≥ 0 .
- For the component Sac ,  we have dSac dt = yac ( 1 -ya ya µa ( Sdc ) + da ) Xa -1 ym µm ( Sac ) Xm with Sac (0) = S 0 ac

.  We have dSac dt ≥ -1 ym µm ( Sac ) Xm for  all t ≥ 0 .  According to the comparison theorem, if S 0 ac &gt; S 0 ,  then Sac ( t ) &gt; S ( t ) , such that S ( t ) is a solution of the differential equation:

<!-- formula-not-decoded -->

If S 0 = 0 , then S ≡ 0 is the only solution of (8), thus S ( t ) &gt; 0 when S 0 &gt; 0 for all t ≥ 0 . Then, if S 0 ac &gt; 0 , we have Sac ( t ) &gt; 0 for all t ≥ 0 .

- For the component Xm ,  we have dXm dt = ( µm ( Sac ) -dm ) Xm with Xm (0) = X 0 m .  The term ( µm ( Sac ) -dm ) Xm is linear with respect to Xm , thus if X 0 0 , we have Xm ( t ) 0 for all t 0 .
- m ≥ ≥ ≥ · From the above, we deduce the non-negativity of the components CH 4 and CO 2 .For boundedness, it suffices to notice that our system is closed, that is:

<!-- formula-not-decoded -->

so, there exists a positive constant C such that for all t ≥ 0 , we have:

We have:

<!-- formula-not-decoded -->

Hence, the result is proven. □

Next, we proceed to investigate the asymptotic behaviour of (1).

Proposition 2 Under hypothesis ( H1 -H3 ),  for  any  non-negative initial condition ( S 0 s , S 0 dc , X 0 a , S 0 ac , X 0 m ) ,  the solution of (1) verifies:

<!-- formula-not-decoded -->

2. There exist two positive real numbers S ∗ dc and S ∗ ac , which satisfy:

<!-- formula-not-decoded -->

Proof We have lim t → + ∞ Ss ( t ) = lim t → + ∞ S 0 s e -k h t = 0 . To prove the convergence of Xa and Sdc , we consider the C 1

-function defined on [0 , + ∞ ) as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Since Xa is non-negative, then V 1 is non-increasing, and minored by 0. So there exists a real l 1 ≥ 0 such that lim t → + ∞ V 1 ( t ) = l 1 ( l 1 &lt; ∞ ) . Moreover, one has:

<!-- formula-not-decoded -->

Since d 2 V 1 dt 2 is bounded, dV 1 dt is uniformly continuous. According to Barbalat's lemma 20 , we have lim t → + ∞ dV 1 dt ( t ) = 0

<!-- formula-not-decoded -->

Additionally, since lim t → + ∞ V 1 ( t ) = lim t → + ∞ Ss ( t ) + 1 ya Xa ( t ) + Sdc ( t ) = l 1 , we have lim t → + ∞ Sdc ( t ) = S ∗ dc = l 1 . Similarly for Xm and Sac , we consider the C 1 -function defined on [0 , + ∞ ) as follows:

<!-- formula-not-decoded -->

we prove that lim t → + ∞ Xm ( t ) = 0 and lim t → + ∞ Sac ( t ) = S ∗ ac . □

Proposition 3 Under hypothesis ( H1 -H3 ),  for  any non-negative initial condition ( S 0 s , S 0 dc , X 0 a , S 0 ac , X 0 m ) ,  the solution of (1) converges asymptotically to an equilibrium (0 , S ∗ dc , 0 , S ∗ ac , 0) , where S ∗ dc and S ∗ ac belong respectively to ξdc and ξac .

Proof Let Sdc ( . ) be a component of the solution of (1) which converges to S ∗ dc ,  and suppose that S ∗ dc doesn't belong to ξdc .

Since µa is continuous on [0 , + ∞ ) , then µa ( Sdc ( t )) tends to µa ( S ∗ dc ) when t approaches + ∞ , leading to:

<!-- formula-not-decoded -->

Choosing ϵ = µa ( S ∗ dc ) -da &gt; 0 , we have, for all t &gt; T :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Letting s ∈ ( T, t ) , integrating from s to t , we get Xa ( t ) &gt; Xa ( s ) e ϵ ( t -s ) , for all t &gt; T . This contradicts the fact that Xa is bounded. Thus, we conclude that S ∗ dc belongs to ξdc .

Similarly, we prove that S ∗ ac belongs to ξac . □

The sub-system (1) has an infinite number of equilibria that are non-hyperbolic, therefore the linearization does not allow us to conclude stability. To overcome this difficulty, we carry out a change of variables that leads to the use of a hyperbolic system. We then apply the stable manifold theorem. However, we obtain the following result.

Proposition  4 Under  hypothesis  ( H1 -H3 ),  for  each  steady  state E = (0 , S ∗ dc , 0 , S ∗ ac , 0) with S ∗ dc ∈ ξdc and S ∗ ac ∈ ξac , there exists an invariant three-dimensional manifold M in R 5 + such that any solution of (1) with an initial condition in M converges asymptotically to E .

Proof Let ( Ss, Sdc, Xa, Sac, Xm ) be a solution of (1) with an initial condition in M . Let Z 1 and Z 2 be the two variables defined by:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and

with

We have:

and

<!-- formula-not-decoded -->

If we define Y = ( Ss, Z 1 , Xa, Z 2 , Xm ) , then we have:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The equivalent system of the system (1) in the domain D = { ( Ss, Z 1 , Xa, Z 2 , Xm ) ∈ R + × R × R ∗ + × R × R ∗ + / ( Z 1 -β 1 ) Xa -Ss + S ∗ dc ≥ 0; ( Z 2 -β 2 ) Xm -yac ( Z 1 -β 1 +1) X is written:

7

and

with

<!-- formula-not-decoded -->

The domain D is  positively invariant for the system (10). Since µa ( S ∗ dc ) ̸ = da and µm ( S ∗ ac ) ̸ = dm ,  0 is the only equilibrium of (10) on D . The Jacobian matrix is given by:

<!-- formula-not-decoded -->

We  have  three  negative  eigenvalues: -kh, µa ( S ∗ dc ) -da and µm ( S ∗ ac ) -dm ,  and  two  positive  eigenvalues: -( µa ( S ∗ dc ) -da ) and -( µm ( S ∗ ac ) -dm ) . By the stable manifold theorem 21 , 0 is a hyperbolic equilibrium with a three-dimensional stable manifold W s and a two-dimensional unstable manifold W u .

We conclude that any trajectory of (10) with an initial value in the three-dimensional invariant manifold M = W s ∩ D converges asymptotically to 0, therefore the corresponding trajectory of (1) converges asymptotically to E = (0 , S ∗ dc , 0 , S ∗ ac , 0) . □

We can now state the corollary.

## Corollary 1 Under hypothesis ( H1 -H3 ), the set:

<!-- formula-not-decoded -->

is an attractor of sub-system (1).

Let's proceed to the sub-system (2).

Proposition 5 Under hypothesis ( H1 -H3 ), for any non-negative initial condition ( S 0 s , S 0 dc , X 0 a , S 0 ac , X 0 m, CH 0 4 , CO 0 2 ) , the solution of (2) verifies:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and

with

<!-- formula-not-decoded -->

Proof From (2), we have:

<!-- formula-not-decoded -->

For all t ≥ 0 , by integrating from 0 to t , we get:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Let's denote lim t → + ∞ CH 4 ( t ) = ̂ CH 4 and lim t → + ∞ CO 2 ( t ) = ̂ CO 2 . Upon taking limits, we obtain:

On the other hand, from Eq. (9), for all t ≥ 0 , we have:

<!-- formula-not-decoded -->

when t tends to + ∞ , we obtain:

<!-- formula-not-decoded -->

From Eq. (11) and Eq. (12), we conclude that:

<!-- formula-not-decoded -->

## Numerical results

In this section, we utilize the Matlab programming language to display numerical results for quantities of biogas produced, impacted by the final values S ∗ dc and S ∗ ac of the concentrations of the dissolved organic and acetate substrates.

The  parameter  values  used  in  our  numerical  simulations  are  inspired  by 10,11,14 and  are  presented  in  the following tables:

We assume that at the beginning of the process, there is no production of biogas, so that CH 0 4 = CO 0 2 = 0 , the other initial conditions are given in Table 1.

Figures 2 and 3 describe the trajectories of the system (1)-(2) corresponding to the Monod and Haldane scenarios, respectively.

In the Monod case, the concentrations of carbon dioxide and methane reach stability at approximately 200 g / l and 250 g / l , respectively, following a storage period of 200 days. Notably, an observation can be made that the anaerobic phase begins at around 100 days, signifying a switch wherein methane production exceeds carbon dioxide production.

In  the  Haldane  case,  the  stabilization  of  carbon  dioxide  and  methane  production  happens  nearly simultaneously but after an extended storage period of 400 days. The start of the anaerobic phase is observed after approximately 300 days in this scenario.

The disparity between the Monod and Haldane cases lies in the convergence behavior of the concentrations Sdc and Sac .  In  the  Monod  case,  the  concentrations  converge  within  connected  sets,  corresponding  to  the connected attractor. In contrast, the Haldane case shows convergence within non-connected sets, corresponding to the non-connected attractor. To validate this assertion, we fix the parameters specified in Table 2 while varying the initial values. We, then, observe the convergence of the concentrations Sdc and Sac .

In the Monod case, from Eq. (3) and Eq. (4), we have λa = 5 . 5 and λm = 60 .

In the Haldane case, Eq. (5) yields λ -a = 5 . 59 and λ + a = 894 . 4 . Figure 6 demonstrates that when:

Figures 4 and 5 illustrate that for any non-negative value of S 0 s , Sdc and Sac converge to values less than λa and λm respectively.

- S 0 s ≤ 3300 , Sdc converges to values less than λ -a .
- S 0 s &gt; 3300 , Sdc converges to values higher than λ + a .Therefore, we find that 3300 is the critical value of S 0 s at which the limit S ∗ dc shifts from the interval λ -a to the interval λ + a .

Similarly, Eq. (6) gives λ -m = 123 . 24 and λ + m = 243 . 42 . Figure 7 shows that when:

- 0 ≤ S 0 s ≤ 600 , Sac converges to values less than λ -m .
- S 0 s ≥ 3900 , Sac converges again to values less than λ -m .Therefore, we find that 600 and 3900 are critical values of S 0 s at which the limit S ∗ ac shifts from λ -m to λ + m and then back to λ -m .
- 600 &lt; S 0 s &lt; 3900 , Sac converges to values higher than λ + m .

Table 1 .  Initial conditions.

<!-- image -->

<!-- image -->

<!-- image -->

Fig. 2 .  Trajectories of the system using the Monod growth function.

Fig. 3 .  Trajectories of the system using the Haldane growth function.

<!-- image -->

Fig. 4 . Sdc trajectories for various values of S 0 s in the Monod case.

<!-- image -->

<!-- image -->

Fig. 5 . Sac trajectories for various values of S 0 s in the Monod case.

<!-- image -->

Fig. 6 . Sdc trajectories for various values of S 0 s in the Haldane case.

<!-- image -->

time (day)

Fig. 7 . Sac trajectories for various values of S 0 s in the Haldane case.

When the Haldane growth function is considered, we observe two regions of convergence of Sdc and two regions of convergence of Sac . In Fig. 8, we illustrate the behavior of the substrate concentrations within the dynamic model (1) and identify the placement of these four regions. Considering initial substrate concentrations S 0 s ranging from 0 to 6000 with an increment of 200, this range includes the switch points 600 and 3900 for S ∗ ac and 3300 for S ∗ dc . We observe the following:

-  When S 0 s ≤ 600 , both S ∗ dc and S ∗ ac are below λ -a and λ -m respectively.
- Between 3300 &lt; S 0 s &lt; 3900 , both S ∗ dc and S ∗ ac exceed λ + a and λ + m respectively.
- For 600 &lt; S 0 s ≤ 3300 , S ∗ dc remains below λ -a , while S ∗ ac surpasses λ + m .
-  When S 0 s ≥ 3900 , S ∗ dc rises above λ + a , while S ∗ ac falls below λ -m .

This figure reveals the impact of inhibition phenomena on the process. Specifically, inhibition can prevent the bacteria from efficiently consuming the substrate, resulting in high concentrations substrate remaining in the process. As a result, the accumulation of unconsumed substrate affects negatively biogas production, as will be further illustrated in the next figure. In contrast, when the Monod growth function is chosen, only one region of convergence is observed, and the remaining substrate does not reach a high concentration.

<!-- image -->

Fig. 8 . Ss , Sdc , and Sac trajectories behavior for various values of S 0 s in the Haldane case.

Fig. 9 .  Biogas production as function of initial stock concentration S 0 s .

<!-- image -->

Fig. 10 .  Biogas production as function of mortality rate da .

<!-- image -->

In the following, we will focus on simulations in the Haldane case.

Figure 9 shows the total biogas (methane + carbon dioxide) produced as a function of the initial substrate concentration S 0 s . According to Proposition 5, the quantity of biogas produced is influenced by the limits S ∗ dc and S ∗ ac , which shift from lower to higher values as S 0 s varies. In this figure, we observe that for 0 ≤ S 0 s ≤ 3300 , Sdc converges below λ -a . This indicates that the dissolved organic substrate is effectively consumed by acidogenic bacteria, resulting in a significant increase in biogas production, which reaches a peak concentration of 1050 g / l . However,  when S 0 s &gt; 3300 , Sdc converges  above λ + a ,  leading  to  less  effective  consumption  of  the  dissolved organic substrate by acidogenic bacteria. Consequently, biogas production declines sharply, with a noticeable fall between 3300 and 3400 in S 0 s , where biogas output falls to 400 g / l . Beyond this point, biogas concentration continues to decrease. Within this range, for S 0 s &gt; 600 , Sdc converges above λ + m , resulting in poor consumption of acetate substrate by methanogenic bacteria, which leads to a decrease in biogas concentration over a small interval, followed by a gradual increase. Similarly, for S 0 s &gt; 3900 , Sdc converges below λ -m , leading to effective consumption of acetate substrate by methanogenic bacteria and a temporary increase in biogas concentration, which is then followed by a continuous decrease.

Fig. 11 .  Biogas production as function of mortality rate dm .

<!-- image -->

These  observations  highlight  that  the  choice  of  growth  functions  significantly  affects  biogas  production. When  both  bacterial  growth  functions  are  Haldane,  biogas  production  exhibits  five  distinct  switches  in monotonicity. In contrast,  when  one  Monod function and one Haldane function are used, there is a single switch value of S 0 s at which biogas production exhibits one change in monotonicity, shifting from increasing to decreasing. When both functions are Monod, biogas production increases linearly with S 0 s without any decrease. This occurs because there is no inhibition phenomenon present, allowing the bacteria to continuously consume the substrate.

Let's examine the impact of bacterial mortality rates on biogas production by considering a small value of S 0 s yielding Biogas- and a large value of S 0 s yielding Biogas + . It can be seen in Fig. 10 that when the initial stock concentration S 0 s is  less  than  3300,  the  mortality  rate  of  acidogenic  bacteria  has  almost  no  influence on the biogas production. In the other hand, Fig. 11 shows that the amount of biogas is first constant and then decreases as function of the mortality rate of methanogenic bacteria.

When S 0 s is higher than 3400, both Figs. 10 and 11 illustrate that the biogas production remains constant when the mortality rates of acidogenic and methanogenic bacteria are below 0.025. However, it starts decreasing once the mortality rates surpass this value. Notably, in this scenario, biogas production decreases sharply with mortality rate of acidogenic bacteria.

## Conclusion

Our study has provided a detailed analysis of biogas production through anaerobic digestion of solid waste, modeled by a system of differential equations. Through our mathematical analysis, we identified the attractor of the system. Our numerical simulations provide important insights into system behavior. When both bacterial growth functions are Monod, the attractor is connected, and biogas production increases linearly with the initial stock concentration S 0 s . When one growth function is Monod and the other is Haldane, the attractor becomes non-connected with two regions of convergence, and biogas production as function of S 0 s exhibits  a  single change in monotonicity. When both functions are Haldane, the attractor is non-connected with four regions of convergence, and biogas production as function of S 0 s exhibits five changes in monotonicity. Additionally, biogas production decreases with higher bacterial mortality rates.

In our future work, we will focus on managing the initial stock concentration to avoid exceeding the switch value of S 0 s that results in optimal biogas production and will explore the impact of spatial diffusion effects on biogas production.

## Data availability

The datasets used and/or analysed during the current study available from the corresponding author on reasonable request.

Received: 12 June 2024; Accepted: 22 October 2024

Published online: 29 October 2024

## References

1.  Farquhar, G. J. &amp; Rovers, F. Gas production during refuse decomposition. Water Air Soil Pollut. 2 , 483-495.   h  t  t  p  s  : /  / d  o  i .  o r  g /  1 0  . 1  0  0 7  / B  F  0  0  5  8  5  0  9  2 (1973).
2.  Chenu, D. Modélisation des transferts réactifs de masse et de chaleur dans les installations de stockage de déchets ménagers: application aux installations de type bioréacteur . Ph.D. thesis (2007).
3.  Aran, C. Modélisation des écoulements de fluides et des transferts de chaleur au sein des déchets ménagers. Application à la réinjection de lixiviat dans un centre de stockage . Ph.D. thesis (2001).
4.  Gholamifard,  S. Modélisation  des  écoulements  diphasiques  bioactifs  dans  les  installations  de  stockage  de  déchets .  Ph.D.  thesis, Université Paris-Est (2009).
5.  Batstone, D. J. et al. The iwa anaerobic digestion model no 1 (ADM1). Water Sci. Technol. 45 , 65-73.   h  t  t  p  s :  / /  d o  i .  o r  g /  1 0  . 2  1  6 6  / w  s  t .  2 0  0  2  .  0  2  9  2 (2002).
6.  Rouez, M. Dégradation anaérobie de déchets solides: Caractérisation, facteurs d'influence et modélisations. Laboratoire de Génie Civil et d'Ingénierie Environnementale. Lyon, Institut National des Sciences Appliquées Docteur 259 (2008).
7.  Bernard, O., Hadj-Sadok, Z., Dochain, D., Genovesi, A. &amp; Steyer, J.-P . Dynamical model development and parameter identification for an anaerobic wastewater treatment process. Biotechnol. Bioeng. 75 , 424-438. https://doi.org/10.1002/bit.10036 (2001).
8.  Rakmak, N., Noynoo, L., Jijai, S. &amp; Siripatana, C. Monod-type two-substrate models for batch anaerobic co-digestion. Lecture notes in applied mathematics and applied science in engineering 11-20 (2019).
9.  Halvadakis, C. P . methanogenesis in solid-waste landfill bioreactors . Ph.D. thesis, Stanford University (1983).
10.  El-Fadel, M., Findikakis, A. &amp; Leckie, J. A numerical model for methane production in managed sanitary landfills. Waste Manag. Res. 7 , 31-42. https://doi.org/10.1016/0734-242X(89)90006-2 (1989).
11.  El-Fadel, M., Findikakis, A. &amp; Leckie, J. Numerical modelling of generation and transport of gas and heat in landfills I. model formulation. Waste Manag. Res. 14 , 483-504. https://doi.org/10.1177/0734242X9601400506 (1996).
12.  Rapaport, A., Nidelet, T., El Aida, S. &amp; Harmand, J. About biomass overyielding of mixed cultures in batch processes. Math. Biosci. 322 , 108322. https://doi.org/10.1016/j.mbs.2020.108322 (2020).
13.  Harmand, J., Lobry, C., Rapaport, A. &amp; Sari, T. The chemostat: Mathematical theory of microorganism cultures Vol. 1 (John Wiley &amp; Sons, 2017).
14.  Ouchtout, S., Mghazli, Z., Harmand, J., Rapaport, A. &amp; Belhachmi, Z. Analysis of an anaerobic digestion model in landfill with mortality term. Commun. Pure Appl. Analy. 19 , 2333-2346. https://doi.org/10.3934/cpaa.2020101 (2020).
15.  Benyahia, B., Sari, T., Cherki, B. &amp; Harmand, J. Bifurcation and stability analysis of a two step model for monitoring anaerobic digestion processes. J. Process Control 22 , 1008-1019. https://doi.org/10.1016/j.jprocont.2012.04.012 (2012).
16.  Berga, H., Alla, A. &amp; El Khattabi, N. Mathematical analysis of an anaerobic co-digestion model with preference function and mortality. Math. Methods Appl. Sci. 46 , 10103-10122. https://doi.org/10.1002/mma.9105 (2023).
17.  Monod, J. The growth of bacterial cultures. Annu. Rev. Microbiol. 3 , 371-394. https:  //d  oi.  or  g/10  .1146/a  nn  ur  ev.mi.  03.1  00149.002103 (1949).
18.  Andrews, J. F. A mathematical model for the continuous culture of microorganisms utilizing inhibitory substrates. Biotechnol. Bioeng. 10 , 707-723. https://doi.org/10.1002/bit.260100602 (1968).
19.  McNabb, A. Comparison theorems for differential equations. J. Math. Anal. Appl. 119 , 417-428.   h  t  t  p  s  : /  / d  o  i .  o r  g /  1 0  . 1  0  1 6  / 0  0  2 2  2  4  7 X  (  8 6  )  9  0  1  6  3  -  0 (1986).
20.  Barbalat, I. Systemes d' équations différentielles d' oscillations non linéaires. Rev. Math. Pures Appl 4 , 267-270 (1959).
21.  Perko, L. Differential equations and dynamical systems Vol. 7 (Springer Science &amp; Business Media, 2013).

## Author contributions

I.A. analyzed the outcomes. A.A. and I.A. conducted the numerical simulations. N.E.K. and A.A. identified the problem and provided supervision. All authors reviewed the manuscript.

## Declarations

## Competing interests

The authors declare no competing interests.

## Additional information

Correspondence and requests for materials should be addressed to I.A.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit   h  t  t  p  :  /  /  c  r  e  a  t  i  v  e  c  o  m  m  o n  s .  o r  g /  l i  c e  n  s e  s /  b y  n  c  n  d  / 4  . 0  /  .

© The Author(s) 2024