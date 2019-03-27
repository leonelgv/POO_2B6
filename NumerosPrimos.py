class NumerosPrimos:
    __numero1 = int(0)
    __primo = bool

    def __init__(self, numero1):
        self.__numero1 = numero1
        self.calcularNumeroPrimo()

    def contarDivisores(self, numero):
        suma = int(0)
        for i in range(1, numero + 1):
            if numero % i == 0:
                suma += 1
        return suma

    def calcularNumeroPrimo(self):
        if self.contarDivisores(self.__numero1) == 2:
            self.__primo = True
        else:
            self.__primo = False

    def getPrimo(self):
        return self.__primo

NP = NumerosPrimos(105)
print (NP.getPrimo())