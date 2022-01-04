from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures



#Porcentaje de muertes frente al total de casos en un país, región o continente. 
class Prediccion16:
    def __init__(self):
        self.muertes=0
        self.casos=0

    def analizar16(self,casosConfirmados,Muertes,filtrar,columnaFiltrar,valorFiltrar):   
        dataTemp = pd.read_csv('archivo.csv')     
        dataTemp=dataTemp.replace(np.nan, 0)
        
        if(filtrar=="si"):
            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]
            dataTemp=data
        #gace la sumatoria de casos en una columna y de muertes y obtiene el porcentaje
        sumaCasos=dataTemp[casosConfirmados].sum()
        sumMuertes=dataTemp[Muertes].sum()
        self.muertes=sumMuertes
        self.casos=sumaCasos
        result=sumMuertes/sumaCasos
        
        return str(result)+""