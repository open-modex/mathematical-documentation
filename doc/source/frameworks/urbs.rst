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