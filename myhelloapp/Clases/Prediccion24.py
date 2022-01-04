import pandas as pandass
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import  mean_squared_error, r2_score

#Comparación entre el número de casos detectados y el número de pruebas de un país.  
class Prediccion24:
    def __init__(self):
        self.resultados=[]
        pass
    
    #Comparación entre el número de casos detectados y el número de pruebas de un país.  
    def analizar24(self,test,casos,filtrar,columnaFiltrar,valorFiltrar):
        
        dataTemp = pandass.read_csv('archivo.csv')
        dataTemp=dataTemp.replace(np.nan, 0)
        if(filtrar=="si"):

            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]

            dataTemp=data

        dataEntrada = []
        x = dataTemp[test]
        y = dataTemp[casos]
        ite=-1
        for i in x:
            ite=ite+1
            dataEntrada.append([  x[ite] ,y[ite]  ])


        X = np.array(dataEntrada)
        scikit = KMeans(n_clusters=3)
        scikit.fit(X)
        self.resultados=scikit.cluster_centers_

        plt.scatter(X[:,0],X[:,1], c=scikit.labels_, cmap='rainbow')
        plt.scatter(scikit.cluster_centers_[:,0], scikit.cluster_centers_[:,1], color='black')
        plt.xlabel("Test Realizados")
        plt.ylabel("Casos Detectados")
        plt.savefig('./helloworld/static/img.png')
        plt.cla()

