urbs
====
On this page, the most important equations like the objective function and constraints are stated.

Objective function
******************
The objective function consists of five parts:

    * Investment costs
    * Fixed costs for operation and maintenance
    * Variable operation and maintenance costs
    * Fuel costs
    * Environment costs like costs for CO_2 emissions


.. math::

    \pi = \pi_{\text{inv}} + \pi_{\text{fix}} + \pi_{\text{var}} + \pi_{\text{fuel}} + \pi_{\text{env}}

    \pi_{\text{inv}}=\sum_{g \in G_{\text{exp}}}f_g \pi^{\text{inv, capa}}_g \widehat{\kappa}_g
    f=\frac{(1+i)^n\cdot i}{(1+i)^n-1}

    \pi_{\text{fix}}=\sum_{g \in G}\pi^{\text{omf,capa}}_g\kappa^{\text{capa}}_g

    \pi_{\text{var}}=w \Delta t \sum_{t \in T_m\\ g \in G} \pi^{\text{omv}}_{gt}\tau_{g,t}


    \pi_{\text{fuel}}=w \Delta t \sum_{t \in T_m\\ f \in F} \pi^{\text{fuel}}_{f}v^{\text{gen}}_{g,t}

    \pi_{\text{env}}=-w \Delta t \sum_{t \in T_m\\ e \in E} \pi^{\text{emi}}_{e}\text{CB}(e,t)


Constraints
***********

Process expansion constraints
-----------------------------
The unit expansion constraints are independent of the modeled time. In case of
the minimal model the are restricted to two constraints only limiting the
allowed capacity expansion for each process. The total capacity of a given
process is simply given by:

.. math::
   &\forall p \in P:\\
   &\kappa_{p}=K_p + \widehat{\kappa}_p,

where :math:`K_p` is the already installed capacity of process :math:`p`.

Process capacity limit rule
~~~~~~~~~~~~~~~~~~~~~~~~~~~
The capacity pf each process :math:`p` is limited by a maximal and minimal
capacity, :math:`\overline{K}_p` and :math:`\underline{K}_p`, respectively,
which are both given to the model as parameters:

.. math::
   &\forall p \in P:\\
   &\underline{K}_p\leq\kappa_{p}\leq\overline{K}_p.

All further constraints are time dependent and are determinants of the unit
commitment, i.e. the time series of operation of all processes and commodity
flows.

Commodity dispatch constraints
------------------------------
In this part the rules governing the commodity flow timeseries are shown.  

Vertex rule ("Kirchhoffs current law")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This rule is the central rule for the commodity flows and states that all
commodity flows, (except for those of environmental commodities) have to be
balanced in each time step. As a helper function the already mentioned
commodity balance is calculated in the following way:

.. math::
   &\forall c \in C,~t\in T_m:\\\\
   &\text{CB}(c,t)=
    \sum_{(c,p)\in C^{\mathrm{out}}_p}\epsilon^{\text{in}}_{cpt}-
    \sum_{(c,p)\in C^{\mathrm{in}}_p}\epsilon^{\text{out}}_{cpt}.

Here, the tuple sets :math:`C^{\mathrm{in,out}}_p` represent all input and
output commodities of process :math:`p`, respectively. The commodity balance
thus simply calculates how much more of commodity :math:`c` is emitted by than
added to the system via process :math:`p` in timestep :math:`t`. Using
this term the vertex rule for the various commodity types can now be written in
the following way:

.. math::
   \forall c \in C_{\text{st}},~t \in T_m:
   \rho_{ct} \geq \text{CB}(c,t),

where :math:`C_{\text{st}}` is the set of stock commodities and:

.. math::
   \forall c \in C_{\text{dem}},~ t \in T_m:
   -d_{ct} \geq \text{CB}(c,t),

where :math:`C_{\text{dem}}` is the set of demand commodities and
:math:`d_{ct}` the corresponding demand for commodity :math:`c` at time
:math:`t`. These two rules thus state that all stock commodities that are
consumed at any time in any process must be taken from the stock and that all
demands have to be fulfilled at each time step.

Stock commodity limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are two rule that govern the retrieval of stock commodities from stock:
The total stock and the stock per hour rule. The former limits the total amount
of stock commodity that can be retrieved annually and the latter limits the
same quantity per timestep. the two rules take the following form:

.. math::
   &\forall c \in C_{\text{st}}:\\
   &w \sum_{t\in T_{m}}\rho_{ct}\leq \overline{L}_c\\\\
   &\forall c \in C_{\text{st}},~t\in T_m:\\
   &\rho_ct\leq \overline{l}_{c},

where :math:`\overline{L}_c` and :math:`\overline{l}_c` are the totally allowed
annual and hourly retrieval of commodity :math:`c` from the stock,
respectively.

Environmental commodity limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Similar to stock commodities, environmental commodities can also be limited
per hour or per year. Both properties are assured by the following two
rules:

