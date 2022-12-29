# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em ºC:'))
f = ((9 * c) / 5) + 32
print(f'A temperatura de {c:.2f}ºC corresponde {f:.2f}ºF')
