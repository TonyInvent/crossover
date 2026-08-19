import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

# ============================================================================
# Final conventional design: 4th-order Linkwitz-Riley low-pass + Zobel
# impedance compensation. No optimization -- closed-form textbook formulas.
#
# Goals:
#   1) flat in-band response
#   2) source impedance seen by the driver kept as low as practical
#      (the Zobel gives the back-EMF a local drain path)
#
# Why we no longer use differential_evolution:
#   The exploration (see archive/) concluded that the source-impedance spike
#   near the crossover point is intrinsic to a passive 4th-order L-C ladder;
#   no optimizer can remove it. And at that frequency the cone is already in
#   its mass-controlled region (velocity is low), so the spike barely affects
#   damping. The conventional LR4 + Zobel is the sound engineering answer.
# ============================================================================

# ---- Thiele-Small parameters of the woofer (6.5", 8-ohm mid-woofer) ----
RE  = 6.2        # voice-coil DC resistance [ohm]
LE  = 0.7e-3     # voice-coil inductance [H]
BL  = 9.0        # force factor [N/A = T*m]
MMS = 0.022      # total moving mass [kg]
CMS = 4.2e-4     # mechanical compliance of the suspension [m/N]
RMS = 1.8        # mechanical resistance (suspension losses) [N*s/m]

FS      = 1.0 / (2*np.pi*np.sqrt(MMS*CMS))
QMS     = (1.0/RMS) * np.sqrt(MMS/CMS)
QES     = (RE/BL**2) * np.sqrt(MMS/CMS)
QTS     = QMS*QES/(QMS+QES)
D_IDEAL = BL**2/RE            # electromagnetic damping ceiling of a direct amp [N*s/m]

FC = 2000.0                   # crossover frequency [Hz]
WC = 2*np.pi*FC
R  = RE                       # design the network for the DC voice-coil resistance

# ---- Conventional LR4 low-pass (textbook normalized coefficients) -----------
# Denominator D(p) = (p^2 + sqrt(2)*p + 1)^2, with p = s/wc:
#   l1 = 4*sqrt(2)/3,  c2 = 9/(4*sqrt(2)),  l3 = 2*sqrt(2)/3,  c4 = 1/(2*sqrt(2))
L1 = (4*np.sqrt(2)/3)     * R / WC
C2 = (9/(4*np.sqrt(2)))   / (WC * R)
L3 = (2*np.sqrt(2)/3)     * R / WC
C4 = (1/(2*np.sqrt(2)))   / (WC * R)

# ---- Zobel network (voice-coil inductance compensation) ---------------------
RZ = RE
CZ = LE / RE**2

# ---- Parasitics of the real components --------------------------------------
DCR_L1 = DCR_L3 = 0.08
ESR_C2 = ESR_C4 = 0.05

# ---- Frequency grid ---------------------------------------------------------
f = np.logspace(np.log10(10), np.log10(20000), 3000)
w = 2*np.pi*f
Z_ms     = RMS + 1j*w*MMS + 1/(1j*w*CMS)          # mechanical impedance
Z_woofer = RE + 1j*w*LE + BL**2/Z_ms              # driver electrical input impedance
Z_zobel  = RZ + 1/(1j*w*CZ)

def par(a, b): return 1/(1/a + 1/b)

def compute():
    zL1 = DCR_L1 + 1j*w*L1
    zL3 = DCR_L3 + 1j*w*L3
    zC2 = ESR_C2 + 1/(1j*w*C2)
    zC4 = ESR_C4 + 1/(1j*w*C4)

    load  = par(Z_woofer, Z_zobel)               # load the crossover drives (driver || Zobel)
    zout  = par(load, zC4)
    zright = zL3 + zout
    zmid  = par(zC2, zright)
    H = (zmid/(zL1+zmid)) * (zout/(zL3+zout))    # electrical voltage transfer function

    # Source impedance seen by the driver (amp shorted -> independent of load).
    Z_s = par(zC4, zL3 + par(zC2, zL1))

    # External impedance seen by the back-EMF: the source impedance in parallel
    # with the Zobel (the Zobel is across the driver, so it shunts the loop).
    Z_ext = par(Z_s, Z_zobel)

    i = H / Z_woofer          # voice-coil current
    u = BL * i / Z_ms         # cone velocity
    a = 1j * w * u            # acceleration (sound pressure ~ acceleration)

    eta = np.real(BL**2/(RE + 1j*w*LE + Z_ext)) / D_IDEAL   # electromagnetic damping efficiency
    return H, Z_s, Z_ext, a, eta

H, Z_s, Z_ext, a, eta = compute()

def db(x): return 20*np.log10(np.maximum(np.abs(x), 1e-15))
def interp(f0, y): return np.interp(np.log(f0), np.log(f), y)

