Archive
=======

.. include:: ../macros.rst

.. Besides math operations and set membership in formulas only placeholders
   should be used to promote consistency.
   To include a new placeholder update `../macros.rst` AND `../notation.rst`.
   This is a global registry of symbol plus superscript combinations
   representing a unique parameter or variable name. The definition of sets is
   also part of `../notation.rst`.

Modelling of technologies
*************************
Here the framework's representations of technologies are shown

VRE-units
'''''''''

.. figure:: images/balmorel_VRE.png
   :width: 70 %

   Used in: Balmorel
   
.. figure:: images/vre_unit_genesys2.png
   :width: 70 %

   Used in: GENESYS_2

Balmorel
""""""""
The related equation for this technology is (TO BE UPDATED):

.. math::

	{v^{gen}_{y,a,g,t}}  = (v^{inv,capa}_{y,a,g}+\kappa^{capa}_{y,a,g})\cdot \gamma^{in,gen}_{g,t} \quad \forall y \in Y, a\in A, g\in G, t\in T

Note - the full load hour is used to generate the profile (the resulting profile here called :math:`\gamma^{in,gen}_{g,t}`) so that it can be scaled according to expected future hours of sun while sticking to the same profile with respect to relative changes.

Urbs
""""
Uses generic process equations. Only difference is that additionally the input depends on the timeseries of the corresponding commodity input/maxinput ratio.


.. math::

    &v^{\text{in}}_{t,y,r,g,c}=\kk_{y,r,g}\cdot \gamma^{\text{supim}}_{r,c,y,t}\cdot \Delta t \\
    &\forall t \in T_m, ~y \in Y, ~r \in R, ~g \in G, ~c \in C^{\text{supIm}}


GENESYS-2
"""""""""
Capacity factor (CF) ist used to calculate generation of VRE-units. \Delta t always equals one hour.

.. math::

	{v^{gen}_{y,r,g,t}}  = v^{capa}_{y,r,g} \cdot CF^{in,gen}_{y,r,g,t} \cdot \Delta t \quad \forall y \in Y, r\in R, g\in G, t\in T
    



Electricity-only units
''''''''''''''''''''''

.. figure:: images/balmorel_elec.png
   :width: 70 %
   
   Used in: Balmorel
   
.. figure:: images/electricity_only_unit_genesys2.png
   :width: 70 %
   
   Used in: GENESYS_2

Balmorel
""""""""

The related equation for this technology is:

.. math::

	{\vu_{y,a,g,t}}  = \frac{\vg_{y,a,g,t}}{\gi_{g}} \quad \forall y \in Y, a\in A, g\in G, t\in T


Urbs
""""
Uses generic process equations.


GENESYS-2
"""""""""
Generation is calculated by using overall plant efficiencies, that are time-independent. \Delta t always equals one hour.

.. math::

	{v^{gen}_{y,r,g,t}}  = v^{fuse}_{y,r,g,t} \cdot \gamma^{total,gen}_{g} \cdot \Delta t \quad \forall y \in Y, r\in R, g\in G, t\in T


Heat-only units
'''''''''''''''

.. figure:: images/balmorel_heat.png
   :width: 70 %

   Used in: Balmorel

Balmorel
""""""""

The related equation for this technology is:

.. math::

	{\vu_{y,a,g,t}}  = \frac{\vh_{y,a,g,t}}{\gi_{g}} \quad \forall y \in Y, a\in A, g\in G, t\in T


Urbs
""""
Uses generic process equations.


GENESYS-2
"""""""""
Currently not modelled with this framework.


CHP units: backpressure
'''''''''''''''''''''''

.. figure:: images/balmorel_chpbp.png
   :width: 70 %

   Used in: Balmorel

Balmorel
""""""""

The related equation for this technology is:

The related equations for this technology is:

1. Fuel usage

.. math::

	& {\vu_{y,a,g,t}}  = \frac{\vg_{y,a,g,t} + \gV_g \cdot \vh_{y,a,g,t}}{\gi_{g}}
	
	& \forall y \in Y, a\in A, g\in G, t\in T

2. Limited by Cb-line:

.. math::

	\vg_{y,a,g,t} = \vh_{y,a,g,t} \cdot \gB_g \quad \forall y \in Y, a\in A, g\in G, t\in T


Urbs
""""
Not modeled in urbs.


GENESYS-2
"""""""""
Currently not modelled with this framework.


