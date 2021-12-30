from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


import numpy as np
import pandas as pd

class Prediccion1:
    def __init__(self):
        pass
    def Parametros(self):
        print("a")
        data = pd.read_csv('archivo.csv')
        # variable="<select class=\"custom-select\"  id=\"variable1\" name=\"variable1\">\n"
        # for i in data.columns.values:
        #     variable+="<option value=\""+i+"\">"+i+"</option>\n"
        # variable+="</select>\n"
        return data.columns.values
    
    def analizar(self):
        print("A")
        data = pd.read_csv('archivo.csv')
        x = np.asarray(data['ColumnaX'].array)[:,np.newaxis]
           
        y = np.asarray(data['ColumnaY'].array)[:,np.newaxis]
        #print(x)
        #print(data.columns.values)
        data
        #x = np.asarray([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])[:,np.newaxis]
        #y = np.asarray([0,1,2,3,6,6,8,9,13,17,19,20,21,24,25,32,34,36,39,46,47,50,61,70,74,80,87,126,139,153,156])[:,np.newaxis]
        plt.scatter(x,y)
        #print(x)
        
        # regression transform
        poly_degree = 3
        polynomial_features = PolynomialFeatures(degree = poly_degree)
        x_transform = polynomial_features.fit_transform(x)

        # fit the modeloo
        modeloo = LinearRegression().fit(x_transform, y)
        y_new = modeloo.predict(x_transform)

        # calculate rmse and r2
        rmse = np.sqrt(mean_squared_error(y, y_new))
        r2 = r2_score(y, y_new)
        #print('RMSE: ', rmse)
        #print('R2: ', r2)

        # prediction
        x_new_min = 0.0
        x_new_max = 50.0

        x_new = np.linspace(x_new_min, x_new_max, 50)
        x_new = x_new[:,np.newaxis]

        x_new_transform = polynomial_features.fit_transform(x_new)
        y_new = modeloo.predict(x_new_transform)
    
        # plot the prediction
        plt.plot(x_new, y_new, color='coral', linewidth=3)
        plt.grid()
        plt.xlim(x_new_min,x_new_max)
        plt.ylim(0,1000)
        title = 'Degree = {}; RMSE = {}; R2 = {}'.format(poly_degree, round(rmse,2), round(r2,2))
        plt.title("Prediction of Infection of Covid-19 in Guatemala\n " + title, fontsize=10)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig('./helloworld/static/img.png')
        print("GUARDA LA IMAGEN.*.*.**.**.***.* ")
        # #plt.show()