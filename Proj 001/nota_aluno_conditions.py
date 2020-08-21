#!/usr/local/bin/python3
import sys
import errno

def calculaNota(nota):
    if nota >= 9:
        print("Quadro de Honra")
    elif nota >= 7:
        print("Aprovado")
    elif nota >= 5 :
        print("Recuperacao")
    elif nota >= 3 :
        print("Recuperacao + trabalho")
    else:
        print("Reprovado!") 

if(len(sys.argv) > 1):
    nota = int(sys.argv[1])
    calculaNota(nota)
else:
    print("Sinto muito mas informe um parametro")
    sys.exit(errno.EPERM)

