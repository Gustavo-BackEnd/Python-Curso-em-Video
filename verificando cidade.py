# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Digite uma cidade: ')).strip()
cid = cidade.upper()
print(f'A cidade {cidade} começa com "Santo"?:{"SANTO" in cid[:5]}')
