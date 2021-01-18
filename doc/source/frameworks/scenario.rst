Mathematical Comparison Scenarios for Open_MODEX
=================================================
This documentation is intended to introduce the scenarios for the mathematical comparison of the open source frameworks for Energy System Modelling under consideration in the project open_MODEX.

* urbs
* Balmorel
* GENESYS-2
* GENeSYS-MOD
* oemof

In the first phase, we try to compare the factors required to model each scenario and intend to make a comparison of how these factors have been incorporated into the frameworks.

Base Scenario
##############
In the base scenario, single year models of electricity sector for the years 2030 and 2050 are intended to be developed. The factors under consideration during the modelling of this scenario are:

1. Cost types per technology
*****************************
Here we have a comparison of how each framework has modelled the cost types per technology.

urbs
^^^^^
* Processes (Power Plants)
   * Investment costs per MW (incurred on new capacity)
   * Annual fixed costs per MW (incurred on total capacity)
   * Variable costs per MWh operation
   * Fuel costs per MWh fuel input
   * Environmental costs per tons of emission
* Storages
   * Investment costs per MWh storage content
   * Investment costs per MW charging/discharging capacity (incurred on new capacity)
   * Annual fixed costs per MWh 
   * Annual fixed costs per MW (incurred on total storage content and charging/discharging capacity) 
   * Variable costs per MWh charging/discharging
   * Variable costs per MWh of current storage state
* Transmission lines
   * Investment costs per MW transmission capacity (incurred on new capacity)
   * Annual fixed costs per MW transmission capacity (incurred on total capacity)
   * Variable costs per MWh flow over line
* Other Costs
   * Not included 
   
Balmorel
^^^^^^^^^
* Processes (Power Plants)
   * Investment costs per MW (incurred on new capacity; dependent on area and technology)
   * Annual fixed operating costs per MW (incurred on total capacity; dependent on area and technology)
   * Variable operative and maintenance costs relative to output (power/heat generation) per MWh (dependent on area and technology) 
   * Variable operating and maintenance costs relative to input (fuel consumption) per MWh (dependent on area and technology)
   * Fuel costs per MWh fuel consumption per GJ but multiplied by 3.6 (dependent on year, area and fuel type)
   * Emission costs related to fuel consumption (tons of emission) per GJ but multiplied by 3.6 (dependent on year and country)
   * Seasonal price for power production from hydro with storage per MWh (dependent on season and area)
* Storages
   * Investment costs per MW (incurred on new capacity; dependent on area and technology)
   * Annual fixed operating costs per MW (incurred on total capacity; dependent on area and technology)
   * Variable operative and maintenance costs relative to output (power/heat generation) per MWh (dependent on area and technology; frequently zero) 
   * Variable operating and maintenance costs relative to input (fuel consumption) per MWh (dependent on area and technology; possible to include in the model but not used)
* Transmission lines
   * Investment costs per MW transmission capacity (incurred on new capacity; dependent on year and transmission line) 
   * Transmission costs between regions per MWh (dependent on transmission line) 
* Other Costs
   * Included as add-ons such as: Grid-tariffs, Subsidies, Taxes, fuel limits, etc. 

GENESYS-2
^^^^^^^^^
* Processes (Power Plants)
   * Investment costs per MW (incurred on new capacity)
   * Annual fixed costs as percentage of investment cost per year
   * Fuel costs per MWh fuel input
   * Environmental costs per tons of emission
* Storages
   * Investment costs per MWh storage content
   * Investment costs per MW charging/discharging capacity (incurred on new capacity)
   * Annual fixed costs per MWh 
   * Annual fixed costs per MW (incurred on total storage content and charging/discharging capacity) 
* Transmission lines
   * Investment costs per MW transmission capacity (incurred on new capacity)
   * Annual fixed costs as percentage of investment cost
* Other Costs 
   * Not included 

GENeSYS-MOD
^^^^^^^^^^^^
* Processes (power plants) 
   * Investment costs per MW (incurred on new capacity)
   * Annual fixed costs per MW (incurred on total capacity) 
   * Variable costs per MWh operation
   * Fuel costs incur at a “process” which produces the required amounts of fuel for only variable costs
   * Emission costs incur at the “fuel-production-process”
* Storages
   * Investment costs per MWh possible but not used since E2P-ratoes are assumed to be constant
   * Investment costs per MW charging/discharging capacity (incurred on new capacity)
   * Annual fixed costs per MW (incurred on installed capacity)
   * Variable costs per MWh charging/discharging
* Transmission lines
   * Investment costs per MW transmission capacity (incurred on new capacity) 
   * Variable costs per MWh flow over line

oemof
^^^^^^
* Processes (Power Plants)
   * Investment costs per MW (incurred on new capacity)
   * Annual fixed costs per MW (incurred on new capacity)
   * Variable costs relative to output per MWh operation
   * Fuel costs relative to fuel consumption per MWh fuel input
   * Environmental costs in terms of fuel consumption
* Storages
   * Not included
* Transmission lines
   * Variable costs per MWh flow over line
* Other Costs 
   * Not included 

2. Annuity calculation for investments
***************************************
Here we have a comparison of how each framework has calculated the annuity for investments.

