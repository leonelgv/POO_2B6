"""
>>> na = NumerosAmigos(5, 7)
>>> na.getAmigos()
True

>>> na = NumerosAmigos(3, 4)
>>> na.getAmigos()
False
"""
class NumerosAmigos:
    __numero1 = int(0)
    __numero2 = int(0)
    __amigos = bool

    def __init__(self, numero1, numero2):
        self.__numero1 = numero1
        self.__numero2 = numero2
        self.calcularNumerosAmigos()

    def sumaDivisores(self, numero):
        suma = int(0)
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    def calcularNumerosAmigos(self):
        if self.sumaDivisores(self.__numero1) == self.sumaDivisores(self.__numero2):
            self.__amigos = True
        else:
            self.__amigos = False

    def getAmigos(self):
        return self.__amigos

if __name__ == '__main__':
    import doctest
    doctest.testmod()
