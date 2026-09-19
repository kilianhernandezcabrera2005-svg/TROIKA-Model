# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Graficas del modelo TOE de 3 fuentes - Mapa de Calor y frecuencias de Rabi
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from toe_dynamics import run_dynamics


g = 1.0

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
print(f"Escritorio detectado: {desktop}")
print()

# Barrido fino de lambda/g
lambdas = np.linspace(0.02, 2.0, 40)
print(f"Numero de valores de lambda: {len(lambdas)}")
print()

t_max = 60.0
n_steps = 4000   # resolución temporal alta para la FFT
dt = t_max / (n_steps - 1)

rabi_freqs = []

print("Calculando frecuencias de Rabi (esto puede tardar varios minutos)...")
for i, lam in enumerate(lambdas):
    print(f"  [{i+1}/{len(lambdas)}] lambda = {lam:.3f}", end="\r", flush=True)
    
    times, F, N1, N2, N3 = run_dynamics(g, lam, t_max=t_max, n_steps=n_steps)

    # Quitamos la componente DC (media) para la FFT
    F_ac = F - F.mean()
    spectrum = np.abs(np.fft.rfft(F_ac))
    freqs = np.fft.rfftfreq(n_steps, d=dt) * 2 * np.pi

    # Frecuencia dominante (excluyendo el bin 0)
    idx_peak = np.argmax(spectrum[1:]) + 1
    omega_rabi = freqs[idx_peak]
    rabi_freqs.append(omega_rabi)

rabi_freqs = np.array(rabi_freqs)
print(f"\nCalculo de Rabi completado ({len(lambdas)} valores)")
print()

# ---------------------------------------------------------------
# Leyes candidatas para comparar
# ---------------------------------------------------------------
law_sqrt = np.sqrt(g**2 + (2*lambdas)**2)

# ---------------------------------------------------------------
# GRAFICA 1: Frecuencia de Rabi (se muestra en Spyder)
# ---------------------------------------------------------------
print("Generando grafica 1: Frecuencia de Rabi...")

fig1, ax1 = plt.subplots(figsize=(9, 6))
ax1.plot(lambdas, rabi_freqs, 'o', color='crimson', ms=5, label=r"$\Omega_{Rabi}$ numérica (FFT)")
ax1.plot(lambdas, law_sqrt, '--', color='navy', lw=2, label=r"$\sqrt{g^2+(2\lambda)^2}$")
ax1.set_xlabel(r"$\lambda/g$")
ax1.set_ylabel(r"Frecuencia de Rabi $\Omega_{Rabi}$ (en unidades de $g$)")
ax1.set_title("Frecuencia de oscilación de la fidelidad vs. acoplamiento oscilador-dirección")
ax1.legend()
ax1.grid(alpha=0.3)
plt.tight_layout()

# Guardar en escritorio
filename1 = os.path.join(desktop, "toe_rabi_frequency.png")
plt.savefig(filename1, dpi=150)
print(f"Figura 1 guardada en: {filename1}")

# ---------------------------------------------------------------
# GRAFICA 2: Mapa de calor F(t) vs lambda
# ---------------------------------------------------------------

t_max2 = 25.0
n_steps2 = 300
lambdas2 = np.linspace(0.02, 2.0, 60)
F_matrix = np.zeros((len(lambdas2), n_steps2))

for i, lam in enumerate(lambdas2):
    print(f"  [{i+1}/{len(lambdas2)}] lambda = {lam:.3f}", end="\r", flush=True)
    
    times2, F2, *_ = run_dynamics(g, lam, t_max=t_max2, n_steps=n_steps2)
    F_matrix[i, :] = F2


fig2, ax2 = plt.subplots(figsize=(9, 6))
im = ax2.imshow(F_matrix, aspect='auto', origin='lower',
                 extent=[0, t_max2, lambdas2[0], lambdas2[-1]],
                 cmap='inferno', vmin=0, vmax=1)
ax2.set_xlabel(r"Tiempo (unidades de $1/\omega$)")
ax2.set_ylabel(r"$\lambda/g$")
ax2.set_title(r"Mapa de fidelidad $|\langle\Psi_{TOE},000|\Psi(t)\rangle|^2$")
cbar = fig2.colorbar(im, ax=ax2)
cbar.set_label("Fidelidad")
plt.tight_layout()

# Guardar en escritorio
filename2 = os.path.join(desktop, "toe_fidelity_map.png")
plt.savefig(filename2, dpi=150)
print(f"Figura 2 guardada en: {filename2}")

# Imprimir tabla resumen
print("\n" + "=" * 60)
print("TABLA RESUMEN")
print("=" * 60)
print("lambda/g | Omega_Rabi (numérica) | sqrt(g^2+(2lam)^2)")
print("-" * 60)
for lam, om in zip(lambdas[::4], rabi_freqs[::4]):
    print(f"{lam:.3f}   |  {om:.4f}  |  {np.sqrt(1+(2*lam)**2):.4f}")
print("=" * 60)

