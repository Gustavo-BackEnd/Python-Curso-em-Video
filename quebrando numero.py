# 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua
# porção Inteira

# Jeito 1 importando a bíblioteca inteira
import math
num = float(input('Digite um número: '))
print(f'A parte inteira de {num} é: {math.trunc(num)}')

# Jeito 2 importando só uma função da biblioteca
from math import trunc
num1 = float(input('Digite um número: '))
print(f'A parte inteira de {num} é: {trunc(num)}')

# Jeito 3 com função interna do python
num = float(input('Digite um númeor: '))
print(f'A porção inteira do número{num} é {num:.0f}')

# Jeito 4 transformando para str
num = float(input('Digite um número: '))
print(f'A porção inteiro do número {num} é: {int(num)}')
