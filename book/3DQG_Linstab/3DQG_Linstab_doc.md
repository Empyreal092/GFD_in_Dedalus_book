# Linear instability analysis of 3DQG baroclinic instability

We solve the linear instability analysis problem of three-dimensional
baroclinic instability in the quasi-geostrophic (QG) model.

We have the 3D QG model in the $\beta$-plane under the mean zonal
velocity $U(z)$. We have the surface meridional buoyancy gradient
$B_y(z=-H, 0)$ from thermal wind balance. This also implies a mean
meridional PV gradient
\begin{align}
    Q_y = \{\xi^{-2}\}\beta-\nabla^2 U-\{\text{Bu}^{-1}\}\frac{\mathrm{d}}{\mathrm{d} z}\left(\frac{f^2}{N^2}\frac{\mathrm{d} U}{\mathrm{d} z}\right)
\end{align}
where we ignore the $\nabla^2 U$ term with our
assumption that $U$ is horizontally constant. Now we have the 3DQG
system: 
\begin{align}
    &\frac{\mathrm{D} q}{\mathrm{D} t}+Uq_x+vQ_y = 0; \\
    &\frac{\mathrm{D} b}{\mathrm{D} t}+Ub_x+vB_y = 0 \quad\text{at}\quad z=-H, 0; \\
    &\nabla^2\psi + \{\text{Bu}^{-1}\}\frac{\partial}{\partial z}\left(\frac{f^2}{N^2}\frac{\partial\psi}{\partial z}\right) = q \\
    &\quad\quad\text{w/}\quad \psi_z = b/f \quad\text{at}\quad z=-H, 0; \\
    &u = -\psi_y, \quad v = \psi_x.
\end{align}
We use the nondimensional number 
\begin{align}
    \xi^{-2} = \frac{f_0 L}{U} \quad\text{,}\quad \text{Bu} = \frac{N(0)^2H^2}{f_0^2L^2} = \frac{L_{d}^2}{L^2}.
\end{align}
Finally for the linear instability analysis we form a
linear system by assuming small perturbation and ignoring all quadratic
in perturbation terms. We then solve the eigenproblem of the linear
system.