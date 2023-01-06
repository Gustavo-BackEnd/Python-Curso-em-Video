# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome: ')).strip() #<---Elimina espaços no começo e no fim'''
print('Analisando seu nome...')
print(f'Seu nome em maiúscula: {nome.upper()}')
print(f'Seu nome em minúscula: {nome.lower()}')
print(f'Seu nome tem um total de {len(nome) - nome.count(" ")} letras') #Tive que por " pra selecionar o espaço
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
nome_separado = nome.split()
print(f'Seu primeiro nome tem {len(nome_separado[0])} letras')
