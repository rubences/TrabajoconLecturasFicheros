#Carga en Python de datos en formato csv desde URL

import pandas
url = "https://datahub.io/machine-learning/diabetes/r/diabetes.csv"
data = pandas.read_csv(url)
print(data)

# En Pandas, el modificador tail nos ofrece una vista de los datos mucho más atractiva
# Ver final
data.tail()

#Carga en Python de datos en formato csv usando Pandas
import pandas
filename = 'diabetes.csv'
data = pandas.read_csv(filename, header=0)

print(data.shape)
print (data.head(10))

#Ejemplo de carga ficheros csv con NumPy
import numpy
filename = 'diabetes.csv'
raw_data = open(filename)
data = numpy.loadtxt(raw_data, delimiter=",",skiprows=1)
print(data.shape)
print(data)

#con modulos
import os
os.chdir("C:\\Datos")
os.getcwd()

import csv
f= open("diabetes.csv")
reader = csv.reader(f)
for row in reader:
    print (row)

# Carga del dataset desde el repositorio usando pandas

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

#Carga de módulos y librerías

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# histogramas
dataset.hist()
plt.show()

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# Dimensiones del dataset
print(dataset.shape)

# Muestra los 20 primeros
print(dataset.head(20))

#Descripción del dataset
print(dataset.describe())