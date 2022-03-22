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
	
	& + \sum_{c\in C, f\in F, g\in G, m\in M, t\in T} (\psi^{emi}_{f} \cdot \gamma^{in,gen}_{g, c, f, m, y} \cdot v^{gen}_{c, g, m, t, y} \cdot \pi^{emi}_{c, e})
	
	& + \sum_{c\in C, \color{red}{{s\in S}}} (\pi^{inv,capa}_{c, s, y} \cdot {\color{red}{{NEWCAPACITY}}_{c, s, y}})
	
	& + \sum_{f\in F, r,r'\in R, t\in T} (v^{trans}_{r, r', t, f, y} \cdot \pi^{omv,trans}_{f, r, r', y})
	
	& + \sum_{r,r'\in R, y\in Y} (\color{red}{{NEWTRADECAPACITY}}_{r, r', 'Electricity', y} \cdot \color{red}{TRADECAPACITYCOST}_{r, r', 'Electricity'})
	
	& ))
	
	& - (1-{\color{red}{{IDISCOUNTFACTOR}}_{y}} \cdot {\color{red}{{IWEIGHTY}}_{y}}) \cdot (
	
	&   \sum_{c\in C, g\in G, t\in T, y\in Y|(y+\color{red}{{OPERLIFE}}_{c, g})>\color{red}{{MAXYEAR}}} (0.8 \cdot \pi^{inv,capa}_{c, g, y} \cdot {\color{red}{{NEWCAPACITY}}_{c, g, y}}) 
	
	& + \sum_{c\in C, \color{red}{{s\in S}}, t\in T, y\in Y|(y+\color{red}{{OPERLIFE}}_{c, s})>\color{red}{{MAXYEAR}}} (0.8 \cdot \pi^{inv,capa}_{c, s, y} \cdot {\color{red}{{NEWCAPACITY}}_{c, s, y}}
	
	& ) )
	
	
Marked in red: things that are not in the terminology. All of these are explained in the following table:

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1


   * - Name 
     - Domains 
     - Type
     - Description
   * - S 
     - -
     - Set 
     - Storages are a distinct set in GENeSYS-MOD, similar to Technologies but with few restrictions  
   	 
   * - IDISCOUNTFACTOR 
     - y 
     - Parameter 
     - Discount factor for weighting future years relative to the first year in Y (~)  
   * - IWEIGHTY 
     - y 
     - Parameter 
     - Relative weight of the individual years in Y  
   * - NEWCAPACITY 
     - c, g or s, y
     - Variable 
     - Amount of new capacity of a technology or storage in a region in a year. Similar to VGKNACCUMNET from Balmorel  
   * - NEWTRADECAPACITY 
     - r, r', Electricity, y 
     - Variable 
     - Amount of new trade capacity for electricity between two regions
   * - TRADECAPACITYCOST 
     - r, r', Electricity 
     - Parameter 
     - Costs for expanding transmission capacity for electricity between two regions  
   * - OPERLIFE 
     - c, g or s
     - Parameter 
     - Lifetime of a technology or storage in years  
   * - MAXYEAR
     - -
     - Scalar
     - Last year of modelling period 
	
	
Constraints
***********