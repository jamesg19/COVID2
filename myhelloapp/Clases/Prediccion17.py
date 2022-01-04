from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pandass
import random

class Prediccion17:
    def __init__(self):
        self.infectados=0
        self.infectados2=0
        self.infectados=0
        self.muertesT=0
        self.tasa=0
        
        
    def analizar17(self,infectados,muertes,filtrar,columnaFiltrar,valorFiltrar,max):
        
        dataTemp = pandass.read_csv('archivo.csv')
        
        if(filtrar=="si"):
            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]
            dataTemp=data
             
        # Fechas = np.asarray(dataTemp[dias].array)[:,np.newaxis]
        # tiempo=[]
        # iterador=-1
        
        # for i in Fechas:
        #     iterador=iterador+1
        #     tiempo.append(iterador)
            
        X = np.asarray(dataTemp[muertes].array)[:,np.newaxis]
        Y = np.asarray(dataTemp[infectados].array)[:,np.newaxis]
        XX = np.asarray(dataTemp[muertes].array)[:,np.newaxis]
        MayorX=dataTemp[muertes].max()

        #contador H
        H=0
        for i in Y:
            #print(i[0])
            H+=i[0]
        #contador M
        M=0
        for i in XX:
            #print(i[0])
            M+=i[0]
        
        self.infectados=H
        self.muertesT=M
            
        
        
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
        X_NEW = np.linspace(0, MayorX, MayorX) 
        X_NEW = X_NEW[:,np.newaxis]  

        X_NEW_TRANSF = polynomial_features.fit_transform(X_NEW)  
        Y_NEW = model.predict(X_NEW_TRANSF)  

        plt.plot(X_NEW, Y_NEW, color='red', linewidth=3)  

        plt.grid()  


        title = 'Degree = {}; RMSE = {}; R2 = {}'.format(nb_degree, round(rmse,2), round(r2,2))
        plt.title('Casos Activos / Muertes por Covid\n ' + title, fontsize=10)
        plt.xlabel('Muertes')  
        plt.ylabel('Infectados')  
        plt.savefig('./helloworld/static/img.png')
        #self.infectados=str(round(r2,2)*100)
        # self.infectados2= str(      round((self.infectados/(self.infectados+self.muertesT))*100,2)     )
        
        print("INFECTADOS")
        print(self.infectados)
        print("MUERTES")
        print(self.muertesT)
        self.tasa=(int(self.muertesT)/self.infectados)*100
        plt.cla()
