# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite seu nome: ')).strip()
nom = nome.upper()
print(f'O nome {nome} tem "Silva" no nome?:{"SILVA" in nom}')
