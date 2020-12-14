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

Constraints
***********

Storages
-----------------------

The storage balance is given by:

.. math::

  E(t) = \\
  E(t-1) \cdot (1 - \beta(t))^{ \Delta t(t)/(t_u)} \\
  - \gamma(t)\cdot (E_{exist} + E_{invest}) \cdot {\Delta t(t) /(t_u)}\\
  - \delta(t) \cdot {\Delta t(t) /(t_u)}\\
  - \frac{v^{out}(t)}{\gamma_{out}(t)} \cdot \Delta t(t)\\
  + v_{in}(t) \cdot \gamma_{in}(t) \cdot \Delta t(t)

=========================== =======================
symbol                      explanation
=========================== =======================
:math:`E(t)`                energy currently stored
:math:`E_{nom}`             nominal capacity of the energy storage
:math:`c(-1)`               state before initial time step
:math:`c_{min}(t)`          minimum allowed storage
:math:`c_{max}(t)`          maximum allowed storage
:math:`\beta(t)`            fraction of lost energy as share of :math:`E(t)` per time unit
:math:`\gamma(t)`           fixed loss of energy  relative to :math:`E_{nom}` per time unit
:math:`\delta(t)`           absolute fixed loss of energy per time unit
:math:`\dot{E}_i(t)`        energy flowing in
:math:`\dot{E}_o(t)`        energy flowing out
:math:`\gamma_in(t)`        conversion factor(i.e. efficiency) when storing energy
:math:`\gamma_out(t)`       conversion factor when
                            (i.e. efficiency)
                            taking stored energy
:math:`\Delta t(t)`          duration of time step
:math:`t_u`                 time unit of :math:`\beta(t), `\gamma(t), \delta(t)` and timeincrement :math:`\tau(t)`
=========================== =======================


Maximum invement is bounded by lower and upper bound set:

.. math::
      E_{invest, min} \le E_{invest} \le E_{invest, max}

The following constraints are created depending on the attributes

If an initialstorage level is given:

.. math:: E(-1) \le E_{invest} + E_{exist}

if not:

.. math:: E(-1) = (E_{invest} + E_{exist}) \cdot c(-1)

Possible coupling of first and last timestep

.. math:: E(-1) = E(t_{last})

Possible to set C-rate of input and storage content by connecting the invest
variables of the storage and the input flow:

.. math::
        P_{i,invest} + P_{i,exist} =
        (E_{invest} + E_{exist}) \cdot r_{cap,in}

and/or for generation of storage

.. math::
    P_{o,invest} + P_{o,exist} =
    (E_{invest} + E_{exist}) \cdot r_{cap,out}

If wanted connect the invest variables of the input and the output:

.. math::
    P_{i,invest} + P_{i,exist} =
    (P_{o,invest} + P_{o,exist}) \cdot r_{in,out}

Upper and lower storage level is given by:

.. math::
    E(t) \leq (E_{exist} + E_{invest}) \cdot c_{max}(t)

.. math:: E(t) \geq (E_{exist} + E_{invest}) \cdot c_{min}(t)




CHP Extraction Turbine
-----------------------

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
------------------------

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