urbs
^^^^^
The annualized investment costs for all investments are given by:

.. math::
   \zeta_{\text{inv}}=\sum_{p \in P_{\text{exp}}}f_p k^{\text{inv}}_p
   \widehat{\kappa}_p,

where :math:`f_p` is the process-specific annuity factor; :math:`k^{\text{inv}}_p` signifies the specific investment costs of process :math:`p` per unit capacity and :math:`P_{\text{exp}}` is the subset of all processes and :math:`\widehat{\kappa}_p` stands for new capacity. 

The annuity factor is given by:

.. math::

   f=\frac{(1+i)^n\cdot i}{(1+i)^n-1}

Balmorel
^^^^^^^^^
For regular production capacity and transmission within one country, the annualized investment costs are calculated in the same way. 
The annuity factor is assumed to be country dependent. Therefore, in the case of transmission capacity between different countries, the annuity factor is taken as the average of the annuity factors for the two countries.   

GENESYS-2
^^^^^^^^^
The annualised investment costs are calculated in the same way. 

GENeSYS-MOD
^^^^^^^^^^^^
No annualisation for investment costs but the investment costs are discounted over years. The algorithm is incorporated into the objecive function
Investment costs only occur in the year of investment. We obtain a salvage value by subtracting the rest of the values of the technology of residual lifetime from investment costs. 

oemof
^^^^^^
The annualised investment costs are estimated in the same way, however they are not calculated sepeately rather incorporated into the objective function as a fixed part. 

3. Grid model (DC/Transport/other)
***********************************
Here we have a comparison of how each framework has modelled the grid.

urbs
^^^^^
* Transport model:
     #. Losses:    :math:`\pi^{\text{out}}_{aft}= e_{af}\cdot \pi^{\text{in}}_{aft}.` 

     #. Capacity Limitation:  :math:`\pi^{\text{in}}_{aft}\leq \Delta t \cdot \kappa_{af}.`

(flows across line type :math:`f` on arc :math:`a` (also holds for other direction :math:`a'`) at time :math:`t`) 

* Power flow on a transmission line modelled with DCPF:  :math:`\pi_{aft}^\text{in} = \frac{(\theta_{v_{\text{in}}t}- \theta_{v_{\text{out}}t})}{57.2958}(-\frac{-1}{X_{af}}){V_{af\text{base}}^2}`

Here :math:`\theta_{v_{\text{in}}t}` and :math:`\theta_{v_{\text{out}}t}` are the voltage angles of the source site
:math:`{v_{\text{in}}}` and destinaton site :math:`v_{\text{out}}`. These are converted to radian from degrees by
dividing by 57,2958. :math:`{X_{af}}` is the reactance of the transmission line in per unit system and
:math:`(-\frac{-1}{X_{af}})` is the admittance of the transmission line. 

Balmorel
^^^^^^^^^
Transmission efficiencies are modelled through the balance equation such that for two two regions with a transmission
from first to the second, import in the second region is equal to the export from the first region minus the transmission losses. 
So, production side includes what is imported to the region :math:`r(v^{\text{trans}}_{re,r,t})`, with the assumption of 
a loss :math:`(e_{\text{re,r}})`.

.. math::
 + \sum_{re \in R}v^{\text{trans}}_{re,r,t}\cdot(1-e_{\text{re,r}})

The demand side includes what is exported from :math:`r(v^{\text{trans}}_{ri,r,t})`

.. math::
 + \sum_{ri \in R}v^{\text{trans}}_{ri,r,t}

If new transmission investments are allowed, electricity transmission is limited by transmission capacity:

.. math::
 \kappa^{\text{trans,exist}}_{re,ri} + v^{\text{trans,new}}_{re,ri}\geq v^{\text{trans}}_{re,ri,t}

where :math:`\kappa^{\text{trans,exist}}_{re,ri}` denotes existing transmission capacity, :math:`v^{\text{trans,new}}_{re,ri}` denotes
newly installed transmission capacity and :math:`v^{\text{trans}}_{re,ri,t}` cover what is being transmitted in :math:`t`. 

Transmission investments are set-symmetric:

.. math::
 v^{\text{trans,new}}_{re,ri} = v^{\text{trans,new}}_{ri,re}

If self-sufficiency is activated, the net import and export in a country are balanced. 

GENESYS-2
^^^^^^^^^
An algorithm is called that tries to balance out remaining positive residual load with exceeding generation of interconnected regions. The aim is to dissipate positive and negative residual loads
from different regions to reach an overall balance. For every region and time-step, the grid algorithm tries to exchange power with a certain distance level of neighbours. 
In a random order, all the regions are balanced per level. The balancing mechanism is based on an iterative approach. The algortihm selects a random starting node with electricity surplus
The user defines the number/amount of neighbouring nodes that can recieve surplus electricity.Then, the algorithm checks 
if electricity can be transferred to neighbouring nodes by considering the existing demand and checking if transfer is allowed and does if possible
If all surplus electricity is distributed to neighbouring nodes, next node is selected and the process is repeated with this node. 

