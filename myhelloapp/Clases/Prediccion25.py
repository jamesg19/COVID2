# #from myhelloapp.Clases.Reporte import Reporte
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.pipeline import make_pipeline
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# import numpy as np
import pandas as pd
import datetime as dt
import random
class Prediccion25:
    def __init__(self):
        pass
    #Predicción de casos confirmados por día
    def analizar25(self,resultados,positivos,filtrar,columnaFiltrar,valorFiltrar,min,max,region):
        
        dataTemp = pd.read_csv('archivo.csv')

        # if(filtrar=="si"):
            
        #     #dataTemp = pd.read_csv('archivo.csv')
        #     newData = dataTemp[columnaFiltrar] == valorFiltrar
        #     data = dataTemp[newData]
            
        #     dataTemp=data
            

        # # dataTemp[dias]= pd.to_datetime(dataTemp[dias])
        # # dataTemp[dias]=dataTemp[dias].map(dt.datetime.toordinal)
        
        # X = np.asarray(dataTemp[resultados].array)[:,np.newaxis]
        # y = np.asarray(dataTemp[positivos].array)


        
        # xTemp, X_test, y_t, y_test = train_test_split(X, y, test_size = 0.3)


        # reg = LinearRegression()
        # reg.fit(xTemp, y_t)

        # y_pred = reg.predict(X_test)

        # df = pd.DataFrame({'Valores reales':y_test, 'Prediccion valores':y_pred})
        # plt.scatter(X_test, y_test, color = 'red')
        # plt.scatter(X_test, y_pred, color = 'blue')
        # plt.plot(xTemp, reg.predict(xTemp), color = 'black')
        # plt.title('Test confirmados / Test realizados')
        # plt.xlabel('Test realizados')
        # plt.ylabel('Test confirmados')
        # plt.savefig('./helloworld/static/img.png')
        # plt.cla()


        