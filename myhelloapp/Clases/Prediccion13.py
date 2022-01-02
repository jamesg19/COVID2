import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pandas as pandass

class Prediccion13:
    def __init__(self):
        self.promedios=[]
    
    def analizar13(self,Muertes,Positivos,Edades,min,pais):   
        dataTemp = pandass.read_csv('archivo.csv')

        x = dataTemp[Muertes]
        y = dataTemp[Positivos]
        z=dataTemp[Edades]
        data=[]
        data2=[]
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
            #a4+=[[i[0]],[i[1]],[i[2]]]
            print("DATA2")
            print(a4)
            self.promedios.append(a4)
            ##print(i)
        print("PROMEDIOS")
        print(self.promedios)
        plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap ='rainbow')
        #para imprimir centroides
        plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color='black')
        plt.savefig('./helloworld/static/img.png')
        plt.cla()