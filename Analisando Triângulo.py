# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.
print('=-' * 20)
print('Analisando triângulo')
print('=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Conseguimos formar um triângulo com os segumentos {r1} {r2} {r3}')
else:
    print(f'Não conseguimos formar um triângulo com os seguimento {r1} {r2} {r3}.')

