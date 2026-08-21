import numpy as np
import matplotlib.pyplot as plt
import lorenz_attractor.lorenz as l
from lorenz_attractor.dmi import dmi

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False  

fig = plt.figure(figsize=(14, 5))

ax = fig.add_subplot(141, projection="3d")
ax.plot(l.x[::2], l.y[::2], l.z[::2], lw=0.3)
ax.set_title("原始 Lorenz 吸引子")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

tau_x=int(dmi(l.x)/2)
tau_y=int(dmi(l.y)/2)    
tau_z=int(dmi(l.z)/2)
# tau_x=70
# tau_y=70
# tau_z=70
Xn = l.x[:-2 * tau_x]
print(len(Xn))
Yn = l.x[tau_x:-tau_x]
Zn = l.x[2 * tau_x:]
ax2 = fig.add_subplot(142, projection="3d")
ax2.plot(Xn[::2], Yn[::2], Zn[::2], lw=0.3)
ax2.set_title(f"τ={tau_x}")
ax2.set_xlabel("x(t)")
ax2.set_ylabel("x(t+τ)")
ax2.set_zlabel("x(t+2τ)")

Xn = l.y[:-2 * tau_y]
Yn = l.y[tau_y:-tau_y]
Zn = l.y[2 * tau_y:]

ax3 = fig.add_subplot(143, projection="3d")
ax3.plot(Xn[::2], Yn[::2], Zn[::2], lw=0.3)
ax3.set_title(f"τ={tau_y}")
ax3.set_xlabel("y(t)")
ax3.set_ylabel("y(t+τ)")
ax3.set_zlabel("y(t+2τ)")

Xn = l.z[:-2 * tau_z]
Yn = l.z[tau_z:-tau_z]
Zn = l.z[2 * tau_z:]

ax4 = fig.add_subplot(144, projection="3d")
ax4.plot(Zn[::2], Xn[::2], Yn[::2], lw=0.3)
ax4.set_title(f"τ={tau_z}")
ax4.set_xlabel("z(t)")
ax4.set_ylabel("z(t+τ)")
ax4.set_zlabel("z(t+2τ)")
plt.savefig("lorenz_attractor.png", dpi=300)
plt.show()