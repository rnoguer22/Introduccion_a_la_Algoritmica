class Media: 
    #Constructor
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    #Funcion para calcular la media
    def media_no_ponderada(self):
        return (sum(self.num1, self.num2, self.num3))/3