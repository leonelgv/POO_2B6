from Recibo import Recibo
from Circulo import Circulo

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
