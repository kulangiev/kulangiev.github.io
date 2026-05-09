"""
T_CMB Prediction Surface Plot
==============================
Visualization of the parameter-free relation from Paper 3 Eq. (T_prediction):

    T_CMB^4 = (45 hbar^3 c^5 alpha^2 H_0^2) / (8 pi^3 k_B^4 G)

The plot shows:
  - Top panel: T_CMB vs H_0 at fixed alpha (CODATA), with the framework's
    global H_0 prediction (68.15) and the SH0ES local value (73.04) marked.
  - Bottom panel: Sensitivity of the prediction to alpha at H_0 = 68.15.

Output: tcmb_prediction.pdf and .png in the running directory.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# =====================================================================
# Constants (CODATA + Planck/observational)
# =====================================================================
hbar = 1.054571817e-34          # J s
c = 2.99792458e8                # m/s
G = 6.67430e-11                 # m^3 kg^-1 s^-2
k_B = 1.380649e-23              # J/K
alpha_CODATA = 7.2973525693e-3  # fine-structure constant
T_FIRAS = 2.7255                # K, Fixsen 2009
T_FIRAS_err = 0.0006            # K
H0_global = 68.15               # km/s/Mpc, framework prediction
H0_planck = 67.36               # km/s/Mpc, Planck 2018
H0_sh0es = 73.04                # km/s/Mpc, SH0ES 2022
Mpc_in_m = 3.0857e22

# =====================================================================
# Prediction function
# =====================================================================
def T_CMB_predicted(H0_kmsmpc, alpha=alpha_CODATA):
    """T_CMB from postulate Omega_gamma = alpha^2."""
    H0_si = H0_kmsmpc * 1000.0 / Mpc_in_m
    T4 = 45.0 * hbar**3 * c**5 * alpha**2 * H0_si**2 / (8.0 * np.pi**3 * k_B**4 * G)
    return T4 ** 0.25


def H0_required(T_K, alpha=alpha_CODATA):
    """Inverse: what H_0 gives the measured T_CMB?"""
    H0_si_2 = 8.0 * np.pi**3 * k_B**4 * G * T_K**4 / (45.0 * hbar**3 * c**5 * alpha**2)
    H0_si = np.sqrt(H0_si_2)
    return H0_si * Mpc_in_m / 1000.0


def alpha_required(T_K, H0_kmsmpc):
    """Inverse: what alpha gives the measured T_CMB at given H_0?"""
    H0_si = H0_kmsmpc * 1000.0 / Mpc_in_m
    alpha2 = 8.0 * np.pi**3 * k_B**4 * G * T_K**4 / (45.0 * hbar**3 * c**5 * H0_si**2)
    return np.sqrt(alpha2)

# =====================================================================
# Data for plot
# =====================================================================
H0_range = np.linspace(60, 80, 400)
T_curve = T_CMB_predicted(H0_range, alpha_CODATA)

# Inverted prediction
H0_pred = H0_required(T_FIRAS, alpha_CODATA)
alpha_pred = alpha_required(T_FIRAS, H0_global)

# Sensitivity to alpha (vary by +-0.01% around CODATA)
alpha_range = alpha_CODATA * np.linspace(0.9999, 1.0001, 200)
T_alpha = T_CMB_predicted(H0_global, alpha_range)

# =====================================================================
# Plotting (journal-ready, white background)
# =====================================================================
fig, axes = plt.subplots(2, 1, figsize=(8.5, 9.5),
                         gridspec_kw={'height_ratios': [3, 2]})

# --- Top panel: T_CMB vs H_0 ---
ax = axes[0]
ax.plot(H0_range, T_curve, color='#0072B2', linewidth=2.2,
        label=r'$T_{\mathrm{CMB}}(\alpha, H_0) \propto \alpha\,H_0^{1/2}\,G^{-1/4}$')

# FIRAS measurement band
ax.axhspan(T_FIRAS - 5*T_FIRAS_err, T_FIRAS + 5*T_FIRAS_err,
           color='#D55E00', alpha=0.18, label=r'FIRAS $T_{\mathrm{CMB}} = 2.7255$ K ($\pm 5\sigma$)')
ax.axhline(T_FIRAS, color='#D55E00', linewidth=1.0, alpha=0.6)

# Mark H_0 values
ax.axvline(H0_planck, color='gray', linestyle=':', linewidth=1.2, alpha=0.7)
ax.axvline(H0_global, color='#009E73', linestyle='--', linewidth=1.5)
ax.axvline(H0_sh0es, color='#CC79A7', linestyle=':', linewidth=1.2, alpha=0.7)

# Mark the framework's prediction point
T_at_global = T_CMB_predicted(H0_global)
ax.plot(H0_global, T_at_global, 'o', color='#009E73',
        markersize=11, markeredgecolor='black', markeredgewidth=0.9, zorder=10,
        label=fr'Framework prediction: $T = {T_at_global:.4f}$ K at $H_0 = 68.15$')

# Annotations for the H_0 reference values
ax.annotate('Planck 67.36', xy=(H0_planck, 2.71), xytext=(H0_planck-0.2, 2.71),
            ha='right', fontsize=9, color='gray', rotation=90, va='top')
ax.annotate('Framework 68.15', xy=(H0_global, 2.85), xytext=(H0_global+0.2, 2.85),
            ha='left', fontsize=9, color='#009E73', rotation=90, va='top', fontweight='bold')
ax.annotate('SH0ES 73.04', xy=(H0_sh0es, 2.71), xytext=(H0_sh0es-0.2, 2.71),
            ha='right', fontsize=9, color='#CC79A7', rotation=90, va='top')

ax.set_xlabel(r'$H_0$ [km s$^{-1}$ Mpc$^{-1}$]', fontsize=12)
ax.set_ylabel(r'$T_{\mathrm{CMB}}$ [K]', fontsize=12)
ax.set_title(r'$T_{\mathrm{CMB}}$ as a parameter-free prediction: '
             r'$T^4 \propto \alpha^2 H_0^2 / G$',
             fontsize=12)
ax.set_xlim(60, 80)
ax.set_ylim(2.5, 2.95)
ax.grid(True, alpha=0.25)
ax.legend(loc='lower right', fontsize=9, framealpha=0.92)

# --- Bottom panel: residual zoom around the framework prediction ---
ax2 = axes[1]
H0_zoom = np.linspace(67.5, 68.7, 300)
T_zoom = T_CMB_predicted(H0_zoom, alpha_CODATA)
T_zoom_resid_ppm = (T_zoom - T_FIRAS) / T_FIRAS * 1e6

ax2.plot(H0_zoom, T_zoom_resid_ppm, color='#0072B2', linewidth=2.2)
ax2.axhline(0, color='#D55E00', linewidth=1.2, alpha=0.7,
            label=r'FIRAS $T_{\mathrm{CMB}} = 2.7255$ K (zero line)')

# FIRAS uncertainty band (ppm)
firas_band_ppm = T_FIRAS_err / T_FIRAS * 1e6
ax2.axhspan(-firas_band_ppm, firas_band_ppm, color='#D55E00', alpha=0.18,
            label=fr'FIRAS $\pm 1\sigma$ ($\pm$ {firas_band_ppm:.0f} ppm)')

# Mark global H_0
ax2.axvline(H0_global, color='#009E73', linestyle='--', linewidth=1.5)
T_global_resid_ppm = (T_at_global - T_FIRAS) / T_FIRAS * 1e6
ax2.plot(H0_global, T_global_resid_ppm, 'o', color='#009E73',
         markersize=11, markeredgecolor='black', markeredgewidth=0.9, zorder=10,
         label=fr'Framework: $\Delta T/T = {T_global_resid_ppm:+.0f}$ ppm at $H_0 = 68.15$')

# Mark the H_0 that EXACTLY reproduces FIRAS
ax2.axvline(H0_pred, color='black', linestyle=':', linewidth=1.0, alpha=0.6)
ax2.annotate(fr'$H_0 = {H0_pred:.3f}$ exactly fits FIRAS',
             xy=(H0_pred, 0), xytext=(H0_pred + 0.05, -300),
             fontsize=9, ha='left',
             arrowprops=dict(arrowstyle='->', color='black', lw=0.7))

ax2.set_xlabel(r'$H_0$ [km s$^{-1}$ Mpc$^{-1}$]', fontsize=12)
ax2.set_ylabel(r'$(T_{\mathrm{predicted}} - T_{\mathrm{FIRAS}}) / T_{\mathrm{FIRAS}}$ [ppm]',
               fontsize=12)
ax2.set_title(r'Zoom near framework prediction: residual at part-in-$10^4$ precision',
              fontsize=12)
ax2.set_xlim(67.5, 68.7)
ax2.set_ylim(-2500, 2500)
ax2.grid(True, alpha=0.25)
ax2.legend(loc='upper left', fontsize=9, framealpha=0.92)

plt.tight_layout()

# Save
folder = os.path.dirname(__file__)
plt.savefig(os.path.join(folder, 'tcmb_prediction.pdf'), dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig(os.path.join(folder, 'tcmb_prediction.png'), dpi=200, bbox_inches='tight', facecolor='white')
print('Plots saved to tcmb_prediction.pdf and .png')
plt.show()

# =====================================================================
# Summary
# =====================================================================
print('=' * 70)
print('Prediction summary')
print('=' * 70)
print()
print(f'Inputs:')
print(f'  alpha (CODATA)         = {alpha_CODATA:.6e}')
print(f'  H_0 (framework global) = {H0_global} km/s/Mpc')
print(f'  G                      = {G:.4e} m^3/(kg s^2)')
print()
print(f'Prediction:')
print(f'  T_CMB(alpha, H_0=68.15) = {T_at_global:.6f} K')
print(f'  FIRAS measurement       = {T_FIRAS} +/- {T_FIRAS_err} K')
print(f'  Difference              = {(T_at_global - T_FIRAS) * 1000:.4f} mK')
print(f'  Fractional difference   = {(T_at_global - T_FIRAS)/T_FIRAS * 100:+.4f}%')
print(f'                          = {(T_at_global - T_FIRAS)/T_FIRAS * 1e6:+.0f} ppm')
print()
print(f'Inversions:')
print(f'  Given T_FIRAS, alpha => H_0 = {H0_pred:.4f} km/s/Mpc')
print(f'  Given T_FIRAS, H_0   => alpha = {alpha_pred:.6e}')
print(f'    (CODATA alpha       = {alpha_CODATA:.6e})')
print(f'    Fractional diff     = {(alpha_pred - alpha_CODATA)/alpha_CODATA * 100:+.4f}%')
print()
print('Interpretation: with Omega_gamma = alpha^2 as input postulate, the')
print('framework over-determines the system {alpha, H_0, T_CMB, G}. Any three')
print('predict the fourth to part-in-10^4 precision.')
