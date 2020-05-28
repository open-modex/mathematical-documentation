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

Electricity-only units
**********************

.. figure:: images/balmorel_elec.png
   :width: 70 %
   
   Used in: Balmorel

Balmorel
''''''''

The related equation for this technology is:

.. math::

	{\vu_{y,a,g,t}}  = \frac{\vg_{y,a,g,t}}{\gi_{g}} \quad \forall y \in Y, a\in A, g\in G, t\in T

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

Storages
********

.. figure:: images/balmorel_sto.png
   :width: 70 %

   Used in Balmorel

Balmorel
''''''''

The necessary equation for this technology is:

.. math::
	& \vsv_{y,a,g,t+1} = \vsv_{y,a,g,t}\cdot \gt_{g} + \vsl_{y,a,g,t}\cdot \gi_{g} - \vg_{y,a,g,t} \cdot \go_{g}

	& \forall y \in Y, a\in A, g\in G, t\in T
    
urbs
''''

.. math::
    &\epsilon^{\text{con}}_{y,d,r,t}=\epsilon^{\text{con}}_{y,d,r,(t-1)}\cdot (1-d_{y,d,r})^{\Delta t}+e^{\text{in}}_{y,d,r}\cdot \epsilon^{\text{in}}_{y,d,r,t}- \frac{\epsilon^{\text{out}}_{y,d,r,t}}{e^{\text{out}}_{y,d,r}}\\
    &\forall y\in Y,~d\in D,~r\in R,~t\in T_m

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

Generic processes
*****************

urbs
''''

.. math::

    &\epsilon^{\text{in}}_{y,g,d,t}=r^{\text{in}}_{y,g,d}\tau_{y,g,t} \\
    &\epsilon^{\text{out}}_{y,g,d,t}=r^{\text{out}}_{y,g,d}\tau_{y,g,t} \\
    &\tau_{y,g,t}\leq \kappa_{y,g} \\
    &\forall y \in Y, ~g \in G, ~d \in D, ~t \in T_m


GENeSYS-MOD	
'''''''''''

.. figure:: images/genesysmod_generic.png
   :width: 70 %
   
This equation counts for all processes, no matter how many input or output fuels are required.   

.. math::

    &\frac{{v^{gen}_{f,g,m,r,t,y}}}{\gamma^{out_gen}_{f,g,m,r,y}} = \sum_{f\in F} v^{fuse}_{f,g,m,r,t,y} \cdot \gamma^{in_gen}_{f,g,m,r,y} \quad \forall f \in F, g \in G, m \in M, r \in R, t \in T, y \in Y\\ 


