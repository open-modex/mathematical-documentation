oemof.tabular
=============


Objective function
******************

The objective function is constructed initializing the model and depends on the objects used to define the energy system. For the most part the objective function is determined by which classes were used to represent flows on edges in an energy system graph representation.
The following terms representing energy system relevant concepts found in the modex scenarios can be implemented and be part of an objective function. This description adhering to the modex terminology is not considered to be complete or exhaustive as of yet.


.. math::

    \pi^{obj} =

    & \sum_{r\in R, g\in G, f\in F(g)} ( \pi^{fuel}_{r, f} \cdot \sum_{t\in T} ( v^{fuse}_{r, t, g} ) )

    & + \sum_{r\in R, g\in G} ( \pi^{omf, gen}_{g, r} \cdot \sum_{t\in T} ( v^{gen}_{r, t, g} ) )

    & + \sum_{r\in R, rr\in RR, t\in T } ( \pi^{omv, trans}_{r, rr} \cdot \sum_{t\in T} ( v^{trans}_{r,rr,t} ) )

    & + \sum_{r\in R, f\in F(g)} ( \pi^{emi}_{f, r} \cdot \sum_{t\in T} ( v^{fuse}_{r, t, g} \cdot \psi^{emi}_{g, CO2} ) )

    & + \sum_{r\in R, g\in G} ( v^{inv, capa}_{r, g} \cdot ( \pi^{inv, capa}_{r, g} + \pi^{omf, capa}_{r, g} ) )

    & + gradientcosts

    & + startup + shutdown + activity cost

Constraints
***********
