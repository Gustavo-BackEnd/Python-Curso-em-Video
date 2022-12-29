# Fazer uma some de número inteiro, que mostre seu sucessor e seu antecessor

n1 = int(input('Digite um número: '))
n2 = int(input('+ '))
r = n1 + n2
print(f'A soma de {n1}+{n2} deu um total de {r}, seu sucessor é {r+1} e seu antecessor é {r-1}.')
