import numpy as np 
from matplotlib import pyplot as plt 
import pandas as pd
import datadotworld as dw

dataset = dw.load_dataset('tonatihu/prueba-sngular')
dataset.describe()
dataframedatos = dataset.dataframes['datos']
dataframeprovincia = dataset.dataframes['provincia']

left = pd.DataFrame(dataframeprovincia)
right = pd.DataFrame(dataframedatos)

mergequery = pd.merge(left,right,on='id_provincia', how='inner')
prov = mergequery.groupby('provincia')
readytoplot = prov['ventas_totales'].agg(np.sum)

print(readytoplot)

plt.title("Ventas por provincia") 
plt.xlabel("Ventas totales") 
plt.ylabel("Provincia") 
plt.plot(readytoplot) 
plt.show()