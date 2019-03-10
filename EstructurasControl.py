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

if __name__ == '__main__':
    import doctest
    doctest.testmod()