Balmorel
========
On this page, the most important equations like the objective function and constraints are stated.

Objective function
******************

I have added input and output to the OM costs as we have it divided.

Our fuel use is in MWh and we use the fuel price in Euro/Mwh (Open_MODEX terminology: euro/EJ) - maybe this should be made clear here.

We are missing something on emissions from fuel use... I have here called it: :math:`\psi^{emi}_{g,e}` to name it something assuming it is in kg/GJ.

.. math::

	{{\pi}} & =  \sum_{y\in Y} ( {\color{red}{{IDISCOUNTFACTOR}}_{y}} \cdot {\color{red}{{IWEIGHTY}}_{y}} \cdot  (  

	& \sum_{a\in A, g\in G, f\in F(g)} ( \pi^{fuel}_{y, a, f} \cdot  \sum_{t\in T} ( v^{fuse}_{y,a,g,t} )  )  

	& +  \sum_{a\in A, g\in G^{elec} } ( \pi^{omv,gen,out}_{a,g} \cdot  \sum_{t\in T} ( v^{gen}_{y,a,g,t} )  )  

	& +  \sum_{a\in A, g\in G } ( \pi^{omv,gen,in}_{a, g} \cdot  \sum_{t\in T} ( v^{fuse}_{y,a,g,t} )  )  

	& +  \sum_{a\in A, g\in G} (  ( {\color{red}{{VGKNACCUMNET}}_{y, a, g}} + \kappa^{capa}_{y,a,g}  )  \cdot \pi^{omf,capa}_{a,g} )  

	& +  \sum_{r\in R, r'\in R } (  \sum_{t\in T} (  ( v^{trans}_{y,r,r',t} \cdot \pi^{omv,trans}_{r,r'} )  )  )  

	& +  \sum_{a\in A, g\in G} ( v^{inv,capa}_{y,a,g} \cdot \pi^{inv,capa}_{a, g} \cdot  \sum_{c \in C(a)}{{\color{red}{ANNUITYCG}}}_{c, g} \cdot  \sum_{y' |  (   {{y'}}    =    {{y}}   ) }{{\color{red}{IYHASANNUITYG}}}_{y, y', g} )  

	& +  \sum_{y'\in Y, a\in A, g\in G | {{y'}}    <    {{y}} } ( v^{inv,capa}_{y',a,g} \cdot \pi^{inv,capa}_{a, g} \cdot  \sum_{c \in C(a)}{{\color{red}{ANNUITYCG}}}_{c, g} \cdot {{\color{red}{IYHASANNUITYG}}}_{y', y, g} )  

	& +  \sum_{r \in R, r'\in R} ( \frac{1}{2} \cdot v^{inv,xcapa}_{y,r,r'} \cdot \pi^{inv,xcapa}_{y,r,r'} \cdot  ( \frac{1}{2} \cdot  (  \sum_{c \in C(r)}{{\color{red}{ANNUITYCX}}}_{c}  +  \sum_{c \in C(r')}{{\color{red}{ANNUITYCX}}}_{c} )  )  \cdot  \sum_{y' |  (   {{y'}}    =    {{y}}   ) }{{\color{red}{IYHASANNUITYX}}}_{y', y} )  

	& +  \sum_{y'\in Y, r \in R, r'\in R |  {{y'}}    <    {{y}} } ( \frac{1}{2} \cdot v^{inv,xcapa}_{y',r,r'} \cdot \pi^{inv,xcapa}_{y',r,r'} \cdot  ( \frac{1}{2} \cdot  (  \sum_{c \in C(r)}{{\color{red}{ANNUITYCX}}}_{c} +  \sum_{c \in C(r')}{{\color{red}{ANNUITYCX}}}_{c} )  )  \cdot {{\color{red}{IYHASANNUITYX}}}_{y', y} )  

	& +  \sum_{c\in C} (  \sum_{a\in A(c), g \in G} (  \sum_{t\in T} (  \frac{3.6}{1000} \cdot \psi^{emi}_{g,CO2} \cdot v^{fuse}_{y,a,g,t} )  \cdot \pi^{emi}_{y,c,CO2} )  )  

	& +  \sum_{c\in C} (  \sum_{a\in A(c), g \in G} (  \sum_{t\in T} (  \frac{3.6}{1000} \cdot \psi^{emi}_{g,SO2} \cdot v^{fuse}_{y,a,g,t} )  \cdot \pi^{emi}_{y,c,SO2} )  )  

	& +  \sum_{c\in C} (  \sum_{a\in A(c), g \in G} (  \sum_{t\in T} (  \frac{3.6}{1000} \cdot \psi^{emi}_{g,NOx} \cdot v^{fuse}_{y,a,g,t} )  \cdot \pi^{emi}_{y,c,NOx} )  )  

	& )  ) 


Marked in red: things that are not in the terminology. All of these are explained in the following table:

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - Name 
     - Domains 
     - Type
     - Description
   * - IDISCOUNTFACTOR 
     - y 
     - Parameter 
     - Discount factor for weighting future years relative to the first year in Y (~)  
   * - IWEIGHTY 
     - y 
     - Parameter 
     - Relative weight of the individual years in Y  
   * - ANNUITYCG 
     - c, g 
     - Parameter 
     - Transforms investment in technologies into annual payment (fraction)  
   * - ANNUITYCX 
     - c 
     - Parameter 
     - Transforms investment in transmission lines into annual payment (fraction)
   * - IYHASANNUITYG 
     - y, y', g 
     - Parameter 
     - Binary parameter to establish whether the annuity of an investment of a technology made in Y (first index) should be paid in the time period Y (second index) (0,1)  
   * - IYHASANNUITYX 
     - y, y' 
     - Parameter 
     - Binary parameter to establish whether the annuity of an investment of a transmission line investment made in Y (first index) should be paid in the time period Y (second index) (0,1)  
   * - VGKNACCUMNET 
     - y, a, g 
     - Variable
     - Accumulated new investments at end of (ULTimo) previous (i.e., start of current) year (MW) 
	
Not relevant for Open_MODEX scenario runs
***************************************** 
so far (should be inside the summation of the y) - should we include them? Not in OpenMODEX terminology yet.	

Heat
''''

.. math::
	+  \sum_{a\in A, g\in G^{heat} } ( \pi^{omv,gen,out}_{a,g} \cdot  \sum_{t\in T} ( {\color{blue}\gamma^{CV}_g} \cdot v^{gen,heat}_{y,a,g,t} )  )  

Hydro price profiles
''''''''''''''''''''

.. math::

	+  \sum_{a\in A, g\in G^{hyrs}} (  \sum_{t\in T} ( {{HYPPROFILS}}_{a, IS3} \cdot v^{gen,elec}_{y,a,g,t} )  )  
	

Constraints
***********

QEEQ
''''
To be included

QGFEQ
'''''
To be included