GENeSYS-MOD
^^^^^^^^^^^^
A transport model with the following notations: :math:`f` is the fuel, :math:`t` is the timestep, :math:`r` and :math:`rr` are the two differnt regions trading, :math:`\pi` is the amount traded and there is an efficiency of connection between the two regions. 

oemof
^^^^^^
The grid model is similar except that since the inputs are given in radiants. 


4. Features for modelling storage 
**********************************

Here we have a comparison of how each framework has modelled storage by considering various features such as energy to power ratio, self-discharge, charge/discharge efficiencies, etc. 

urbs
^^^^^
1. Change of storage content

In a storage, the energy content :math:`\epsilon^{\text{con}}_{yvst}` has to be calculated. This is achieved by simply adding all inputs to and subtracting all outputs from the storage content at the previous time step :math:`\epsilon^{\text{con}}_{yvs(t-1)}`:

.. math::
   \epsilon^{\text{con}}_{yvst} = \epsilon^{\text{con}}_{yvs(t-1)} \cdot (1 - d_{yvs})^{\Delta t} + e^{\text{in}}_{yvs} \cdot \epsilon^{\text{in}}_{yvst} - \frac{\epsilon^{\text{out}}_{yvst}}{e^{\text{out}}_{yvs}}

Here, :math:`e^{\text{in,out}}_{yvs}` are the efficiencies for charging and discharging, respectively, and :math:`d_{yvs}` is the hourly self discharge rate.

2. Capacity Limitations

Similar to processes and transmission lines, inputs and outputs are limited by the power capacity of the storage:

.. math::
   \epsilon^{\text{in,out}}_{yvst} \leq \Delta t \cdot \kappa^{\text{p}}_{yvs}

Additionally, the storage content is limited by the total storage energy capacity:

.. math::
  \epsilon^{\text{con}}_{yvst}\leq\kappa^{\text{c}}_{yvs}

3. Cyclicity Rule

In order to avoid windfall profits for the optimization by, e.g., emptying a
storage over the model horizon, the initial and final storage content are
linked via:

.. math::
  \epsilon_{yvs(t_1)}^\text{con} \leq \epsilon_{yvst_N}^\text{con}

where :math:`t_{1,N}` are the initial and final modeled timesteps, respectively.

4. Fixed initial State of Charge (SoC) Rule

It is possible for the user to fix the initial storage content via:

.. math::
   \epsilon_{yvs(t_1)}^\text{con} = \kappa_{yvs}^\text{c} I_{yvs},

where :math:`I_{yvs}` is the fraction of the total storage capacity that is
filled at the beginning of the modeling period.

5. Fixed energy to power ratio

It is sometimes desirable to fix the ratio between energy capacity and
charging/discharging power for a given storage. This is modeled by the
possibility to set a linear dependence between the capacities through a
user-defined "energy to power ratio" :math:`k_{yvs}^\text{E/P}`. Note that this
constraint is only active for the storages with a positive value under the
column "ep-ratio" in the input file, and when this value is not given, the
power and energy capacities can be sized independently

.. math::
   \kappa_{yvs}^c = \kappa_{yvs}^p k_{yvs}^\text{E/P}.

Balmorel
^^^^^^^^^
Electricity storage balance equation (short term) (MWh) is given by:

.. math::
 v^{\text{sto,vol}}_{a,g,t+1} = v^{\text{sto,vol}}_{a,g,t} + v^{\text{sto,load}}_{a,g,t} - \frac{v^{\text{gen}}_{a,g,t}}{\gamma_{\text{g}}}

Here, :math:`v^{\text{sto,vol}}_{a,g,t}` is the volume in storage :math:`g` in an area :math:`a` at time :math:`t`, :math:`v^{\text{sto,load}}_{a,g,t}` is the loaded electricity at time 
:math:`t`, :math:`v^{\text{gen}}_{a,g,t}` is the discharge electricity in time :math:`t` and the discharge happens at efficiency :math:`\gamma_{\text{g}}` which is storage type :math:`g` 
specific. 

If new investments are allowed, there is an upper limit to electricity storage loading in MW:

.. math::
 \frac{\kappa^{\text{sto,exist}}_{y,a,g} + v^{\text{sto,new}}_{y,a,g}}{\delta^{\text{load}}_{g}} \geq v^{\text{sto,load}}_{y,a,g,t}

Here :math:`\kappa^{\text{sto,exist}}_{y,a,g}` and :math:`v^{\text{sto,new}}_{y,a,g}` are the existing and new capacity for storage 
charging and :math:`\delta^{\text{load}}_{g}` indicate how many hours it takes to charge the storage. So, what is charged in :math:`t`
is limited by the variable capacity accounted for the time it takes to charge. 

Electricity storage output limit (MW):

.. math::
 \frac{\kappa^{\text{sto,exist}}_{y,a,g} + v^{\text{sto,new}}_{y,a,g}}{\delta^{\text{unload}}_{g}} \geq v^{\text{gen}}_{y,a,g,t}

Here, :math:`\delta^{\text{unload}}_{g}` indicate how many hours it takes to discharge the storage and :math:`v^{\text{gen}}_{y,a,g,t}` is the discharged power. So, what is available in :math:`t` is 
limited by the available capacity accounted for the time it takes to discharge. 

