# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotusa

# Maneira 1
from math import hypot
co = float(input('Comprimeto cateto oposto? '))
ca = float(input('Comprimento cateto adjacente? '))
hi = hypot(co, ca)
print(f'O comprimento da hipotenusa é: {hi:.2f}')

# Maneira 2
from math import sqrt
co = float(input('Comprimeto cateto oposto? '))
ca = float(input('Comprimento cateto adjacente? '))
hi = (co * 2) + (ca * 2)
print(f'O comprimento da hipotenusa é: {sqrt(hi):.2f}')

# Maneira 3
co = float(input('Comprimento do cateto oposto? '))
ca = float(input('Comprimento do cateto adjacente? '))
hi = ((co ** 2) + (ca ** 2)) ** (1/2)
print(f'O comprimento da hipotensa é: {hi:.2f}')


