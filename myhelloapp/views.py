from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from werkzeug.utils import secure_filename
import pathlib
from io import StringIO
from myhelloapp.Clases.Prediccion16 import Prediccion16
from myhelloapp.Clases.Prediccion17 import Prediccion17
from myhelloapp.Clases.Prediccion21 import Prediccion21
import numpy as np
import pandas as pd
import os
import csv
#import base64 as base64Imagen
from os import remove
from myhelloapp.Clases.Codigo64 import Codigo64
from myhelloapp.Clases.GestorReporte import GestorReporte
from myhelloapp.Clases.LeerColumnas import LeerColumnas
from myhelloapp.Clases.Prediccion1 import Prediccion1
from myhelloapp.Clases.Prediccion10 import Prediccion10
from myhelloapp.Clases.Prediccion11 import Prediccion11
from myhelloapp.Clases.Prediccion12 import Prediccion12
from myhelloapp.Clases.Prediccion13 import Prediccion13
from myhelloapp.Clases.Prediccion15 import Prediccion15
from myhelloapp.Clases.Prediccion19 import Prediccion19
from myhelloapp.Clases.Prediccion2 import Prediccion2
from myhelloapp.Clases.Prediccion22 import Prediccion22
from myhelloapp.Clases.Prediccion23 import Prediccion23
from myhelloapp.Clases.Prediccion24 import Prediccion24
from myhelloapp.Clases.Prediccion25 import Prediccion25
from myhelloapp.Clases.Prediccion4 import Prediccion4
# Create your views here.

#james= Django(__name__)
def home(request):
    
    return render(request,'principal.html')


def procesarArchivo(request):

    extension = request.POST['extension']
    filee = request.POST['area']
    tipoReporte=request.POST['tipoReporte']
    
    
    try:
        remove("archivo.csv")
        remove("archivoT.csv")
        remove("./Conversiones/archivoT.xlsx")
        remove("./Conversiones/archivoT.json")
    except:
        pass
    try:
        remove("./helloworld/static/img.png")
        print("IMAGEEEEEEEN CORRECTAMENTEE")
    except:
        pass

    #si es .csv
    if(extension=="csv"):
        
        try:
            #guarda ek archivo
            archivo=open('archivoT.csv','w')
            archivo.write(filee)
            archivo.close()
            with open('archivoT.csv','r',encoding = 'utf-8') as fr,open('archivo.csv','w',encoding = 'utf-8') as fd:
                for text in fr.readlines():
                        if text.split():
                                fd.write(text.replace(';', ','))
                fd.close
            print('La salida es exitosa ...')
        except:
            print("Se produjo un error al guardar el archivo")
            return render(request,'principal.html')
        # #reconocer columnas
        columnas= LeerColumnas()
        gestor=GestorReporte()
        
        titulo=gestor.obtenerTitulo(tipoReporte)
        context={
            "titulo":titulo,
            "variable1":columnas.Parametros()
        }
        
        FrameParametro=GestorReporte()
        ventana=FrameParametro.obtenerParametroHtml(tipoReporte)
        
        return render(request,ventana+'.html',context)
    #si es .xlsx
    elif(extension=="xlsx"):
        
        #guarda el EXCEL
        archivo=open('./Conversiones/archivoT.json','w')
        archivo.write(filee)
        archivo.close()
        #leemos el archivo
        read_file=pd.read_json(r'./Conversiones/archivoT.json')
        #convertimos a CSV
        read_file.to_csv(r'archivo.csv',index="None",header=True)
        
        # #reconocer columnas
        columnas= LeerColumnas()
        gestor=GestorReporte()
        
        titulo=gestor.obtenerTitulo(tipoReporte)
        context={
            "titulo":titulo,
            "variable1":columnas.Parametros()
        }
        
        FrameParametro=GestorReporte()
        ventana=FrameParametro.obtenerParametroHtml(tipoReporte)
        
        return render(request,ventana+'.html',context)
    
    #si es json
    elif(str(extension).lower() =="json"):

        #guarda el JSON
        archivo=open('./Conversiones/archivoT.json','w')
        archivo.write(filee)
        archivo.close()
        #leemos el archivo
        read_file=pd.read_json(r'./Conversiones/archivoT.json')
        #convertimos a CSV
        read_file.to_csv(r'archivo.csv')
        
        # #reconocer columnas
        columnas= LeerColumnas()
        gestor=GestorReporte()
        
        titulo=gestor.obtenerTitulo(tipoReporte)
        context={
            "titulo":titulo,
            "variable1":columnas.Parametros()
        }
        
        FrameParametro=GestorReporte()
        ventana=FrameParametro.obtenerParametroHtml(tipoReporte)
        
        return render(request,ventana+'.html',context)
    

