#Jeito 1 importando tudo
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
#arredondando                       ......I.........
print(f'A raiz quadrada de {num} é {math.ceil(raiz)} ')

#Jeito 2
from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz quadrada de {num} é {floor(raiz)}. ')
