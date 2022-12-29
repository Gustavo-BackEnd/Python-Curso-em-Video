# Crie um programa que que leia quantos R$ tem na carteira e quanto US$ podemos comprar

r = float(input('Digite quanto R$ você possui: R$'))
d = float(input('Qual o valor do US$ atual? US$'))
q = r // d
print(f'Você possui R${r}, o dolar está valento {d}, consegue comprar US${q}')
