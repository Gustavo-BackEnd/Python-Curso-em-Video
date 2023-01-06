# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print(f'Você excedeu o limite de 80km/h, sua multa é de R$ {(velocidade - 80) * 7 :.2f}')
else:
    print('Muito bem, você não ultrapassou o limite de velocidade.')
