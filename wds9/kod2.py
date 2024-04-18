import pandas as pd

data = pd.read_csv("gastro21.csv", header=None).T
data.columns = ["Typ punktu", "Rok", "Liczba"]
data["Rok"] = pd.Series(data["Rok"], dtype=int)
data["Liczba"] = pd.Series(data["Liczba"], dtype=int)
