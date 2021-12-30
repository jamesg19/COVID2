from django.urls import path
#from sklearn.linear_model import LinearRegression
#from .views import  procesarArchivo


from . import views
urlpatterns =[
    path('',views.home, name='home'),
    #path('procesarArchivo',procesarArchivo),

]
