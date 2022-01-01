from os import remove
import random
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


class Prediccion1:
    def __init__(self):
        pass

    
    def analizar(self,dias,infectados,filtrar,columnaFiltrar,valorFiltrar,min,max):
        
        dataTemp = pd.read_csv('archivo.csv')
        
        if(filtrar=="si"):
            
            #dataTemp = pd.read_csv('archivo.csv')
            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]
            
            dataTemp=data
            print(dataTemp)
            x = np.asarray(data[dias].array)[:,np.newaxis]
            y = np.asarray(data[infectados].array)[:,np.newaxis]
        
            
        x = np.asarray(dataTemp[dias].array)[:,np.newaxis]
        y = np.asarray(dataTemp[infectados].array)[:,np.newaxis]
        
        plt.scatter(x,y)
        
        # regression transform
        poly_degree = 3
        polynomial_features = PolynomialFeatures(degree = poly_degree)
        x_transform = polynomial_features.fit_transform(x)

        # AJUSTAR MODELO
        modeloo = LinearRegression().fit(x_transform, y)
        y_new = modeloo.predict(x_transform)

        # calculate rmse and r2
        rmse = np.sqrt(mean_squared_error(y, y_new))
        r2 = r2_score(y, y_new)

        # prediction
        x_new_min = int(min)*1.0
        x_new_max = int(max)*1.0

        x_new = np.linspace(x_new_min, x_new_max, 50)
        x_new = x_new[:,np.newaxis]

        x_new_transform = polynomial_features.fit_transform(x_new)
        y_new = modeloo.predict(x_new_transform)
    
        # plot the prediction
        plt.plot(x_new, y_new, color='coral', linewidth=3)
        plt.grid()
        # plt.xlim(x_new_min,x_new_max)
        # plt.ylim(0,10000)
        
        title = 'Degree = {}; RMSE = {}; R2 = {}'.format(poly_degree, round(rmse,2), round(r2,2))
        plt.title("Prediccion de infectado de COVID en "+valorFiltrar+"\n" + title, fontsize=10)
        plt.xlabel('x')
        plt.ylabel('y')
        try:
            remove("./helloworld/static/img.png")
            print("IMAGEN ANTERIOR ELIMINADA")
        except:
            print("imagenn anterior sin eliminar")
        #numero = random.randint(1, 6)
        #plt.savefig("./helloworld/static/"+str(numero)+".png")
        
        plt.savefig('./helloworld/static/img.png')
        plt.cla()
        
    def analizar9(self,dias,infectados,filtrar,columnaFiltrar,valorFiltrar,min,max):
        
        dataTemp = pd.read_csv('archivo.csv')
        
        if(filtrar=="si"):
            
            #dataTemp = pd.read_csv('archivo.csv')
            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]
            
            dataTemp=data
            print(dataTemp)
            x = np.asarray(data[dias].array)[:,np.newaxis]
            y = np.asarray(data[infectados].array)[:,np.newaxis]
            dataTemp[dias]= pd.to_datetime(dataTemp[dias])
            dataTemp[dias]=dataTemp[dias].map(dt.datetime.toordinal)
        
            
        x = np.asarray(dataTemp[dias].array)[:,np.newaxis]
        y = np.asarray(dataTemp[infectados].array)[:,np.newaxis]
        
        plt.scatter(x,y)
        
        # regression transform
        poly_degree = 3
        polynomial_features = PolynomialFeatures(degree = poly_degree)
        x_transform = polynomial_features.fit_transform(x)

        # AJUSTAR MODELO
        modeloo = LinearRegression().fit(x_transform, y)
        y_new = modeloo.predict(x_transform)

        # calculate rmse and r2
        rmse = np.sqrt(mean_squared_error(y, y_new))
        r2 = r2_score(y, y_new)

        # prediction
        x_new_min = int(min)*1.0
        x_new_max = int(max)*1.0

        x_new = np.linspace(x_new_min, x_new_max, 50)
        x_new = x_new[:,np.newaxis]

        x_new_transform = polynomial_features.fit_transform(x_new)
        y_new = modeloo.predict(x_new_transform)
    
        # plot the prediction
        plt.plot(x_new, y_new, color='coral', linewidth=3)
        plt.grid()
        
        title = 'Degree = {}; RMSE = {}; R2 = {}'.format(poly_degree, round(rmse,2), round(r2,2))
        plt.title("Tendencia de la vacunación de en un País."+valorFiltrar+"\n" + title, fontsize=10)
        plt.xlabel('x')
        plt.ylabel('y')
        
        try:
            remove("./helloworld/static/img.png")
            print("IMAGEN ANTERIOR ELIMINADA")
        except:
            print("imagenn anterior sin eliminar")

        plt.savefig('./helloworld/static/img.png')
        plt.cla()
        
