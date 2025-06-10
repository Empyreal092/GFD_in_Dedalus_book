# The barotropic vorticity model

We start with perhaps the most simple model of geophysical turbulence,
barotropic vorticity model. We can write the model in vorticity form
[@Vallis_17 §4.2.1]: $$\begin{aligned}
    &\frac{\DD}{\DD t}\left( \{\text{Ro}^{-1}\}f+\zeta \right) = 0,\\
    &\zeta = \nabla^2\psi,\\
    &u = -\frac{\pe\psi}{\pe y}, v = \frac{\pe\psi}{\pe x}.
\end{aligned}$$ where $$\begin{aligned}
    \text{Ro} = \frac{U}{fL}.
\end{aligned}$$

If $f$ is constant, it is the 2D incompressible Euler equation. We note
that we do not use quasi-geostrophic to describe this model and reserve
that name to the model with a finite deformation radius.
