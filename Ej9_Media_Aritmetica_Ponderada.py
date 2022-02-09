def media(num1, num2, num3):
    return (sum(num1, num2, num3)/3)

def pedir_numero():
    while True:
        numero = input("Introduzca un numero: ")
        try:
            numero = float(numero)
            break
        except:
            pass
    return numero