GENESYS-2
^^^^^^^^^
Generally, storages always require a storage unit connected to a charger/discharger unit. Charger and discharger can either be one unit called ‘bicharger’ or can be modelled seperately with different efficiencies.
The following equations apply to modelling storage in this framework:
1. Intial storage level

.. math::
 v_{y,r,g,t=0}^{\text{sto,vol}} = 0

2. Charge/discharge level

.. math::
 v_{y,r,g,t}^{\text{gen, load}} = v_{y,r,g,t}^{\text{sto,charge}} \cdot \gamma_{y,r,g,t}^{\text{in,gen}} \cdot \Delta t
 v_{y,r,g,t}^{\text{gen, unload}} = v_{y,r,g,t}^{\text{sto,discharge}} \cdot \gamma_{y,r,g,t}^{\text{out,gen}} \cdot \Delta t
 \text{Condition:} v_{y,r,g,t}^{\text{gen, load}} \geq 0 + v_{y,r,g,t}^{\text{gen, unload}} \geq 1

3. Storage level

.. math::
 v_{y,r,g,t}^{\text{sto,vol}} = v_{y,r,g,t-1}^{\text{sto,vol}} + v_{y,r,g,t}^{\text{gen, load}} \cdot \gamma_{y,r,g,t}^{\text{total,gen,sto}} - v_{y,r,g,t}^{\text{gen, unload}} 

4. Total losses

.. math::
 \gamma_{y,r,g,t}^{\text{loss,con}} = v_{y,r,g,t}^{\text{sto,charge}} \cdot (1 - \gamma_{y,r,g,t}^{\text{in, gen}}) + v_{y,r,g,t}^{\text{sto,discharge}} \cdot (1 - \gamma_{y,r,g,t}^{\text{out, gen}}) + v_{y,r,g,t}^{\text{gen,load}} \cdot (1 - \gamma_{y,r,g,t}^{\text{total,gen,sto}})  

GENeSYS-MOD
^^^^^^^^^^^^
* Fixed enery to power ratio
* No time dependent losses (self-discharge)
* Initial state of charge is assumed to be zero
* :math:`v^{\text{sto,vol}}_{g,r,t,y} = v^{\text{sto,vol}}_{g,r,t-1,y} + v^{\text{sto,load}}_{g,r,t-1,y}\cdot \gamma^{\text{in}}_{g,y} - \frac{v^{\text{sto,unload}}_{g,r,t-1,y}}{\gamma^{\text{in}}_g,y}`

oemof
^^^^^^
* Storage loss is dependent on storage type
* Self discharges are incorporated
* It is optional to set the initial storage level but by default, it is activated
* Seperate capacity for charging/discharging

5. Power plant efficiencies
****************************
Here we have a comparison of the model constraints for power plant operation and expansion of each framework.

urbs
^^^^^
1. Input/Output flows from a process

The operational state of the process is then captured in just one
variable, the process throughput :math:`\tau_{pt}` and is linked to the
commodity flows via the following two rules:

.. math::
   &\epsilon^{\text{in}}_{pct}=r^{\text{in}}_{pc}\tau_{pt}\\
   &\epsilon^{\text{out}}_{pct}=r^{\text{out}}_{pc}\tau_{pt},

where :math:`r^{\text{in, out}}_{pc}` are the constant factors linking the
commodity flow to the operational state. The efficiency :math:`\eta` of the
process :math:`p` for the conversion of commodity :math:`c_1` into commodity
:math:`c_2` is then simply given by:

.. math::
   \eta=\frac{r^{\text{out}}_{pc_2}}{r^{\text{in}}_{pc_1}}.
 
2. Capacity and part load Limitations

The throughput :math:`\tau_{pt}` of a process is limited by its installed
capacity and the specified minimal operational state.

.. math::
   \tau_{pt}\leq \Delta t  \kappa_{p}
   \\\tau_{pt}\geq \Delta t  \underline{P}_{p}\kappa_{p}\\

where :math:`\underline{P}_{p}` is the normalized, minimal operational state of
the process.

3. Intermittent supply

For input commodity of type SupIm, or whenever a certain operation time series of
a given process is desired

.. math::
   \epsilon^{\text{in}}_{cpt}= \Delta t s_{ct}\kappa_{p}.

Here, :math:`s_{ct}` is the time series that governs the exact operation of
process :math:`p` i.e. the capacity factor, leaving only its capacity :math:`\kappa_{p}` as a free
variable.

4. Ramp Limitations

The switching speed of a process can be limited:

.. math::
   \tau_{pt}-\tau_{p(t-1)}|\leq \Delta t\overline{PG}_p\kappa_{p},

where :math:`\overline{PG}_p` the normalized, maximal gradient of the
operational state in full capacity per timestep.

5. Exogenous time-variable efficiencies

It is possible to manipulate the operation of a process by introducing a time
series, which changes the output ratios and thus the efficiency of a given
process in each given timestep. 

.. math::
   \epsilon^{\text{out}}_{ypct}=r^{\text{out}}_{ypc}f^{\text{out}}_{ypt} \tau_{ypct}
   

