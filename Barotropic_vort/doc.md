(chap:Baro_vort)=
# The barotropic vorticity model

We start with perhaps the most simple model of geophysical turbulence,
barotropic vorticity model. We can write the model in vorticity form
{cite:t}`Vallis_17` §4.2.1: 
\begin{align}
    &\frac{\mathrm{D}}{\mathrm{D} t}\left( \{\text{Ro}^{-1}\}f+\zeta \right) = 0,\\
    &\zeta = \nabla^2\psi,\\
    &u = -\frac{\partial\psi}{\partial y}, v = \frac{\partial\psi}{\partial x}.
\end{align}
where 
\begin{align}
    \text{Ro} = \frac{U}{fL}.
\end{align}

If $f$ is constant, it is the 2D incompressible Euler equation. We note
that we do not use quasi-geostrophic to describe this model and reserve
that name to the model with a finite deformation radius.
