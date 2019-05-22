from Circulo import Circulo

def main():
    radio = float(input("Escribe el radio: "))
    miRadio = Circulo(radio)
    print ("El área es igual a: ", miRadio.getArea())
    print ("El perimetro es igual a: ", miRadio.getPerimetro())

if __name__ == '__main__':
    main()