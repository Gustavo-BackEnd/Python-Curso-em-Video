# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
print('Vamos ver se você advinha o número que eu vou escolher...')
sleep(2)
ne = int(input('Escolha um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if ne == escolhido:
    print(f'Parabéns o número escolhido foi {escolhido}.')
else:
    print(f'Errou, o número escolhido foi {escolhido}.')

