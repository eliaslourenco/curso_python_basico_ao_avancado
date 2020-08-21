#!/usr/local/bin/python3
from math import pi

# print('nome do módulo', __name__)
# Se eu rodar este arquivo diretamente eu irei exibir o nome do modulo como o mais
#Ja caso eu importe vai passar a ser o proprio area_circulo_v5

def calculaAreaCirculo():
    raio = input('Informe o raio do Circulo:')
    resultado_circunferencia = pi * float(raio)**2
    print("Resultado: ", resultado_circunferencia)
    print('Foi um prazer, bye bye')
