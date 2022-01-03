from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures



#Tendencia de casos confirmados de Coronavirus en un departamento de un País.
class Prediccion15:
    def __init__(self):
        pass

    def analizar15(self,listaDepartamentos,pais):   
        print(listaDepartamentos+" AQUI LLEGA ASI")
        listaColumnas=listaDepartamentos.split(sep=',')
        data = pd.read_csv('archivo.csv')
        LCasos=""
        contador=-1
        for ite in listaColumnas:
            contador=contador+1
            if(contador==0):
                a=np.asarray(data[ite].array)
                print(a)
                LCasos=a
        contador2=-1        
        for ite in listaColumnas:
            contador2=contador2+1
            if(contador2!=0):
                a=np.asarray(data[ite].array)
                LCasos+=a            
            
        
        # dataTemp = pd.read_csv('archivo.csv')
        
        Accumulate = np.cumsum(LCasos)
        #print(Accumulate)

        #DayList = days from March 13 to November 8
        DayList = np.array(range(len(Accumulate)))
        seq = np.linspace(DayList.min(), DayList.max()+20, len(Accumulate)).reshape(-1, 1)

        #model creation
        degree=9
        polyreg=make_pipeline(PolynomialFeatures(degree), LinearRegression())
        polyreg.fit(DayList[:, np.newaxis], Accumulate)

        plt.figure()
        plt.scatter(DayList, Accumulate)
        plt.plot(seq, polyreg.predict(seq), color="red")
        plt.title("Trend of confirmed Coronavirus cases \n in the department of Guatemala)")
        plt.savefig('./helloworld/static/img.png')
        plt.cla()