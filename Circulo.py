"""
>>> miCirculo = Circulo(2)
>>> miCirculo.calcularArea()
>>> miCirculo.getArea()
12.566370616
"""

class Circulo:
    __radio = float(0)
    __perimetro = float(0)
    __area = float(0)

    def __init__(self, radio):
        if(radio < 1 and radio > 1000):
            self.__radio = 0
        else:
            self.__radio = radio
        self.calcularArea()
        self.calcularPerimetro()

    def calcularArea(self):
        self.__area = 3.141592654 * (self.__radio * self.__radio)

    def calcularPerimetro(self):
        self.__perimetro = (2 * 3.141592654) * self.__radio

    def getArea(self):
        return self.__area

    def getPerimetro(self):
        return self.__perimetro

if __name__ == '__main__':
    import doctest
    doctest.testmod()