import base64 as base64Imagen
class Codigo64:
    def __init__(self):
        pass
    
    
    def obtenerCodigo(self):
        image = open('./helloworld/static/img.png', 'rb')
        image_read = image.read()
        image_64_encode = base64Imagen.encodebytes(image_read)

        newcode=str(image_64_encode)[2:-1]
        return newcode.replace('\\n', '')