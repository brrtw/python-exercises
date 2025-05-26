jogador = {}
gols = 0

jogador['nome'] = input('Qual o nome do jogador? ')
partidas = int(input(f'quantas partidas {jogador["nome"]} jogou? '))

for i in range (partidas):
    g = int(input(f'Quantos gols o {jogador["nome"]} fez na {i+1} partida: '))
    gols += g
    
jogador['partidas'] = [partidas]
jogador['totalgols'] = [g]

print(f'{jogador["nome"]} em {partidas} partidas fez {gols} gols')