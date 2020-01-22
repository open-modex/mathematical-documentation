Balmorel
========
On this page, the most important equations like the objective function and constraints are stated.

Objective function
******************

Marked in red: things that are not relevant for the current Open_MODEX runs but should be there later.

Marked in blue: things that are not in the terminology

I have further added input and output to the OM costs as we have it divided. I also added an extra superscript to the variable on generation for heat or electricity.
For the current scenarios, heat is not relevant but maybe in the future?

.. math::

	{{\pi}} & =  \sum_{y\in Y} ( {\color{red}{{IDISCOUNTFACTOR}}_{y}} \cdot {\color{red}{{IWEIGHTY}}_{y}} \cdot  (  

	& \sum_{a\in A, g\in G, f\in F  | {{IGF}}_{g, f}} ( \pi^{fuel}_{y, a, f} \cdot  \sum_{t\in T} ( v^{fuse}_{y,a,g,t} )  )  

	& +  \sum_{a\in A, g\in G^{elec} } ( \pi^{omv,gen,out}_{a,g} \cdot  \sum_{t\in T} ( v^{gen,elec}_{y,a,g,t} )  )  

	& +  \sum_{a\in A, g\in G^{heat} } ( \pi^{omv,gen,out}_{a,g} \cdot  \sum_{t\in T} ( {\color{blue}\gamma^{CV}_g} \cdot v^{gen,heat}_{y,a,g,t} )  )  

	& +  \sum_{a\in A, g\in G } ( \pi^{omv,gen,in}_{a, g} \cdot  \sum_{t\in T} ( v^{fuse}_{y,a,g,t} )  )  

	& +  \sum_{a\in A, g\in G} (  ( {\color{red}{{VGKNACCUMNET}}_{y, a, g}} + \kappa^{capa}_{y,a,g}  )  \cdot \pi^{omf,capa}_{a,g} )  

	& +  \sum_{r\in R, r'\in R } (  \sum_{t\in T} (  ( v^{trans}_{y,r,r',t} \cdot \pi^{omv,trans}_{r,r'} )  )  )  

	& )  ) 
	
Not in the objective function in the Open_MODEX scenario runs so far (should be inside the summation of the y) - should we include them? Not in OpenMODEX terminology yet.	

Hydro price profiles
''''''''''''''''''''

.. math::

	+  \sum_{a\in A, g\in G^{hyrs}} (  \sum_{t\in T} ( {{HYPPROFILS}}_{a, IS3} \cdot v^{gen,elec}_{y,a,g,t} )  )  
	
Investment costs
''''''''''''''''
	
.. math::
	
	& +  \sum_{a\in A, g\in G | {{IAGKNY}}_{y, a, g}} ( {{VGKN}}_{y, a, g} \cdot pi^{inv,capa}_{a, g} \cdot  \sum_{c | {{ICA}}_{c, a}}{{ANNUITYCG}}_{c, g} \cdot  \sum_{y' |  (   {{y'}}    =    {{y}}   ) }{{IYHASANNUITYG}}_{y, y', g} )  

	& +  \sum_{y', a\in A, g\in G |  ( {{IAGKNY}}_{y', a, g} \wedge  (   {{y'}}    <    {{y}}   )  )} ( {{VGKN}}_{y', a, g} \cdot pi^{inv,capa}_{a, g} \cdot  \sum_{c | {{ICA}}_{c, a}}{{ANNUITYCG}}_{c, g} \cdot {{IYHASANNUITYG}}_{y', y, g} )  

	& +  \sum_{IRE, IRI | {{IXKN}}_{y, IRI, IRE}} ( {{IOF05}} \cdot {{VXKN}}_{y, IRE, IRI} \cdot {{XINVCOST}}_{y, IRE, IRI} \cdot  ( {{IOF05}} \cdot  (  \sum_{c | {{cCCRRR}}_{c, IRE}}{{ANNUITYCX}}_{c}  +  \sum_{c\in C | {{cCCRRR}}_{c, IRI}}{{ANNUITYCX}}_{c} )  )  \cdot  \sum_{y' |  (   {{y'}}    =    {{y}}   ) }{{IYHASANNUITYX}}_{y', Y} )  

	& +  \sum_{y', IRE, IRI |  ( {{IXKN}}_{y', IRI, IRE} \wedge  (   {{y'}}    <    {{y}}   )  )} ( {{IOF05}} \cdot {{VXKN}}_{y', IRE, IRI} \cdot {{XINVCOST}}_{y', IRE, IRI} \cdot  ( {{IOF05}} \cdot  (  \sum_{c | {{cCCRRR}}_{c, IRE}}{{ANNUITYCX}}_{c} +  \sum_{c | {{cCCRRR}}_{c, IRI}}{{ANNUITYCX}}_{c} )  )  \cdot {{IYHASANNUITYX}}_{y', Y} )  

Environmental costs
'''''''''''''''''''

.. math::	
	& +  \sum_{c\in C} (  \sum_{a\in A, g |  ( {{ICA}}_{c, a} )} (  \sum_{t\in T} (  ( {{IM\_CO2}}_{G} \cdot {{IOF0001}} )  \cdot {{IOF3P6}} \cdot v^{fuse}_{y,a,g,t} )  \cdot {{M\_POL}}_{y, tt{TAX\_CO2}, c} )  )  

	& +  \sum_{c\in C} (  \sum_{a\in A, g |  ( {{ICA}}_{c, a} )} (  \sum_{t\in T} (  ( {{IM\_SO2}}_{G} \cdot {{IOF0001}} )  \cdot {{IOF3P6}} \cdot v^{fuse}_{y,a,g,t} )  \cdot {{M\_POL}}_{y, tt{TAX\_SO2}, c} )  )  

	& +  \sum_{c\in C} (  \sum_{a\in A, g |  ( {{ICA}}_{c, a} )} (  \sum_{t\in T} (  ( {{GDATA}}_{g, tt{GDNOX}} \cdot {{IOF0000001}} )  \cdot {{IOF3P6}} \cdot v^{fuse}_{y,a,g,t} )  \cdot {{M\_POL}}_{y, tt{TAX\_Nox}, c} )  )  

Constraints
***********

QEEQ
''''
To be included

QGFEQ
'''''
To be included