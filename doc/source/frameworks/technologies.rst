.. include:: ../macros.rst

.. Besides math operations and set membership in formulas only placeholders
   should be used to promote consistency.
   To include a new placeholder update `../macros.rst` AND `../notation.rst`.
   This is a global registry of symbol plus superscript combinations
   representing a unique parameter or variable name. The definition of sets is
   also part of `../notation.rst`.

.. sphinx.ext.graphviz

.. Sources
   https://graphviz.org/doc/info/attrs.html
   https://stackoverflow.com/questions/14873205/horizontal-trees-in-graphviz
   https://stackoverflow.com/questions/6450765/how-do-you-center-a-title-for-a-diagram-output-to-svg-using-dot

.. `dot2tex` could perhaps be integrated in the graphviz extension to allow
   for LaTEX labels.

Modelling of technologies
=========================
Here the framework's representations of technologies are shown

VRE-units
*********

.. graphviz::

  digraph G {
    rankdir="LR";
    node [ shape=box ];

    i -> box [ label="Curtailment" ];
    box -> o [ label="Electricity\nproduction" ];

    i [ style="invis" ];
    o [ style="invis" ];
    box [ label="Parameters:\nProfile\nFull load hours"];

    label="Used in: Balmorel"
  }

.. figure:: images/balmorel_VRE.png
   :width: 70 %

   Used in: Balmorel

.. graphviz::

  digraph G {
    rankdir="LR";
    node [ shape=box ];

    i1 -> box ;
    i2 -> box ;
    box -> o1 ;
    box -> o2 ;

    i1 [ label="Capacity Factor" ];
    i2 [ label="Electricity Demand" ];
    o1 [ label="Electricity Output" ];
    o2 [ label="Cost (FixOM, VarOM)" ];
    box [ label="Parameters:\ncapacity\nefficiency\ncost\nlifetime\nOaM-rate\nbidirectional"];

    label="Used in: GENESYS_2"
  }

.. figure:: images/vre_unit_genesys2.png
   :width: 70 %

   Used in: GENESYS_2

.. graphviz::

  digraph G {
    rankdir="LR";
    node [ shape=box ];

    box -> o [ label="Electricity production" ];

    o [ style="invis" ];
    box [ label="bus\ncapacity\nprofile\nmarginal_cost\ncapacity_cost\nexpandable\noutput_parameters\ncapacity_potential" ];

    label="Used in: oemof.tabular"
  }


Balmorel
''''''''
The related equation for this technology is (TO BE UPDATED):

.. math::

	{v^{gen}_{y,a,g,t}}  = (v^{inv,capa}_{y,a,g}+\kappa^{capa}_{y,a,g})\cdot \gamma^{in,gen}_{g,t} \quad \forall y \in Y, a\in A, g\in G, t\in T

Note - the full load hour is used to generate the profile (the resulting profile here called :math:`\gamma^{in,gen}_{g,t}`) so that it can be scaled according to expected future hours of sun while sticking to the same profile with respect to relative changes.

Urbs
''''''''
Uses generic process equations. Only difference is that additionally the input depends on the timeseries of the corresponding commodity input/maxinput ratio.


.. math::

    &v^{\text{in}}_{t,y,r,g,c}=\kk_{y,r,g}\cdot \gamma^{\text{supim}}_{r,c,y,t}\cdot \Delta t \\
    &\forall t \in T_m, ~y \in Y, ~r \in R, ~g \in G, ~c \in C^{\text{supIm}}


GENESYS-2
''''''''''
Capacity factor (CF) ist used to calculate generation of VRE-units. \Delta t always equals one hour.

.. math::

	{v^{gen}_{y,r,g,t}}  = v^{capa}_{y,r,g} \cdot CF^{in,gen}_{y,r,g,t} \cdot \Delta t \quad \forall y \in Y, r\in R, g\in G, t\in T
    



Electricity-only units
**********************

.. figure:: images/balmorel_elec.png
   :width: 70 %
   
   Used in: Balmorel
   
.. figure:: images/electricity_only_unit_genesys2.png
   :width: 70 %
   
   Used in: GENESYS_2

Balmorel
''''''''

The related equation for this technology is:

.. math::

	{\vu_{y,a,g,t}}  = \frac{\vg_{y,a,g,t}}{\gi_{g}} \quad \forall y \in Y, a\in A, g\in G, t\in T


Urbs
''''''''
Uses generic process equations.


GENESYS-2
''''''''''
Generation is calculated by using overall plant efficiencies, that are time-independent. \Delta t always equals one hour.

.. math::

	{v^{gen}_{y,r,g,t}}  = v^{fuse}_{y,r,g,t} \cdot \gamma^{total,gen}_{g} \cdot \Delta t \quad \forall y \in Y, r\in R, g\in G, t\in T


Heat-only units
***************

.. figure:: images/balmorel_heat.png
   :width: 70 %

   Used in: Balmorel

Balmorel
''''''''

The related equation for this technology is:

