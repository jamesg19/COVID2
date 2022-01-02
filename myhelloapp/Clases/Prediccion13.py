import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pandas as pandass
from sklearn import preprocessing

class Prediccion13:
    def __init__(self):
        self.promedios=[]
        self.regiones=[]
    
    def analizar13(self,Muertes,Positivos,Edades,min,pais):   
        dataTemp = pandass.read_csv('archivo.csv')

        x = dataTemp[Muertes]
        y = dataTemp[Positivos]
        z=dataTemp[Edades]
        data=[]
        var=-1;
        for i in x:
            var=var+1
            data.append([x[var], y[var],z[var] ])
            
        X=np.array(data)
        plt.scatter(X[:,0],X[:,1], label='True Position')
        kmeans = KMeans(n_clusters = int(min))
        kmeans.fit(X)
        
        #print(kmeans.cluster_centers_)
        for i in kmeans.cluster_centers_:

            a4=[[i[0]],[i[1]],[i[2]]]

            self.promedios.append(a4)

        plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap ='rainbow')
        #para imprimir centroides
        plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color='black')
        plt.savefig('./helloworld/static/img.png')
        plt.cla()
        
        
    #Muertes según regiones de un país - Covid 19.    
    def analizar14(self,Regiones,Muertes,min,pais):
        
        dataTemp = pandass.read_csv('archivo.csv')
        x = dataTemp[Regiones]
        y = dataTemp[Muertes]
        
        label = preprocessing.LabelEncoder()
        tempRegiones=dataTemp[Regiones].unique().tolist()
        
        # Convertir strings en numeros
        regX = label.fit_transform(x)
        
        ite=-1
        for i in tempRegiones:
            ite=ite+1

            a=[[i],[ite]]
            self.regiones.append(a)
        #print(self.regiones)
        
        data=[]
        var=-1;
        for i in x:
            var=var+1
            data.append([regX[var], y[var]])
        
        xx=np.array(data)
        #print(xx)
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(xx)
        try:
            plt.scatter(xx[:,0], xx[:,1], c=kmeans.labels_, cmap='rainbow')
            plt.title("Muertes según regiones de un país - Covid 19."+pais)
            plt.xlabel('Regiones')
            plt.ylabel('Total fallecidos')
            #print("ENTRA EN ERROR")
            plt.savefig('./helloworld/static/img.png')
            #print("ENTRA GUARDA")
            plt.cla()
        except:
            print("ENTRA EN ERROR except")
            plt.cla()
