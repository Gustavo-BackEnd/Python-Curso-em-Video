# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase qualquer:')).upper().strip()
print(f'A letra A aparece {frase.count("A")}x.')
print(f'A primeira vez que a letra A aparece é {frase.find("A")}')
print(f'A ultima vez que a letra A aparece é {frase.rfind("A")}')