.. math::
   &\forall c \in C_{\text{env}}:\\
   &-w \sum_{t\in T_{m}}\text{CB}(c,t)\leq \overline{M}_c\\\\
   &\forall c \in C_{\text{env}},~t\in T_m:\\
   & -\text{CB}(c,t)\leq \overline{m}_{c},

where :math:`\overline{M}_c` and :math:`\overline{m}_c` are the totally allowed
annual and hourly emissions of environmental commodity :math:`c` to the
atmosphere, respectively.

Process dispatch constraints
----------------------------
So far, apart from the commodity balance function, the interaction between
processes and commodities have not been discussed. It is perhaps in order to
start with the general idea behind the modeling of the process operation. In
urbs all processes are mimo-processes, i.e., in general they in take in
multiple commodities as inputs and give out multiple commodities as outputs.
The respective ratios between the respective commodity flows remain normally
fixed. The operational state of the process is then captured in just one
variable, the process throughput :math:`\tau_{pt}` and is is linked to the
commodity flows via the following two rules:

.. math::
   &\forall p\in P,~c\in C,~t \in T_m:\\
   &\epsilon^{\text{in}}_{pct}=r^{\text{in}}_{pc}\tau_{pt}\\
   &\epsilon^{\text{out}}_{pct}=r^{\text{out}}_{pc}\tau_{pt},

where :math:`r^{\text{in, out}}_{pc}` are the constant factors linking the
commodity flow to the operational state. The efficiency :math:`\eta` of the
process :math:`p` for the conversion of commodity :math:`c_1` into commodity
:math:`c_2` is then simply given by:

.. math::
   \eta=\frac{r^{\text{out}}_{pc_2}}{r^{\text{in}}_{pc_1}}.

Basic process throughput rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The throughput :math:`\tau_{pt}` of a process is limited by its installed
capacity and the specified minimal operational state. Furthermore, the
switching speed of a process can be limited:

.. math::
   &\forall p\in P,~t\in T_m:\\
   &\tau_{pt}\leq \kappa_{p}\\
   &\tau_{pt}\geq \underline{P}_{p}\kappa_{p}\\
   &|\tau_{pt}-\tau_{p(t-1)}|\leq \Delta t\overline{PG}_p\kappa_{p},

where :math:`\underline{P}_{p}` is the normalized, minimal operational state of
the process and :math:`\overline{PG}_p` the normalized, maximal gradient of the
operational state in full capacity per timestep.

Intermittent supply rule
~~~~~~~~~~~~~~~~~~~~~~~~
If the input commodity is of type 'SupIm', which means that it represents an
operational state rather than a proper material flow, the operational state of
the process is governed by this alone. This feature is typically used for
renewable energies but can be used whenever a certain operation time series of
a given process is desired

.. math::
   &\forall p\in P,~c\in C_{\text{sup}},~t\in T_m:\\
   &\epsilon^{\text{in}}_{cpt}=s_{ct}\kappa_{p}.

Here, :math:`s_{ct}` is the time series that governs the exact operation of
process :math:`p`, leaving only its capacity :math:`\kappa_{p}` as a free
variable.

Part load behavior
~~~~~~~~~~~~~~~~~~
Many processes show a non-trivial part-load behavior. In particular, often a
nonlinear reaction of the efficiency on the operational state is given.
Although urbs itself is a linear program this can with some caveats be captured
in many cases. The reason for this is, that the efficiency of a process is
itself not modeled but only the ratio between input and output multipliers. It
is thus possible to use purely linear functions to get a nonlinear behavior of
the efficiency of the form:

.. math::
   \eta=\frac{a+b\tau_{pt}}{c+d\tau_{pt}},

where a,b,c and d are some constants. Specifically, the input and output ratios
can be set to vary linearly between their respective values at full load
:math:`r^{\text{in,out}}_{pc}` and their values at the minimal allowed
operational state :math:`\underline{P}_{p}\kappa_p`, which are given by
:math:`\underline{r}^{\text{in,out}}_{pc}`. This is achieved with the following
equations:

.. math::
   &\forall p\in P^{\text{partload}},~c\in C,~t\in T_m:\\\\
   &\epsilon^{\text{in,out}}_{pct}=\Delta t\cdot\left(
   \frac{\underline{r}^{\text{in,out}}_{pc}-r^{\text{in,out}}_{pc}}
   {1-\underline{P}_p}\cdot \underline{P}_p\cdot \kappa_p+
   \frac{r^{\text{in,out}}_{pc}-
   \underline{P}_p\underline{r}^{\text{in,out}}_{pc}}
   {1-\underline{P}_p}\cdot \tau_{pt}\right).

A few restrictions have to be kept in mind when using this feature:

* :math:`\underline{P}_p` has to be set larger than 0 otherwise the feature
  will work but not have any effect.
* Environmental output commodities have to mimic the behavior of the inputs by
  which they are generated. Otherwise the emissions per unit of input would
  change together with the efficiency, which is typically not the desired
  behavior.
