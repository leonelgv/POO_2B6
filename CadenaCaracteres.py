class CadenaCaracteres:
    __cadena = ""
    __totalCaracteres = int(0)

    def __init__(self, cadena):
        self.__cadena = cadena
        self.contarCaracteres()

    def contarCaracteres(self):
        self.__totalCaracteres = len(self.__cadena)

    def getTotalCaracteres(self):
        return self.__totalCaracteres