# Tendencia de la infección por Covid-19 en un País. 
def Reporte1(request):
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            min = request.POST['min']
            max = request.POST['max']
            
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            reporte1=Prediccion1();
            reporte1.analizar(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max)
            
            titulo="Tendencia de infeccion en un pais \n"
            desc="\nLa tendencia de las infecciones en un país se lleva \na cabo a través de un máximo de: "+max+"(unidades de tiempo)\nlo cual en base a los datos obtenidos se hace \nuna estimación de la tendencia para los proximos \n"+max+" (unidades tiempo)."
            desc+="\nAdemas se utiliza la columna "+variable1+" en el eje X \ny  la columna "+variable2+" en el eje Y "
            
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
            }
            
            return render(request,'reporte.html',context)
        else:

            return render(request,'principal.html') 
    # except:
    #     return render(request,'principal.html')



# PREDICCION DE INFECTADOS DE UN PAIS
def Reporte2(request):
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            min = request.POST['min']
            max = request.POST['max']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            
            reporte2=Prediccion2();
            reporte2.analizar(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max,"Pais")
            
            titulo="PREDICCION DE INFECTADOS DE UN PAIS"
            desc="\nLa prediccion de infectados en un país se lleva \n"
            desc+="a cabo a través de un máximo de: "+max+"(unidades tiempo)\n"
            desc+="lo cual en base a los datos obtenidos se hace una \n"
            desc+="estimación de la tendencia para los proximos "+max+"\n"
            desc+="(unidades tiempo).\n"
            desc+="Ademas se utiliza la columna "+variable1+" en el eje X \ny  la columna "+variable2+" en el eje Y .\n"
            desc+="\nLa linea amarilla representa prediccion y \nla linea azul(es) los casos reales."
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
            }

            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')

def Reporte3(request):
    #try:
        if request.method == "POST":
            np1 = request.POST['npHoy']
            np2 = request.POST['npAyer']
            ts1 = request.POST['tsHoy']
            ts2 = request.POST['tsAyer']

            
            reporte3=Prediccion1();
            
            
            titulo="Indice de Progresión de la pandemia. \n"
            # igual a 0 significa que las epidemias se detienen, es decir, todas las personas que se hicieron un hisopo son negativas para el coronavirus.
            desc="\nDonde np (i) representa el número total de casos positivos\n"
            desc+="de coronavirus el día i (por ejemplo, hoy), np (i-1)\n"
            desc+="el número total de casos positivos de coronavirus el\n"
            desc+="día i-1 (por ejemplo, ayer), ts (i) el número total de\n"
            desc+="hisopos hechos el día i-1. EPI es un número entre 0 y 1.\n"
            desc+="Cuando EPI es igual a 1, significa que todas las personas\n"
            desc+="que han tenido un hisopo son positivas para el coronavirus.\n"
            desc+="Por el contrario, un valor EPI igual a 0 significa que\n"
            desc+="las epidemias se detienen es decir no hay infectados.\n"
            desc+="RESULTADO: EPI="+str(reporte3.analizar3(np1,np2,ts1,ts2))+". \n"
            
            context={
                "titulo":titulo,
                "desc":desc,
            }
            
            return render(request,'reporte3.html',context)
        else:

            return render(request,'principal.html') 
    # except:
    #     return render(request,'principal.html')



#Predicción de mortalidad por COVID en un Departamento.
def Reporte4(request):
    try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            min = request.POST['min']
            max = request.POST['max']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            
            reporte4=Prediccion4();
            reporte4.analizar(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max,"Departamento")
            
            titulo="\nPredicción de mortalidad por COVID en un Departamento\n"
            desc="\n\nSe pueden predecir como maximo 30 dias posteriores al\n"
            desc+="ultimo dato,y hacer una prediccion muy lejana puede dar\n" 
            desc+="una prediccion con decremento por lo tanto la prediccion\n"
            desc+="de esta grafica tiene como maximo predecir  "+max+" dias.\n"
            desc+="La linea naranja representa la prediccion.\n"
            desc+="La linea azul representa el numero de muertes reales.\n"
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    except:
        return render(request,'principal.html')

