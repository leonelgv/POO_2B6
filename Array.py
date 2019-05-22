nombres = ['Rene', 'Sergio', 'Carmen', 'Paloma', 'Alexis', 'Rene']
try:
    print (nombres)
    # Agrega un elemento al final de la lista
    nombres.append('Yulibeth')
    print(nombres)
    # Agrega un elemento en un índice dado
    nombres.insert(2, 'Shania')
    print(nombres)
    # Nos muestra el tamaño de la lista
    print (len(nombres))
    # Nos muestra el número de veces que aparece el elemento en la lista
    print (nombres.count('Alexis'))
    #
    nombres.remove('Rene')
    print(nombres)
    # Quita el ítem en la posición dada de la lista, y lo devuelve.
    print(nombres.pop())
    print(nombres)
    if 'Carlos' in nombres:
        print ('Puede ir al viaje de estudios')
    else:
        print('No puede ir al viaje de estudios')
    nombres = ['carlos', 'Humberto', 'Agustin'] + nombres
    print(nombres)
    #nombres.sort()
    #print (nombres)
    #nombres.sort(reverse=True)
    #print(nombres)
    print (nombres[-1])
    # Sublistas
    print(nombres[0:4])
    print (nombres[0:4:2])
    print (nombres[2:])
    print (nombres[:2])
    print (nombres[:-2])
    print (nombres[-2:])
    print(nombres[::-1])

    print (max(nombres))
    print(min(nombres))
    print(nombres)
    print(nombres.index('paloma'))
    nombres.clear()
    print(nombres)

except IndexError:
    print ('No existe el elemento')
except ValueError:
    print('No existe el elemento')

class Arreglos:
    __lista = []

    def __init__(self, list):
        self.__lista = list

    def getLista(self):
        return self.__lista

    def recorrerArreglo(self):
        for x in self.getLista():
            print(self.getLista().index(x) + 1, x)

    def agregarelementoarray(self, elemento):
        self.__lista.append(elemento)

    def ordenarLista(self):
        self.__lista.sort()

    def eliminarNElementos(self, num):
        self.__lista.pop(num)

    def eliminarElemento(self, elemento):
        self.__lista.remove(elemento)

    def insertarNPosicion(self, num, elemento):
        self.__lista.insert(num, elemento)

    def imprimirLista(self):
        print(self.__lista)

    def extraerUltimoElemento(self):
        self.__lista.pop