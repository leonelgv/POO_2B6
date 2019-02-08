class Recibo:
    __costoKw = float(0)
    __lecturaActual = int(0)
    __lecturaAnterior = int(0)
    __consumoKw = int(0)
    __totalAPagar = float(0)

    def __init__(self, costoKw, lecturaActual, lecturaAnterior):
        self.__costoKw = costoKw
        self.__lecturaActual = lecturaActual
        self.__lecturaAnterior = lecturaAnterior
        self.calcularPago()

    def calcularPago(self):
        self.__consumoKw = self.__lecturaActual - self.__lecturaAnterior
        if(self.__consumoKw < 501):
            self.__totalAPagar = (self.__consumoKw * self.__costoKw) * 1.22
        elif(self.__consumoKw > 500 & self.__consumoKw < 901):
            self.__totalAPagar = (self.__consumoKw * self.__costoKw) * 1.18
        elif(self.__consumoKw > 900):
            self.__totalAPagar = (self.__consumoKw * self.__costoKw) * 1.12

    def getTotalAPagar(self):
        return self.__totalAPagar