Here, :math:`f^{\text{out}}_{pt}` represents the normalized time series of the
varying output ratio.

6. Part-load dependent efficiencies

For a process with part load behavior the equation for the time variable efficiency case takes the form:

.. math::
   \epsilon^{\text{out}}_{ypct} = \Delta t \cdot f^{\text{out}}_{ypt} \cdot \left(\frac{\underline{r}^{\text{out}}_{ypc}-r^{\text{out}}_{ypc}} {1-\underline{P}_{yp}}\cdot \underline{P}_{yp}\cdot \kappa_{yp} + \frac{r^{\text{out}}_{ypc}- \underline{P}_{yp}\underline{r}^{\text{out}}_{ypc}} {1-\underline{P}_{yp}}\cdot \tau_{ypt}\right)

Balmorel
^^^^^^^^^
1. Fuel consumption rate:

.. math::
 v^{\text{fuse}}_{y,a,g,t} = \frac{v^{\text{gen}}_{y,a,g,t}}{\gamma^{\text{g}}}

where :math:`v^{\text{gen}}_{y,a,g,t}` is the power generated and :math:`\gamma^{\text{g}}` is the fuel efficiency.

2. Minimum and maximum electricity generation:

.. math::
 \kappa^{\text{gen,min}}_{c,f}\leq \sum_{a \in c,g \in f, t \in y}v^{\text{gen}}_{y,a,g,t}\leq \kappa^{\text{gen,max}}_{c,f}

where :math:`\kappa^{\text{gen,max}}_{c,f}` and :math:`\kappa^{\text{gen,min}}_{c,f}` are the parameters stating maximum and minimum electricity generation by fuel respectively
and :math:`v^{\text{gen}}_{y,a,g,t}` is the generation from technology :math:`g`.

3. Minimum and maximum fuel use:

.. math::
 \kappa^{\text{fuse,min}}_{y,c,f}\leq \sum_{a \in c,g \in f, t \in y}v^{\text{fuse}}_{y,a,g,t}\leq \kappa^{\text{fuse,max}}_{y,c,f}

where :math:`\kappa^{\text{fuse,max}}_{y,c,f}` and :math:`\kappa^{\text{fuse,min}}_{c,f}` are the parameters stating maximum and minimum fuel use in GJ per year respectively.

4. Exact fuel use:

.. math::
 \sum_{a \in c,g \in f, t \in y}v^{\text{fuse}}_{y,a,g,t} = \kappa^{\text{fuse,exact}}_{y,c,f}


where :math:`\kappa^{\text{fuse,exact}}_{y,c,f}` is the required fuel in GJ per year. 

5. If investments are allowed, capacity constraint on technologies with endogeneous investment:

.. math::
 v^{\text{gen}}_{y,a,g,t} \leq \kappa^{\text{gen,exist}}_{y,a,g} + v^{\text{gen,new}}_{y,a,g}

6. Capacity constraint on power from hydro-run-of-river, wind, solar, wave cannot be dispatched:

.. math::
 v^{\text{renew}}_{y,a,g,t} \leq \frac{\sigma^{\text{renew}}_{a}\cdot cf^{\text{renew}}_{a,t}}{\sum_{t \in y}cf^{\text{renew}}_{a,t}}(\kappa^{\text{renew,exist}}_{y,a,g} + v^{\text{renew,new}}_{y,a,g})

where :math:`v^{\text{renew}}_{y,a,g,t}` is the generated renewable power, :math:`cf^{\text{renew}}_{a,t}` is the capacity factor (availability of the renewable source) in a specific hour and :math:`\sigma^{\text{renew}}_{a}` is the amount of full-load hours. Again, 
:math:`\kappa^{\text{renew,exist}}_{y,a,g}` is the existing renewable capacity and :math:`v^{\text{renew,new}}_{y,a,g}` is the newly installed capacity. 

7. Maximum electricity capacity:

.. math::
 \sum_{a \in c, g \in f}\kappa^{\text{exist}}_{y,a,g} + v^{\text{new}}_{y,a,g} \leq \kappa^{\text{fuel potential}}_{c,f}
 
where :math:`\kappa^{\text{fuel potential}}_{c,f}` indicates the full potential restriction by geography (MW).

8. Capacity restrictions by fuel - Minimum and Maximum capacity:

.. math::
 \kappa^{\text{capa,min}}_{y,c,f} \leq \sum_{a \in c, g \in f}\kappa^{\text{exist}}_{y,a,g} + v^{\text{new}}_{y,a,g} \leq \kappa^{\text{capa,max}}_{y,c,f}

where :math:`\kappa^{\text{capa,min}}_{y,c,f}` and :math:`\kappa^{\text{capa,max}}_{y,c,f}` are the minimum and maximum capacity by fuel per year (MW) respectively. 

9. Exact fuel use:

.. math::
 \sum_{a \in c, g \in f}\kappa^{\text{exist}}_{y,a,g} + v^{\text{new}}_{y,a,g} = \kappa^{\text{capa,exact}}_{y,c,f}

where :math:`\kappa^{\text{capa,exact}}_{y,c,f}` is the required capacity by fuel per year (MW).

GENESYS-2
^^^^^^^^^
Part-load behaviour is not modelled. 

