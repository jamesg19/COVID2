import base64 as james
image = open('C:\\Users\\james\\Desktop\\1.png', 'rb')
image_read = image.read()
image_64_encode = james.encodebytes(image_read)
print("data:image/png;base64,"+str(image_64_encode))

