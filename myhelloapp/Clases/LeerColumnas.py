from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


import numpy as np
import pandas as pd

class LeerColumnas:
    def __init__(self):
        pass
    def Parametros(self):
        print("a")
        data = pd.read_csv('archivo.csv')
        # variable="<select class=\"custom-select\"  id=\"variable1\" name=\"variable1\">\n"
        # for i in data.columns.values:
        #     variable+="<option value=\""+i+"\">"+i+"</option>\n"
        # variable+="</select>\n"
        return data.columns.values