# Manual Tecnico

## Tabla de Contenido
**[Introducción](#introduccion)**

**[Objetivos Generales](#obgenerales)**

**[Objetivos Específicos](#obespe)**

**[Descripcion](#descripcion)**

**[Tecnologias](#tecnologia)**

**[Usabilidad](#usabilidad)**

## Introducción <a name="introduccion"></a>

Coronavirus Data Analysis with Scikit-Learn [Enlace](https://github.com/jamesg19/COVID2) , cuenta con una variedad de tipos de analisis respecto a la pandemia global que sufrimos al dia de hoy y este proyecto hace prediccion y tendencias 
de las reguntas que nos hacemos dia a dia sobre que pasará con el avance de la pantemia y sus nuevas cepas.

## Objetivos Generales <a name="obgenerales"></a>

- Desarrollar un analisis de datos y hacer predicciones a base de los datos recopilados y realizar graficas de tendencia y prediccion.

## Objetivos Específicos <a name="obespe"></a>

- Crear un analisis de datos
- Realizar predicciones y tendencias con la libreria scikit-learn
- Analizar datos de ciertas columnas de los archivos de informacion
- Desplegar una aplicacion web que permita a cualquier usuario hacer el calculo de tendencia de la pandemia y predicciones en base a los datos recopilados que ingrese el usuario

## Descripcion <a name="descripcion"></a>

Es aplicacion web que permita a cualquier usuario hacer el calculo de tendencia de la pandemia y predicciones en base a los datos recopilados que ingrese el usuario, acepta archivos .csv.

![img_patron_interprete](https://github.com/jamesg19/COMPILADORES_DICIEMBRE_2021/blob/main/img_patron.png)

Donde el proyecto se encuentra estructurado de la siguiente manera

- Tendencia de la infección por Covid-19 en un País.
- Predicción de Infertados en un País.
- Indice de Progresión de la pandemia.
- Predicción de mortalidad por COVID en un Departamento.
- Predicción de mortalidad por COVID en un País.
- Análisis del número de muertes por coronavirus en un País.
- Tendencia del número de infectados por día de un País.
- Predicción de casos de un país para un año.
- Tendencia de la vacunación de en un País.
- Ánalisis Comparativo de Vacunaciópn entre 2 paises.
- Porcentaje de hombres infectados por covid-19 en un País desde el primer caso activo
- Ánalisis Comparativo entres 2 o más paises o continentes.
- Muertes promedio por casos confirmados y edad de covid 19 en un País.
- Muertes según regiones de un país - Covid 19.
- Tendencia de casos confirmados de Coronavirus en un departamento de un País.
- Porcentaje de muertes frente al total de casos en un país, región o continente.
- Tasa de comportamiento de casos activos en relación al número de muertes en un continente.
- Comportamiento y clasificación de personas infectadas por COVID-19 por municipio en un País.
- Predicción de muertes en el último día del primer año de infecciones en un país.
- Tasa de crecimiento de casos de COVID-19 en relación con nuevos casos diarios y tasa de muerte por COVID-19
- Predicciones de casos y muertes en todo el mundo - Neural Network MLPRegressor
- Tasa de mortalidad por coronavirus (COVID-19) en un país.
- Factores de muerte por COVID-19 en un país.
- Comparación entre el número de casos detectados y el número de pruebas de un país.
- Predicción de casos confirmados por día


## Tecnologias <a name="tecnologia"></a>

- Python3
```bash
  #instalar Python3
  sudo apt update
  sudo apt-get upgrade
  sudo apt install python3.8
```
- Django 4.0
```bash
#instalamos Django 4.0
pip install Django==4.0
```
- scikit-learn
```bash
  pip install -U scikit-learn
```
## Usabilidad <a name="usabilidad"></a>

Para evitar resultados inesperados se debe de utilizar las tecnologias anteriormente mencioandas.

Pasos (Linux)

```bash
#clona el proyecto desde el repositorio ofical
git clone https://github.com/jamesg19/COVID2

#se desplaza a la carpeta donde se encentra el proyecto
cd COMPILADORES\_DICIEMBRE\_202

#comando para instalar las dependencias y libreria utilizadas 

pip install -r requeriments.txt
#usa la funcionalidad para ejecutar el servidor local host
python3 manage.py runserver


```

si se desea modificar los archivos y agregar nuevas funcionalidades y ejecutarlas en conjunto

```bash
    python3 manage.py migrate
    python3 manage.py makemigrations
```
