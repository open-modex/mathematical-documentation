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
