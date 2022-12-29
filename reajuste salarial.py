# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
si = float(input('Salário inicial R$:'))
sn = si + (si*15/100)
print(f'O salário de R${si:.2f} com 15% de aumento vai passar a ser {sn:.2f}')
