class Rectangulo():
    __base = float(0)
    __altura = float(0)
    __perimetro = float(0)
    __area = float(0)

    def calcularArea(self, base, altura):
        if (base < 0 or altura < 0):
            self.__base = 0
            self.__altura = 0
        else:
            self.__base = base
            self.__altura = altura
        self.__area = (self.__base * self.__altura)
        return self.__area

    def calcularPerimetro(self, base, altura):
        if (base < 0 or altura < 0):
            self.__base = 0
            self.__altura = 0
        else:
            self.__base = base
            self.__altura = altura
        self.__perimetro = (self.__base * 2) + (self.__altura * 2)
        return self.__perimetro

class Rectangulos:

    def leerArchivo(self, archivo):
        datos = []
        elementos = []
        file = open(archivo, 'r')
        for f in file.readlines():
            linea = f.replace('\n','')
            elementos = linea.split(',')
            try:
                datos.append([float(elementos[0]), float(elementos[1])])
            except ValueError:
                datos.append([0.0,0.0])
        return datos
        file.close()

    def realizarCalculos(self, lista):
        area = float(0)
        perimetro = float(0)
        rectangulo = Rectangulo()
        resultados = []
        for f in range(0, len(lista)):
            area = rectangulo.calcularArea(lista[f][0], lista[f][1])
            perimetro = rectangulo.calcularPerimetro(lista[f][0], lista[f][1])
            resultados.append([area, perimetro])
        return resultados

    def guardarResultados(self, archivo, datos, resultados):
        file = open(archivo, 'w')
        for f in range(0, len(datos)):
            linea = str(datos[f][0]) + ',' + str(datos[f][1]) + ',' + str(resultados[f][0]) + ',' + str(resultados[f][1]) + '\n'
            file.write(linea)
        file.close()


def main():
    file = Rectangulos()
    arreglo = []
    arreglo = file.leerArchivo('cuadrados.txt')
    resultados = file.realizarCalculos(arreglo)
    file.guardarResultados('rectangulos.csv',arreglo, resultados)
    print(resultados)

if __name__==  '__main__':
   main()