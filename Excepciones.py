"""
>>> op = Operaciones()
>>>
>>> op.dividirNumeros(1,0)
'No se puede dividir'
>>> op.dividirNumeros(4,2)
2.0
"""
class Operaciones:

    def dividirNumeros(self, operador1, operador2):
        try:
            a = operador1 / operador2
            return a
        except ZeroDivisionError:
            return 'No se puede dividir'


if __name__ == '__main__':
    import doctest
    doctest.testmod()