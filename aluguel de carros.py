# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias ficou com o carro? '))
k = float(input('Quantos Km andou? '))
t = (d * 60) + (k * 0.15)
print(f'Ficou com o carro {d} dias, andou {k}km, total de R${t:.2f}')