.. math::

	{\vu_{y,a,g,t}}  = \frac{\vh_{y,a,g,t}}{\gi_{g}} \quad \forall y \in Y, a\in A, g\in G, t\in T


Urbs
''''''''
Uses generic process equations.


GENESYS-2
''''''''''
Currently not modelled with this framework.


CHP units: backpressure
***********************

.. figure:: images/balmorel_chpbp.png
   :width: 70 %

   Used in: Balmorel

Balmorel
''''''''

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
''''''''
Not modeled in urbs.


GENESYS-2
''''''''''
Currently not modelled with this framework.


CHP units: extraction
*********************

.. figure:: images/balmorel_chpext.png
   :width: 70 %

   Used in: Balmorel

Balmorel
''''''''

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
''''''''
Not modeled in urbs.


GENESYS-2
''''''''''
Currently not modelled with this framework.


Storages
********

.. figure:: images/balmorel_sto.png
   :width: 70 %

   Used in: Balmorel
   
.. figure:: images/storage_unit_genesys2.png
   :width: 70 %

   Used in: GENESYS_2


Balmorel
''''''''

The necessary equation for this technology is:

.. math::
	& \vsv_{y,a,g,t+1} = \vsv_{y,a,g,t}\cdot \gt_{g} + \vsl_{y,a,g,t}\cdot \gi_{g} - \vg_{y,a,g,t} \cdot \go_{g}

	& \forall y \in Y, a\in A, g\in G, t\in T
    
urbs
''''

.. math::
   &\vsv_{t,y,r,s,c}=\vsv_{(t-1),y,r,s,c}\cdot (1-\gL_{y,r,s,c})^{\Delta t}+\gi_{y,r,s,c}\cdot \vsl_{t,y,r,s,c}- \frac{\vsu_{t,y,r,s,c}}{\go_{y,r,s,c}}\\
    &\forall t\in T_m,~y\in Y,~r\in R,~s\in S,~c\in C

GENeSYS-MOD	
'''''''''''

Do I understand it correct with Balmorel that \vsv refers to the amount of energy in a storage at a given time? Then I will use it this way here as well.

.. math::

    &\vsv_{g,r,t,y} = \vsv_{g,r,t-1,y} + \vsl_{g,r,t-1,y}\cdot \gamma^{in}_{g,y} - \frac{\vsu_{g,r,t-1,y}}{\gamma^{in}_{g,y}} \quad \forall g \in G, r \in R, t \in T, y \in Y\\



oemof.tabular
'''''''''''''

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
''''''''''
Generally, storages in GENESYS-2 always require a storage unit connected to a charger/discharger unit. Charger and discharger can either be one unit called 'Bicharger' or can be modelled seperately with diffrent efficiencies.

initial storage level
----------------------
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
**********

oemof.tabular
'''''''''''''

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
***********

oemof.tabular
'''''''''''''

Load
----

.. math::

  & {E^{gen}_{y,r,g,t} = E^{capa}_{y,r,g,t}}
  \\
  & \yrgt


Bus
***

oemof.tabular
'''''''''''''

Bus
---

.. math::

  & {v^{in}_{y,r,g,t} = \vg_{y,r,g,t}}
  \\
  & \yrgt


Grid
****

oemof.tabular
'''''''''''''

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
''''

.. math::

   & v^{\text{trans,out}}_{t,y,r_{in},r_{out},x,c}= v^{\text{trans,in}}_{t,y,r_{in},r_{out},x,c}\cdot \gamma^{\text{trans}}_{y,r_{in},r_{out},x,c}\\
    &\forall t\in T_m,~y\in Y,~r_{in}\in R,~r_{out}\in R,~x\in X,~c\in C
	

GENESYS-2
'''''''''
	
.. math::

   & v^{\text{trans,out}}_{t,y,r_{in},r_{out},x,c}= v^{\text{trans,in}}_{t,y,r_{in},r_{out},x,c}\cdot \gamma^{\text{trans}}_{y,r_{in},r_{out},x,c}\\
    &\forall t\in T_m,~y\in Y,~r_{in}\in R,~r_{out}\in R,~x\in X,~c\in C


Generic processes
*****************

urbs
''''

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
'''''''''''

.. figure:: images/genesysmod_generic.png
   :width: 70 %
   
This equation counts for all processes, no matter how many input or output fuels are required.   

.. math::

    &\frac{{v^{gen}_{f,g,m,r,t,y}}}{\gamma^{out_gen}_{f,g,m,r,y}} = \sum_{f\in F} v^{fuse}_{f,g,m,r,t,y} \cdot \gamma^{in_gen}_{f,g,m,r,y} \quad \forall f \in F, g \in G, m \in M, r \in R, t \in T, y \in Y\\ 
	
	
intertemporal
*************

How are costs handled in intertemporal models (investments and also other types of costs

GENESYS-2
'''''''''
	
.. math::
	\pi^{intertemporal,year1,year2,yearX} = \pi^{anuity,capa,gen,year1} + \pi^{anuity,capa,gen,year2} + \pi^{anuity,capa,gen,yearX}
   


