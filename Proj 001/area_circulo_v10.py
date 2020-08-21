#!/usr/local/bin/python3
from math import pi
import sys

def circulo(raio):
    resultado_circunferencia = pi * float(raio)**2
    return resultado_circunferencia

if __name__ == '__main__':
    # Para passar o argumento coloca ./nome_script 69 <- '69' é o valor
    raio = sys.argv[1]
    resultado = circulo(raio)
    print("Área do círculo: ", resultado)

