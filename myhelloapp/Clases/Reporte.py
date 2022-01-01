
import PaPDF
#python -m pip install PaPDF --upgrade --force
class Reporte:
    def __init__(self):
        pass
    #iniciamos la creacion del PDF
    def CrearPDF(self):
        with PaPDF("Reporte.pdf") as pdf:
            pdf.addText(40,290,"Reporte Analisis")
            pdf.addPage()
            
            pdf.addImagen('./helloworld/static/img.png')