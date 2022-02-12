class Triangulo:
    #Constructor
    def __init__(self, lado, altura):
        self.lado = lado
        self.altura = altura
    
    #Funcion para calcular el area
    def area(self):
        return (self.lado*self.altura)/2

