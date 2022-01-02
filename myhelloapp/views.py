from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
import pathlib
import os
import csv
#import base64 as base64Imagen
from os import remove
from myhelloapp.Clases.Codigo64 import Codigo64
from myhelloapp.Clases.GestorReporte import GestorReporte
from myhelloapp.Clases.LeerColumnas import LeerColumnas
from myhelloapp.Clases.Prediccion1 import Prediccion1
from myhelloapp.Clases.Prediccion2 import Prediccion2
from myhelloapp.Clases.Prediccion25 import Prediccion25
from myhelloapp.Clases.Prediccion4 import Prediccion4
# Create your views here.

#james= Django(__name__)
def home(request):
    
    return render(request,'principal.html')


def procesarArchivo(request):
    filee = request.POST['area']
    tipoReporte=request.POST['tipoReporte']
   
    try:
        remove("archivo.csv")
        remove("archivoT.csv")
    except:
        pass
    try:
        remove("./helloworld/static/img.png")
        print("IMAGEEEEEEEN CORRECTAMENTEE")
    except:
        pass
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

# Tendencia de la infección por Covid-19 en un País. 
def Reporte1(request):
    try:
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
            reporte1.analizar(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max)
            
            titulo="Tendencia de infeccion en un pais \n"
            desc="La tendencia de las infecciones en un país se lleva a cabo\na través de un máximo de: "+max+"(unidades de tiempo) lo cual en base \na los datos obtenidos se hace una estimación de la tendencia \npara los proximos "+max+" (unidades tiempo)."
            desc+="\nAdemas se utiliza la columna "+variable1+" en el eje X \ny  la columna \nen el eje Y "+variable2
            
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



# PREDICCION DE INFECTADOS DE UN PAIS
def Reporte2(request):
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
            
            
            reporte2=Prediccion2();
            reporte2.analizar(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max,"Pais")
            
            titulo="PREDICCION DE INFECTADOS DE UN PAIS"
            desc="la prediccion de infectados en un país se lleva a cabo\na través de un máximo de: "+max+"(unidades de tiempo) lo cual en base \na los datos obtenidos se hace una estimación de la tendencia \npara los proximos "+max+" (unidades tiempo)."
            desc+="\nAdemas se utiliza la columna "+variable1+" en el eje X \ny  la columna \nen el eje Y "+variable2+"."
            desc+="\n la linea amarilla representa prediccion y \n la linea azul(es) los casos reales."
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

def Reporte3(request):
    pass



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
            
            titulo="Predicción de mortalidad por COVID en un Departamento"

            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
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
            
            titulo="Predicción de mortalidad por COVID en un País"
            descripcion=""
            
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    except:
        return render(request,'principal.html')
    
    
def Reporte6(request):
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
            reporte4.analizar6 (variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,0,0,"Pais")
            
            titulo="Análisis del número de muertes por coronavirus en un País."
            descripcion=""
            
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'reporte.html')
            
    except:
        return render(request,'principal.html')



def Reporte7(request):
    pass


def Reporte8(request):
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
            reporte4.analizar8("",variable2,filtrar,columnaFiltrar,valorFiltrar,0,0,"Pais")
            
            titulo="Predicción de casos de un país para un año."
            descripcion=""
            
            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
            }
            
            return render(request,'reporte.html',context)
        else:
           return render(request,'principal.html') 
            
    except:
        return render(request,'principal.html')

#Tendencia de la vacunación de en un País. 

def Reporte9(request):
    try:
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


            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    except:
        return render(request,'principal.html')




def Reporte10(request):
    pass
def Reporte11(request):
    pass
def Reporte12(request):
    pass
def Reporte13(request):
    pass


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
            
            titulo="Predicción de casos confirmados por día"


            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
            }
            
            return render(request,'reporte.html',context)
        else:
            
            return render(request,'principal.html')
            
    except:
        return render(request,'principal.html')

