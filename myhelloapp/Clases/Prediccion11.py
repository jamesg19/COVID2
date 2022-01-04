from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pandass
import random

class Prediccion11:
    def __init__(self):
        self.infectados=""
        self.infectados2=""
        self.totalCasosH=""
        self.totalCasosM=""
        
        
    def analizar11(self,dias,infectados,mujeres,filtrar,columnaFiltrar,valorFiltrar,max):
        
        dataTemp = pandass.read_csv('archivo.csv')
        dataTemp=dataTemp.replace(np.nan, 0)
        if(filtrar=="si"):
            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]
            dataTemp=data 
        Fechas = np.asarray(dataTemp[dias].array)[:,np.newaxis]
        tiempo=[]
        iterador=-1
        for i in Fechas:
            iterador=iterador+1
            tiempo.append(iterador)
            
        X = np.asarray(tiempo)[:,np.newaxis]
        Y = np.asarray(dataTemp[infectados].array)[:,np.newaxis]
        XX = np.asarray(dataTemp[mujeres].array)[:,np.newaxis]
        
        #contador H
        H=0
        for i in Y:
            print(i[0])
            H+=i[0]
        #contador M
        M=0
        for i in XX:
            print(i[0])
            M+=i[0]
        
        self.totalCasosH=H
        self.totalCasosM=M
            
        
        
        plt.scatter(X,Y)  

        nb_degree = 4
        polynomial_features = PolynomialFeatures(degree = nb_degree) 
        X_TRANSF = polynomial_features.fit_transform(X)  

        model = LinearRegression() 
        model.fit(X_TRANSF, Y)  

        Y_NEW = model.predict(X_TRANSF)  
        rmse = np.sqrt(mean_squared_error(Y,Y_NEW)) 
        r2 = r2_score(Y,Y_NEW)  

        #prediccion
        X_NEW = np.linspace(0, int(max), 50) 
        X_NEW = X_NEW[:,np.newaxis]  

        X_NEW_TRANSF = polynomial_features.fit_transform(X_NEW)  
        Y_NEW = model.predict(X_NEW_TRANSF)  

        plt.plot(X_NEW, Y_NEW, color='red', linewidth=3)  

        plt.grid()  
        plt.xlim(0,int(max))  
        plt.ylim(0,2000)  

        title = 'Degree = {}; RMSE = {}; R2 = {}'.format(nb_degree, round(rmse,2), round(r2,2))
        plt.title('Guatemala \n ' + title, fontsize=10)
        plt.xlabel('Dias')  
        plt.ylabel('Infectados')  
        plt.savefig('./helloworld/static/img.png')
        self.infectados=str(round(r2,2)*100)
        self.infectados2= str(      round((self.totalCasosH/(self.totalCasosH+self.totalCasosM))*100,2)     )
        
        plt.cla()
