#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# tratando como str
num = int(input('Digite um número maior que 1000 e menor que 9999: '))
n = str(num)# transformando número inteiro em string ou num = str(input
print(f'unidade {n[3]}')
print(f'dezena {n[2]}0')
print(f'centena {n[1]}00')
print(f'milhar {n[0]}000')

# tratando como número inteiro
num = int(input('Digite um número maior que 0 e menor que 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'unidade {u}')
print(f'dezena {d}')
print(f'centena {c}')
print(f'milhar {m}')

