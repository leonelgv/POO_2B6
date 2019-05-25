class Recibo:
    __costoKw = float(0)
    __lecturaActual = int(0)
    __lecturaAnterior = int(0)
    __consumoKw = int(0)
    __totalAPagar = float(0)

    def calcularPago(self, costoKw, lecturaActual, lecturaAnterior):
        self.__costoKw = costoKw
        self.__lecturaActual = lecturaActual
        self.__lecturaAnterior = lecturaAnterior
        self.__consumoKw = self.__lecturaActual - self.__lecturaAnterior
        if(self.__consumoKw < 501):
            self.__totalAPagar = (self.__consumoKw * self.__costoKw) * 1.22
        elif(self.__consumoKw > 500 & self.__consumoKw < 901):
            self.__totalAPagar = (self.__consumoKw * self.__costoKw) * 1.18
        elif(self.__consumoKw > 900):
            self.__totalAPagar = (self.__consumoKw * self.__costoKw) * 1.12
        return self.__totalAPagar

    def getTotalAPagar(self):
        return self.__totalAPagar


class Recibos:
    def leerArchivo(self, archivo):
        file = open(archivo, 'r')
        lineas_archivo = []
        lineas = []
        for linea in file.readlines():
            lineas = linea.replace('\n', '').split('#')
            try:
                lineas_archivo.append([float(lineas[0]), int(lineas[1]), int(lineas[2])])
            except ValueError:
                lineas_archivo.append([0.0, 0.0, 0.0])
        return lineas_archivo

def main():
    recibo = Recibos()
    print(recibo.leerArchivo('recibo_luz.txt'))

if __name__==  '__main__':
   main()