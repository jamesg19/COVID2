from django.urls import path
#from sklearn.linear_model import LinearRegression
from .views import  procesarArchivo, Reporte1, Reporte2, Reporte3, Reporte4, Reporte5, Reporte6, Reporte7, Reporte8, Reporte9, Reporte10, Reporte11
from .views import Reporte12, Reporte13


from . import views
urlpatterns =[
    path('',views.home, name='home'),
    path('procesarArchivo',procesarArchivo),
    path('Reporte1',Reporte1),
    path('Reporte2',Reporte2),
    path('Reporte3',Reporte3),
    path('Reporte4',Reporte4),
    path('Reporte5',Reporte5),
    path('Reporte6',Reporte6),
    path('Reporte7',Reporte7),
    path('Reporte8',Reporte8),
    path('Reporte9',Reporte9),
    path('Reporte10',Reporte10),
    path('Reporte11',Reporte11),
    path('Reporte12',Reporte12),
    path('Reporte13',Reporte13),
    

]
