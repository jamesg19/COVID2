from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
import pathlib
import os
import csv
from os import remove
from myhelloapp.Clases.GestorReporte import GestorReporte
from myhelloapp.Clases.LeerColumnas import LeerColumnas
from myhelloapp.Clases.Prediccion1 import Prediccion1
from myhelloapp.Clases.Prediccion2 import Prediccion2
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
                            fd.write(text)
            fd.close
        print('La salida es exitosa ...')
    except:
        print("Se produjo un error al guardar el archivo")
        return render(request,'principal.html')
    # #reconocer columnas
    columnas= LeerColumnas()
    #predic.analizar()
    
    titulo="Tendencia de infeccion en un pais"
    context={
        "titulo":titulo,
        "variable1":columnas.Parametros()
    }
    
    FrameParametro=GestorReporte()
    ventana=FrameParametro.obtenerParametroHtml(tipoReporte)
    
    return render(request,ventana+'.html',context)

# Tendencia de la infección por Covid-19 en un País. 
def Reporte1(request):
    
    variable1 = request.POST['variable1']
    variable2 = request.POST['variable2']
    filtrar=request.POST['filtrar']
    columnaFiltrar=""
    valorFiltrar=""
    min = request.POST['min']
    max = request.POST['max']
    print("JAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(min)
    print(max)
    
    
    if(filtrar=="si"):
        columnaFiltrar=request.POST['columnaFiltrar']
        valorFiltrar=request.POST['valorFiltrar']
    
    reporte1=Prediccion1();
    reporte1.analizar(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max)
    
    titulo="Tendencia de infeccion en un pais"
    try:
        remove("archivo.csv")
        remove("archivoT.csv")
        print("ELIMINADO CORRECTAMENTEE ARCHIVOS")
    except:
        print("_____________==================__________________")
        pass

    context={
        "titulo":titulo,
        #APP CONFIG
    }
    
    return render(request,'reporte.html',context)


# PREDICCION DE INFECTADOS DE UN PAIS
def Reporte2(request):
    
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
    
    
    reporte1=Prediccion2();
    reporte1.analizar(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max)
    
    titulo="PREDICCION DE INFECTADOS DE UN PAIS"
    try:
        remove("archivo.csv")
        remove("archivoT.csv")
        print("ELIMINADO CORRECTAMENTEE ARCHIVOS")
    except:
        print("_____________==================__________________")
        pass

    context={
        "titulo":titulo,
        #APP CONFIG
    }
    
    return render(request,'reporte.html',context)

def Reporte3(request):
    pass

def Reporte4(request):
    pass

def Reporte5(request):
    pass
    
    