from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
import lorenz_attractor.lorenz as l
def mutual_info(series, tau, bins=128):
    x0 = series[:-tau]
    x1 = series[tau:]
    hist, _, _ = np.histogram2d(x0, x1, bins=bins, density=True)
    hist /= hist.sum()
    px = hist.sum(axis=1)
    py = hist.sum(axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        mi = np.nansum(hist * np.log2(hist / (px[:, None] * py[None, :])))
    return mi
def dmi(series):
    # tau_opt = None
    taus = np.arange(1, 160)
    mis = [mutual_info(series, tau) for tau in taus]
    for i in range(1, len(mis) - 1):
        if mis[i] < mis[i - 1] and mis[i] <= mis[i + 1]:
           tau_opt = taus[i]
           break
    # if tau_opt is None:
    #     tau_opt = int(taus[np.nanargmin(mis)])
    return tau_opt
if __name__ == "__main__":
    fig, ax = plt.subplots()
    taus = np.arange(1, 160)
    mis = [mutual_info(l.x, tau) for tau in taus]
    tau_opt = dmi(l.x)
    ax.plot(taus, mis, "o-")
    ax.axvline(tau_opt, color="red", ls="--")
    ax.set_xlabel("tau")
    ax.set_ylabel("I(tau)")
    ax.set_title("Mutual Information")
    plt.show()    


