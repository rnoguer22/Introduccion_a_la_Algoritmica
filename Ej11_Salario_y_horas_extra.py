#Funcion para calcular las horas extra de cada tipo
def horas_remuneradas(horas_semana):
    if 36 <= horas_semana <= 43:
        horas_extra_1 = horas_semana - 35
        horas_extra_2 = 0
    else:
        horas_extra_1 = 8
        horas_extra_2 = horas_semana - 43
    #La funcion devuelve una lista con el numero de horas de ambos tipos
    return [horas_extra_1, horas_extra_2]

class Horas_Extra:
    #Constructor
    def __init__(self, sal_men_bruto, horas_semana):
        self.sal_men_bruto = sal_men_bruto
        self.horas_semana = horas_semana
    
    #Funcion que nos calcula el salario bruto por hora
    def precio_hora_bruto(self):
        return (self.sal_men_bruto*12)/(self.horas_semana*52)
    
    #Funcion que devuelve el salario por hora remunerado
    def precio_hora_remunerada(self):
        horas_125 = horas_remuneradas(self.horas_semana)[0]
        horas_150 = horas_remuneradas(self.horas_semana)[1]
        precio_final = (35*self.precio_hora_bruto() + (horas_125*self.precio_hora_bruto()*1.25 + horas_150*self.precio_hora_bruto()*1.50))/self.horas_semana
        return precio_final

#Funcion para introducir las horas por semana por teclado
def introducir_horas_semana():
    while True:
        horas = input("Introduzca el numero de horas por semana: ")
        try:
            horas = int(horas)
            horas >= 35
            break
        except:
            print ("Introduzca un valor correcto por favor")
            pass
    return horas


#Funcion para pedir al usuario el salario mensual bruto
def introducir_sal_men_bruto():
    while True:
        salario = input("Introduzca el salario mensual bruto: ")
        try:
            salario = int(salario)
            salario > 0
            break
        except:
            print ("Introduzca un valor correcto por favor")
            pass
    return salario


if __name__ == "__main__":

    #Introducimos los datos por teclado
    salario_mensual_bruto = introducir_sal_men_bruto()
    horas_semana = introducir_horas_semana()

    #Definimos resultado como una instancia de clase y hallamos los salarios
    resultado = Horas_Extra(salario_mensual_bruto, horas_semana)
    print ("Su precio por hora bruto es: {}€".format(round(resultado.precio_hora_bruto(), 2)))
    print ("Su precio por hora remunerado es: {}€".format(round(resultado.precio_hora_remunerada(), 2)))