CHP units: extraction
'''''''''''''''''''''

.. figure:: images/balmorel_chpext.png
   :width: 70 %

   Used in: Balmorel

Balmorel
""""""""

The related equations for this technology is:

1. Fuel usage

.. math::

	& {\vu_{y,a,g,t}}  = \frac{\vg_{y,a,g,t} + \gV_g \cdot \vh_{y,a,g,t}}{\gi_{g}}
	
	& \forall y \in Y, a\in A, g\in G, t\in T

2. Limited by Cb-line:

.. math::

	\vg_{y,a,g,t} \geq \vh_{y,a,g,t} \cdot \gB_g \quad \forall y \in Y, a\in A, g\in G, t\in T

3. Limited by Cv-line:

.. math::

	\vg_{y,a,g,t} \leq \kk_{y,a,g} + v^{capa}_{y,a,g} - \vh_{y,a,g,t} \cdot \gV_g \quad \forall y \in Y, a\in A, g\in G, t\in T


Urbs
""""
Not modeled in urbs.


GENESYS-2
"""""""""
Currently not modelled with this framework.


Storages
''''''''

.. figure:: images/balmorel_sto.png
   :width: 70 %

   Used in: Balmorel
   
.. figure:: images/storage_unit_genesys2.png
   :width: 70 %

   Used in: GENESYS_2


Balmorel
""""""""

The necessary equation for this technology is:

.. math::
	& \vsv_{y,a,g,t+1} = \vsv_{y,a,g,t}\cdot \gt_{g} + \vsl_{y,a,g,t}\cdot \gi_{g} - \vg_{y,a,g,t} \cdot \go_{g}

	& \forall y \in Y, a\in A, g\in G, t\in T
    
urbs
""""

.. math::
   &\vsv_{t,y,r,s,c}=\vsv_{(t-1),y,r,s,c}\cdot (1-\gL_{y,r,s,c})^{\Delta t}+\gi_{y,r,s,c}\cdot \vsl_{t,y,r,s,c}- \frac{\vsu_{t,y,r,s,c}}{\go_{y,r,s,c}}\\
    &\forall t\in T_m,~y\in Y,~r\in R,~s\in S,~c\in C

GENeSYS-MOD	
"""""""""""

Do I understand it correct with Balmorel that \vsv refers to the amount of energy in a storage at a given time? Then I will use it this way here as well.

.. math::

    &\vsv_{g,r,t,y} = \vsv_{g,r,t-1,y} + \vsl_{g,r,t-1,y}\cdot \gamma^{in}_{g,y} - \frac{\vsu_{g,r,t-1,y}}{\gamma^{in}_{g,y}} \quad \forall g \in G, r \in R, t \in T, y \in Y\\



oemof.tabular
"""""""""""""

.. math::

  & \epsilon^{con}_{y,r,g,t} =
    \epsilon^{con}_{y,r,g,t-1} \cdot (1 - \gL_{r,g})
    - \frac{\epsilon^{out}_{y,r,g,t}}{\gamma^{out}_{r,g}}
    + \epsilon^{in}_{y,r,g,t} \cdot \gamma^{in}_{y,r,g}
  \\
  & {\epsilon^{con}_{y,r,g,t_0} = \epsilon^{con}_{y,r,g,t_{\infty}}} \\
  & t_0, t_{\infty} \in T
  \\
  & \forall y \in Y, r\in R, g\in G, t\in T\setminus\{t_0\}
  
  

GENESYS-2
"""""""""
Generally, storages in GENESYS-2 always require a storage unit connected to a charger/discharger unit. Charger and discharger can either be one unit called 'Bicharger' or can be modelled seperately with diffrent efficiencies.

initial storage level
---------------------
.. math::
	{v^{sto,vol}_{y,r,g,t=0}}  = 0 \quad \forall y \in Y, r\in R, g\in G, t\in T \\
	
charge/discharge processes
--------------------------
.. math::
	{v^{gen,load}_{y,r,g,t}}  = v^{sto,charge}_{y,r,g,t} \cdot \gamma^{in,gen}_{y,r,g,t} \cdot \Delta t \quad \forall y \in Y, r\in R, g\in G, t\in T \\
	{v^{gen,unload}_{y,r,g,t}}  = v^{sto,discharge}_{y,r,g,t} \cdot \gamma^{out,gen}_{y,r,g,t} \cdot \Delta t \quad \forall y \in Y, r\in R, g\in G, t\in T \\
	Condition: v^{gen,load}_{y,r,g,t} >= 0 + v^{gen,unload}_{y,r,g,t} > 0 = 1

storage level
--------------------------
.. math::
	{v^{sto,vol}_{y,r,g,t}}  = v^{sto,vol}_{y,r,g,t-1} + v^{gen,load}_{y,r,g,t} - v^{gen,unload}_{y,r,g,t} \cdot (1+\gamma^{total,gen,sto}_{y,r,g,t}) \quad \forall y \in Y, r\in R, g\in G, t\in T \\

total losses
--------------------------
.. math::
	{\gamma^{loss,con}_{y,r,g,t}}  = v^{sto,charge}_{y,r,g,t} \cdot (1 - \gamma^{in,gen}_{y,r,g,t}) + v^{sto,discharge}_{y,r,g,t} \cdot (1 - \gamma^{out,gen}_{y,r,g,t}) + v^{gen,load}_{y,r,g,t} \cdot (1 - \gamma^{total,gen,sto}_{y,r,g,t})  \quad \forall y \in Y, r\in R, g\in G, t\in T \\
 
 

Generation
''''''''''

oemof.tabular
"""""""""""""

Dispatchable
------------

.. math::

  & {0 <= \vg_{y,r,g,t} <= \kk_{r,g}}
  \\
  & \yrgt


Conversion
----------

.. math::

  & {\vu_{y,r,g,t}} =
  \frac{1}{\go_{r,g}}{\vg_{y,r,g,t}}
  \\
  & \yrgt


Volatile
--------

.. math::

  & {\vg_{y,r,g,t} = \kk_{r,g} \cdot \gamma^{capa}_{y,r,g,t}}
  \\
  & \yrgt


Consumption
'''''''''''

oemof.tabular
"""""""""""""

Load
----

.. math::

  & {E^{gen}_{y,r,g,t} = E^{capa}_{y,r,g,t}}
  \\
  & \yrgt


Bus
'''

