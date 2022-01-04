from django.urls import path
#from sklearn.linear_model import LinearRegression
from .views import  procesarArchivo, Reporte1, Reporte2, Reporte3, Reporte4, Reporte5, Reporte6, Reporte7, Reporte8, Reporte9, Reporte10, Reporte11,Reporte12, Reporte13, Reporte14, Reporte15,Reporte16, Reporte17, Reporte19,Reporte21 , Reporte22,Reporte23,Reporte24, Reporte25


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
    path('Reporte14',Reporte14),
    path('Reporte15',Reporte15),
    path('Reporte16',Reporte16),
    path('Reporte17',Reporte17),
    path('Reporte19',Reporte19),
    path('Reporte21',Reporte21),
    path('Reporte22',Reporte22),
    path('Reporte23',Reporte23),
    path('Reporte24',Reporte24),
    path('Reporte25',Reporte25),
    

]
