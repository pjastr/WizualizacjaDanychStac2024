import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_excel("samochody02.xlsx", header=None).T
data.columns = ["Rodzaj", "Rok", "Wartość"]
autobusy = data[data["Rodzaj"] == "autobusy"]
plt.bar(autobusy["Rok"], autobusy["Wartość"])
plt.show()