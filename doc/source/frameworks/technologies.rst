Modelling of technologies
=========================
Here the framework's representations of technologies are shown

Generation
**********

oemof.tabular
'''''''''''''

Dispatchable
------------

.. math::

  & {0 <= v^{gen}_{y,r,g,t} <= \kappa}^{capa}_{r,g}
  \\
  & \forall y \in Y, r \in R, g \in G, t \in T


Conversion
----------

.. math::

  & {v^{fuse}_{y,r,g,t}} =
  \frac{1}{\gamma^{out,gen}_{r,g}}{v^{gen}_{y,r,g,t}}
  \\
  & \forall y \in Y, r \in R, g \in G, t \in T


Volatile
--------

.. math::

  & {v^{gen}_{y,r,g,t} = \kappa^{capa}_{r,g} \cdot \gamma^{capa}_{y,r,g,t}}
  \\
  & \forall y \in Y, r \in R, g \in G, t \in T


Consumption
***********

oemof.tabular
'''''''''''''

Load
----

.. math::

  & {E^{gen}_{y,r,g,t} = E^{capa}_{y,r,g,t}}
  \\
  & \forall y \in Y, r \in R, g \in G, t \in T


Bus
***

oemof.tabular
'''''''''''''

Bus
---

.. math::

  & {v^{in}_{y,r,g,t} = v^{gen}_{y,r,g,t}}
  \\
  & \forall y \in Y, r \in R, g \in G, t \in T


Grid
****

oemof.tabular
'''''''''''''

Link
----


Electricity-only units
**********************

Balmorel
''''''''

.. image:: images/balmorel_elec.png
   :width: 70 %

The related equation for this technology is:

.. math::

	{v^{fuse}_{y,a,g,t}}  = \frac{v^{gen}_{y,a,g,t}}{\gamma^{in,gen}_{g}} \quad \forall y \in Y, a\in A, g\in G, t\in T

Heat-only units
***************

Balmorel
''''''''

.. image:: images/balmorel_heat.png
   :width: 70 %

The related equation for this technology is:

.. math::

	{v^{fuse}_{y,a,g,t}}  = \frac{v^{gen,heat}_{y,a,g,t}}{\gamma^{in,gen}_{g}} \quad \forall y \in Y, a\in A, g\in G, t\in T

CHP units: backpressure
***********************

Balmorel
''''''''

.. image:: images/balmorel_chpbp.png
   :width: 70 %

The related equation for this technology is:

The related equations for this technology is:

1. Fuel usage

.. math::

	& {v^{fuse}_{y,a,g,t}}  = \frac{v^{gen}_{y,a,g,t} + \gamma^{CV}_g \cdot v^{gen,heat}_{y,a,g,t}}{\gamma^{in,gen}_{g}}
	
	& \forall y \in Y, a\in A, g\in G, t\in T

2. Limited by Cb-line:

.. math::

	v^{gen}_{y,a,g,t} = v^{gen,heat}_{y,a,g,t} \cdot \gamma^{CB}_g \quad \forall y \in Y, a\in A, g\in G, t\in T

CHP units: extraction
*********************

Balmorel
''''''''

.. image:: images/balmorel_chpext.png
   :width: 70 %

The related equations for this technology is:

1. Fuel usage

.. math::

	& {v^{fuse}_{y,a,g,t}}  = \frac{v^{gen}_{y,a,g,t} + \gamma^{CV}_g \cdot v^{gen,heat}_{y,a,g,t}}{\gamma^{in,gen}_{g}}
	
	& \forall y \in Y, a\in A, g\in G, t\in T

2. Limited by Cb-line:

.. math::

	v^{gen}_{y,a,g,t} \geq v^{gen,heat}_{y,a,g,t} \cdot \gamma^{CB}_g \quad \forall y \in Y, a\in A, g\in G, t\in T

3. Limited by Cv-line:

.. math::

	v^{gen}_{y,a,g,t} \leq \kappa^{capa}_{y,a,g} + v^{capa}_{y,a,g} - v^{gen,heat}_{y,a,g,t} \cdot \gamma^{CV}_g \quad \forall y \in Y, a\in A, g\in G, t\in T

Generic processes
*****************

urbs
''''

.. math::
	&\epsilon^{\text{in}}_{y,g,d,t}=r^{\text{in}}_{y,g,d}\tau_{y,g,t} \forall y\in Y,\forall g\in G,~d\in D,~t \in T_m
    &\epsilon^{\text{out}}_{y,g,d,t}=r^{\text{out}}_{y,g,d}\tau_{y,g,t} \forall y\in Y\forall g\in G,~d\in D,~t \in T_m
    &\tau_{y,g,t}\leq \kappa_{y,g} \forall y\in y\forall g\in G,~d\in D,~t \in T_m

Storages
********

Balmorel
''''''''

.. image:: images/balmorel_sto.png
   :width: 70 %

The necessary equation for this technology is:

.. math::
	& v^{sto,vol}_{y,a,g,t+1} = v^{sto,vol}_{y,a,g,t}\cdot \gamma^{total,gen}_{g} + v^{sto,load}_{y,a,g,t}\cdot \gamma^{in,gen}_{g} - v^{gen}_{y,a,g,t} \cdot \gamma^{out,gen}_{g}

	& \forall y \in Y, a\in A, g\in G, t\in T
    
urbs
''''

.. math::
    &\forall y\in Y,~d\in D,~r\in R,~t\in T_m:\\
    &\epsilon^{\text{con}}_{y,d,r,t}=\epsilon^{\text{con}}_{y,d,r,(t-1)}\cdot (1-d_{y,d,r})^{\Delta t}+e^{\text{in}}_{y,d,r}\cdot \epsilon^{\text{in}}_{y,d,r,t}- \frac{\epsilon^{\text{out}}_{y,d,r,t}}{e^{\text{out}}_{y,d,r}}.


oemof.tabular
'''''''''''''

.. math::

        {0 = \epsilon^{con}_{y,r,g,t} - \epsilon^{con}_{y,r,g,t-1} \cdot (1 - \gamma^{loss,con}_{y,r,g}) - \epsilon^{in}_{y,r,g,t} \cdot \gamma^{in}_{y,r,g} + \epsilon^{out}_{y,r,g,t} \cdot \gamma^{out}_{y,r,g}}  \forall y \in Y, r\in R, g\in G, t\in T > 0

        {\epsilon^{con}_{y,r,g,t0} = \epsilon^{con}_{y,r,g,t-1}} \forall y \in Y, r\in R, g\in G, t\in T
