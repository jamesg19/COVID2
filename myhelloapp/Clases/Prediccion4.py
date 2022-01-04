from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
class Prediccion4:
    def __init__(self):
        pass
    #Predicción de mortalidad por COVID en un Departamento.
    def analizar(self,dias,infectados,filtrar,columnaFiltrar,valorFiltrar,min,max,region):
        
        dataTemp = pd.read_csv('archivo.csv')
        dataTemp=dataTemp.replace(np.nan, 0)
        if(filtrar=="si"):
            
            #dataTemp = pd.read_csv('archivo.csv')
            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]
            
            dataTemp=data
            

        # dataTemp[dias]= pd.to_datetime(dataTemp[dias])
        # dataTemp[dias]=dataTemp[dias].map(dt.datetime.toordinal)
        
        #X = np.asarray(dataTemp[dias].array)[:,np.newaxis]
        yTemp = np.asarray(dataTemp[infectados])
        Y=[]
        for i in yTemp:
            Y.append(i)
        print(Y)

        Y.insert(0, 0)
        y = np.array(Y)
        x = np.array(range(len(Y)))

        sec = np.linspace(x.min(), x.max()+int(max), len(Y)).reshape(-1, 1)
        value = 9
        graph = make_pipeline(PolynomialFeatures(value), LinearRegression())
        graph.fit(x[:, np.newaxis], y)
        self.pinta(x, y, sec, graph,valorFiltrar)

    def pinta(self,ax, ay, sec, graph,valorFiltrar):
        plt.figure()
        plt.scatter(ax, ay)
        plt.plot(sec, graph.predict(sec), color="red")
        plt.title("Prediccion de muertes departamento "+valorFiltrar+"\n por Covid19 Regresion Polinomial")
        plt.savefig('./helloworld/static/img.png')
        plt.cla()

    
    def analizar5(self,dias,infectados,filtrar,columnaFiltrar,valorFiltrar,min,max,region):
        dataTemp = pd.read_csv('archivo.csv')
        dataTemp=dataTemp.replace(np.nan, 0)
        if(filtrar=="si"):
            
            #dataTemp = pd.read_csv('archivo.csv')
            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]
            
            dataTemp=data
            #print(dataTemp)
        
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
        model = make_pipeline(PolynomialFeatures(7), LinearRegression())
        model.fit(days, count_cases)
        plt.figure()
        plt.scatter(days, count_cases)

        # MODELO
        plt.plot(sequence, model.predict(sequence), color="red")
        plt.title("Prediccion de muertes en un Pais "+valorFiltrar+" - Covid-19")
        # plt.title("Prediccion de muertes departamento "+valorFiltrar+"\n por Covid19 Regresion Polinomial")
        plt.savefig('./helloworld/static/img.png')
        plt.cla()
        
    def analizar6(self,dias,infectados,filtrar,columnaFiltrar,valorFiltrar,min,max,region):
        dataTemp = pd.read_csv('archivo.csv')
        dataTemp=dataTemp.replace(np.nan, 0)
        if(filtrar=="si"):
            
            #dataTemp = pd.read_csv('archivo.csv')
            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]
            
            dataTemp=data

        # dataTemp[dias]= pd.to_datetime(dataTemp[dias])
        # dataTemp[dias]=dataTemp[dias].map(dt.datetime.toordinal)
        
        xTemp = np.asarray(dataTemp[dias])
        cases=[]
        var=0
        for i in xTemp:
            var+=1
            cases.append(var) 
        
        X = np.asarray(cases)[:,np.newaxis]
        Y = np.asarray(dataTemp[infectados])[:,np.newaxis]
        
        #AJUSTAMOS EL MODELO
        linear_regressor = LinearRegression()
        linear_regressor.fit(X, Y)
        Y_pred = linear_regressor.predict(X)
        #Creamos la grafica
        title = "Analisis del Numero de muertes en un pais"+valorFiltrar+"\n"+'Modelo: Y = ' + str(linear_regressor.coef_[0][0]) + 'X+' + str(linear_regressor.intercept_[0])
        plt.title("Regresion lineal polinomial \n" + title, fontsize=9)
        plt.xlabel("Eje X "+dias)
        plt.ylabel("Eje Y "+infectados)
        plt.scatter(X, Y)
        plt.plot(X, Y_pred, color='red')
        plt.savefig('./helloworld/static/img.png')
        plt.cla()
        
    def analizar8(self,dias,infectados,filtrar,columnaFiltrar,valorFiltrar,min,max,region):
        
        dataTemp = pd.read_csv('archivo.csv')
        dataTemp=dataTemp.replace(np.nan, 0)
        if(filtrar=="si"):

            #dataTemp = pd.read_csv('archivo.csv')
            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]

            dataTemp=data
            print(dataTemp)

        yTemp = np.asarray(dataTemp[infectados])
        
        cases=[]
        for i in yTemp:
            cases.append(i)
        print(cases)
        
        X = np.array(range(len(cases)))
        sequencia = np.linspace(X.min(), X.max(), len(cases)).reshape(-1, 1)

        degree = 10

        polyreg=make_pipeline(PolynomialFeatures(degree), LinearRegression())
        polyreg.fit(X[:, np.newaxis], cases)
        #grafica
        plt.figure()
        #formando la grafica
        plt.xlabel("Eje X Dias del Año ")
        plt.ylabel("Eje Y Casos"+infectados)
        plt.scatter(X, cases) 
        #linea de prediccion
        plt.plot(sequencia, polyreg.predict(sequencia), color = "orange") 
        plt.title("Predicción de casos de un país "+valorFiltrar+" para un año.\n Regresion Lineal")
        plt.savefig('./helloworld/static/img.png')
        plt.cla()
        
        

        