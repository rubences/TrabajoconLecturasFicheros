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
