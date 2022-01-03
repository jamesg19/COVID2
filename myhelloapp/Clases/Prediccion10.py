from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Prediccion10:
    def __init__(self):
        self.poblacion=0
        pass

    def analizar10(self,dias,infectados1,filtrar,columnaFiltrar,valorFiltrar,max,img):
        
        dataTemp = pd.read_csv('archivo.csv')     
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
        Y = np.asarray(dataTemp[infectados1].array)[:,np.newaxis]
        self.poblacion=dataTemp[infectados1].max()
        
        #Z = np.asarray(dataTemp[infectados2].array)[:,np.newaxis]
        plt.scatter(X,Y)  


        nb_degree = 4
        polynomial_features = PolynomialFeatures(degree = nb_degree) 
        #print(X) 
        X_TRANSF = polynomial_features.fit_transform(X)  



        model = LinearRegression() 
        model.fit(X_TRANSF, Y)  

        
        Y_NEW = model.predict(X_TRANSF)  
        rmse = np.sqrt(mean_squared_error(Y,Y_NEW)) 
        r2 = r2_score(Y,Y_NEW)  


        x_new_min = 0.0 
        x_new_max = int(max)

        X_NEW = np.linspace(x_new_min, x_new_max, 50) 
        X_NEW = X_NEW[:,np.newaxis]  

        X_NEW_TRANSF = polynomial_features.fit_transform(X_NEW)  
        Y_NEW = model.predict(X_NEW_TRANSF)  

        plt.plot(X_NEW, Y_NEW, color='coral', linewidth=3)  

        plt.grid()  
        plt.xlim(x_new_min,x_new_max)  
        #plt.ylim(0,170000)  

        title = 'Degree = {}; RMSE = {}; R2 = {}'.format(nb_degree, round(rmse,2), round(r2,2))
        plt.title(infectados1+"\n" + title, fontsize=10)
        plt.xlabel('Dias')  
        plt.ylabel('Infectados')  
        plt.savefig('./helloworld/static/'+img+'.png')
        plt.cla()
        