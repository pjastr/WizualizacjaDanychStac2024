import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("medale01.csv",sep=";")
letnie = data[data["Rodzaj"]=="Letnie"]