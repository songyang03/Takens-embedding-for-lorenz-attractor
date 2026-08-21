import numpy as np
from scipy.spatial import cKDTree
import lorenz_attractor.lorenz as l
from lorenz_attractor.dmi import dmi
import matplotlib.pyplot as plt
def fnn(series, tau, max_dim=10, R_tol=10.0,
        theiler=0):
    series = np.asarray(series, dtype=float)
    n = len(series)
    max_offset = (max_dim - 1) * tau
    centers = np.arange(n - max_offset)
    num = len(centers)
    k=list()
    for m in range(1, max_dim + 1):
        M = np.column_stack([series[centers + k * tau] for k in range(m)])
        tree = cKDTree(M[:-1])
        dists, idx = tree.query(M[:-1], k=2)
        ncount = 0
        for i in range(num-1):
            j = idx[i, 1]
            if abs(i - j) <= theiler:
                continue
            R_m = dists[i, 1]
            R_m1 = np.linalg.norm(M[i+1] - M[j+1])
            if R_m == 0:
                continue
            if (R_m1 / R_m > R_tol) :
                ncount += 1
        k.append(ncount / (num-m+1))     
    return k
tau=dmi(l.z)
p=fnn(l.z, tau)
fig, ax = plt.subplots()
ax.plot(range(1, len(p) + 1), p, "o-")
ax.set_xlabel("Embedding Dimension")
ax.set_ylabel("False Nearest Neighbors")
ax.set_title("FNN Method")
plt.show()
print(p)