def Reporte5(request):
    try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            min = request.POST['min']
            max = request.POST['max']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            
            reporte4=Prediccion4();
            reporte4.analizar5(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max,"Pais")
            
            titulo="Predicción de mortalidad por COVID en un País\n"
            # de muertes confirmadas y la linea roja representa la prediccion de muertes en dicho pais.

            desc="\nSe realiza la prediccion de mortalidad de un pais\n"
            desc+="al dia "+max+" donde la linea azul representa los casos\n"
            desc+="reales de muertes confirmadas y la linea roja representa\n"
            desc+="la prediccion de muertes en dicho pais.\n"
            desc+="El eje X representa el tiempo(Unidades de tiempo)\n"
            desc+="de la columna "+variable1+".\n"
            desc+="El eje Y representa el numero de decesos de personas\n"
            desc+="de la columna "+variable2+".\n"
                        
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    except:
        return render(request,'principal.html')
    
    
def Reporte6(request):
    #pass
    try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']

            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            
            reporte4=Prediccion4();
            reporte4.analizar6(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,0,0,"Pais")
            
            titulo="Análisis del número de muertes por coronavirus en un País.\n"
            desc="\nAnálisis del número de muertes por coronavirus en un pais\n"
            desc+="mediante una regresión lineal, se dice que cuando las\n"
            desc+="muertes reportadas estan muy cerca al comportamiento\n"
            desc+="de la prediccion es porque hay una buena toma de datos,\n"
            desc+="pero si estan dispersas indica que hay factores\n"
            desc+="externos que aumentan los datos.\n"
            desc+="El Eje X: "+variable1+" representa el tiempo,\n"
            desc+="El Eje Y:"+variable2+" representa el numero de muertes.\n"
            #muertes reportadas están lejos de lo que debería ser el comportamiento real de dicho evento. Donde los puntos azules representan las muertes reales, y la linea roja representa la prediccion de muertes.
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'reporte.html')
            
    except:
        return render(request,'principal.html')



def Reporte7(request):
    #pass
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            min = request.POST['min']
            max = request.POST['max']

            print(min)
            print(max)
            
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            reporte1=Prediccion1();
            reporte1.analizar7(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max)
            
            titulo="Tendencia del número de infectados por día de un País..\n"
            desc="\n\nSe hace el calculo de la tendencia con regresion\n"
            desc+="lineal grado 3 y una estimacion hasta "+max+" (dias/meses)"
            desc+="lo cual refleja la proyeccion de los dias posteriores\n"
            desc+="el eje X representa el tiempo y el eje Y los\n"
            desc+="infectados."

            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')


def Reporte8(request):
    #pass
    #try:
        if request.method == "POST":
            #variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']

            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            reporte4=Prediccion4();
            reporte4.analizar8("",variable2,filtrar,columnaFiltrar,valorFiltrar,0,0,"Pais")
            
            titulo="Predicción de casos de un país para un año."
            desc="\n\nLa grafica muestra la prediccion con una linea\n"
            desc+="amarilla lo cual hace una proyeccion y la\n"
            desc+="linea azul representa los datos reales\n"
            desc+="Se utiliza regresion lineal de grado 4 para\n"
            desc+="hacer una estimacion ajustada a los datos reales\n"
            desc+="para tener mejores resultados, ej eje X(Tiempo)\n"
            desc+="y el eje Y representa los casos en "+variable2
            
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
            }
            
            return render(request,'reporte.html',context)
        else:
           return render(request,'principal.html') 
            
    # except:
    #     return render(request,'principal.html')

#Tendencia de la vacunación de en un País. 

def Reporte9(request):
    #pass
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            min = request.POST['min']
            max = request.POST['max']

            print(min)
            print(max)
            
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            reporte1=Prediccion1();
            reporte1.analizar9(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max)
            
            titulo="Tendencia de la vacunación de en un País."
            desc="\nSe obtiene la tendencia de vacunacion de un\n"
            desc+="pais: , y se utiliza regresion lineal grado3\n"
            desc+="ya que la tendencia no puede disminuir, esta\n"
            desc+="tendencia solo puede mantenerse o aumentar,\n"
            desc+="por lo tanto utiliza grado 3."
            desc+="El eje X representa el tiempo de la columna:\n"
            desc+= variable1+" y el eje Y utiliza los datos de la\n "
            desc+=" columna: "+variable2
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')




