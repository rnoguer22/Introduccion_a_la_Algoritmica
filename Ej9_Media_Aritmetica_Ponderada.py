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

if __name__ == "__main__":

    #Creamos una lista vacia donde se almacenaran los 3 numeros
    r = []
    for i in range(3):   #Bucle para introducir los numeros por teclado
        num = introducir_numero(i)
        r.append(num)
    
    resultado = Media(r[0], r[1], r[2])
    print ("La media aritmetica de {}, {}, {} es {}".format(r[0], r[1], r[2], resultado.media_no_ponderada()))
    