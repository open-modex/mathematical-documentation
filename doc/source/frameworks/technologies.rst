Modelling of technologies
=========================
Here the framework's representations of technologies are shown

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