def Reporte10(request):
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            variable3 = request.POST['variable3']
            poblacion1Total = request.POST['poblacion1']
            poblacion2Total = request.POST['poblacion2']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            min = request.POST['min']
            max = request.POST['max']

            print(min)
            print(max)
            
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            reporte10=Prediccion10();
            reporte10.analizar10(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,max,"img")
            infectados1=reporte10.poblacion
            
            reporte10B=Prediccion10();
            reporte10B.analizar10(variable1,variable3,filtrar,columnaFiltrar,valorFiltrar,max,"img1")
            infectados2=reporte10B.poblacion
            
            p1=str(round(( int(infectados1)/int(poblacion1Total)),5))
            p2=str(round((int(infectados2)/int(poblacion2Total) ),5))
            ul=""
            if(p1>p2):
                ul+="y se determina que el pais "+variable2+" esta\n"
                ul+="vacunando mas que "+variable3+"\n"
            elif(p2>p1):
                ul+="y se determina que el pais "+variable3+" esta\n"
                ul+="vacunando mas que "+variable2+"\n"
            titulo="Ánalisis Comparativo de Vacunación entre 2 paises. "
            desc="\nSe realiza un analisis de vacunancion entre dos paises\n"
            desc+="y para el pais: \""+variable2+"\" se tiene una poblacion \n"
            desc+="de:"+str(poblacion1Total)+" y la cantidad de vacunados: "+str(infectados1)+"\n"
            desc+="con un porcentaje de vacunacion "+p1+"% \n "
            desc+="Para el pais: \""+variable3+"\" se tiene una poblacion \n"
            desc+="de:"+str(poblacion2Total)+" y la cantidad de vacunados: "+str(infectados2)+"\n"
            desc+="con un porcentaje de vacunacion "+p2+"% \n "
            desc+=ul


            newcode=Codigo64()
            newcode2=Codigo64()
            context={
                "titulo":titulo,
                "desc":desc,
                "codigo":newcode.obtenerCodigo(),
                "codigo2":newcode2.obtenerCodigo2(),
            }
            
            return render(request,'reporte12.html',context)
        else:
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')
    






def Reporte11(request):
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            variable3 = request.POST['variable3']
            min = request.POST['min']
            max = request.POST['max']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            
            
            
            reporte11=Prediccion11();
            reporte11.analizar11(variable1,variable2,variable3,filtrar,columnaFiltrar,valorFiltrar,max)
            var=reporte11.infectados2
            titulo="Porcentaje de hombres infectados por covid-19 en un \nPaís desde el primer caso activo"
            desc="\n\n\nSe estima que el "+var+"% de \n"
            desc+="infectados son hombres y le utiliza la herramienta\n"
            desc+="scikit-learn con Regresion Polinomial Grado:4\n"
            desc+="Los puntos azules representan los casos reales\n"
            desc+=" y la linea roja representa una prediccion de \n"
            desc+="de hombres infectados."
           
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
            }

            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')
    
    
    
    
def Reporte12(request):
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            variable3 = request.POST['variable3']
            poblacion1Total = request.POST['poblacion1']
            poblacion2Total = request.POST['poblacion2']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            min = request.POST['min']
            max = request.POST['max']

            print(min)
            print(max)
            
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            reporte12=Prediccion12();
            reporte12.analizar12(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,max,"img")
            infectados1=reporte12.poblacion
            reporte12B=Prediccion12();
            reporte12B.analizar12(variable1,variable3,filtrar,columnaFiltrar,valorFiltrar,max,"img1")
            infectados2=reporte12B.poblacion
            p1=str(round(( int(infectados1)/int(poblacion1Total)),5))
            p2=str(round((int(infectados2)/int(poblacion2Total) ),5))
            ul=""
            if(p1>p2):
                ul+="y se determina que el pais "+variable2+" esta\n"
                ul+="siendo mas afectado que "+variable3+"\n"
            elif(p2>p1):
                ul+="y se determina que el pais "+variable3+" esta\n"
                ul+="siendo mas afectado que "+variable2+"\n"
            titulo="Ánalisis Comparativo entres 2 paises o continentes"
            desc="\nSe realiza un analisis entre los dos paises o continentes\n"
            desc+="y para el pais: \""+variable2+"\" se tiene una poblacion \n"
            desc+="de:"+str(poblacion1Total)+" y la cantidad de infectados: "+str(infectados1)+"\n"
            desc+="con un porcentaje de infeccion "+p1+"% \n "
            desc+="Para el pais: \""+variable3+"\" se tiene una poblacion \n"
            desc+="de:"+str(poblacion2Total)+" y la cantidad de infectados: "+str(infectados2)+"\n"
            desc+="con un porcentaje de infeccion "+p2+"% \n "
            desc+=ul


            newcode=Codigo64()
            newcode2=Codigo64()
            context={
                "titulo":titulo,
                "desc":desc,
                "codigo":newcode.obtenerCodigo(),
                "codigo2":newcode2.obtenerCodigo2(),
            }
            
            return render(request,'reporte12.html',context)
        else:
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')
    
    
    
    

