def area(lado, h):
    return (lado*h)/2

while True:
    lado = input("Introduzca lo que mide el lado: ")
    try:
        lado = float(lado)
        lado > 0
        break
    except:
        pass

while True:
    h = input("Introduzca lo que mide la altura: ")
    try:
        h = float(h)
        h > 0
        break
    except:
        pass

print ("El area del triangulo es {}".format(area(lado, h)))