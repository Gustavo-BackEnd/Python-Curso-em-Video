# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o primeiro nº: '))
b = int(input('Digite o segundo nº: '))
c = int(input('Digite o terceiro nº: '))
menor = a
maior = a
#verificando quem é o menor
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando quem é o maior
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior nº: {maior}')
print(f'E o menor nº: {menor}')

