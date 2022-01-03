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
from myhelloapp.Clases.Prediccion13 import Prediccion13
from myhelloapp.Clases.Prediccion15 import Prediccion15
from myhelloapp.Clases.Prediccion19 import Prediccion19
from myhelloapp.Clases.Prediccion2 import Prediccion2
from myhelloapp.Clases.Prediccion22 import Prediccion22
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
            
            
            if(filtrar=="si"):
                columnaFiltrar=request.POST['columnaFiltrar']
                valorFiltrar=request.POST['valorFiltrar']
            
            reporte1=Prediccion1();
            reporte1.analizar(variable1,variable2,filtrar,columnaFiltrar,valorFiltrar,min,max)
            
            titulo="Tendencia de infeccion en un pais \n"
            desc="La tendencia de las infecciones en un país se lleva \na cabo a través de un máximo de: "+max+"(unidades de tiempo)\nlo cual en base a los datos obtenidos se hace \nuna estimación de la tendencia para los proximos \n"+max+" (unidades tiempo)."
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
            desc="la prediccion de infectados en un país se lleva \n"
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
            
            titulo="\n\n\n\n\nPredicción de mortalidad por COVID en un Departamento\n"
            desc="Se pueden predecir como maximo 30 dias posteriores al\n"
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

            desc="Se realiza la prediccion de mortalidad de un pais\n"
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
            
            titulo="Tendencia del número de infectados por día de un País.."


            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')


def Reporte8(request):
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


            newcode=Codigo64()
            context={
                "titulo":titulo,
                "codigo":newcode.obtenerCodigo(),
            }
            
            return render(request,'reporte.html',context)
        else:
            return render(request,'principal.html')
            
    # except:
    #     return render(request,'principal.html')




def Reporte10(request):
    pass
def Reporte11(request):
    pass
def Reporte12(request):
    pass

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


            titulo="Muertes según regiones de un país - Covid 19. en "+pais+"\n"
            desc="Hace de un calculo de las muertes por region\n"
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
            print("_____________********______________")
        
            reporte15=Prediccion15();
            reporte15.analizar15(variable1[:-1],pais)


            titulo="Tendencia de casos confirmados de Coronavirus en \nun departamento del pais "+pais+"\n"
            desc="\n\nEl proceso de predicción se realizó mediante regresión lineal.\n"
            desc+=" y la grafica representa la tendencia de los departamentos seleccionados"
            


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
    
def Reporte19(request):
    try:
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
            
            titulo="Predicción de muertes en el último día del primer año \nde infecciones en un país.\n"
            # de muertes confirmadas y la linea roja representa la prediccion de muertes en dicho pais.

            desc="\n\nSe realiza la prediccion de muertes usando\n"
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
            
    except:
        return render(request,'principal.html')    
    
    
    
    
    
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
            desc="Para calcular la mortalidad necesitamos:\n"
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
            desc="Se hace una predicción con regresión lineal de Sklearn,\n"
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

