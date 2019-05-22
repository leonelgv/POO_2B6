"""
>>> EC = EstructurasControl()
>>> EC.EstructuraIf(78)
True
>>> EC.EstructuraIf(67)
False
>>> EC.EstructuraIf(120)
False
>>> EC.convertirOctalNumero(10153)
23651
"""
class EstructurasControl:

    def EstructuraIf(self, nota):
        if(nota >= 70 and nota <= 100):
            return True
        else:
            return False

    def EstructuraFor(self, numero):
        for a in range(1,11):
            print (numero, "x", a, " = ", numero*a)

    def convertirBinarioNumero(self, numero):
        if (numero < 256):
            res = 0
            div = numero
            resultado = 0
            acumulador = 1
            while True:
                res = div % 2
                div = int(div / 2)
                resultado = res * acumulador + resultado
                acumulador = acumulador * 10
                if (div == 0):
                    break
            return resultado
        else:
            return 0

    def convertirOctalNumero(self, numero):
        res = 0
        div = numero
        resultado = 0
        acumulador = 1
        while True:
            res = div % 8
            div = int(div / 8)
            resultado = res * acumulador + resultado
            acumulador = acumulador * 10
            if (div == 0):
                break
        return resultado

    def obtenerHexadecimalNumero(self, numero):
        div1 = numero
        resultado = ''
        numHexa = ''
        while True:
            # Se guarda el residuo de división
            res = div1 % 16
            div1 = int(div1 / 16)
            if res == 10:
                numHexa = 'A'
            elif res == 11:
                numHexa = 'B'
            elif res == 12:
                numHexa = 'C'
            elif res == 13:
                numHexa = 'D'
            elif res == 14:
                numHexa = 'E'
            elif res == 15:
                numHexa = 'F'
            else:
                numHexa = str(res)
            resultado = numHexa + resultado
            if (div1 == 0):
                break
        return resultado


if __name__ == '__main__':
    import doctest
    doctest.testmod()