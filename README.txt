Optimal AFC shape calculation & implimentation. 

Creating the AFC teeth in parallel using an optical pulse train. The desired AFC shape can be calculated using just the desired storage time and OD of the QM. 

storage time = tau # storage time of pulse
Delta = 1/tau # spacing between each tooth
Finesse = Delta/gamma

Optimal Finnese and therefore optimal AFC shape can be calculated using F_opt = pi/arctan(2pi/OD)

optimal_afc_shape_paper.ipynb

Towards highly multimode optical quantum memory for quantum repeaters.
Pierre Jobez, Nuala Timoney, Cyril Laplane, Jean Etesse, Alban Ferrier, Philippe Goldner, Nicolas Gisin, and Mikael Afzelius
Phys. Rev. A 93, 032327 – Published 21 March 2016