def calcular_precio(precio):
    precio *= 1.21
    return precio

while True:
    precio = input("Introduzca el valor del precio: ")
    try:
        precio = float(precio)
        break
    except:
        pass

print ("Precio original: {}. Precio con IVA: {}".format(precio, calcular_precio(precio)))

Falta el apartado 2 !!!