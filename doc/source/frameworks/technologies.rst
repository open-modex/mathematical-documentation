.. include:: ../macros.rst

.. Besides math operations and set membership in formulas only placeholders
   should be used to promote consistency.
   To include a new placeholder update `../macros.rst` AND `../notation.rst`.
   This is a global registry of symbol plus superscript combinations
   representing a unique parameter or variable name. The definition of sets is
   also part of `../notation.rst`.

Modelling of technologies
=========================
Here the framework's representations of technologies are shown

VRE-units
*********

.. figure:: images/balmorel_VRE.png
   :width: 70 %

   Used in: Balmorel
   
.. figure:: images/vre_unit_genesys2.png
   :width: 70 %

   Used in: GENESYS_2

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


