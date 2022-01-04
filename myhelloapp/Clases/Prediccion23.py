from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Prediccion23:
    
    def __init__(self):
        pass
    
    def analizar23(self,sexo,edad, muertes,ListaColumnas):
        data = pd.read_csv('archivo.csv')
        data=data.replace(np.nan, 0)
        listaFactores=[sexo]
        listaFactores.append(edad)

        listaFactores2=ListaColumnas.split(sep=',')

        for i in listaFactores2:
            listaFactores.append(i)
        

         #['tip', 'sex', 'day']
        X=data.loc[:,listaFactores].values
        yTemp=[muertes]
        Y=data.loc[:,yTemp].values
        

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)


        

        model = GaussianNB()
        model.fit(X_train, Y_train)
        Y_predict = model.predict(X_test)

        #print('Original\t', Y_test)
        #print('Prediction\t', Y_predict)

        cm = confusion_matrix(Y_test, Y_predict)
        #print('Confusion Matrix:')
        #print(cm)
        #print('Accuracy Rate:', (cm[0, 0] + cm[1, 1]) / 1250 * 100)
        #print('Error Rate:', (cm[0, 1] + cm[1, 0]) / 1250 * 100)


        plot_confusion_matrix(model, X_test, Y_test, display_labels=["death", "alive"])
        plt.savefig('./helloworld/static/img.png')
        plt.cla()