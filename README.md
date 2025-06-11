# GFD in Dedalus
This is a collection of computer simulations of Geophysical Fluid Dynamics (GFD) models using the [Dedalus version 3 solver](https://dedalus-project.org/). The built book is accessible [here](https://empyreal092.github.io/GFD_in_Dedalus_book). 

The examples in this note expand on the examples provided by the Dedalus documentation. We also implement some common functions used in GFD studies. Now we list all the models in the note:

 - Barotropic vorticity model
	 - Implement CFL-based adaptive timestep for models where velocities are based on streamfunctions.
	 - Include function for calculating spectra for doubly periodic fields.
	 - Solve the Stommel and Munk model on the circle. The only curvilinear example in the note.
 - 2D QG-Near Inertial Wave (QG-NIW) model
 - The Quasi-Geostrophic (QG) model
 	 - Baroclinically unstable two-layer QG
     - Rossby wave in linear QG
 - Baroclinic modes of arbitrary stratification
 - Linear instability of 3DQG

Please contact us if you find any mistakes. Please consider contributing to this note.

