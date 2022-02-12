class Media: 
    #Constructor
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    #Funcion para calcular la media
    def media_no_ponderada(self):
        return (sum(self.num1, self.num2, self.num3))/3

#Funcion para introducir los numeros por teclado
def introducir_numero(i):
    while True:
        numero = input("Introduzca el {}º numero: ".format(i+1))
        try:
            numero = float(numero)
            break
        except:
            print ("Introduzca un valor correcto por favor")
            pass
    return numero    