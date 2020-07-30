# IS3 In Vivo Virtual Network Simulations
=========================================

Luo X, Guet-McCreight A, Villette V, Francavilla R, Marino B, Chamberland S, Skinner FK, Topolnik L. (2020). Synaptic Mechanisms Underlying the Network State-Dependent Recruitment of VIP-Expressing Interneurons in the CA1 Hippocampus. Cerebral Cortex, bhz334,  https://doi.org/10.1093/cercor/bhz334

Run this script to simulate and plot the IS3 models (code also available at https://github.com/FKSkinnerLab/IS3-Cell-Model/tree/master/RhythmTests). Note that this code was written for use with python 2.7 but has been adapted here for use in python 3.

Directories
-----------

1       /SWR/ - Simulates in vivo-like inputs + SWR-timed inputs and plots results

2       /Theta/ - Simulates in vivo-like inputs + theta-timed inputs and plots results

3       /Theta_DoubledInputs/ - Simulates in vivo-like inputs + theta-timed inputs + doubling specific inputs and then plots results

4       /Theta_RemovedInputs/ - Simulates in vivo-like inputs + theta-timed inputs + removing specific inputs and then plots results

5       /Theta_NoiseTests/ - Simulates in vivo-like inputs + theta-timed inputs + effects of noise and then plots results

List of models (ModelDB accession #: 223031)
-------------
The models currently available are:

1       /SDprox1/

2       /SDprox2/

From: Guet-McCreight A, Camiré O, Topolnik L, Skinner F. (2016). Using a semi-automated strategy to develop multi- compartment models that predict biophysical properties of interneuron- specific 3 (IS3) cells in hippocampus. eNeuro. 3:4. https://doi.org/10.1523/ENEURO.0087-16.2016


Model invocation
----------------
Before running the simulations you must first compile the mod files using the following command:

		nrnivmodl

To run simulations, first cd into the directory of interest and then use python as a command-line argument as follows:

		python init.py
