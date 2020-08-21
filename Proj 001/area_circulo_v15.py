#!/usr/local/bin/python3
from math import pi
import sys
import errno

#Desta maneira eu coloco as cores no global, porem quanto mais variaveis estiverem la, 
#maior a chance de sobreescrever alguma funcao global, sendo assim melhor usar uma classe:
#ERRO = '\033[91m'
#NORMAL = '\033[0m'
class CoresTerminal:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'

def circulo(raio):
    resultado_circunferencia = pi * float(raio)**2
    return resultado_circunferencia


def help():
    print(CoresTerminal.ERRO,"É necessário informar o raio do círculo",CoresTerminal.NORMAL)
    print(CoresTerminal.ERRO,"Sintaxe: {} <raio>".format(sys.argv[0]),CoresTerminal.NORMAL)
        

if __name__ == '__main__':
    # Para passar o argumento coloca ./nome_script 69 <- '69' é o valor do argumento 1 e o proprio script e o valor 0
    if len(sys.argv) < 2:
        help() 
        sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric() : #note que ao contrario das demias python nao usa ! e sim not
        help()
        print(CoresTerminal.ERRO+
              'O raio deve ser um valor númerico', CoresTerminal.NORMAL) # ERRO e a constante com a cor vermelha e NORMAL ele volta para  a padrao
        sys.exit(errno.EINVAL)
    else:
        raio = sys.argv[1]
        resultado = circulo(raio)
        print("Área do círculo: ", resultado)


