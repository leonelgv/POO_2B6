from random import *

class JuegoAhorcado:
    def main(self):
        palabras = ["programacion", "manzana", "informatica", "automovil", "pizarron", "computadora", "robot", "teclado", "redes", "monitor", "procesador", "memoria", "disco"]
        palabraIndice = randrange(len(palabras)-1)
        #print (len(palabras))

        letras = list(palabras[palabraIndice])
        letrasIndice = randrange(len(letras)-1)
        pistas = 0

        longitudPalabra = len(letras)-1
        if longitudPalabra > 0 and longitudPalabra <= 5:
            pistas = 1
        if longitudPalabra > 5 and longitudPalabra <= 10:
            pistas = 2
        if longitudPalabra > 10 and longitudPalabra <= 15:
            pistas = 3
        if longitudPalabra > 15 and longitudPalabra <= 20:
            pistas = 4

        contador = 0
        pista1 = randrange(len(letras) - 1)
        pista2 = randrange(len(letras) - 1)
        pista3 = randrange(len(letras) - 1)
        pista4 = randrange(len(letras) - 1)

        for i in range(len(letras)):
            if pista1 == i or pista2 == i:
                try:
                    print(" ", letras[i],end="")
                except IndexError:
                    print("No existe esa posición")
            else:
                print (" _ ", end="")

        print ()
        print ()
        letraAPedir = input("Escribe la letra para jugar: ")
        letraEncontrada = False
        indiceLetra = []

        for i in range(len(letras)):
            if letras[i] == letraAPedir:
                letraEncontrada = True
                indiceLetra.append(i)



        if letraEncontrada:
            print ("Si existe la letra en la palabra")
            print ("Existe ", len(indiceLetra), " veces")
            for i in range(len(indiceLetra)):
                print ("La posición es: ", indiceLetra[i])
        else:
            print ("No existe la letra en la palabra")

        contador = 0
        if (letraEncontrada):
            for i in range(len(letras)):
                try:
                    if pista1 == i or pista2 == i or indiceLetra[contador] == i:
                        try:
                            print(" ", letras[i], end="")
                            #print(contador, end="")
                            if (indiceLetra[contador] == letraAPedir):
                                contador += 1
                                print (contador, end="")
                            else:
                                contador = contador
                        except IndexError:
                            print("No existe esa posición")
                    else:
                        print(" _ ", end="")
                except IndexError:
                    print("No existe esa posición")


juego = JuegoAhorcado()
juego.main()