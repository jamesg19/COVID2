
import pandas as pd

class LeerColumnas:
    def __init__(self):
        pass
    def Parametros(self):

        data = pd.read_csv('archivo.csv')
        # variable="<select class=\"custom-select\"  id=\"variable1\" name=\"variable1\">\n"
        # for i in data.columns.values:
        #     variable+="<option value=\""+i+"\">"+i+"</option>\n"
        # variable+="</select>\n"
        return data.columns.values