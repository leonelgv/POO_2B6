from Circulo import *
class Archivos():

    def leerArchivo(self, archivo):
        file = open(archivo,'r')
        lineas_archivo = []
        for a in file.readlines():
            lineas_archivo.append(a.replace('\n', ''))
        file.close()
        return lineas_archivo

    def convertirStringANumero(self, lista):
        lineas_archivo = []
        try:
            for a in range(0, len(lista)):
                lineas_archivo.append(int(lista[a]))
        except ValueError:
            lineas_archivo.append(0)
        return lineas_archivo

    def generarResultados(self, archivo, lista):
        file = open(archivo, 'w')
        circulo = Circulo2()
        for r in range(0, len(lista)):
            area = circulo.calcularArea(lista[r])
            perimetro = circulo.calcularPerimetro(lista[r])
            linea = str(lista[r]) + ',' + str(area) + ',' + str(perimetro) + '\n'
            file.write(linea)
        file.close()

def main():
    file = Archivos()
    arreglo = []
    arreglo = file.leerArchivo('radios.txt')
    radios = []
    radios = file.convertirStringANumero(arreglo)
    file.generarResultados('resultados.csv',radios)

if __name__==  '__main__':
   main()