oemof.tabular
"""""""""""""

Bus
---

.. math::

  & {v^{in}_{y,r,g,t} = \vg_{y,r,g,t}}
  \\
  & \yrgt


Grid
''''

oemof.tabular
"""""""""""""

Link
----

.. image:: images/link.png
   :width: 50 %

.. math::

  & {v^{trans,in_i}_{y,r,g,t} =
    \frac{1}{\gamma^{trans}_{r,g}} \cdot v^{trans,gen_i}_{y,r,g,t}}
  \\
  & \yrgt, i \in \{1, 2\}


urbs
""""

.. math::

   & v^{\text{trans,out}}_{t,y,r_{in},r_{out},x,c}= v^{\text{trans,in}}_{t,y,r_{in},r_{out},x,c}\cdot \gamma^{\text{trans}}_{y,r_{in},r_{out},x,c}\\
    &\forall t\in T_m,~y\in Y,~r_{in}\in R,~r_{out}\in R,~x\in X,~c\in C
	

GENESYS-2
"""""""""
	
.. math::

   & v^{\text{trans,out}}_{t,y,r_{in},r_{out},x,c}= v^{\text{trans,in}}_{t,y,r_{in},r_{out},x,c}\cdot \gamma^{\text{trans}}_{y,r_{in},r_{out},x,c}\\
    &\forall t\in T_m,~y\in Y,~r_{in}\in R,~r_{out}\in R,~x\in X,~c\in C


Generic processes
'''''''''''''''''

urbs
""""

Every generic process is described by the following equations:

.. math::

    &v^{\text{in}}_{t,y,r,g,c}=\gi_{y,g,c} \cdot \tau_{t,y,r,g} \\
    &\vg_{t,y,r,g,c}=\go_{y,g,c} \cdot \tau_{t,y,r,g} \\
    &\tau_{t,y,r,g}\leq \Delta t \cdot \kk_{y,r,g} \\
    &\forall t \in T_m, y \in Y, ~r \in R, ~g \in G, ~c \in C


Processes can also have a maximum change in throughput in a single time step, which is modeled by:

.. math::

    &\tau_{t-1,y,r,g} - \kk_{y,r,g} \cdot \gamma^{\Delta\tau^{max}}_{y,r,g} \cdot \Delta t \leq \tau_{t,y,r,g} \\
    &\tau_{t-1,y,r,g} + \kk_{y,r,g} \cdot \gamma^{\Delta\tau^{max}}_{y,r,g} \cdot \Delta t \geq \tau_{t,y,r,g} \\
    &\forall t \in T_m, y \in Y, ~r \in R, ~g \in G, ~c \in C


Some processes also have a minimum throughput ratio (minimum throughput/maximum throughput) for operation and a different efficieny when operating with less than maximum throughput:

.. math::

    &\tau_{t,y,r,g} \geq \kk_{y,r,g} \cdot \gamma^{\text{min}}_{y,r,g}  \cdot \Delta t \\
    &v^{\text{in}}_{t,y,r,g,c}=\Delta t \cdot \kk_{y,r,g} \cdot \frac{\gamma^{\text{min}}_{y,r,g} \cdot (\gamma^{\text{in,gen,min}}_{y,g,c}-\gi_{y,g,c})}{1-\gamma^{\text{min}}_{y,r,g}} + \tau_{t,y,r,g} \cdot \frac{\gi_{y,g,c}-\gamma^{\text{min}}_{y,r,g} \cdot \gamma^{\text{in,gen,min}}_{y,g,c}}{1-\gamma^{\text{min}}_{y,r,g}}\\
    &\vg_{t,y,r,g,c}=\Delta t \cdot \kk_{y,r,g} \cdot \frac{\gamma^{\text{min}}_{y,r,g} \cdot (\gamma^{\text{out,gen,min}}_{y,g,c}-\go_{y,g,c})}{1-\gamma^{\text{min}}_{y,r,g}} + \tau_{t,y,r,g} \cdot \frac{\go_{y,g,c}-\gamma^{\text{min}}_{y,r,g} \cdot \gamma^{\text{out,gen,min}}_{y,g,c}}{1-\gamma^{\text{min}}_{y,r,g}}\\
    &\forall t \in T_m, y \in Y, ~r \in R, ~g \in G, ~c \in C



GENeSYS-MOD	
"""""""""""

.. figure:: images/genesysmod_generic.png
   :width: 70 %
   
This equation counts for all processes, no matter how many input or output fuels are required.   

.. math::

    &\frac{{v^{gen}_{f,g,m,r,t,y}}}{\gamma^{out_gen}_{f,g,m,r,y}} = \sum_{f\in F} v^{fuse}_{f,g,m,r,t,y} \cdot \gamma^{in_gen}_{f,g,m,r,y} \quad \forall f \in F, g \in G, m \in M, r \in R, t \in T, y \in Y\\ 
	
	
intertemporal
'''''''''''''

