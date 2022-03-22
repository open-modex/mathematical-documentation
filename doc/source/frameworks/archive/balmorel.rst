Archive
=======


Balmorel
********
On this page, the most important equations like the objective function and constraints are stated.

Objective function
''''''''''''''''''

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
''''''''''''''''''''''''''''''''''''''''' 
so far (should be inside the summation of the y) - should we include them? Not in OpenMODEX terminology yet.	

Heat
""""

.. math::
	+  \sum_{a\in A, g\in G^{heat} } ( \pi^{omv,gen,out}_{a,g} \cdot  \sum_{t\in T} ( {\color{blue}\gamma^{CV}_g} \cdot v^{gen,heat}_{y,a,g,t} )  )  

Hydro price profiles
""""""""""""""""""""

.. math::

	+  \sum_{a\in A, g\in G^{hyrs}} (  \sum_{t\in T} ( {{HYPPROFILS}}_{a, IS3} \cdot v^{gen,elec}_{y,a,g,t} )  )  
	

Constraints
'''''''''''

QEEQ: Electricity generation equals demand (MW)
"""""""""""""""""""""""""""""""""""""""""""""""

.. math::

	&\sum_{a\in A(r)} \sum_{g\in G^{elec}} {v^{gen}_{y,a,g,t}}  + \sum_{r\in R} {v^{trans}_{y,r,r',t}} (1-{\gamma^{trans}_{r,r'}})

	& - \sum_{a\in A(r)} \sum_{g\in G^{storage}} {\color{red}{{VESTOLOADT}}_{y,a,g,t}} - \sum_{a\in A(r)} \sum_{g\in G^{storage}} {\color{red}{{VESTOLOADTS}}_{y,a,g,t}}
	
	&= {\color{red}{{IX3FX\_T}}_{y,r,t}} +\sum_{r\in R} {v^{trans}_{y,r,r',t}}
	
	&+ \frac{\sum_{\color{red}{DEUSER}}\frac{{{\color{red}{DE}}_{y,r,\color{red}{DEUSER}}} \cdot {\epsilon^{gen}_{r,\color{red}{DEUSER},t}} }{{\color{red}{{IDE\_SUMST}}_{r,DEUSER}}}[\color{red}{IDE\_SUMST}_{r,\color{red}{DEUSER}>0}]}{(1-{\color{red}{{DISLOSS\_E}}_{r}})},
 
	&\forall y \in Y, r\in R, t\in T
	

Marked in red: things that are not in the terminology. All of these are explained in the following table:

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - Name 
     - Domains 
     - Type
     - Description
   * - DEUSER 
     - DEUSER 
     - Set 
     - Electricity demand user groups
   * - DE 
     - y,r,DEUSER 
     - Parameter 
     - Annual electricity consumption (MWh)
   * - IDE\_SUMST 
     - r,DEUSER 
     - Parameter 
     - Annual amount of nominal electricity demand (MWh)  
   * - DISLOSS\_E 
     - r
     - Parameter
     - Loss in electricity distribution (fraction)  
   * - IX3FX_T 
     - y,r,t 
     - Parameter 
     - Fixed export to third countries for each time segment (MW)
   * - VESTOLOADT 
     - y,a,g,t 
     - Variable (positive)
     - Intra-seasonal electricity storage loading (MW)  
   * - VESTOLOADTS 
     - y,a,g,t 
     - Variable (positive)
     - Inter-seasonal electricity storage loading (MW) 

	
Not relevant for Open_MODEX scenario runs
'''''''''''''''''''''''''''''''''''''''''
so far (should be inside the summation of the y) - should we include them? Not in OpenMODEX terminology yet.	

Heat (left side of equation)
""""""""""""""""""""""""""""

.. math::
	- \sum_{a\in A(r)} {\sum_{g\in G^{heat}} v^{gen}_{y,a,g,t}} 


QGFEQ: Calculate fuel consumption, existing units (MW)
""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. math::

	&{v^{fuse}_{y,a,g,t}}  = ( ( \frac{v^{gen}_{y,a,g,t}}{\gamma^{total,gen}_{g}[1$(NOT {\color{red}{GEFFRATE}}_{a,g})+\color{red}{GEFFRATE}_{a,g}]})$[g\in G^{elec}\setminus \color{red}{GSET}]
	
	&+ (\frac{{\color{blue}\gamma^{CV}_g}\cdot v^{gen,heat}_{y,a,g,t}}{\gamma^{total,gen}_{g}[1$(NOT \color{red}{GEFFRATE}_{a,g})+\color{red}{GEFFRATE}_{a,g}]})$[g\in G^{heat}] )$[NOT \color{red}{IGBYPASS}_g]
	
	& + ( {\color{blue}\gamma^{CB}_g} \frac{(\frac{ \color{red}{GDBYPASSC}_{g} \cdot v^{gen,heat}_{y,a,g,t} + v^{gen}_{y,a,g,t}}{{\color{blue}\gamma^{CB}_g}+\color{red}{GDBYPASSC}_{g}})}{{\gamma^{total,gen}_{g}}[1$(NOT \color{red}{GEFFRATE}_{a,g})+\color{red}{GEFFRATE}_{a,g}]}

	& + {\color{blue}\gamma^{CV}_g}\frac{(\frac{ \color{red}{GDBYPASSC}_{g} \cdot v^{gen,heat}_{y,a,g,t} + v^{gen}_{y,a,g,t}}{{\color{blue}\gamma^{CB}_g}+\color{red}{GDBYPASSC}_{g}})}{{\gamma^{total,gen}_{g}}[1$(NOT \color{red}{GEFFRATE}_{a,g})+\color{red}{GEFFRATE}_{a,g}]} )$(\color{red}{IGBYPASS}_g)

	& \forall y \in Y, r\in R, g\in G, t\in T


Marked in red: things that are not in the terminology. All of these are explained in the following table:

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - Name 
     - Domains 
     - Type
     - Description
   * - GSET 
     - g
     - Set 
     - Electric heaters, heat pumps,electrolysis plants  
   * - \gamma^{total,gen}_{g} 
     - g
     - Parameter 
     - Fuel efficiency (GDATA(G,'GDFE'))
   * - GDBYPASSC 
     - g 
     - Parameter 
     - ramp-down limit (% of capacity/h) (GDATA(G,'GDBYPASSC') )
   * - GEFFRATE 
     - a,g 
     - Parameter 
     - Fuel efficiency rating (strictly positive, typically close to 1; default/1/, use eps for 0)
   * - IGBYPASS 
     - g
     - Set
     - Technologies that may apply turbine bypass mode (subject to option bypass) 
   * - \color{blue}\gamma^{CV} 
     - g 
     - Parameter 
     - Cb-value for CHP (GDATA(G,'GDCB'))
   * - \color{blue}\gamma^{CV} 
     - g 
     - Parameter 
     - Cv-value for CHP-Ext (GDATA(G,'GDCV'))
	 
	 	
QESTOVOLTS: Inter-seasonal electricty storage dynamic equation (MWh)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""