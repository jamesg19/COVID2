from django.urls import path
#from sklearn.linear_model import LinearRegression
from .views import  procesarArchivo, Reporte1, Reporte2, Reporte3, Reporte4, Reporte5


from . import views
urlpatterns =[
    path('',views.home, name='home'),
    path('procesarArchivo',procesarArchivo),
    path('Reporte1',Reporte1),
    path('Reporte2',Reporte2),
    path('Reporte3',Reporte3),
    path('Reporte4',Reporte4),
    path('Reporte5',Reporte5),
    

]
