import pandas as pandass
from sklearn.linear_model import LinearRegression
import numpy as np

#Tasa de mortalidad por coronavirus (COVID-19) en un país. 
class Prediccion22:
    def __init__(self):
        self.muertes=0
        self.confirmados=0
        pass
    #Tasa de mortalidad por coronavirus (COVID-19) en un país. 
    def analizar22(self,dias,confirmados,muertes):
        
        dataTemp = pandass.read_csv('archivo.csv')
        dataTemp=dataTemp.replace(np.nan, 0)
        X = np.asarray(dataTemp[dias].array)[:,np.newaxis]
        y = np.asarray(dataTemp[confirmados].array)[:,np.newaxis]
        z = np.asarray(dataTemp[muertes].array)[:,np.newaxis]

        model = LinearRegression()
        model.fit(X=X, y=y)

        predict = [365]
        predict = np.array(predict).reshape(-1,1) 

        prediccionConfirmado = model.predict(predict)

        model.fit(X=X, y=z)
        prediccionesMuerto = model.predict(predict)
        mt=round(prediccionesMuerto[0][0],2)
        conf=round(prediccionConfirmado[0][0],2)
        self.muertes=str(mt)
        self.confirmados=str(conf)
        rat=(prediccionesMuerto[0][0] / prediccionConfirmado[0][0])*100
        rate2=round(rat,2)
        return str(rate2)