#Muertes promedio por casos confirmados y edad de covid 19 en un País.
def Reporte13(request):
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            variable3 = request.POST['variable3']
            min=request.POST['min']
            pais=request.POST['pais']
            
            

            reporte13=Prediccion13();
            reporte13.analizar13(variable1,variable2,variable3,min,pais)

            #Como se puede apreciar en la imagen, la predicción toma una forma lineal (puntos azules) y los datos reales (puntos rojos), en realidad tienen muy poca correlación con la predicción.
            #sea positiva o negativa. El número total de casos fallecidos.
            titulo="Muertes promedio por casos confirmados y edad de covid 19\n en un País en "+pais+"\n"
            desc="\n\nSe calculan los centroides y estan a "+min+" unidades\n"
            desc+="representados por los puntos negros,\n"
            desc+="en la siguiente tabla se pueden ver los \n"
            desc+="promedios(Mortalidad e infectados) en relacion a la edad\n"
            desc+="El eje X representa la cantidad de muertes \n"
            #desc+="El eje Y representa la cantidad de infectados \n"min
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
                "variable1":reporte13.promedios ,
            }
            
            return render(request,'reporte13.html',context)
        else:
            
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')
    
#Reporte14 Muertes según regiones de un país - Covid 19. 
def Reporte14(request):
    #try
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            min=request.POST['min']
            pais=request.POST['pais']
            
            reporte14=Prediccion13();
            reporte14.analizar14(variable1,variable2,min,pais)


            titulo="Muertes según regiones de un país - Covid 19. \nen "+pais+"\n"
            desc="\n\nHace de un calculo de las muertes por region\n"
            desc+="del pais: "+pais+" analiza los datos ingresados\n"
            desc+="y hace una estimacion en base a cada region\n"
            desc+="utiliando regresion en sklearn.\n"
            desc+="El eje X depresenta las regiones y cada\n"
            desc+="region cuenta con un identificador (Ver tabla)\n"
            desc+="El eje Y representa el total de fallecidos\n"


            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
                "variable1":reporte14.regiones,
                
            }
            
            return render(request,'reporte14.html',context)
        else:
            
            return render(request,'principal.html')
    # except:
    #     return render(request,'principal.html')
    
    
def Reporte15(request):
    #try
        if request.method == "POST":
            variable1 = request.POST['variable1']
            pais=request.POST['pais']
            
        
            reporte15=Prediccion15();
            reporte15.analizar15(variable1[:-1],pais)


            titulo="Tendencia de casos confirmados de Coronavirus en \nun departamento del pais "+pais+"\n"
            desc="\n\n\nEl proceso de predicción se realizó mediante regresión lineal.\n"
            desc+="y la grafica representa la tendencia de los departamentos.\n"
            desc+="La linea roja representa la tendencia de los casos confirmados\n"
            desc+="y los puntos azules representan los casos reales.\n"
            desc+="Se ha utilizado regresion lineal grado: 9\n"
            


            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
                #"variable1":reporte14.regiones,
                
            }
            
            return render(request,'reporte.html',context)
        else:
            
            return render(request,'principal.html')
    # except:
    #     return render(request,'principal.html') 
    
