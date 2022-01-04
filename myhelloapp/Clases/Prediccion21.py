from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Prediccion21:
    def __init__(self):
        pass

    def analizar21(self,infectados,filtrar,columnaFiltrar,valorFiltrar,max,titulo,img):
            dataTemp = pd.read_csv('archivo.csv')
            dataTemp=dataTemp.replace(np.nan, 0)
            
            if(filtrar=="si"):
                
                #dataTemp = pd.read_csv('archivo.csv')
                newData = dataTemp[columnaFiltrar] == valorFiltrar
                data = dataTemp[newData]
                
                dataTemp=data

            
            yTemp = np.asarray(dataTemp[infectados])
            cases=[]
            for i in yTemp:
                cases.append(i)
            print(cases)
            
            count_cases = []
            val = 0
            for i in cases:
                val = val+i
                count_cases.append(val)

            print(len(count_cases))

            days = []
            for i in range(len(count_cases)):
                days.append(i + 1)

            count_cases = np.asarray(count_cases)
            days = np.asarray(days)

            count_cases = count_cases[:, np.newaxis]
            days = days[:, np.newaxis]

            # Prediccion para dia
            sequence = np.linspace(days.min(), int(max), int(max)+50).reshape(-1, 1)
            #Grado7 para evaluar
            model = make_pipeline(PolynomialFeatures(4), LinearRegression())
            model.fit(days, count_cases)
            plt.figure()
            plt.scatter(days, count_cases)

            # MODELO
            plt.plot(sequence, model.predict(sequence), color="red")
            plt.title(titulo+" "+valorFiltrar+" - Covid-19 en todo el mundo")
            # plt.title("Prediccion de muertes departamento "+valorFiltrar+"\n por Covid19 Regresion Polinomial")
            plt.savefig('./helloworld/static/'+img+'.png')
            plt.cla()