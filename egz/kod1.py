import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.arange(0,10, 0.1)
fig, ax1 = plt.subplots()
y1 = x**2 +3
ax1.plot(x,y1,"red")
ax1.set_title("Dwa Wykresy")
ax1.set_ylabel(r"$y=x^2+3$")
ax2 = ax1.twinx()
y2 = np.exp(x) -1
ax2.plot(x,y2)
ax2.set_ylabel(r"$y=e^x-1$")
plt.tight_layout()
plt.savefig("zad1.tiff")
plt.show()
