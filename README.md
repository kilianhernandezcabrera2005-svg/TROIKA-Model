# TROIKA Model: Triple Rotor Oscillator Interlinked with K-cycle Architecture

A quantum mechanics and information framework exploring the directional and vibrational coupling of three entangled sources. This repository contains the complete theoretical description and the MATLAB scripts used to simulate the system's dynamics, hybrid entanglement entropy, and Wigner quasiprobability distributions.

## 🌌 Overview

The **TROIKA model** introduces a quantum system of three harmonic oscillators, each equipped with an internal 3-level degree of freedom (qutrit) encoding discrete spatial directions.

The fundamental state is cyclically entangled and represented as:

```math

\vert{}\Psi_{TROIKA}\rangle = \frac{1}{\sqrt{3}} ( |xyz\rangle + \vert{}yzx\rangle + \vert{}zxy\rangle )
```

A central property of this state is the **enforced trihedron**: measuring the direction of any single source collapses the remaining two into an orthogonal triad.
<img width="1731" height="908" alt="Esquema operadores reloj modelo TOE" src="https://github.com/user-attachments/assets/6ab41c01-6406-47fd-ba8c-9d7a18a05156" />
## 🛠️ Hamiltonian and Formalism

The complete dynamics of the system are governed by the total Hamiltonian:

```math
\hat{H} = \hat{H}_0 + \hat{H}_{int}^{dir} + \hat{H}_{int}^{osc-dir}
```

Where each term corresponds to:

* **Free Oscillators:**
```math
\hat{H}_0 = \sum_{i=1}^3 \hbar \omega_i ( \hat{N}_i + \frac{1}{2} )
````
* **Directional Interaction:**
```math
\hat{H}_{int}^{dir} = \frac{\hbar g}{2} ( \hat{X}_1 \hat{X}_2 \hat{X}_3 + h.c. )
```
modulated by Weyl-Heisenberg shift operators.

* **Vibrational-Directional Coupling:**
```math
\hat{H}_{int}^{osc-dir} = \hbar \lambda \sum_{i=1}^3 ( \hat{X}_i \hat{a}_i^\dagger + \hat{X}_i^\dagger \hat{a}_i )
```
### Invariant Sectors
The model exhibits a strict global symmetry since the operator:
```math
\hat{K} = \hat{k}_1 + \hat{k}_2 + \hat{k}_3 \pmod 3
````
commutes with the full Hamiltonian. This restricts the dynamics of the prepared state exactly within the:
```math
K = 0
```
block, reducing the active Hilbert space dimension from:
```math
27(N+1)^3
```
to:
```math
9(N+1)^3
```

## 📊 Key Simulation Results

The codebase solves the time-independent Schrödinger equation via exact matrix diagonalization using Kronecker products, tracking two main regimes:

1. **Protected Subspace:** For:
```math
\lambda \ll g
```
The directional trihedron remains highly stable with a fidelity:
```math
\mathcal{F}(t) \approx 1 
```
2. **Coherent Exchange:** For:
```math
\lambda \sim g
```
Reversible quantum information transfer triggers non-Markovian **Rabi Revivals**, showing an exact anti-correlation between directional fidelity and the creation of vibrational bosons.
<img width="1250" height="1406" alt="toe_2f_fidelity_occupation" src="https://github.com/user-attachments/assets/a8c51a2c-37c9-41f9-8fe1-362a7df81738" />

The scripts also implement partial traces over the 1728-dimensional space to compute:
* **Von Neumann Entanglement Entropy:**
```math
S(\hat{\rho}_{dir})
```
<img width="643" height="511" alt="grafica_entropia_von_neumann" src="https://github.com/user-attachments/assets/9e91b72c-0dc3-428d-9a5a-94e8498d0797" />

Quantifying the hybrid mixing.
* **Wigner Quasiprobability Distributions:**
```math
W(x_1, p_1)
```
<img width="721" height="350" alt="grafica wigner instante 7,5" src="https://github.com/user-attachments/assets/c61cb23f-4386-4eb1-a930-aa41395582b8" />

Revealing quantum negativity wells and Schrödinger cat-like superpositions at the fidelity minima.

## 📂 Repository Structure

This repository contains almost every source I used in the development of this project: MATLAB codes for Wigner distributions, simulations, ... ; moreover, I have added both paper's full text in English and Spanish.

---
**Author:** Kilian Hernández Cabrera  
**Affiliation:** Universidad de Las Palmas de Gran Canaria (ULPGC)  
**Academic Year:** 2025–2026