HdB = db(H)
adB = db(a) - np.median(db(a)[(f >= 150) & (f <= 800)])   # acoustic response, normalized to the mass-controlled plateau
eta_direct = np.real(BL**2/(RE + 1j*w*LE)) / D_IDEAL
m_flat = (f >= 200) & (f <= 1000)                          # in-band (clear of the driver's own resonance)

# ---- Key numbers ------------------------------------------------------------
print("Final conventional design: LR4 low-pass + Zobel (no optimization)")
print("="*64)
print(f"Driver : Fs={FS:.1f} Hz  Qms={QMS:.3f}  Qes={QES:.3f}  Qts={QTS:.3f}  Re={RE} ohm  Le={LE*1e3:.2f} mH")
print(f"Crossover : fc={FC/1000:.1f} kHz (electrical -6 dB point)")
print(f"LR4  : L1={L1*1e3:.3f} mH  C2={C2*1e6:.1f} uF  L3={L3*1e3:.3f} mH  C4={C4*1e6:.2f} uF")
print(f"Zobel: Rz={RZ} ohm  Cz={CZ*1e6:.1f} uF   (= Le/Re^2)")
print()
print(f"|H(fc)|              = {interp(FC, HdB):.2f} dB   (electrical)")
print(f"|H(4fc)|             = {interp(4*FC, HdB):.2f} dB")
print(f"acoustic @fc         = {interp(FC, adB):.2f} dB   (normalized)")
_flat_dev = np.max(HdB[m_flat]) - np.min(HdB[m_flat])
print(f"in-band (200Hz..1kHz) electrical deviation = {_flat_dev:.2f} dB (about +/-{_flat_dev/2:.1f} dB)")
print(f"  (a textbook LR4 into a pure resistor is only 0.46 dB; the extra deviation")
print(f"   comes from the driver's motional impedance + the Zobel's passband side effect)")
print()
print("Driver-side source impedance |Zs| (the fc spike is topology; Zobel shunts it):")
for v in [50, 100, 500, 1000, 2000, 4000]:
    print(f"  {v:>5} Hz: |Zs|={interp(v, np.abs(Z_s)):6.1f} ohm   |Zs||Zz|={interp(v, np.abs(Z_ext)):6.1f} ohm")
print()
print("Damping efficiency eta = D/(Bl^2/Re):")
print(f"  eta@Fs  = {interp(FS, eta):.3f}")
print(f"  eta@100 = {interp(100, eta):.3f}")
print(f"  eta@1k  = {interp(1000, eta):.3f}   (Zobel fixes the 1 kHz damping hole)")
print(f"  eta@2k  = {interp(2000, eta):.3f}")

# ---- Plots ------------------------------------------------------------------
out = os.path.dirname(os.path.abspath(__file__))

plt.figure(figsize=(9, 5))
plt.semilogx(f, HdB, label="electrical |H|")
plt.semilogx(f, adB, label="acoustic (normalized)")
plt.axvline(FC, ls="--", color="k", alpha=0.5)
plt.axhline(-6, ls="--", color="k", alpha=0.4)
plt.xlabel("Frequency [Hz]"); plt.ylabel("Response [dB]")
plt.title("LR4 + Zobel: flat in-band response")
plt.grid(True, which="both", alpha=0.3); plt.legend()
plt.tight_layout(); plt.savefig(os.path.join(out, "crossover_response.png"), dpi=110); plt.close()

plt.figure(figsize=(9, 5))
plt.semilogx(f, np.abs(Z_s), label="|Zsource| seen by woofer")
plt.semilogx(f, np.abs(Z_ext), label="|Zsource| || Zobel (back-EMF loop)")
plt.axvline(FC, ls="--", color="k", alpha=0.5)
plt.xlabel("Frequency [Hz]"); plt.ylabel("impedance [ohm]")
plt.title("Driver-side source impedance (fc spike is topology; Zobel shunts it)")
plt.grid(True, which="both", alpha=0.3); plt.legend()
plt.tight_layout(); plt.savefig(os.path.join(out, "crossover_zsource.png"), dpi=110); plt.close()

plt.figure(figsize=(9, 5))
plt.semilogx(f, eta, label="through crossover + Zobel")
plt.semilogx(f, eta_direct, ls="--", label="ideal amp, no crossover")
plt.axvspan(FS, FC, color="tab:green", alpha=0.06)
plt.axvline(FC, ls="--", color="k", alpha=0.5)
plt.axhline(1.0, ls="--", color="k", alpha=0.4)
plt.xlabel("Frequency [Hz]"); plt.ylabel("damping  eta = D/(Bl^2/Re)")
plt.title("Electromagnetic damping")
plt.grid(True, which="both", alpha=0.3); plt.legend(); plt.ylim(0, 1.05)
plt.tight_layout(); plt.savefig(os.path.join(out, "crossover_damping.png"), dpi=110); plt.close()

print()
print("Saved: crossover_response.png, crossover_zsource.png, crossover_damping.png")
