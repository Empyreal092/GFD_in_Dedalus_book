# Introduciton
We will be using the newest version of the Dedalus solver, a flexible
and efficient spectral partial differential equations solver. Dedalus
comes with [great documentation](https://dedalus-project.readthedocs.io/en/latest/index.html) and a few [illuminating examples](https://dedalus-project.readthedocs.io/en/latest/pages/tutorials.html#example-scripts) that
showcase its features. This collection aims to expand on the list of
examples. We focus in implementing models in GFD. These implementations could be the start of
deeper study of these models, or they could be examples on how to use
Dedalus.

The rest of the introduction lists some things to note before we dive into specific examples.

## Note about Dedalus

### Working with distributed parallelism via MPI
Dedalus uses distributed parallelism via MPI. Dedalus
hides much of the complexity of working with MPI. However, an advanced
user of Dedalus cannot forget its parallel architecture. Examples codes work with multiple cores in distributed systems (a server with
multiple nodes). For a tutoruial on how to use Dedalus v3 on the NYU
Greene supercomputer, see this [tutorial](https://github.com/CAOS-NYU/Dedalusv3_GreeneSingularity).

(dedalus-gfd-tools)=
### Dedalus GFD tools 
Along the way we will introduce some tools and tricks that makes working with Dedalus easier. Here is a growing list:

#### Adaptive timestep for when velocity comes from a streamfunction
The examples on Dedalus' website that have adaptive timestep uses the
`d3.CFL` function, that take a vector field velocity as the input for
calculating the timestep. However, often in GFD models, velocity comes
from the derivatives of a streamfunction, and is not a vector field in
Dedalus. We implement a simple CFL based adaptive timestep that take in
the velocity as separate scalar fields. See the 2D Euler code in {numref}`chap:Baro_vort` for an example. Note that we
need to use the `d3.GlobalFlowProperty` to take maximum over MPI.

#### Calculating spectrum

The spectra of a turbulence field is a commonly calculated quantity {cite:p}`Yaglom_62`. It is particularly easy to calculate the spectra in a perdiodic simulation represented using Fourier modes. 
However, it is important that the calculated spectra sum up to equal the $L^2$-norm of the underlying field, folliwng the Parseval's theorem. 
This can be tricky when calculating the isotropic spectra of 2D fields, where one needs to make sure no modes are left over and no modes are counted twice. 
The first section will be a tutorial about calculating the 2D isotropic spectra. The result is the [`isospectrum` function](https://github.com/Empyreal092/GFD_in_Dedalus/blob/main/dedalus_subroutines/.py) that is used for the rest of the book.

<!-- ## Desired features in Dedalus

Despite the power of Dedalus, there are some features we would like that
is not currently implemented. This is a list of wants we have for
Dedalus. We feel these should be possible to implement in the spectral
set-up of Dedalus. We would be happy to contribute and implement them,
but we are currently unclear how.

#### Arbitrary linear operators in doubly periodic domain {#sec:ded_want_linop}

We would like a way to define new linear operators that is only
expressible as operations on the Fourier coefficient. More specifically,
the linear operator $\mathcal{P}$ is defined by a user provided a matrix
$\boldsymbol P$ such that $$\begin{aligned}
    \mathcal{F}\{\mathcal{P}(\psi)\}_{\boldsymbol k} = \boldsymbol P_{\boldsymbol k}\hat\psi_{\boldsymbol k}.
\end{aligned}$$ where $\cal{F}$ and $\hat{\cdot}$ both means the Fourier
transform and $\boldsymbol P_{\boldsymbol k}$ is the $\boldsymbol k=(k,\ell)$ element of the
$\boldsymbol P$ matrix.

These operators are very common in GFD models. They include fractional
and negative Laplacian of the form $|k|^{-d}$ used for the inversion in
the famous $\alpha$-turbulence models
[{cite:p}`PierrehumbertEtAl_94`; cite'SmithEtAl_02'] and for hypo-diffusion in
turbulence simulation with inverse cascade
{cite:p}`MajdaEtAl_97; @VallgrenLindborg_11; @CalliesEtAl_16]. There are also
more unconventional operators in the literature, e.g., the $\mathcal{P}$ in
{cite:p}`Xie_20 (3.2)]: $$\begin{aligned}
    \mathcal{P} = \frac{i}{2}\frac{\nabla^2}{-1+\nabla^2/4}\label{eq:YBJp_pop}
\end{aligned}$$ where we have suppressed the geophysical constants for
clarity. This operator still follows the form
[\[eq:YBJp_pop\]](#eq:YBJp_pop){reference-type="eqref"
reference="eq:YBJp_pop"}.

Going a bridge further, some linear operator takes vector Fourier
coefficient. That is $$\begin{aligned}
    \mathcal{F}\{\mathcal{P}(\boldsymbol\psi)\}_{\boldsymbol k} = \boldsymbol P_{\boldsymbol k}\hat{\boldsymbol\psi}_{\boldsymbol k}
\end{aligned}$$ where $$\begin{aligned}
    \boldsymbol\psi(x,y) = \begin{bmatrix}
        \psi_1(x,y)\\
        \psi_2(x,y)\\
        \vdots\\
        \psi_n(x,y)
    \end{bmatrix}
\end{aligned}$$ is a $n$-vector of 2D fields and each $\boldsymbol P_{\boldsymbol k}$ is
a $n$-by-$n$ matrix. This means $\boldsymbol P$ is a $n\times n\times m\times m$
tensor where $m$ is the maximally resolved wave numbers. An example of
this kind of linear operator is {cite:p}`CalliesEtAl_16], which is a
generalization of the Eady model {cite:p}`Eady_49; @TullochSmith_09]. These
operators essentially comes from Green's function of elliptic equations
and reduce a 3D elliptic solve to a few 2D Fourier transforms. Being
able to define these linear operators in Dedalus would be immensely
helpful.

## Shortcomings of Dedalus

Dedalus is not without its shortcomings. Here we list a few that we face
occasionally. Compare with the last section, these are inherent
deficiencies of the spectral method or needs significant software
engineering to fix. We list them here to inform potential users know the
sacrifice that comes with using Dedalus. But obviously we still love
Dedalus as a tool since we are writing this collection.

#### Limited domain

Being a spectral solver, Dedalus cannot solve problems that are on
arbitrary domains.

A surprising discovery for us is that Dedalus cannot use parallelism on
a closed box. In Cartesian settings, it needs a direction to be Fourier
to be able to run in parallel[^3]. This is disappointing since this
exclude efficient simulation of classic models like the barotropic
vorticity model of wind-driven gyres in a box {cite:p}`Vallis_17 §19.4]. We
simulate it on a disk in Section
[\[sec:wind_gyres_disk\]](#sec:wind_gyres_disk){reference-type="ref"
reference="sec:wind_gyres_disk"}. -->

## Note about the GFD models

In research, one comes up with the model first and choose the
appropriate solver. Dedalus aims to be a competent solver for many
models. Since this collection is GFD in Dedalus, we take the opposite
approach and pick models that is well set-up for Dedalus to solve. This
means we will solve problems that are in periodic domain or on a circle
or sphere. We aim to implement all GFD models that are commonly solved
spectrally. This includes the examples in [pyqg](https://pyqg.readthedocs.io/en/latest/equations.html) and
[GeophysicalFlows.jl](https://fourierflows.github.io/GeophysicalFlowsDocumentation/stable/).
<!-- About SQG, see [1.3.0.1](#sec:ded_want_linop){reference-type="ref" reference="sec:ded_want_linop"}. -->

More importantly, Dedalus is a PDE solver. It is well suited to perform
Direct Numerical Simulation (DNS), as opposed to Large Eddy Simulation
(LES) or General Circulation Model (GCM). They are different tools that
solve different problems. Here, we will minaly use Dedalus to solve austere models in
idealized set-ups. We take a philosophical approach well summarized in
{cite:p}`Vallis_16`:
> The moniker 'GFD' has also come to imply a methodology in which one makes the maximum possible simplifications to a problem, perhaps a seemingly very complex problem, seeking to reduce it to some bare essence. It suggests an austere approach, devoid of extraneous detail or superfluous description, so providing the fundamental principles and language for understanding geophysical flows without being overwhelmed by any inessentials that may surround the core problem. In this sense, GFD describes a method as well as an object of study.

### Nondimensionalization

One consequence of simulating austere models is that nondimensionalizing
the equations often will produce only a few relevant nondimensional
parameters for the dynamics. For us, this greatly simplifies the task of
understanding the model and generalize the conclusion we obtain. We will
always simulate the nondimensional version of the equations in the
following examples.

In particular, we will use the notation of {cite:p}`Vallis_96a`:
> Here, and in the rest of the paper, expressions are written in dimensional form. The relevant non-dimensional parameters are also given, enclosed in curly brackets, $\{\}$. The pure dimensional form may be recovered simply by setting to unity the contents of the curly brackets. The non-dimensional form is recovered by setting all the physical parameters (such as $g$ and $f$) to unity. This notation enables both the asymptotic ordering and physical appreciation of the terms to be facilitated.

For example, the Boussinesq system under the geostrophic scaling reads
(cf. {cite:p}`Vallis_17`(PE.1-4)): 
\begin{align}
    &\{\text{Ro}\}\left(\frac{\mathrm{D} u}{\mathrm{D} t}-\beta y v\right)-fv = -\phi_x,\\
    &\{\text{Ro}\}\left(\frac{\mathrm{D} v}{\mathrm{D} t}+\beta y u\right)+fu = -\phi_y,\\
    &\phi_z = b,\\
    &\{\text{Ro}\}\left(\frac{\mathrm{D} b}{\mathrm{D} t}\right)+\left\{\frac{\text{Ro}^2}{\text{Fr}^2}\right\}N^2w = 0,\\
    &u_x+v_y+w_z = 0
\end{align}
where we have the two nondimensional number
\begin{align}
    \text{Ro}:= \frac{U}{fL};\qquad \text{Fr}= \frac{U}{NH}.
\end{align}

### Models to be implemented

Dedalus is powerful and it takes many examples to explore all its
features. The implemented models at the moments reflect our bias. Here is a
list of models seems worthwhile to us to implement in Dedalus. We
especially encourage students of GFD to try to implement some models.

- The Matsuno-Gill model for equatorial dynamics {cite:p}`Matsuno_66`, {cite:p}`Gill_80`. The same model on the sphere is done recently
  by {cite:p}`ShamirEtAl_23`.

- Some linear model of tide and lee waves. Possible examples are
  {cite:p}`SmithYoung_02`, {cite:p}`Cushman-RoisinBeckers_11`(13.2), and
  {cite:p}`NikurashinFerrari_10`.