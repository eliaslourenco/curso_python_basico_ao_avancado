#!/usr/local/bin/python3
from math import pi
import sys

def circulo(raio):
    resultado_circunferencia = pi * float(raio)**2
    return resultado_circunferencia

if __name__ == '__main__':
    # Para passar o argumento coloca ./nome_script 69 <- '69' é o valor do argumento 1 e o proprio script e o valor 0
    if len(sys.argv) < 2:
        print("É necessário informar o raio do círculo")
        print("Sintaxe: "+__file__[2:]+" <raio>")
        print("Sintaxe: {} <raio>".format(sys.argv[0]))

    else:
        raio = sys.argv[1]
        resultado = circulo(raio)
        print("Área do círculo: ", resultado)


