# $$Physics$$

## $$General~Physics~I$$

### $$\text{Module 1 : Mechanics basics}$$

### $$\text{Module 2 : Energy and Oscillations }$$

#### $$\text{Potential Energy and Conservation of Energy}$$

##### $\text{Potential Energy}$

- Conservative Force

  - Conservative Force are forces for which W1=-W2 is always ture
  - Examples:gravitational force, spring force
  - Otherwise we could not speak of their potential energies
  
- Gravatational Potential Energy

$$
U(y)=mgy
$$

- Elastic Potential Energy

$$
U(x)=\frac{1}{2}kx^2
$$

##### $\text{Conservation of Mechanical Energy}$

- Reading a Potential Energy Curve

##### $\text{Work Done on ta System by an External Force}$

- Power

$$
P_{avg} = \frac{\Delta E}{\Delta t}
\\
\,
\\
P = \frac{dE}{dt}
$$

##### $\text{Conservation of Energy}$

##### $\text{Equilibrium}$

- Static equilibrium

  - $F_{net} = 0$
  - $\tau _{net} = 0$

##### $\text{Elasticity}$

- $Stress\,=\,modulus\,\times\,strian$
- Young's mudules,**E**,used for tension/compreession（拉力/压力）:

$$\frac{F}{A}\,=\,E\,\frac{\Delta L}{L}$$

- Shear mudules,**G**,used for shearing（剪切力）:

  - $\Delta x \,\text{is along a different axis than L}$

$$\frac{F}{A}\,=\,G\,\frac{\Delta x}{L}$$

- Bulk mudules,**B**,used for hydraulic compression（液压压力）:

  - Relates pressure to volume change

$$p\,=\,B\,\frac{\Delta V}{V}$$

#### $$\text{Gravitation}$$

##### $\text{Newton's Law of Gravitation}$

- Gravitation and the principle of Superposition

$$F\,=\,G\,\frac{m_1m_2}{r^2}$$

- hell's theorem
- Gravitation Near Earth's surface

  - Combine $F\,=\,\frac{GMm}{r^2}\, \text{and}\,F\,=\,ma_g$
  
$$
a_g=\frac{GM}{r^2}
$$

$$
F_N-ma_g=m(-\omega^2R)
$$

$$
g=a_g-\omega^2R
$$

$a_g \approx 9.8m/s^2 \\ \omega \approx 7.3 \times 10^{-5} rad/s \\ R \approx 6357km $

- Gravitation Inside Earth

$$
F=\frac{GmM_{ins}}{r^2}
$$

$$
\rho = \frac{M_{ins}}{\frac {4}{3}\pi r^3} = \frac {M}{\frac{4}{3}\pi R^3}
$$

$$
F=\frac {GMm}{R^3}r
$$

##### $\text{Gravitational Potential Energy}$

$$
U=-\frac{GMm}{r}
$$

$$
K+U=\frac{1}{2}mv^2+(-\frac{GMm}{R})=0
\\
\,
\\
v=\sqrt{\frac{2GM}{R}}
$$

##### $\text{Satellites: Orbits and Energy}$

- Escape Speed

$$
m\frac{v^2}{r}=\frac{GMm}{r^2}
\\
\,
\\
K=\frac{1}{2}mv^2=\frac{GMm}{2r}
\\
\,
\\
K=-\frac{U}{2}\,(circular\,orbit)
\\
\,
\\
E=K+U=-\frac{GMm}{2r}\,(circular\,orbit)
\\
\,
\\
T^2=\frac{4\pi ^2}{GM}r^3
$$

#### $$\text{Oscillations}$$

##### $\text{Simple Harmonic Motion}$

- Frequency
- Period

$$
T=\frac{1}{f}
\\
\,
\\
x(t)=x_mcos(\omega t+\phi)
\\
\,
\\
\omega=\frac{2\pi}{T}=2\pi f
\\
\,
\\
v(t)=\frac{dx}{dt}=-\omega x_msin(\omega t+\phi)
\\
\,
\\
a(t)=\frac{dv}{dt}=\frac{d^2x}{dt^2}=-\omega^2x_mcos(\omega t+\phi)=-\omega^2x(t)
\\
\,
\\
F=ma=-m\omega^2x
\\
\,
\\
\omega = \sqrt{\frac{k}{m}}\,(\text{Linear simple harmonic oscillation})
$$

##### $\text{Energy in Simple Harmonic Motion}$\

$$
U(t)=\frac{1}{2}kx^2=\frac{1}{2}kx_m^2cos^2(\omega t+\phi)
\\
\,
\\
K(t)=\frac{1}{2}mv^2=\frac{1}{2}kx_m^2sin^2(\omega t+\phi)
\\
\,
\\
E=U+K=\frac{1}{2}kx_m^2
$$

##### $\text{An Angular Simple Harmonic Oscillator}$

$$
\tau =-\kappa \theta
\\
\,
\\
T=2\pi \sqrt{\frac{I}{\kappa}}
$$

