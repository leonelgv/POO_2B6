"""
Programación estructurada
"""
radio = float(input("Escribe el radio: "))
area = 3.141592654 * (radio * radio)
perimetro = (2 * 3.141592654) * radio
print ("El área es igual a: ", area)
print ("El perimetro es igual a: ", perimetro)

lado = float(input("Escribe el lado del cuadrado: "))
area2 = lado * lado
perimetro2 = lado * 4
print ("El área es igual a: ", area2)
print ("El perimetro es igual a: ", perimetro2)

base = float(input("Escribe la base del rectangulo: "))
altura = float(input("Escribe la altura del rectangulo: "))
area3 = base * altura / 2
print ("El área es igual a: ", area3)

"""
Programación orientada a objetos



"""

import math

class Circulo:
    __radio = float(0)
    __perimetro = float(0)
    __area = float(0)

    def __init__(self, radio):
        if (radio < 0):
            self.__radio = 0
        else:
            self.__radio = radio
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        self.__area = math.pi * (self.__radio * self.__radio)

    def calcularPerimetro(self):
        self.__perimetro = (2 * math.pi) * self.__radio

    def getArea(self):
        return self.__area

    def getPerimetro(self):
        return self.__perimetro

class Cuadrado:
    __lado = float(0)
    __perimetro = float(0)
    __area = float(0)

    def __init__(self, lado):
        if (lado < 0):
            self.__lado = 0
        else:
            self.__lado = lado
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        self.__area = self.__lado * self.__lado

    def calcularPerimetro(self):
        self.__perimetro = self.__lado * 4

    def getArea(self):
        return self.__area

    def getPerimetro(self):
        return self.__perimetro

class Rectangulo:
    __base = float(0)
    __altura = float(0)
    __area = float(0)
    __perimetro = float(0)

    def __init__(self, base, altura):
        if (base < 0 or altura < 0):
            self.__base = 0
            self.__altura = 0
        else:
            self.__base = base
            self.__altura = altura
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        self.__area = (self.__base * self.__altura)

    def calcularPerimetro(self):
        self.__perimetro = (self.__base * 2) + (self.__altura * 2)

    def getArea(self):
        return self.__area

    def getPerimetro(self):
        return self.__perimetro