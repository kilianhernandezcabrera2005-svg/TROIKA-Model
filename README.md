# TROIKA Model: Triple Rotor Oscillator Interlinked with K-cycle Architecture

A quantum mechanics and information framework exploring the directional and vibrational coupling of three entangled sources. This repository contains the complete theoretical description and the MATLAB scripts used to simulate the system's dynamics, hybrid entanglement entropy, and Wigner quasiprobability distributions.

## 🌌 Overview

The **TROIKA model** introduces a quantum system of three harmonic oscillators, each equipped with an internal 3-level degree of freedom (qutrit) encoding discrete spatial directions (\(\lvert x \rangle, \lvert y \rangle, \lvert z \rangle\)). 

The fundamental state is cyclically entangled:
\[\lvert \Psi_{\text{TROIKA}} \rangle = \frac{1}{\sqrt{3}} \left( \lvert xyz \rangle + \lvert yzx \rangle + \lvert zxy \rangle \right)\]

A central property of this state is the **enforced trihedron**: measuring the direction of any single source collapses the remaining two into an orthogonal triad.

## 🛠️ Hamiltonian and Formalism

The complete dynamics of the system are governed by the total Hamiltonian:
\[\hat{H} = \hat{H}_0 + \hat{H}_{\text{int}}^{\text{dir}} + \hat{H}_{\text{int}}^{\text{osc-dir}}\]

Where:
* **Free Oscillators:** \(\hat{H}_0 = \sum_{i=1}^3 \hbar \omega_i \left( \hat{N}_i + \frac{1}{2} \right)\)
* **Directional Interaction:** \(\hat{H}_{\text{int}}^{\text{dir}} = \frac{\hbar g}{2} \left( \hat{X}_1 \hat{X}_2 \hat{X}_3 + \text{h.c.} \right)\) modulated by Weyl-Heisenberg shift operators.
* **Vibrational-Directional Coupling:** \(\hat{H}_{\text{int}}^{\text{osc-dir}} = \hbar \lambda \sum_{i=1}^3 \left( \hat{X}_i \hat{a}_i^\dagger + \hat{X}_i^\dagger \hat{a}_i \right)\)

### Invariant Sectors
The model exhibits a strict global symmetry since the operator \(\hat{K} = \hat{k}_1 + \hat{k}_2 + \hat{k}_3 \pmod 3\) commutes with the full Hamiltonian. This restricts the dynamics of the prepared state exactly within the \(K=0\) block, reducing the active Hilbert space dimension from \(27(N+1)^3\) to \(9(N+1)^3\).

## 📊 Key Simulation Results

The codebase solves the time-independent Schrödinger equation via exact matrix diagonalization using Kronecker products, tracking two main regimes:
1. **Protected Subspace (\(\lambda \ll g\)):** The directional trihedron remains highly stable with a fidelity \(F(t) \approx 1\).
2. **Coherent Exchange (\(\lambda \sim g\)):** Reversible quantum information transfer triggers non-Markovian **Rabi Revivals**, showing an exact anti-correlation between directional fidelity and the creation of vibrational bosons.

The scripts also implement partial traces over the 1728-dimensional space to compute:
* **Von Neumann Entanglement Entropy (\(S(\hat{\rho}_{\text{dir}})\)):** Quantifying the hybrid mixing.
* **Wigner Quasiprobability Distributions (\(W(x_1, p_1)\)):** Revealing quantum negativity wells and Schrödinger cat-like superpositions at the fidelity minima.

## 📂 Repository Structure

This repository contains almost every source I used in the development of this proyect: MATLAB codes for Wigner distributions, simulations, ... ; more over, I have add both paper's full text in english and spanish.

---
**Author:** Kilian Hernández Cabrera  
**Affiliation:** Universidad de Las Palmas de Gran Canaria (ULPGC)  
**Academic Year:** 2025–2026  


