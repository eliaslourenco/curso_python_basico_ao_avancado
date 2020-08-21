#!/usr/local/bin/python3
from math import pi
import sys
import errno


def circulo(raio):
    resultado_circunferencia = pi * float(raio)**2
    return resultado_circunferencia


def help():
    print("É necessário informar o raio do círculo")
    print("Sintaxe: {} <raio>".format(sys.argv[0]))
        

if __name__ == '__main__':
    # Para passar o argumento coloca ./nome_script 69 <- '69' é o valor do argumento 1 e o proprio script e o valor 0
    if len(sys.argv) < 2:
        help() 
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric() : #note que ao contrario das demias python nao usa ! e sim not
        help()
        print('O raio deve ser um valor númerico')
        sys.exit(errno.EINVAL)
    else:
        raio = sys.argv[1]
        resultado = circulo(raio)
        print("Área do círculo: ", resultado)


