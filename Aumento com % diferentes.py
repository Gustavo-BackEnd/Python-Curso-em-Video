# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Qual o salário atual do trabalhador?'))
if sal > 1250:
    salario = (sal * 10 / 100) + sal
    print(f'O salário de {sal} terá um aumento de 10%, passando a ser {salario}')
else:
    salario = (sal * 15 / 100) + sal
    print(f'O salário de {sal} terá um aumento de 15%, passando a ser {salario}')

