from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

sigma, rho, beta =16.0, 45.91, 4.0
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False  
def lorenz(t, s):
    x, y, z = s
    return [
        sigma * (y - x),
        x * (rho - z) - y,
        x * y - beta * z,
    ]
t = np.linspace(0, 60, 30000)
sol = solve_ivp(
    lorenz, [t[0], t[-1]], [-7.0, 3.0, 9.0],
    t_eval=t, rtol=1e-9, atol=1e-11,
)
x, y, z = sol.y