import pandas as pandass
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.metrics import  mean_squared_error, r2_score

#Predicción de muertes en el último día del primer año de infecciones en un país.  
class Prediccion19:
    def __init__(self):
        pass
    
    #Predicción de muertes en el último día del primer año de infecciones en un país. 
    def analizar19(self,dias,fallecidos,filtrar,columnaFiltrar,valorFiltrar,max):
        
        dataTemp = pandass.read_csv('archivo.csv')
        
        if(filtrar=="si"):

            newData = dataTemp[columnaFiltrar] == valorFiltrar
            data = dataTemp[newData]

            dataTemp=data
           

        xTemp = dataTemp[dias].array
        yTemp = dataTemp[fallecidos].array

        X = np.asarray(xTemp)[:,np.newaxis]
        Y = np.asarray(yTemp)[:,np.newaxis]


        plt.scatter(X,Y)

        grado = 4

        polynomial_features = PolynomialFeatures(degree = grado)

        X_TRANF = polynomial_features.fit_transform(X)

        #define and train a model

        model = LinearRegression()
        model.fit(X_TRANF, Y)

    
        Y_NEW = model.predict(X_TRANF)

        rmse = np.sqrt(mean_squared_error(Y,Y_NEW))
        r2 = r2_score(Y,Y_NEW)

        #Realizamos la prediccion

        x_new_min = 0.0
        x_new_max = int(max)

        X_NEW = np.linspace(x_new_min,x_new_max,int(max))
        X_NEW = X_NEW[:,np.newaxis]

        X_NEW_TRANSF = polynomial_features.fit_transform(X_NEW)

        Y_NEW = model.predict(X_NEW_TRANSF)

        plt.plot(X_NEW,Y_NEW,color='red',linewidth=3)

        plt.grid()
        plt.xlim(x_new_min,x_new_max+100)
        plt.ylim(0,300)

        title = 'Degree = {}; RMSE = {}; R2 = {}'.format(grado,round(rmse,2),round(r2,2))

        plt.title("Regresion Lineal Polinomial\n"+title,fontsize=12)

        plt.ylabel('Numero de muertes')
        plt.xlabel('Dias')
        plt.savefig('./helloworld/static/img.png')
        plt.cla()

