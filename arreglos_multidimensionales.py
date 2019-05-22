numeros = [
    [4, 6, 7],
    [3, 9, 8],
    [2, 5, 9]
]
arreglo = [
    [
        [1, 2, 3], [4, 5, 6], [7, 8, 9]
    ],[
        [11, 12, 13], [14, 15, 16], [17, 18, 19]
    ],[
        [21, 22, 23], [24, 25, 26], [27, 28, 29]
    ]
]

try:
    numeros[1].insert(2, 4)
    #print(numeros[1][2])
    #print(arreglo[2][1][0])
    print(numeros)
    arreglo[0][0].insert(0,3)
    print (arreglo)
    print (len(arreglo[0][0]))
except IndexError:
    print('No existe el elemento')