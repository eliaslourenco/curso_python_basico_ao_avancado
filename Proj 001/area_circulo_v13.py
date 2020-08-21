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
        # Retorna o codigo de erro e para execucao
        # onde o 0 e sucesso e qualquer outro representa um erro
        # temos a biblioteca errno tem varias constantes de erros por exemplo o EPERM e igual a 1
        sys.exit(errno.EPERM)    

    raio = sys.argv[1]
    resultado = circulo(raio)
    print("Área do círculo: ", resultado)


