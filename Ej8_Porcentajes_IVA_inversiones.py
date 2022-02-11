from cmath import inf


class Prima_Anual:
    def __init__(self, antiguedad, distancia, accidentes):
        self.antiguedad = antiguedad
        self.distancia = distancia
        self.accidentes = accidentes
    
    def calcular_prima():

        #Funcion para calcular el impuesto asociado a la antiguedad
        def prima_antiguedad (self, antiguedad):
            if antiguedad < 4:
                return 0
            else:
                return (200 + 20*(antiguedad-4))
        
        #Funcion que calcula el impuesto de la distancia
        def prima_distancia(self, distancia):
            return inf(0.01*distancia, 400)
        
        #Funcion que nos calcula la prima ponderada
        def ponderacion(self, accidentes):
            prima = prima_antiguedad(self, antiguedad) + prima_distancia(self, distancia)
            if accidentes < 3:
                prima /= (accidentes+1)
            else:
                prima = 0
            return prima

#Funcion para pedir los datos al usuario
def pedir_datos(valor):
    while True:
        numero = input("{}: ".format(valor))
        try:
            numero = int(numero)
            break
        except:
            print ("Introduzca un valor correcto por favor")
            pass
    return numero

if __name__ == '__main__':

    accidentes = pedir_datos("accidentes")
    distancia = pedir_datos("distancia")
    antiguedad = pedir_datos("antiguedad")

resultado = Prima_Anual(accidentes=accidentes, distancia=distancia, antiguedad=antiguedad)
print (resultado)