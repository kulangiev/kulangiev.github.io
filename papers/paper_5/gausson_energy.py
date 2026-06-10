# gausson_energy.py -- EXACT stationary 3D Gausson + energy functional (analytic, sympy)
# Logarithmic Schroedinger:  i hbar d_t psi = -(hbar^2/2m) lap psi - b ln(|psi|^2/rho*) psi
# (b = b_E, energy units; this is the NR reduction of the relativistic log-KG)
import sympy as sp

r, sigma, A, m, hbar, b, rho_star, c = sp.symbols('r sigma A m hbar b rho_star c', positive=True)

# --- 1. Gausson ansatz solves the stationary equation EXACTLY ---
phi = A*sp.exp(-r**2/(2*sigma**2))
lap = sp.simplify(sp.diff(r**2*sp.diff(phi,r),r)/r**2)        # radial 3D Laplacian
stationary = sp.expand(-(hbar**2/(2*m))*lap - b*sp.log(phi**2/rho_star)*phi)  # = hbar*Omega*phi
ratio = sp.simplify(stationary/phi)                          # must be r-independent for exact soln
coeff_r2 = sp.simplify(sp.expand(ratio).coeff(r,2))          # coefficient of r^2 -> must vanish
sigma_sol = sp.solve(sp.Eq(coeff_r2,0), sigma**2)
print("r^2 coefficient (must vanish):", coeff_r2)
print("=> Gausson width  sigma^2 =", sigma_sol, "  i.e. sigma^2 = hbar^2/(2 m b)   [EXACT]")

sig2 = hbar**2/(2*m*b)
# --- 2. Energy functional pieces as exact Gaussian integrals ---
gauss = lambda f: sp.integrate(f*4*sp.pi*r**2, (r,0,sp.oo))   # 3D radial integral
N   = sp.simplify(gauss(phi**2))                              # norm
T   = sp.simplify(gauss((hbar**2/(2*m))*sp.diff(phi,r)**2))   # kinetic energy
rho = phi**2
Ulog= sp.simplify(gauss(-b*rho*sp.log(rho/rho_star) + b*rho)) # log potential energy
print("\nNorm     N    =", N)
print("Kinetic  T    =", sp.simplify(T.subs(sigma**2, sig2)), " = (3/2) b N :", sp.simplify(T.subs(sigma**2,sig2) - sp.Rational(3,2)*b*N.subs(sigma**2,sig2))==0)
print("Log U    Ulog =", sp.simplify(Ulog.subs(sigma**2, sig2)))
E = sp.simplify((T+Ulog).subs(sigma**2, sig2))
print("Total E       =", E, "  (depends on ln(A^2/rho*) -> on the AMPLITUDE/norm choice)")

# --- 3. The dimensionless number that fixes the depletion prefactor ---
bR = 2*m*b/hbar**2                       # relativistic coupling (1/m^2) from b_E
print("\nRelativistic coupling  b_R = 2 m b_E/hbar^2")
print("EXACT invariant:  b_R * sigma^2 =", sp.simplify(bR*sig2), "  <-- the integral's clean output")
xi = hbar/(m*c)                          # 'sound' healing length convention
print("If xi := sigma (core = healing length):  b_R xi^2 = 1  -> ~c_s^2 = c^2/2 -> epsilon = -2U")
print("If xi := hbar/(m c) (BEC c_s convention): sigma = xi/sqrt2, b_R xi^2 = 2 -> ~c_s^2 = c^2 -> epsilon = -U")
print("ratio (xi_BEC/sigma)^2 =", sp.simplify((xi**2)/sig2.subs(b, m*c**2)), " (using b_E=m c^2)")
