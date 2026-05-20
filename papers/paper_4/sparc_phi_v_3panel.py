"""
SPARC Phi_v Analysis: Publication Figure (3 panels)
=====================================================
Panels:
  (a) Required delta_v(r) for all 112 galaxies
  (b) Stability census histogram
  (c) |delta_v| vs g_bar
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))

c_km = 3e5
G_N = 4.3009e-6
STABILITY_LIMIT = 1.0 / np.e

def parse_sparc(filename=None):
    if filename is None:
        for candidate in ['Table2.mrt', 'datafile2.txt']:
            candidate_path = os.path.join(script_dir, candidate)
            if os.path.exists(candidate_path):
                filename = candidate_path
                break
    elif not os.path.isabs(filename):
        filename = os.path.join(script_dir, filename)

    galaxies = defaultdict(lambda: {'r': [], 'vobs': [], 'errv': [],
                                     'vgas': [], 'vdisk': [], 'vbul': []})
    if filename is None or not os.path.exists(filename):
        print("ERROR: SPARC data file not found!"); sys.exit(1)
    print(f"Reading: {filename}")
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('#') or line.startswith('|') or \
               line.startswith('-') or line.strip() == '' or \
               line.startswith('T') or line.startswith('A') or \
               line.startswith('B') or line.startswith('N') or \
               line.startswith('='):
                continue
            try:
                name = line[0:11].strip()
                r = float(line[19:25])
                vobs = float(line[26:32])
                errv = float(line[33:38])
                vgas = float(line[39:45])
                vdisk = float(line[46:52])
                vbul = float(line[53:59])
                if name == '' or r <= 0: continue
                galaxies[name]['r'].append(r)
                galaxies[name]['vobs'].append(vobs)
                galaxies[name]['errv'].append(errv)
                galaxies[name]['vgas'].append(vgas)
                galaxies[name]['vdisk'].append(vdisk)
                galaxies[name]['vbul'].append(vbul)
            except (ValueError, IndexError):
                continue
    for name in galaxies:
        for key in galaxies[name]:
            galaxies[name][key] = np.array(galaxies[name][key])
    return dict(galaxies)

def compute_phi_v(gal, ML_disk=0.5, ML_bul=0.7):
    r = gal['r']; vobs = gal['vobs']
    vgas = gal['vgas']; vdisk = gal['vdisk']; vbul = gal['vbul']
    v_bar_sq = np.abs(vgas)*vgas + ML_disk*np.abs(vdisk)*vdisk + \
               ML_bul*np.abs(vbul)*vbul
    vobs_sq = vobs**2
    v_missing_sq = vobs_sq - np.maximum(v_bar_sq, 0)
    d_delta_dr = v_missing_sq / (c_km**2 * r)
    delta_v = np.zeros_like(r)
    for i in range(len(r)-2, -1, -1):
        delta_v[i] = delta_v[i+1] - d_delta_dr[i+1] * (r[i+1] - r[i])
    g_obs = vobs_sq / r * 1e6 / 3.086e19
    g_bar = np.maximum(np.maximum(v_bar_sq, 0), 1.0) / r * 1e6 / 3.086e19
    return {'r': r, 'delta_v': delta_v, 'g_obs': g_obs, 'g_bar': g_bar}

# Load and analyze
galaxies = parse_sparc()
all_profiles = {}
max_delta_list = []
all_delta_flat = []
all_gbar_flat = []
all_g_obs = []
all_g_bar = []

for name in sorted(galaxies.keys()):
    gal = galaxies[name]
    if len(gal['r']) < 3: continue
    prof = compute_phi_v(gal)
    all_profiles[name] = prof
    max_delta_list.append(np.max(np.abs(prof['delta_v'])))
    valid = (prof['g_bar'] > 1e-13) & (prof['g_obs'] > 1e-13)
    all_delta_flat.extend(np.abs(prof['delta_v'][valid]))
    all_gbar_flat.extend(prof['g_bar'][valid])
    all_g_obs.extend(prof['g_obs'][valid])
    all_g_bar.extend(prof['g_bar'][valid])

max_deltas = np.array(max_delta_list)
all_delta_flat = np.array(all_delta_flat)
all_gbar_flat = np.array(all_gbar_flat)
n_gal = len(all_profiles)

print(f"\nAnalyzed {n_gal} galaxies")
print(f"Max |delta_v|:       {np.max(max_deltas):.2e}")
print(f"Median |delta_v|:    {np.median(max_deltas):.2e}")
print(f"Stability limit:     {1-STABILITY_LIMIT:.4f}")
print(f"All within stability: {np.max(max_deltas) < (1-STABILITY_LIMIT)}")
print(f"Margin:              {(1-STABILITY_LIMIT)/np.max(max_deltas):.0f}x")

# Pick sample galaxies for highlighting
sample_names = []
for known in ['NGC6503', 'NGC2403', 'NGC3198', 'NGC7331', 'DDO154', 'UGC128']:
    if known in all_profiles:
        sample_names.append(known)
if len(sample_names) < 5:
    extras = sorted(all_profiles.keys())[::n_gal//5]
    for e in extras:
        if e not in sample_names:
            sample_names.append(e)
        if len(sample_names) >= 5:
            break
colors = plt.cm.tab10(np.linspace(0, 1, len(sample_names)))

# =====================================================================
# 3-PANEL FIGURE
# =====================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

# --- (a) delta_v(r) profiles ---
ax = axes[0]
for name in sorted(all_profiles.keys()):
    p = all_profiles[name]
    ax.plot(p['r'], p['delta_v'] * 1e6, '-', color='#0072B2',
            alpha=0.06, linewidth=0.5)
for name, col in zip(sample_names, colors):
    p = all_profiles[name]
    ax.plot(p['r'], p['delta_v'] * 1e6, '-', color=col,
            linewidth=1.5, label=name)
ax.axhline(0, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('$r$ (kpc)', fontsize=13)
ax.set_ylabel(r'$\delta_v(r) \;\;[\times 10^{-6}]$', fontsize=13)
ax.set_title(f'(a) Required vacuum perturbation ({n_gal} galaxies)',
             fontsize=12)
ax.set_xlim(0, 50)
ax.legend(fontsize=8, loc='lower left')
ax.grid(True, alpha=0.2)

# --- (b) Stability histogram ---
ax = axes[1]
ax.hist(np.log10(max_deltas), bins=25, color='#0072B2',
        edgecolor='white', alpha=0.8)
ax.axvline(np.log10(1 - STABILITY_LIMIT), color='red',
           linestyle='--', linewidth=2.5,
           label=f'Stability limit ($|\\delta_v| = 0.63$)')
ax.set_xlabel(r'$\log_{10}\;\mathrm{max}|\delta_v|$ per galaxy',
              fontsize=13)
ax.set_ylabel('Number of galaxies', fontsize=13)
ax.set_title('(b) Stability census', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.2)

# Annotate the gap
ax.annotate(f'$10^5 \\times$ margin',
            xy=(np.log10(1-STABILITY_LIMIT)-0.3, 1),
            fontsize=12, color='red', fontweight='bold',
            ha='right')

# --- (c) |delta_v| vs g_bar ---
ax = axes[2]

log_g_bins = np.linspace(-13, -9, 35)
delta_median = np.zeros(len(log_g_bins)-1)
delta_16 = np.zeros(len(log_g_bins)-1)
delta_84 = np.zeros(len(log_g_bins)-1)
g_cen = np.zeros(len(log_g_bins)-1)

for i in range(len(log_g_bins)-1):
    mask = (np.log10(all_gbar_flat) >= log_g_bins[i]) & \
           (np.log10(all_gbar_flat) < log_g_bins[i+1])
    if np.sum(mask) > 5:
        delta_median[i] = np.median(all_delta_flat[mask])
        delta_16[i] = np.percentile(all_delta_flat[mask], 16)
        delta_84[i] = np.percentile(all_delta_flat[mask], 84)
        g_cen[i] = 10**(0.5*(log_g_bins[i] + log_g_bins[i+1]))

vb = delta_median > 0
ax.fill_between(np.log10(g_cen[vb]), delta_16[vb], delta_84[vb],
                alpha=0.25, color='#D55E00')
ax.semilogy(np.log10(g_cen[vb]), delta_median[vb], 'o-',
            color='#D55E00', linewidth=2, markersize=4,
            label=r'Median $|\delta_v|$')
ax.axhline(1 - STABILITY_LIMIT, color='red', linestyle='--',
           linewidth=2.5, label=f'Stability limit (0.63)')
ax.set_xlabel(r'$\log_{10}\;g_{\mathrm{bar}}$ (m/s$^2$)', fontsize=13)
ax.set_ylabel(r'$|\delta_v|$', fontsize=13)
ax.set_title(r'(c) Required $|\delta_v|$ vs baryonic acceleration',
             fontsize=12)
ax.set_xlim(-13, -9)
ax.set_ylim(1e-9, 1)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'sparc_phi_v_3panel.png'), dpi=200,
            bbox_inches='tight', facecolor='white')
plt.savefig(os.path.join(script_dir, 'sparc_phi_v_3panel.pdf'), dpi=300,
            bbox_inches='tight', facecolor='white')
print(f"\nPlots saved to {script_dir}")
plt.show()