GENeSYS-MOD
^^^^^^^^^^^^
* No part load efficiency has been implemented
* For a generic process: :math:`\frac{v^{\text{gen}}_{f,g,m,r,t,y}}{\gamma^{\text{outgen}}_{f,g,m,r,y}} = \sum_{f \in F}v^{\text{fuse}}_{f,g,m,r,t,y} \cdot \gamma^{\text{ingen}}_{f,g,m,r,y}`

oemof
^^^^^^
* Dispatchable: :math:`0 \leq v^{\text{gen}}_{y,r,g,t} \leq \kappa^{\text{capa}}_{r,g}`
* Conversion: :math:`v^{\text{fuse}}_{y,r,g,t} = \frac{1}{\gamma^{\text{out,gen}}_{r,g}} \cdot v^{\text{fuse}}_{y,r,g,t}`
* Volatile: :math:`v^{\text{gen}}_{y,r,g,t} = \kappa^{\text{capa}}_{r,g} \cdot \gamma^{\text{capa}}_{y,r,g,t}`
* It is possible to include ramping constraints and part-load behaviour.

6. Imports/Exports
*******************

Here we have a comparison of how each framework has incorporated the concept of imports/exports.

urbs
^^^^^
Buying/Selling electricity from/to an external market is possible with limited interconnector capacities (expansion is alos allowed), and time-variable buying/selling prices per MWh. 

Balmorel
^^^^^^^^^
* Balmorel per default operates with fixed import/export in specified hours. This is provided through an input file (X3FX_VAR_T) with either a positive (net export) or negative (net import) number (included in the balance equation as additional/substracted demand).
* Additionally an add-on (X3V) allow for the model to decide on import/export by including time series for import/export prices (X3VPEX(IM) dependent on year, region, time). This exchange can only appear on pre-specified connections and an upper limit is imposed. The exchange is assumed to be lossless and without transmission cost. 

GENESYS-2
^^^^^^^^^
Imports/exports are not incorporated into the model. 

GENeSYS-MOD
^^^^^^^^^^^^
Buying/Selling electricity from/to an external market is possible with limited interconnector capacities (expansion is alos allowed), and yearly (not time-variable) buying/selling prices per MWh.
All cost parameters are on an yearly basis.  

oemof
^^^^^^
Imports/Exports are modelled with hourly variable prices. It is also possible to set restrictions on the import/exports.

Scenario Variation I
#####################
In scenario variation I, an intertemporal model of the electricity sector is intended to be developed.

1. Intertemporal cost models
*****************************
Here we have a comparison of how each framework handles the costs for intertemporal models. 

urbs
^^^^^

A discount rate :math:`(j)` is used for the time value of money. Fixed, variable, fuel and environmental costs at each support year are repeatedly incurred until the next support year (which is after :math:`k` years), while being discounted by the factor :math:`(1-j)` each year in between: 

.. math::
   D_m&=\sum_{l=m}^{m+k-1}(1+j)^{-l}=(1+j)^{-m}\sum_{l=0}^{k-1}(1+j)^{-l}=(1+j)^{-m}\frac{1-(1+j)^{-k}}{1-(1+j)^{-1}}=(1+j)^{1-m}\frac{1-(1+j)^{-k}}{j}

This factor is then used to calculate the costs associated with the support year :math:`m` as follows (example given for variable costs, but also holds for fixed, fuel and environmental costs): 

.. math::
   \zeta_{\text{var}}^{\{m,m+1,..,m+k-1\}}=D_m\cdot\zeta_{\text{var}}^{m},

In contrary to the former mentioned type of costs, the investment costs have to be first annualized. This leads to another way of calculating its intertemporal costs (for an investment made in year :math:`m`): 

.. math::
   C^{\text{total}}_{\text{m}}&=D_{m}\cdot f \cdot C =
   (1+j)^{1-m}\frac{1-(1+j)^{-k}}{j} \cdot \frac{(1+i)^n\cdot i}{(1+i)^n-1}
   \cdot C\underbrace{(1+j)^{1-m}\cdot \frac{i}{j}\cdot
   \left(\frac{1+i}{1+j}\right)^n\cdot
   \frac{(1+j)^n-(1+j)^{n-k}}{(1+i)^n-1}}_{=:I_{\text{m}}}\cdot C

Now that :math:`k` in above equation gives the number of years of investments's lifetime that fall into the model horizon. This means that the portion of the investment that falls beyond model horizon are deducted from the investment. 

Balmorel
^^^^^^^^^
* Discounting mechanisms on the objective are appplied, making distant future years count less in the model than near years.
   * Discount factor represents society's perception of how future years' costs and benefits shall be evaluated. Discount factor for weighting future years relative to the first year in :math:`Y` is calculated where :math:`D` is a scalar of value 0.04 and :math:`(y-y')` is the distance to the first year in the model.
