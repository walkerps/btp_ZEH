import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt 
#from nltk import word_tokenizer

file = 'data_set.csv'

data = pd.read_csv(file)

data.plot.line(x = 'Hour',y = 'DCO')
plt.xlabel("Day of month")
plt.ylabel("DC Array Output")

data.plot.scatter(x = 'BI',y = 'DI',c = 'r')
plt.xlabel("Beam Irradiance")
plt.ylabel("Diffuse Irradiance")

data.plot.scatter(x = 'BI',y = 'AT')
plt.xlabel("Beam Irridance")
plt.ylabel("Ambient Temperature")

data.plot.scatter(x = 'BI',y = 'WS')
plt.xlabel("Beam Irridance")
plt.ylabel("Wind Speed")

data.plot.scatter(x = 'BI',y = 'PAI')
plt.xlabel("Beam Irridance")
plt.ylabel("Plane of Array Irridance")

data.plot.scatter(x = 'BI',y = 'CT')
plt.xlabel("Beam Irridance")
plt.ylabel("Cell Temperature")

data.plot.scatter(x = 'BI',y = 'DCO')
plt.xlabel("Beam Irridance")
plt.ylabel("DC Array Output")

data.plot.scatter(x = 'DI',y = 'AT')
plt.xlabel("Diffuse Irridance")
plt.ylabel("Ambient Temperature")

data.plot.scatter(x = 'DI',y = 'WS')
plt.xlabel("Diffuse Irradiance")
plt.ylabel("Wind Speed")

data.plot.scatter(x = 'DI',y = 'PAI')
plt.xlabel("Diffuse Irradiance")
plt.ylabel("Plane of Array Irradiance")

data.plot.scatter(x = 'DI',y = 'CT')
plt.xlabel("Diffuse Irradiance")
plt.ylabel("Cell Temperature")

data.plot.scatter(x = 'DI',y = 'DCO')
plt.xlabel("Diffuse Irradiance")
plt.ylabel("DC Array Output")

data.plot.scatter(x = 'AT',y = 'WS')
plt.xlabel("Ambient Temperature")
plt.ylabel("Cell Temperature")

data.plot.scatter(x = 'AT',y = 'PAI')
plt.xlabel("Ambient Temperature")
plt.ylabel("Plane of Array Irradiance")

data.plot.scatter(x = 'AT',y = 'CT')
plt.xlabel("Ambient Temperature")
plt.ylabel("Cell Temperature")

data.plot.scatter(x = 'AT',y = 'DCO')
plt.xlabel("Ambient temperature")
plt.ylabel("DC Array Output")

data.plot.scatter(x = "WS",y = 'PAI')
plt.xlabel("Wind Speed")
plt.ylabel("Plane of Array Irradiance")

data.plot.scatter(x = 'WS',y = 'CT')
plt.xlabel("Wind Speed")
plt.ylabel("Cell Temperature")

data.plot.scatter(x = 'WS',y = 'DCO')
plt.xlabel("Wind Speed")
plt.ylabel("DC Array Output")

data.plot.scatter(x = 'PAI',y = 'CT')
plt.xlabel("Plane of Array Irradiance")
plt.ylabel("Cell Temperature")

data.plot.scatter(x = 'PAI',y = 'DCO')
plt.xlabel("Plane of Array Irradiance")
plt.ylabel("DC Output Array")

data.plot.scatter(x = "CT",y = 'DCO')
plt.xlabel("Cell Temperature")
plt.ylabel("DC Output Array")

plt.show()