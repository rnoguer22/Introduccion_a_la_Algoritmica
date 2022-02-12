class Triangulo:
    #Constructor
    def __init__(self, lado, altura):
        self.lado = lado
        self.altura = altura
    
    #Funcion para calcular el area
    def area(self):
        return (self.lado*self.altura)/2

#Funcion para pedir los datos al usuario
def dame_datos(dato):
    while True:
        numero = input("¿{}? ".format(dato))
        try:
            numero = float(numero)
            numero > 0 == True
            break
        except:
            print ("Introduzca un valor correcto por favor")
            pass
    return numero 


if __name__ == '__main':
    #Introducimos los datos por teclado
    lado = dame_datos("Lado")
    altura = dame_datos("Altura")
