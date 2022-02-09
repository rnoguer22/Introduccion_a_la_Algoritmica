def calcular_precio(precio):
    precio *= 1.21
    return precio

while True:
    precio = input("Introduzca el valor del precio: ")
    try:
        float(precio) == True
        break
    except:
        pass