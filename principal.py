from Recibo import Recibo
from Circulo import Circulo
import math
from CadenaCaracteres import CadenaCaracteres

"""
reciboFernando = Recibo(10, 100, 10)
print('Fernando va a pagar de energía eléctrica la cantidad de ', reciboFernando.getTotalAPagar())

miCirculo = Circulo(45)
miCirculo.calcularPerimetro()
miCirculo.calcularArea()

print ('El área del circulo es: ', miCirculo.getArea())
print ('El perimetro del circulo es: ', miCirculo.getPerimetro())

miCirculo2 = Circulo(-434)
miCirculo2.calcularPerimetro()
miCirculo2.calcularArea()

print ('El área del circulo es: ', miCirculo2.getArea())
print ('El perimetro del circulo es: ', miCirculo2.getPerimetro())
"""

print (int(5/3))
print (5%3)

hora = 0
minuto = 59
segundo = 59

segundo = segundo + 1
if(segundo>59):
    segundo = segundo - 60
    minuto = minuto + 1
if(minuto>59):
    minuto = minuto - 60
    hora = hora + 1
if(hora >23):
    hora = hora - 24

print (hora, minuto, segundo)

dia = 30
mes = 12
anio = 2019

dia = dia + 1
if(dia>30):
    dia = dia - 30
    mes = mes + 1
if(mes>12):
    mes = mes - 12
    anio = anio + 1
print (dia, mes, anio)

bisiesto = anio % 4
if(bisiesto == 0):
    aniobisiesto = 1
else:
    aniobisiesto = 0

print(aniobisiesto)

letra = '0'
print(ord(letra))
if(letra == 'a' or letra == 'b' or letra == 'c' or letra == 'd' or letra == 'e'):
    tipoLetra = 'minuscula'
b = 3
for a in range(0,11):
    print (b, ' ^ ', a , ' = ', (pow(b,a)))


contador = CadenaCaracteres("Popocatepetl")
print (contador.getTotalCaracteres())