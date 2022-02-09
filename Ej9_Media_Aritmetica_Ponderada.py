def media(num1, num2, num3):
    media_aritmetica = (num1+num2+num3)/3
    print ("La media de {}, {}, {} es {}".format(num1, num2, num3, media_aritmetica))

def pedir_numero():
    while True:
        numero = input("Introduzca un numero: ")
        try:
            numero = float(numero)
            break
        except:
            pass
    return numero

lista_num = []   # Definimos una lista vacia donde se almacenaran los 3 numeros
for i in range (3):
    num = pedir_numero()
    lista_num.append(num)   # Introducimos el numero en la lista

media (lista_num[0], lista_num[1], lista_num[2])