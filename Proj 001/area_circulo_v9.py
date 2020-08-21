#!/usr/local/bin/python3
from math import pi

def circulo(raio):
    resultado_circunferencia = pi * float(raio)**2
    return resultado_circunferencia

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    resultado = circulo(raio)
    print("Área do círculo: ", resultado)

