# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 parta viagens mais longas.
distancia = float(input('Quantos Km tem de distância? '))

if distancia >= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45
print(f'Sua viagem vai custar R$:{preço}')
