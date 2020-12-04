Genesys2
========
On this page, the most important equations like the objective function and constraints are stated.

Objective function
******************


.. math::

	\pi^{\text{objective}} = C_{\text{real}}(\pi^{inv,capa,g},\pi^{omf,capa,g},\pi^{omv,gen,g}) + C_{\text{penalty}}(\varepsilon^{\text{deviation}})

	\pi^{\text{objective}} = \sum_{T_{interval}}^{} \sum_{regions}^{} \sum_{components}^{} \pi^{inv,capa,g} + \pi^{omf,capa,g} + \pi^{omv,gen,g} + \sum_{years}^{} \sum_{regions}^{} \pi^{penalty,unsupplied\_load} (\varepsilon^{\text{unsupplied}})^2 + \pi^{penalty,selsupplied\_quota} \varepsilon^{\text{selfsupply}}

	\pi^{\text{objective}} = \sum_{T_{interval}}^{} \sum_{regions}^{} \sum_{components}^{} ANF*[\pi^{inv,capa,g} + \pi^{inv,capa,g} \gamma^{inv,capa,g}] + \pi^{omv,gen,g} + \sum_{T_{interval}}^{} \sum_{regions}^{} \pi^{penalty,unsupplied\_load} (\varepsilon^{\text{unsupplied}})^2 + \pi^{penalty,selsupplied\_quota} \varepsilon^{\text{selfsupply}}
	
	\pi^{\text{objective}} = \sum_{T_{interval}}^{} \sum_{regions}^{} \sum_{components}^{} \frac{(1+i)^{n}i}{(1+i)^{n}-1}*[\pi^{inv,capa,g} + \pi^{inv,capa,g} \gamma^{inv,capa,g}] + [\pi^{fuel,f}+\pi^{emi,e}] \varepsilon^{gen,t} + \sum_{T_{interval}}^{} \sum_{regions}^{} \pi^{penalty,unsupplied\_load} (\varepsilon^{\text{unsupplied}})^2 + \pi^{penalty,selsupplied\_quota} \varepsilon^{\text{selfsupply}}

Constraints
***********