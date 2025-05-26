from random import randint

dados = {'Jogador 1': randint(1,6),
         'Jogador 2': randint(1,6),
         'Jogador 3': randint(1,6),
         'Jogador 4': randint(1,6)}

for jogador, valor in dados.items():
    print(f'{jogador} tirou {valor} no dado')
    
vencedor = ''
maiorv = 0

for jogador, valor in dados.items():
    if valor>maiorv:
        maiorv = valor
        vencedor = jogador
      
print(f'O vencedor foi o {vencedor}!')    