#Porcentaje de muertes frente al total de casos en un país, región o continente.   
def Reporte16(request):
    #try
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            pais=request.POST['pais']
            
            
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            min = request.POST['min']
            max = request.POST['max']

            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            
            reporte16=Prediccion16();
            percentage=reporte16.analizar16(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar)


            titulo="Porcentaje de muertes frente al total de casos en un país\n, región o continente. Pais:"+pais+"\n"
            desc="\n\n\nSe ha estimado el porcentaje de muertes con\n"
            desc+="los datos ingresados de la columna "+variable1+" para\n"
            desc+="casos confimados y de la columna "+variable2+" para\n"
            desc+="las muertes registradas."
            desc+="Se obtuvieron un total de: "+str(reporte16.muertes)+" muertes por COVID\n"
            desc+="un total de :"+str(reporte16.casos)+" casos confirmados de COVID\n"
            desc+="y como resultado obtuvimos un "+percentage+"% de mortalidad.\n"
            
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "desc":desc,
                #"variable1":reporte14.regiones,
                
            }
            
            return render(request,'reporte16.html',context)
        else:
            
            return render(request,'principal.html')
    # except:
    #     return render(request,'principal.html')
    
    
def Reporte17(request):
    #try
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            pais=request.POST['pais']
            
            
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            min = request.POST['min']
            max = request.POST['max']

            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            
            reporte17=Prediccion17();
            reporte17.analizar17(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,300)


            titulo="Tasa de comportamiento de casos activos en relación al \nnúmero de muertes en un continente. \n"
            desc="\n\n\nSe determina que la tasa de comportamiento\n"
            desc+="en relacion de casos activos y numero de muertes\n"
            desc+="es de: "+str(round((reporte17.tasa),2))+"% (caso Actico/muertes) con realacion\n"
            desc+="a las muertes por el continente: "+pais+"\n"
            desc+="Donde el eje X representa las muertes de dicho\n"
            desc+="continente y el eje Y los casos activos."
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "desc":desc,
                "codigo":newcode.obtenerCodigo(),
                #"variable1":reporte14.regiones,
                
            }
            
            return render(request,'reporte.html',context)
        else:
            
            return render(request,'principal.html')
    # except:
    #     return render(request,'principal.html')
    
    
    
    
    
    
def Reporte19(request):
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            max = request.POST['max']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            
            reporte19=Prediccion19();
            reporte19.analizar19(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,max)
            
            titulo="Predicción de muertes en el último día del primer \naño de infecciones en un país.\n"
            # de muertes confirmadas y la linea roja representa la prediccion de muertes en dicho pais.

            desc="\n\n\nSe realiza la prediccion de muertes usando\n"
            desc+="usando regresion lineal polinomial grado 4\n"
            desc+="de la columna \""+variable1+"\" como eje X (tiempo)\n"
            desc+="y la columna \""+variable2+"\" como eje Y (muertes).\n"
            desc+="la grafica muestra una prediccion a "+max+" dias.\n"
           
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),#codigo Base64 para imagen del reporte
                "desc":desc,
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')    
    
def Reporte21(request):
    #try:
        if request.method == "POST":
            variable2 = request.POST['variable2']
            variable3 = request.POST['variable3']
            max = request.POST['max']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            
            #casos
            reporte21A=Prediccion21();
            reporte21A.analizar21(variable2,filtrar,columnaFiltrar,valorFiltrar,max,"Predicciones de casos en todo el mundo","img")
            #muertes
            reporte21B=Prediccion21();
            reporte21B.analizar21(variable3,filtrar,columnaFiltrar,valorFiltrar,max,"Predicciones de muertes en todo el mundo","img1")


            titulo="Predicciones de casos y muertes en todo el mundo\n"
            desc="\n\nSe realiza la prediccion de casos y muertes en todo el\n"
            desc+="mundo y la estimacion a: \""+str(max)+"\" unidades de tiempo\n "
            desc+="la grafica muestra: \"una tendencia de crecimiento\""
            desc+="para ambas predicciones."
            desc+="Se realiza la regresion polinomial grado 4"
            desc+=""
            desc+=""
            desc+=""

            newcode=Codigo64()
            newcode2=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "codigo2":newcode2.obtenerCodigo2(),
                "desc":desc,
            }
            
            return render(request,'reporte12.html',context)
        else:
            
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')    
    
    
    