How are costs handled in intertemporal models (investments and also other types of costs

GENESYS-2
"""""""""
	
.. math::
	\pi^{intertemporal,year1,year2,yearX} = \pi^{anuity,capa,gen,year1} + \pi^{anuity,capa,gen,year2} + \pi^{anuity,capa,gen,yearX}
   



Balmorel
********
On this page, the most important equations like the objective function and constraints are stated.

Objective function
''''''''''''''''''

I have added input and output to the OM costs as we have it divided.

Our fuel use is in MWh and we use the fuel price in Euro/Mwh (Open_MODEX terminology: euro/EJ) - this should be made clear here.


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
	 
oemof.tabular
*************


Objective function
''''''''''''''''''

The objective function is constructed initializing the model and depends on the objects used to define the energy system. For the most part the objective function is determined by which classes were used to represent flows on edges in an energy system graph representation.
The following terms representing energy system relevant concepts found in the modex scenarios can be implemented and be part of an objective function. This description adhering to the modex terminology is not considered to be complete or exhaustive as of yet.


.. math::

    \pi^{obj} =

    & \sum_{r\in R, g\in G, f\in F(g)} ( \pi^{fuel}_{r, f} \cdot \sum_{t\in T} ( v^{fuse}_{r, t, g} ) )

    & + \sum_{r\in R, g\in G} ( \pi^{omf, gen}_{g, r} \cdot \sum_{t\in T} ( v^{gen}_{r, t, g} ) )

    & + \sum_{r\in R, rr\in RR, t\in T } ( \pi^{omv, trans}_{r, rr} \cdot \sum_{t\in T} ( v^{trans}_{r,rr,t} ) )

    & + \sum_{r\in R, f\in F(g)} ( \pi^{emi}_{f, r} \cdot \sum_{t\in T} ( v^{fuse}_{r, t, g} \cdot \psi^{emi}_{g, CO2} ) )

    & + \sum_{r\in R, g\in G} ( v^{inv, capa}_{r, g} \cdot ( \pi^{inv, capa}_{r, g} + \pi^{omf, capa}_{r, g} ) )

Constraints
'''''''''''

Storages
""""""""

The storage balance is given by:

.. math::

  \epsilon(t) = \\
  \epsilon(t-1) \cdot (1 - \gamma^{frac}(t))^{ \Delta t(t)/(t_u)} \\
  - \gamma^{fix}(t)\cdot (\epsilon_{exist} + \epsilon_{invest}) \cdot {\Delta t(t) /(t_u)}\\
  - \gamma^{abs}(t) \cdot {\Delta t(t) /(t_u)}\\
  - \frac{\epsilon^{out}(t)}{\gamma_{out}(t)} \cdot \Delta t(t)\\
  + \epsilon_{in}(t) \cdot \gamma_{in}(t) \cdot \Delta t(t)

=========================== =======================
symbol                      explanation
=========================== =======================
:math:`\epsilon(t)`         energy currently stored
:math:`\epsilon_{nom}`      nominal capacity of the energy storage
:math:`c(-1)`               state before initial time step
:math:`c_{min}(t)`          minimum allowed storage
:math:`c_{max}(t)`          maximum allowed storage
:math:`\gamma^{frac}(t)`            fraction of lost energy as share of :math:`E(t)` per time unit
:math:`\gamma^{fix}(t)`     fixed loss of energy  relative to :math:`E_{nom}` per time unit
:math:`\gamma^{abs}(t)`           absolute fixed loss of energy per time unit
:math:`\dot{E}_i(t)`        energy flowing in
:math:`\dot{E}_o(t)`        energy flowing out
:math:`\gamma_in(t)`        conversion factor(i.e. efficiency) when storing energy
:math:`\gamma_out(t)`       conversion factor when
                            (i.e. efficiency)
                            taking stored energy
:math:`\Delta t(t)`          duration of time step
:math:`t_u`                 time unit of :math:`\gamma^{frac}, `\gamma^{fix}(t), \gamma^{abs}(t)` and timeincrement :math:`\tau(t)`
=========================== =======================


Maximum invement is bounded by lower and upper bound set:

.. math::
      \epsilon_{invest, min} \le E_{invest} \le E_{invest, max}

The following constraints are created depending on the attributes

If an initialstorage level is given:

.. math:: \epsilon(-1) \le \epsilon_{invest} + \epsilon_{exist}

if not:

.. math:: \epsilon(-1) = (\epsilon_{invest} + \epsilon_{exist}) \cdot c(-1)

Possible coupling of first and last timestep

.. math:: \epsilon(-1) = \epsilon(t_{last})

Possible to set C-rate of input and storage content by connecting the invest
variables of the storage and the input flow:

.. math::
        \epsilon_{in,invest} + \epsilon_{in,exist} =
        (\epsilon_{invest} + \epsilon_{exist}) \cdot r_{cap,in}

and/or for generation of storage

.. math::
    \epsilon_{out,invest} + \epsilon_{out,exist} =
    (\epsilon_{invest} + \epsilon_{exist}) \cdot r_{cap,out}

If wanted connect the invest variables of the input and the output:

.. math::
    \epsilon_{in,invest} + \epsilon_{in,exist} =
    (\epsilon_{out,invest} + \epsilon_{out,exist}) \cdot r_{in,out}

Upper and lower storage level is given by:

.. math::
    \epsilon(t) \leq (\epsilon_{exist} + \epsilon_{invest}) \cdot c_{max}(t)

.. math:: \epsilon(t) \geq (\epsilon_{exist} + \epsilon_{invest}) \cdot c_{min}(t)




CHP Extraction Turbine
""""""""""""""""""""""

.. math::

  v^{gen, el} \leq \kappa^{capa} \\
  \kappa^{capa} \leq \overline{\kappa}^{capa}

.. math::
    v^{fuse}(t) =
    \frac{v^{gen, el}(t) + v^{gen, th}(t) \
    \cdot \beta(t)}{\gamma^{cond}(t)}
    \qquad \forall t \in T

.. math::
    v^{gen, el}(t)  \geq  v^{gen, th}(t) \cdot
    \frac{\gamma^{el}(t)}{\gamma^{th}(t)}
    \qquad \forall t \in T


where :math:`\gamma^{cond}` is the electrical efficiency in full extraction mode
and :math:`\beta` is the power-loss index defined as:

.. math::
    \beta(t) = \frac{\gamma^{cond}(t) -
    \gamma^{el}(t)}{\gamma^{th}(t)}
    \qquad \forall t \in T


CHP Backpressure Turbine
""""""""""""""""""""""""

Backpressure turbines are modelled based on their time dependent electrical
and thermal efficiency in backpressure mode.

.. math::

    v^{fuse}(t) =
    \frac{v^{gen, el}(t) + v^{gen, th}(t)}{\gamma^{th}(t) + \gamma^{el}(t)}
    \qquad \forall t \in T

.. math::

    \frac{v^{gen, el}(t)}{v_{gen, th}(t)} =
    \frac{\gamma^{el}(t)}{\gamma^{th}(t)}
    \qquad \forall t \in T

urbs
****
On this page, the most important equations like the objective function and constraints are stated.

Objective function
''''''''''''''''''
The objective function consists of five parts:

.. math::

    \pi^\text{obj} = \pi_{\text{inv}} + \pi_{\text{fix}} + \pi_{\text{var}} + \pi_{\text{fuel}} + \pi_{\text{env}}


Investment costs

    * consists of investment costs for generation, transmission and storage
    * investment costs for trans and sto are calculated the same way as for gen,
      except sto costs are based on newly installed storage capacity **and** power

.. math::

    \pi_{\text{inv}}= \pi_{\text{inv,gen}} + \pi_{\text{inv,trans}} + \pi_{\text{inv,sto}}

    \pi_{\text{inv,gen}} = \sum_{p \in P} {\color{red}{{INVESTFAC}}_{p}} \cdot \pi^{\text{inv, capa}}_p \cdot {\color{red}{{NEWCAPACITY}}_{p}} -  \sum_{p \in P} {\color{red}{{OVRPAYFAC}}_{p}} \cdot \pi^{\text{inv, capa}}_p \cdot {\color{red}{{NEWCAPACITY}}_{p}}


Graphical representation and example of the calculation of total costs for an investment

.. figure:: images/urbs_costfac.png
   :width: 70 %

.. figure:: images/urbs_costfac2.png
   :width: 70 %


Fixed costs for operation and maintenance

    * consists of fixed costs for generation, transmission and storage
    * fixed costs for trans and sto are calculated the same way as for gen,
      except again sto costs are based on installed storage capacity **and** power

.. math::

    \pi_{\text{fix}}= \pi_{\text{fix,gen}} + \pi_{\text{fix,trans}} + \pi_{\text{fix,sto}}

    \pi_{\text{fix,gen}}=\sum_{p \in P} {\color{red}{{COSTFAC}}_{p}} \cdot \pi^{\text{omf,capa}}_p \cdot \kappa^{\text{capa}}_p


Variable operation and maintenance costs

    * consists of fixed costs for generation, transmission and storage
    * fixed costs for trans and sto are calculated the same way as for gen,
      except trans costs are only based on transmission input and sto costs are based on energy content, inflow and outflow

.. math::

    \pi_{\text{var}}= \pi_{\text{var,gen}} + \pi_{\text{var,trans}} + \pi_{\text{var,sto}}

    \pi_{\text{var,gen}}=\sum_{t \in T_m\\ p \in P} \pi^{\text{omv,gen}}_{p} \cdot {\color{red}{Weight}} \cdot {\color{red}{{COSTFAC}}_{p}} \cdot \tau_{t,p}


Fuel costs

.. math::

    \pi_{\text{fuel}}=\sum_{t \in T_m\\ f \in F} \pi^{\text{fuel}}_{f} \cdot {\color{red}{Weight}} \cdot {\color{red}{{COSTFAC}}_{f}} \cdot v^{\text{fuse}}_{t,f}


Environment costs like costs for CO_2 emissions

.. math::

    \pi_{\text{env}}= \sum_{t \in T_m\\ e \in E} \pi^{\text{emi}}_{e} \cdot {\color{red}{Weight}} \cdot {\color{red}{{COSTFAC}}_{e}} \cdot -{\color{red}{{CB(e,t)}}}



Marked in red: things that are not in the terminology. All of these are explained in the following table:

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1


   * - Name
     - Domains
     - Type
     - Description
   * - P
     - -
     - Set
     - Tuple including all sets describing processes (year, site, process)
   * - F, E
     - -
     - Set
     - Tuples inluding all sets describing commodities (year, site, com, com type), where e is the subset of stock and f the subset of environmental commodities
   * - INVESTFAC
     - p
     - Parameter
     - Scales the investment costs taking into account the depreciation duration, interest rate and discount rate
   * - OVRPAYFAC
     - p
     - Parameter
     - Similar to INVESTFAC but calculates the investment cost payments that fall beyond the optimization period, thus should not be considered
   * - NEWCAPACITY
     - p
     - Variable
     - Amount of new capacity of a technology
   * - COSTFAC
     - p, e or f
     - Parameter
     - Includes discount factor and relative weight of a year for intertemporal model, for single year equals one
   * - Weight
     - -
     - Parameter
     - Scales the costs to a full year
   * - CB(e,t)
     - -
     - Function
     - Balance equation returning the amount of environmental commodity created




Constraints
'''''''''''

Process expansion constraints
"""""""""""""""""""""""""""""
The unit expansion constraints are independent of the modeled time. In case of
the minimal model the are restricted to two constraints only limiting the
allowed capacity expansion for each process. The total capacity of a given
process is simply given by:

.. math::
   &\forall y \in Y, \forall g \in G:\\
   &\kappa_{y,g}=K_{y,g} + \widehat{\kappa}_{y,g},

where :math:`K_{y,g}` is the already installed capacity of process (generator) :math:`g` in year `y`.

Process capacity limit rule
"""""""""""""""""""""""""""
The capacity pf each process :math:`g` is limited by a maximal and minimal
capacity, :math:`\overline{K}_g` and :math:`\underline{K}_g`, respectively,
which are both given to the model as parameters:

.. math::
   &\forall y \in Y, \forall g \in G:\\
   &\underline{K}_{y,g}\leq\kappa_{y,g}\leq\overline{K}_{y,g}.

All further constraints are time dependent and are determinants of the unit
commitment, i.e. the time series of operation of all processes and commodity
flows.

Commodity dispatch constraints
""""""""""""""""""""""""""""""
In this part the rules governing the commodity flow timeseries are shown.  

Vertex rule ("Kirchhoffs current law")
""""""""""""""""""""""""""""""""""""""
This rule is the central rule for the commodity flows and states that all
commodity flows, (except for those of environmental commodities) have to be
balanced in each time step. As a helper function the already mentioned
commodity balance is calculated in the following way:

.. math::
   &\forall y \in Y, \forall d \in D,~t\in T_m:\\\\
   &\text{CB}(y,d,t)=
    \sum_{(d,g)\in D^{\mathrm{out}}_{g}}\epsilon^{\text{in}}_{y,d,g,t}-
    \sum_{(d,g)\in D^{\mathrm{in}}_g}\epsilon^{\text{out}}_{y,d,g,t}.

Here, the tuple sets :math:`D^{\mathrm{in,out}}_g` represent all input and
output commodities of process :math:`g`, respectively. The commodity balance
thus simply calculates how much more of commodity :math:`d` is emitted by than
added to the system via process :math:`g` in timestep :math:`t`. Using
this term the vertex rule for the various commodity types can now be written in
the following way:

.. math::
   \forall y \in Y, \forall d \in D_{\text{st}},~t \in T_m:\;
   \rho_{y,d,t} \geq \text{CB}(y,d,t),

where :math:`D_{\text{st}}` is the set of stock commodities and:

.. math::
   \forall y \in Y, \forall d \in D_{\text{dem}},~ t \in T_m:\;
   -E_{y,d,t} \geq \text{CB}(y,d,t),

where :math:`D_{\text{dem}}` is the set of demand commodities and
:math:`E_{y,d,t}` the corresponding demand for commodity :math:`d` at time
:math:`t` at year :math:`y`. These two rules thus state that all stock commodities that are
consumed at any time in any process must be taken from the stock and that all
demands have to be fulfilled at each time step.

Stock commodity limitations
"""""""""""""""""""""""""""
There are two rule that govern the retrieval of stock commodities from stock:
The total stock and the stock per hour rule. The former limits the total amount
of stock commodity that can be retrieved annually and the latter limits the
same quantity per timestep. the two rules take the following form:

.. math::
   &\forall y \in Y, \forall d \in D_{\text{st}}:\\
   &w \sum_{t\in T_{m}}\rho_{y,d,t}\leq \Lambda_{y,d}\\\\
   &\forall d \in D_{\text{st}},~t\in T_m:\\
   &\rho_{y,d,t}\leq \lambda_{y,d},

where :math:`\Lambda_{y,d}` and :math:`\lambda_{y,d}` are the totally allowed
annual and hourly retrieval of commodity :math:`d` from the stock,
respectively, in year :math:`y`.

Environmental commodity limitations
"""""""""""""""""""""""""""""""""""
Similar to stock commodities, environmental commodities can also be limited
per hour or per year. Both properties are assured by the following two
rules:

.. math::
   &\forall y \in Y, \forall d \in D_{\text{env}}:\\
   &-w \sum_{t\in T_{m}}\text{CB}(y,d,t)\leq \Lambda^\text{env}_{y,d}\\\\
   &\forall y \in Y, \forall d \in D_{\text{env}},~t\in T_m:\\
   & -\text{CB}(y,d,t)\leq \lambda^\text{env}_{y,d}\,

where :math:`\Lambda^\text{env}_{y,d}` and :math:`\lambda^\text{env}_{y,d}` are the totally allowed
annual and hourly emissions of environmental commodity :math:`d` to the
atmosphere, respectively, in year :math:`y`.

Process dispatch constraints
""""""""""""""""""""""""""""
So far, apart from the commodity balance function, the interaction between
processes and commodities have not been discussed. It is perhaps in order to
start with the general idea behind the modeling of the process operation. In
urbs all processes are mimo-processes, i.e., in general they in take in
multiple commodities as inputs and give out multiple commodities as outputs.
The respective ratios between the respective commodity flows remain normally
fixed. The operational state of the process is then captured in just one
variable, the process throughput :math:`\tau_{gt}` and is is linked to the
commodity flows via the following two rules:

.. math::
   &\forall y \in Y, \forall g\in G,~d\in D,~t \in T_m:\\
   &\epsilon^{\text{in}}_{y,g,d,t}=r^{\text{in}}_{y,g,d}\tau_{y,g,t}\\
   &\epsilon^{\text{out}}_{y,g,d,t}=r^{\text{out}}_{y,g,d}\tau_{y,g,t},

where :math:`r^{\text{in, out}}_{y,g,d}` are the constant factors linking the
commodity flow to the operational state. The efficiency :math:`\eta` of the
process :math:`g` for the conversion of commodity :math:`d_1` into commodity
:math:`d_2` is then simply given by:

.. math::
   \eta=\frac{r^{\text{out}}_{y,g,d_2}}{r^{\text{in}}_{y,g,d_1}}.

Basic process throughput rules
""""""""""""""""""""""""""""""
The throughput :math:`\tau_{gt}` of a process is limited by its installed
capacity and the specified minimal operational state. Furthermore, the
switching speed of a process can be limited:

.. math::
   &\forall y \in Y, \forall g\in G,~t\in T_m:\\
   &\tau_{y,g,t}\leq \kappa_{y,g}\\
   &\tau_{y,g,t}\geq \underline{P}_{y,g}\kappa_{y,g}\\
   &|\tau_{y,g,t}-\tau_{y,g,(t-1)}|\leq \Delta t\overline{PG}_{y,g}\kappa_{y,g},

where :math:`\underline{P}_{y,g}` is the normalized, minimal operational state of
the process and :math:`\overline{PG}_{y,g}` the normalized, maximal gradient of the
operational state in full capacity per timestep.

Intermittent supply rule
""""""""""""""""""""""""
If the input commodity is of type 'SupIm', which means that it represents an
operational state rather than a proper material flow, the operational state of
the process is governed by this alone. This feature is typically used for
renewable energies but can be used whenever a certain operation time series of
a given process is desired

.. math::
   &\forall y \in Y, \forall g\in G,~d\in D_{\text{sup}},~t\in T_m:\\
   &\epsilon^{\text{in}}_{y,g,d,t}=\gamma^{capa}_{y,g,t}\kappa_{y,g}.

Here, :math:`\gamma^{capa}_{y,g,t}` is the time series that governs the exact operation of
process :math:`g`, leaving only its capacity :math:`\kappa_{y,g}` as a free
variable.

Part load behavior
""""""""""""""""""
Many processes show a non-trivial part-load behavior. In particular, often a
nonlinear reaction of the efficiency on the operational state is given.
Although urbs itself is a linear program this can with some caveats be captured
in many cases. The reason for this is, that the efficiency of a process is
itself not modeled but only the ratio between input and output multipliers. It
is thus possible to use purely linear functions to get a nonlinear behavior of
the efficiency of the form:

.. math::
   \eta=\frac{a+b\tau_{y,g,t}}{c+d\tau_{y,g,t}},

where a,b,c and d are some constants. Specifically, the input and output ratios
can be set to vary linearly between their respective values at full load
:math:`r^{\text{in,out}}_{y,g,d}` and their values at the minimal allowed
operational state :math:`\underline{P}_{y,g}\kappa_{y,g}`, which are given by
:math:`\underline{r}^{\text{in,out}}_{y,g,d}`. This is achieved with the following
equations:

.. math::
   &\forall y \in Y, \forall g\in G^{\text{partload}},~d\in D,~t\in T_m:\\\\
   &\epsilon^{\text{in,out}}_{y,g,d,t}=\Delta t\cdot\left(
   \frac{\underline{r}^{\text{in,out}}_{g,d}-r^{\text{in,out}}_{y,g,d}}
   {1-\underline{P}_{y,g}}\cdot \underline{P}_g\cdot \kappa_{y,g}+
   \frac{r^{\text{in,out}}_{y,g,d}-
   \underline{P}_g\underline{r}^{\text{in,out}}_{y,g,d}}
   {1-\underline{P}_{y,g}}\cdot \tau_{y,g,t}\right).

A few restrictions have to be kept in mind when using this feature:

* :math:`\underline{P}_{y,g}` has to be set larger than 0 otherwise the feature
  will work but not have any effect.
* Environmental output commodities have to mimic the behavior of the inputs by
  which they are generated. Otherwise the emissions per unit of input would
  change together with the efficiency, which is typically not the desired
  behavior.

Genesys2
********
On this page, the most important equations like the objective function and constraints are stated.

Objective function
''''''''''''''''''


.. math::

	\pi^{\text{objective}} = C_{\text{real}}(\pi^{inv,capa,g},\pi^{omf,capa,g},\pi^{omv,gen,g}) + C_{\text{penalty}}(\varepsilon^{\text{deviation}})

	\pi^{\text{objective}} = \sum_{T_{interval}}^{} \sum_{regions}^{} \sum_{components}^{} \pi^{inv,capa,g} + \pi^{omf,capa,g} + \pi^{omv,gen,g} + \sum_{years}^{} \sum_{regions}^{} \pi^{penalty,unsupplied\_load} (\varepsilon^{\text{unsupplied}})^2 + \pi^{penalty,selsupplied\_quota} \varepsilon^{\text{selfsupply}}

	\pi^{\text{objective}} = \sum_{T_{interval}}^{} \sum_{regions}^{} \sum_{components}^{} ANF*[\pi^{inv,capa,g} + \pi^{inv,capa,g} \gamma^{inv,capa,g}] + \pi^{omv,gen,g} + \sum_{T_{interval}}^{} \sum_{regions}^{} \pi^{penalty,unsupplied\_load} (\varepsilon^{\text{unsupplied}})^2 + \pi^{penalty,selsupplied\_quota} \varepsilon^{\text{selfsupply}}
	
	\pi^{\text{objective}} = \sum_{T_{interval}}^{} \sum_{regions}^{} \sum_{components}^{} \frac{(1+i)^{n}i}{(1+i)^{n}-1}*[\pi^{inv,capa,g} + \pi^{inv,capa,g} \gamma^{inv,capa,g}] + [\pi^{fuel,f}+\pi^{emi,e}] \varepsilon^{gen,t} + \sum_{T_{interval}}^{} \sum_{regions}^{} \pi^{penalty,unsupplied\_load} (\varepsilon^{\text{unsupplied}})^2 + \pi^{penalty,selsupplied\_quota} \varepsilon^{\text{selfsupply}}

GENeSYS-MOD
***********
On this page, the most important equations like the objective function and constraints are stated.

Objective function
''''''''''''''''''


.. math::

	
	{{\pi}}  & =  \sum_{y\in Y} ({\color{red}{{IDISCOUNTFACTOR}}_{y}} \cdot {\color{red}{{IWEIGHTY}}_{y}} \cdot  (  

	& \sum_{c\in C, g\in G, m\in M, t\in T} ( \pi^{omv,gen}_{c, g, m, y} \cdot   v^{gen}_{c, g, m, t, y}   )
	
	& + \sum_{c\in C, g\in G} (\pi^{omf,capa}_{c, g, y} \cdot \kappa^{capa}_{c, g, y})
	
	& + \sum_{c\in C, g\in G} (\pi^{inv,capa}_{c, g, y} \cdot {\color{red}{{NEWCAPACITY}}_{c, g, y}})
	
	& + \sum_{c\in C, f\in F, g\in G, m\in M, t\in T} (\psi^{emi}_{f} \cdot \gamma^{in,gen}_{g, c, f, m, y} \cdot v^{gen}_{c, g, m, t, y} \cdot \pi^{emi}_{c, e})
	
	& + \sum_{c\in C, \color{red}{{s\in S}}} (\pi^{inv,capa}_{c, s, y} \cdot {\color{red}{{NEWCAPACITY}}_{c, s, y}})
	
	& + \sum_{f\in F, r,r'\in R, t\in T} (v^{trans}_{r, r', t, f, y} \cdot \pi^{omv,trans}_{f, r, r', y})
	
	& + \sum_{r,r'\in R, y\in Y} (\color{red}{{NEWTRADECAPACITY}}_{r, r', 'Electricity', y} \cdot \color{red}{TRADECAPACITYCOST}_{r, r', 'Electricity'})
	
	& ))
	
	& - (1-{\color{red}{{IDISCOUNTFACTOR}}_{y}} \cdot {\color{red}{{IWEIGHTY}}_{y}}) \cdot (
	
	&   \sum_{c\in C, g\in G, t\in T, y\in Y|(y+\color{red}{{OPERLIFE}}_{c, g})>\color{red}{{MAXYEAR}}} (0.8 \cdot \pi^{inv,capa}_{c, g, y} \cdot {\color{red}{{NEWCAPACITY}}_{c, g, y}}) 
	
	& + \sum_{c\in C, \color{red}{{s\in S}}, t\in T, y\in Y|(y+\color{red}{{OPERLIFE}}_{c, s})>\color{red}{{MAXYEAR}}} (0.8 \cdot \pi^{inv,capa}_{c, s, y} \cdot {\color{red}{{NEWCAPACITY}}_{c, s, y}}
	
	& ) )
	
	
Marked in red: things that are not in the terminology. All of these are explained in the following table:

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1


   * - Name 
     - Domains 
     - Type
     - Description
   * - S 
     - -
     - Set 
     - Storages are a distinct set in GENeSYS-MOD, similar to Technologies but with few restrictions  
   	 
   * - IDISCOUNTFACTOR 
     - y 
     - Parameter 
     - Discount factor for weighting future years relative to the first year in Y (~)  
   * - IWEIGHTY 
     - y 
     - Parameter 
     - Relative weight of the individual years in Y  
   * - NEWCAPACITY 
     - c, g or s, y
     - Variable 
     - Amount of new capacity of a technology or storage in a region in a year. Similar to VGKNACCUMNET from Balmorel  
   * - NEWTRADECAPACITY 
     - r, r', Electricity, y 
     - Variable 
     - Amount of new trade capacity for electricity between two regions
   * - TRADECAPACITYCOST 
     - r, r', Electricity 
     - Parameter 
     - Costs for expanding transmission capacity for electricity between two regions  
   * - OPERLIFE 
     - c, g or s
     - Parameter 
     - Lifetime of a technology or storage in years  
   * - MAXYEAR
     - -
     - Scalar
     - Last year of modelling period 
	