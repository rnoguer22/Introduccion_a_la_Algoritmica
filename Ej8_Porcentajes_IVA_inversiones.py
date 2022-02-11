class Prima_Anual:
    def __init__(self, antiguedad, distancia, accidentes):
        self.antiguedad = antiguedad
        self.distancia = distancia
        self.accidentes = accidentes

    #Funcion para calcular el impuesto asociado a la antiguedad
    def prima_antiguedad(self):
        if self.antiguedad < 4:
            return 0
        else:
            return (200 + 20*(self.antiguedad-4))
        
    #Funcion que calcula el impuesto de la distancia
    def prima_distancia(self):
        return min(self.distancia*0.01, 400)
        
    #Funcion que nos calcula la prima ponderada
    def ponderacion(self, prima_antiguedad, prima_distancia):
        prima = prima_antiguedad + prima_distancia
        if self.accidentes < 3:
            prima /= (self.accidentes+1)
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

    #Pedimos al usuario los datos
    accidentes = pedir_datos("accidentes")
    distancia = pedir_datos("distancia")
    antiguedad = pedir_datos("antiguedad")

resultado = Prima_Anual(accidentes=accidentes, distancia=distancia, antiguedad=antiguedad)
print (resultado.ponderacion(resultado.prima_antiguedad(), resultado.prima_distancia()))