* Additionally in the objective:
   * Annuity factor is multiplied directly on the investment costs in order to have it annualised.
   * Since balmorel is defined over a set :math:`YYY` but may only be calculated for a subset of these years, a weighting is provided to all selected years, indicating the share of the time horizon in :math:`YYY` that the selected year represents. For example, if :math:`YYY = \{2020,2021,2022,2023,2024,2025\}`, then the selection could be :math:`Y = \{2020,2024\}` and the weighting could then indicate that 2020 represents the first 3 years while 2024 represents the latter 3 years. It could also be a subjective weighting making some years count more.  

GENESYS-2
^^^^^^^^^^
Annuities are calculated for each year and added to the total annuity sum. 

GENeSYS-MOD
^^^^^^^^^^^^
All costs (investment, fixed, variable, trade, emissions) are calculated as in the base scenario. There is no annualisation of investment costs. 

oemof
^^^^^^
Intertemporal constraints aren't an atomic building block in oemof. It is possible to manually build a model using them, but the mathematical formulation is not generic but specific to the particular model.
No connection between time steps can be established, support years can be calculated individually, no FW inherent functionality 


2. Carrying on technology capacities across years
**************************************************
Here we have a comparison of how each framework has modelled carrying on technology capacities across years.

urbs
^^^^^
Urbs uses a 'single problem approach'. The model has the perfect foresight of capacities across all support years. For the first support year of the model, already existing capacities for technologies are given with a remaining lifetime. For new installations, the economic lifetime behaves also as the technical lifetime. The units exceeding their technical lifetimes are decommissioned. 
Sets that determine for process :math:`p`, that is built in year :math:`y_{i}`, whether it is operational in later year :math:`y_{j}`: :math:`O_{\text{inst}}`: for the first support year of the model, :math:`O` for the rest of the support years)

.. math::
   O:=\{(p,y_i,y_j)|p\in P,~\{y_i,y_j\}\in Y,~y_i\leq y_j,~ y_i + L_p \geq\ y_{j+1}\}\\\\
   O_{\text{inst}}:=\{(p, y_j)|p\in P_0,~y\in Y,~y_0+T_p\geq y_{j+1}\}

Using these sets, the available capacities are determined at each support year:

.. math::
   \kappa_{yp} = \sum_{y^{\prime}\in Y\\(p,y^{\prime},y)\in O} \widehat{\kappa}_{y^{\prime}p} + K_{p} ~,~~\text{if}~(p,y)\in O_{\text{inst}}\\\\
   \kappa_{yp} = \sum_{y^{\prime}\in Y\\(p,y^{\prime},y)\in O} \widehat{\kappa}_{y^{\prime}p}

Balmorel
^^^^^^^^^
* Decommission: Implemented as an add-on which may be activated. It holds different options both for existing capacity and for invested capacity.
   * Decommission due yo lifetime
   * Decommission due to profitability
   * Additional option for the system to buy back decommissioned capacity. 
* Foresight:  We define the full time horizon by :math:`YYY` and make a selection for the years we want to actually consider in the model (:math:`Y`). Consequently an optimisation is performed for each element in Y but each run may cover more years from Y. We define by YMODEL how many years of :math:`Y` that the model, in each model run know with perfect foresight. YMODELDELTA indicate the range between each of the foresight years. Therefore, investments made in year :math:`Y` may be selected based on foresight on some future years and the selected capacities are then transferred to the next year, where new decisions are made, also based on foresight years. 

GENESYS-2
^^^^^^^^^^
Capacities are carried on as long as the end of lifetime is reached. There can be initial capacities defined in the starting year but it is not mandatory. 

GENeSYS-MOD
^^^^^^^^^^^^
Single problem approach. The model has the perfect foresight of capacities across all support years. For all years, the remaining amount of capacities built before the modleling horizon are given by the modeler. For new installations, the economic lifetime behaves also as the technical lifetime. The units exceeding their technical lifetimes are decommissioned. If investments expire between two support years, they are added to the previous year. 

oemof
^^^^^^
No perfect foresight

3. :math:`CO_{2}` budget instead of yearly limits
**************************************************
Here we have a comparison of how each framework has incorporated the emission budget in its framework.  

urbs
^^^^^
While in an intertemporal model all the yearly commodity costraints remain valid, one addition is possible concerning :math:`CO_{2}` emissions. Here, a budget can be given, which is valid over the entire modelling horizon:

.. math::
   -w\sum_{y\in Y\\t\in T_{m}}\text{CB}(y,\text{CO}_2,t)\leq \overline{\overline{L}}_{\text{CO}_2}

where :math:`w` are the weights of a given support year (number of years until the next support year, and a user-input value for the last support year in the model). Currently, this is hard-coded for :math:`CO_{2}` only.  

Balmorel
^^^^^^^^^
Balmorel only have yearly limits and a cost of emission in the objective but no emission budget.
The limit on annual :math:`CO_{2}`-emission by year and country in kg/MW is given by:

.. math::
 \sum_{a \in c, t \in y}\lambda_{\text{g}}^{\text{co2}} \cdot v^{\text{fuse}}_{\text{y,a,g,t}} \leq \Lambda_{\text{y,c}}^{\text{CO2}}

where :math:`\lambda_{\text{g}}^{\text{co2}}` is the emission per production from :math:`g` and :math:`\Lambda_{\text{y,c}}^{\text{CO2}}` is the country and year specific limitation. 

