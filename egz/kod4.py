import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_csv("hotele4.csv", sep="#")
data2 = data.melt(id_vars="Nazwa", value_vars=["2017", "2018", "2019"],
                  var_name="Rok", value_name="Wartość")
data2["Rok"] = pd.Series(data2["Rok"], dtype=int)
pomorskie = data2[data2["Nazwa"]=="POMORSKIE"]
plt.scatter(pomorskie["Rok"], pomorskie["Wartość"])
plt.show()
