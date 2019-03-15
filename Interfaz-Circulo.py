# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from Circulo import *

class Programa:

    def __init__(self, window):
        # Inicializar
        self.window = window
        self.window.configure(bg = 'white')
        self.window.title('Circulo')

        # Agregar un contenedor (frame)

        frame = LabelFrame(self.window, text = 'Calcular área y perímetro')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20, padx = 20)

        # Input - Datos de entrada

        # Agregar una etiqueta (label)
        Label(frame, text = 'Radio: ').grid(row = 1, column = 0)

        # Agregar una caja de texto (textbox)
        self.radio = Entry(frame)
        self.radio.focus()
        self.radio.grid(row = 1, column = 1)

        # Output - Datos de salida

        # Agregar una etiqueta (Label)

        Label(frame, text = 'Área: ').grid(row = 2, column = 0)

        self.area = Label(frame, text = 'Área', fg = 'blue')
        self.area.grid(row = 2, column = 1)

        Label(frame, text='Perímetro: ').grid(row = 3, column = 0)

        self.perimetro = Label(frame, text = 'Perímetro', fg = 'red')
        self.perimetro.grid(row = 3, column = 1)

        # Agregar botones (Button)

        ttk.Button(frame, text = 'Calcular', command = self.calcular).grid(row = 4, column = 0)
        ttk.Button(frame, text = 'Salir', command = quit).grid(row = 4, column = 1)

    def validacion(self):
        return len(self.radio.get()) != 0

    def calcular(self):
        if self.validacion():
            try:
                radio = float(self.radio.get())
                circulo = Circulo(radio)
                self.area['text'] = circulo.getArea()
                self.perimetro['text'] = circulo.getPerimetro()
            except ValueError:
                self.area['text'] = 'El radio debe ser un número'
                self.perimetro['text'] = 'El radio debe ser un número'
        else:
            self.area['text'] = 'El radio está vacio'
            self.perimetro['text'] = 'El radio está vacio'
        return 0


def main():
    window = Tk()
    programa = Programa(window)
    window.mainloop()
    return 0

if __name__ == '__main__':
    main()