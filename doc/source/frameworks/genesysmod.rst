GENeSYS-MOD
===========
On this page, the most important equations like the objective function and constraints are stated.

Objective function
******************


.. math::

	
	{{\pi}}  & =  \sum_{y\in Y} ({\color{red}{{IDISCOUNTFACTOR}}_{y}} \cdot {\color{red}{{IWEIGHTY}}_{y}} \cdot  (  

	& \sum_{c\in C, g\in G, m\in M, t\in T} ( \pi^{omv,gen}_{c, g, m, y} \cdot   v^{gen}_{c, g, m, t, y}   )
	
	& + \sum_{c\in C, g\in G} (\pi^{omf,capa}_{c, g, y} \cdot \kappa^{capa}_{c, g, y})
	
	& + \sum_{c\in C, g\in G} (\pi^{inv,capa}_{c, g, y} \cdot {\color{red}{{NEWCAPACITY}}_{c, g, y}})
	
	& ))
	
Constraints
***********