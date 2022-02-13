#HORAS EXTRA
#125% si 36<=x<=43
#150% si x>43
#Horas por semana (sin horas extra) = 35; 35x4 = 140 horas al mes
#Precio por hora bruto = salario mensual bruto x 12 / (horas por semana x52)

class Horas_Extra:
    #Constructor
    def __init__(self, sal_men_bruto, horas_semana):
        self.sal_men_bruto = sal_men_bruto
        self.horas_semana = horas_semana
    
    #Funcion que nos calcula el salario por hora
    def precio_hora_bruto (self):
        return (self.sal_men_bruto*12)/(self.horas_semana*52)