from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
import pathlib
import os
import csv
from os import remove

from myhelloapp.Clases.Prediccion1 import Prediccion1
# Create your views here.


def home(request):
    
    return render(request,'principal.html')


def procesarArchivo(request):
    filee = request.POST['area']
    print("///////////////////////////GUARDA UN ARCHIVO////////////////////////////////////")
    print(filee)
    try:
        remove("archivoT.csv")
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
    predic= Prediccion1()
    predic.analizar()
    titulo="Tendencia de infeccion en un pais"
    context={
        "titulo":titulo,
        "variable1":predic.Parametros()
    }
    #print(filee)
    return render(request,'parametros.html',context)
