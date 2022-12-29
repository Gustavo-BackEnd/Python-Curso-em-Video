# Faça um programa que calcule a área de uma parede e mostre quantos litros de tintas precisam para pinta-la
#obs 1L de tinta pinta 2m²

A = float(input('Qual a altura da parede? '))
L = float(input('Qual a largura da parede? '))
a = A * L
p = a / 2
print(f'Para pintar {a}m² você vai precisar de {p} litros de tinta')
