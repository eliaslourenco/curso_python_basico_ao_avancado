#!/usr/local/bin/python3
from math import pi

def circulo(raio):
    resultado_circunferencia = pi * float(raio)**2
    print("Área do círculo: ", resultado_circunferencia)

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)