#reporte22
def Reporte22(request):
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            variable3 = request.POST['variable3']
            pais=request.POST['pais']
            
            

            reporte22=Prediccion22();
            rate=reporte22.analizar22(variable1,variable2,variable3)
            NoM=reporte22.muertes
            NoCon=reporte22.confirmados
            #Como se puede apreciar en la imagen, la predicción toma una forma lineal (puntos azules) y los datos reales (puntos rojos), en realidad tienen muy poca correlación con la predicción.
            #sea positiva o negativa. El número total de casos fallecidos.
            titulo="Tasa de mortalidad por coronavirus (COVID-19) en un país\n"
            desc="\n\nPara calcular la mortalidad necesitamos:\n"
            desc+="El número de casos acumulados registrados del pais,\n"
            desc+="sea positiva o negativa. El número total de casos \n"
            desc+="fallecidos.\nY se obtuvo el numero de casos confirmados: "+NoCon+"\n"
            desc+="Y el numero de muertes confirmados: "+NoM+"\n"
            desc+="Utilizando la fórmula de Tasa de mortalidad por infección \n"
            desc+="Muertes / Casos ="+NoM+" / "+NoCon+" = "+rate+"%  (Tasa de Mortalidad)\n"+pais
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":"m",
                "desc":desc,
            }
            
            return render(request,'reporte22.html',context)
        else:
            
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')
    
      
    
def Reporte23(request):
        #try
        if request.method == "POST":
            sexo = request.POST['sexo']
            edad = request.POST['edad']
            muertes = request.POST['muertes']
            factores = request.POST['variable1']
            # pais=request.POST['pais']
            print("_____________********______________")
            print(factores)
            reporte23=Prediccion23();
            reporte23.analizar23(sexo,edad,muertes,factores[:-1])


            titulo="Factores de muerte por COVID-19 en un país."
            desc="\n\nSegun los factores de muerte seleccionados\n"
            desc+="se clasifican en factores de vida y/o muerte\n"
            desc+="y se agrega una barra 100-900 segun el factor de riesgo,\n"
            desc+="un factor de riego cerca de 900 es propenso a fallecer"
            desc+=" al contraer covid."
            desc+="Ademas es muy dificil predecir si es un factor de\n"
            desc+="alto riego para covid ya que estas investigaciones\n"
            desc+="requieren mas datos cientificos de cada infeccion,\n"
            


            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
                #"variable1":reporte14.regiones,
                
            }
            
            return render(request,'reporte.html',context)
        else:
            
            return render(request,'principal.html')
    # except:
    #     return render(request,'principal.html')    
    
    
    
    
def Reporte24(request):
    #try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            pais = request.POST['pais']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            reporte24=Prediccion24();
            reporte24.analizar24(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar)
            datos=reporte24.resultados
            
            
            titulo="Comparación entre el número de casos detectados y el \número de pruebas de un país "+pais
            desc="\n\n\nSe realiza un analisis de casos y pruebas realizadas\n"
            desc+="En la siguiente tabla se puede observar la cantidad\n"
            desc+="de test realizados y la cantidad de infectados\n"
            desc+="La cantidad de evidencia en relación al número\n"
            desc+="de casos positivos, pero en algunas fases podría\n"
            desc+="intensificarse para obtener un dato más realista."
            desc+="La cantidad de pruebas positivas y casos detectados\n"
            desc+="es: RELEVANTE\n"
            

            newcode=Codigo64()

            context={
                "titulo":titulo,
                "desc":desc,
                "codigo":newcode.obtenerCodigo(),
                "variable1":np.round(datos, decimals=0) ,

            }
            
            return render(request,'reporte24.html',context)
        else:
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')
       
    
    
    
    
    
    
    
#Predicción de casos confirmados por día

def Reporte25(request):
    try:
        if request.method == "POST":
            variable1 = request.POST['variable1']
            variable2 = request.POST['variable2']
            filtrar=request.POST['filtrar']
            columnaFiltrar=""
            valorFiltrar=""
            min = request.POST['min']
            max = request.POST['max']
            
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            reporte25=Prediccion25();
            reporte25.analizar25(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max,"Pais")
            #Como se puede apreciar en la imagen, la predicción toma una forma lineal (puntos azules) y los datos reales (puntos rojos), en realidad tienen muy poca correlación con la predicción.

            titulo="Predicción de casos confirmados por día\n"
            desc="\n\nSe hace una predicción con regresión lineal de Sklearn,\n"
            desc+="para determinar el número de casos confirmados que\n"
            desc+="deberían existir para cada fecha.\n"
            desc+="Como se puede apreciar en la imagen, la predicción \n(puntos azules) y los datos reales (puntos rojos)\n"
            desc+="Se deja el siguiente grafico para su interpretacion: "
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
                "desc":desc,
            }
            
            return render(request,'reporte.html',context)
        else:
            
            return render(request,'principal.html')
            
    except:
        return render(request,'principal.html')
        #pass

