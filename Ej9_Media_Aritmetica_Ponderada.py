def media(num1, num2, num3):
    media_aritmetica = (num1+num2+num3)/3
    
    def media_ponderada(media_aritmetica):
        #Vamos a redondear a las unidades, a partir del 0.5
        return round(media_aritmetica, 0)

    print ("La media de {}, {}, {} es {}".format(num1, num2, num3, media_aritmetica))
    print ("La media ponderada es: {}".format(media_ponderada(media_aritmetica)))

def pedir_numero():
    while True:
        numero = input("Introduzca un numero: ")
        try:
            numero = float(numero)
            break
        except:
            print ("Introduzca un valor correcto por favor")
            pass
    return numero

lista_num = []   # Definimos una lista vacia donde se almacenaran los 3 numeros
for i in range (3):
    num = pedir_numero()
    lista_num.append(num)   # Introducimos el numero en la lista

media (lista_num[0], lista_num[1], lista_num[2])