##### $\text{Pendulums, Circular motion}$

$$
\tau=-L(F_gsin\theta)
\\
\,
\\
\alpha=-\frac{mgL}{I}\theta
\\
\,
\\
\omega=\sqrt{\frac{mgL}{I}}
\\
\,
\\
T=2\pi \sqrt{\frac{F}{g}}=2\pi\sqrt{\frac{I}{mgh}}
$$

##### $\text{Damped Simple Harmonic Motion}$

$$
F_d=-bv
\\
\,
\\
m\frac{d^2x}{dt^2}+b\frac{dx}{dt}+kx=0
\\
\,
\\
x(t)=x_me^{\frac{-bt}{2m}}cos(\omega't+\phi)
\\
\,
\\
\omega'=\sqrt{\frac{k}{m}-\frac{b^2}{4m^2}}
\\
\,
\\
E(t)\approx\frac{1}{2}Kx_m^2e^{\frac{-bt}{m}}
$$

#### $$\text{Waves}$$

##### $\text{Sinusoidal Waves}$

- Transverse Waves

$$
y(x,t)=y_msin(kx-\omega t)
\\
\,
\\
k=\frac{2\pi}{\lambda}\,(\text{angular wave number})
\\
\,
\\
\omega = \frac{2\pi}{T}\,(\text{angular frequency})
\\
\,
\\
f=\frac{1}{T}=\frac{\omega}{2\pi}\,(\text{frequency})
$$

- Longitudinal Waves
Sound Waves

$$
B=-\frac{\varDelta p}{\varDelta V/V}=\rho v^2
\\
\,
\\
v=\sqrt{\frac{B}{\rho}}
\\
\,
\\
I=\frac{P_s}{4\pi r^2}\,(\text{Intensity})
$$

##### $\text{Wave Speed}$

$$
v=\frac{\omega}{k}=\frac{\lambda}{T}=\lambda f\,(\text{wave speed})
$$

- Wave Speed on a Stretched String

$$
\mu =\frac{m}{l}\,(\text{linear density})
\\
\,
\\
v=\sqrt{\frac{\tau}{\mu}}\,(\text{speed})
$$

##### $\text{Energy and Power of a Wave Travelling along a String}$

$$
dK=\frac{1}{2}dmu^2
\\
\,
\\
\frac{dK}{dt}=\frac{1}{2}\frac{dm}{dt}u^2=\frac{1}{2}\mu v \omega^2y_m^2cos^2(kx-\omega t)
\\
\,
\\
(\frac{dK}{dt})_{avg}=\frac{1}{4}\mu v \omega^2y_m^2=(\frac{dU}{dt})_{avg}
\\
\,
\\
P_{avg}=\frac{d(K+U)}{dt}=2(\frac{dK}{dt})_{avg}=\frac{1}{2}\mu v \omega^2y_m^2
\\
\,
\\
a_y=\frac{d^2y}{dt^2}
\\
\,
\\
\frac{d^2y}{dx^2}=\frac{\mu}{\tau}\frac{d^2y}{dt^2}
\\
\,
\\
\frac{\partial^2y}{\partial x^2}=\frac{1}{v^2}\frac{\partial^2y}{\partial t^2}\,(\text{wave equation})
$$

##### $\text{Interference of Waves}$

$$
y'(x,t)=y_1(x,t)+y_2(x,t)
\\
\,
\\
If:
\\
\,
\\
y_1(x,t)=y_msin(kx-\omega t)
\\
\,
\\
y_2(x,t)=y_msin(kx-\omega t+\phi)
\\
\,
\\
s.t.
\\
\,
\\
y'(x,t)=[2y_mcos\frac{1}{2}\phi]sin(kx-\omega t+\frac{1}{2}\phi)
$$

- Sound Interference

$$
\phi =\frac{\varDelta L}{\lambda}2\pi
$$

##### $\text{Phasors}$

##### $\text{Standing Waves}$

$$
If:
\\
\,
\\
y_1(x,t)=y_msin(kx-\omega t)
\\
\,
\\
y_2(x,t)=y_msin(kx+\omega t)
\\
\,
\\
s.t.
\\
\,
\\
y'(x,t)=[2y_msinkx]cos\omega t
$$

- Resonance

- A pipe open at both ends

$$
sin(kL)=0 \rightarrow KL=\frac{2\pi}{\lambda}L=n\pi
\\
\,
\\
f=\frac{v}{\lambda}=\frac{nv}{2L}\,,\,n=1,2,3,\dots
$$

- A pipe closed at one end and open at the other

$$
f=\frac{v}{\lambda}=\frac{nv}{4L}\,,\,n=1,3,5,\dots
$$

##### $\text{Doppler's Effect}$

$$
f'=f\frac{v\pm v_D}{v\pm v_S}
\\
\,
\\
sin\theta=\frac{v}{v_S}
$$

### $$\text{Module 3 : Thermodynamics}$$
