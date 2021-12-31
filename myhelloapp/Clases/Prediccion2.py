from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
class Prediccion2:
    def __init__(self):
        pass
    #PREDICCION DE INFECTADOS DE UN PAIS
    def analizar(self,dias,infectados,filtrar,columnaFiltrar,valorFiltrar,min,max):
        
        if(filtrar=="si"):
            dataTemp = pd.read_csv('archivo.csv')
            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]
            
            X = np.asarray(data[dias].array)[:,np.newaxis]
            Y = np.asarray(data[infectados].array)[:,np.newaxis]
        else:
            data = pd.read_csv('archivo.csv')
            X = np.asarray(data[dias].array)[:,np.newaxis]
            Y = np.asarray(data[infectados].array)[:,np.newaxis]


        plt.scatter(X,Y)  

        nb_degree = 4
        polynomial_features = PolynomialFeatures(degree = nb_degree) 

        X_TRANSF = polynomial_features.fit_transform(X)  

        model = LinearRegression() 
        model.fit(X_TRANSF, Y)  


        Y_NEW = model.predict(X_TRANSF)  
        rmse = np.sqrt(mean_squared_error(Y,Y_NEW)) 
        r2 = r2_score(Y,Y_NEW)  

        x_new_min = min 
        x_new_max = max

        X_NEW = np.linspace(x_new_min, x_new_max, 50) 
        X_NEW = X_NEW[:,np.newaxis]  

        X_NEW_TRANSF = polynomial_features.fit_transform(X_NEW)  
        Y_NEW = model.predict(X_NEW_TRANSF)  

        plt.plot(X_NEW, Y_NEW, color='coral', linewidth=3)  

        plt.grid()  
        plt.xlim(x_new_min,x_new_max)  
        plt.ylim(0,170000)  

        title = 'Grados = {}; RMSE = {}; R2 = {}'.format(nb_degree, round(rmse,2), round(r2,2))
        plt.title("Pais:  "+valorFiltrar+" " + title, fontsize=10)
        plt.xlabel('Dias')  
        plt.ylabel('Infectados')
        plt.savefig('./helloworld/static/img.png')
        plt.cla()
        