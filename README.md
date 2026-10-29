# Paper3-VacuumVessel-TsaiWu

## 📌 Repository Overview
Computational benchmark and numerical yield solver for **Paper III**:
> **"Evaluating Vacuum Vessel Structural Reserves Under Asymmetric Halo Currents Using 3D Anisotropic Tsai-Wu Failure Envelopes"**
> *Target Journal:* **Fusion Engineering and Design** (Elsevier)
> *Publishing Model:* **Traditional Subscription (No-Fee Publishing Model)**
> *Author:* **Jacob James Rasmussen**

## 🔬 Benchmark Physics & Margins
- **Material:** Inconel 718 shear key pin interlocks
- **Failure Criterion:** 3D anisotropic Tsai-Wu interactive failure surface ($f_{\text{TW}} \le 1.0$)
- **Energy Positivity Constraint:** $T_{00} \ge 0$
- **Coordinate Stresses:** $\sigma_1 = -158.5\text{ MPa}$, $\sigma_2 = -110.0\text{ MPa}$, $\tau_{13} = 180.0\text{ MPa}$
- **Dynamic Response:** Peak DAF = 1.85 ($I_{\text{halo}} = 1.8\text{ MA}$, 50–200 Hz)
- **Evaluated Safety Metrics:** Failure Index $f_{\text{TW}} = 0.244 \le 1.0$, Strength Reserve Ratio $SRR = 1.61 > 1.0$
- **3D Grid Convergence:** $\text{GCI}_{12} = 0.42\% \le 0.50\%$