The limit on annual :math:`CO_{2}`-emission by year for aggregated countries in kg/MW is given by:

.. math::
 \sum_{a \in C, t \in y}\lambda_{\text{g}}^{co2} \cdot v^{\text{fuse}}_{y,a,g,t} \leq \Lambda_{\text{y}}^{CO2}

where :math:`\Lambda_{\text{y,c}}^{CO2}` is the year specific limitation over aggregated countries. 

GENESYS-2
^^^^^^^^^^
* Weighting emissions at each support year: All are rated the same and the sum of the complete emissions is taken. 
* Weighting emissions at the end of the modelling horizon: An optimal expansion path formed based on the expansion optimisation for support years and every year we consider the sum of capacity expansion and emission

GENeSYS-MOD
^^^^^^^^^^^^
Weighted annual emissions and linear interpolation between support years.

oemof
^^^^^^
Heuristic approach, no optimisation approach when manually allocating budget to years.

Scenario Variation II
#####################
In scenario variation II, an intertemporal model of the electricity as well as heat sector is intended to be developed.

1. Emission limits by sector
*****************************
Here we have a comparison of how each framework has modelled the emission limits by sector.

urbs
^^^^^
In urbs, the :math:`CO_{2}` limit is set in a sector-neutral way. Sector-specific limits could however be implemented by reformulating the commodity flows in emitting processes

Balmorel
^^^^^^^^^
The emission limits are country and year specific and not specified per sector. 

GENESYS-2
^^^^^^^^^^
Emission limits cannot be modelled as sector-specific.

GENeSYS-MOD
^^^^^^^^^^^^
Annual sectoral emission limits are possible for emissions :math:`e`, sector :math:`se`, year :math:`y`, region :math:`r`. :math:`T` denotes technologies that are part of sector :math:`se`.

oemof
^^^^^^
It is possible to specify sector-specific emission limits.

2.Modelling of multiple input- multiple output technologies
************************************************************
Here we have a comparison of how each framework has modelled multiple input- multiple output technologies.

urbs
^^^^^
Similar to single input- single output technologies, multiple input- multiple output technologies are also modelled either with constant efficiencies, exogeneously variable efficiencies or load-dependent efficiencies. Modelling the dependency between the thermal and electrical efficiency is not possible.

Balmorel
^^^^^^^^^
The equations related to CHP backpressure:

1. Fuel usage

.. math::
 \upsilon^{\text{fuse}}_{y,a,g,t} = \frac{\upsilon^{\text{gen}}_{y,a,g,t} + \gamma^{\text{CV}}_{g} \cdot \upsilon^{\text{gen,heat}}_{y,a,g,t}}{\gamma^{\text{in,gen}}_{g}}

2. Limited by Cb-line:

.. math::
 \upsilon^{\text{gen}}_{y,a,g,t} = \upsilon^{\text{gen,heat}}_{y,a,g,t} \cdot \gamma^{\text{CB}}_{g}

The equations related to CHP extraction:

1. Fuel usage

.. math::

	\upsilon^{\text{fuse}}_{y,a,g,t} = \frac{\upsilon^{\text{gen}}_{y,a,g,t} + \gamma^{\text{CV}}_{g} \cdot \upsilon^{\text{gen,heat}}_{y,a,g,t}}{\gamma^{\text{in,gen}}_{g}}

2. Limited by Cb-line:

.. math::

	\upsilon^{\text{gen}}_{y,a,g,t} \geq \upsilon^{\text{gen,heat}}_{y,a,g,t} \cdot \gamma^{\text{CB}}_{g}

3. Limited by Cv-line:

.. math::

	\upsilon^{\text{gen}}_{y,a,g,t} \leq \kappa^{\text{capa}}_{y,a,g} + \upsilon^{\text{capa}}_{y,a,g} - \upsilon^{\text{gen,heat}}_{y,a,g,t} \cdot \gamma^{\text{CB}}_{g}


GENESYS-2
^^^^^^^^^^
Modelling of multiple input- multiple output technologies is not possible. 

GENeSYS-MOD
^^^^^^^^^^^^
Multiple input- multiple output technologies are modelled in the same way as regular processes. Modelling the dependency between thermal and electrical efficiency is not possible. Constant efficiency and thermal/electrical rate can be modelled. CHP have predefined power to heat ratios.

oemof
^^^^^^
The equations related to CHP Extraction Turbine are given below:

.. math::

  v^{gen, el} \leq \kappa^{capa} \\\\
  \kappa^{capa} \leq \overline{\kappa}^{capa}

.. math::
    v^{fuse}(t) =
    \frac{v^{gen, el}(t) + v^{gen, th}(t) \\\\
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


CHP backpressure turbines are modelled based on their time dependent electrical and thermal efficiency in backpressure mode.

.. math::

    v^{fuse}(t) =
    \frac{v^{gen, el}(t) + v^{gen, th}(t)}{\gamma^{th}(t) + \gamma^{el}(t)}
    \qquad \forall t \in T

.. math::

    \frac{v^{gen, el}(t)}{v_{gen, th}(t)} =
    \frac{\gamma^{el}(t)}{\gamma^{th}(t)}
    \qquad \forall t \in T

