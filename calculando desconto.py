# Faça um programa que leia o preço de um produtoe mostre seu novo preço com 5% de desconto

p1 = float(input('Qual o valor do produto: '))
d = (p1 * 5) / 100
t = p1 - d
print(f'O produto custa {p1:.2f} e passa a custar {t:.2f} com 5% de desconto.')
