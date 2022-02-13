#HORAS EXTRA
#125% si 36<=x<=43
#150% si x>43
#Precio por hora bruto = salario mensual bruto x 12 / (horas por semana x52)

class Horas_Extra:
    #Constructor
    def __init__(self, sal_men_bruto, horas_semana):
        self.sal_men_bruto = sal_men_bruto
        self.horas_semana = horas_semana
    
    #Funcion que nos calcula el salario bruto por hora
    def precio_hora_bruto(self):
        return (self.sal_men_bruto*12)/(self.horas_semana*52)
    
    def precio_hora_remunerada(self, horas_ext, horas_125, horas_150):
        horas_ext = self.horas_semana - 35

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
        salario = input("Introduzca el salario mensua bruto: ")
        try:
            salario = int(salario)
            salario > 0
            break
        except:
            print ("Introduzca un valor correcto por favor")
            pass
    return salario