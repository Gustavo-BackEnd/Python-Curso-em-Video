# Faça um programa que leia o nome completo e mostre o primeiro e o último separadamente.
nome = str(input('Digite seu nome completo: '))
PN = nome.split()
print(f'O primeiro nome é {PN[0]}')
print(f'O último nome é {PN[-1]}')
