import random

mega = []

qjogos = int(input('informe a quantidade de jogos que deseja fazer: '))

for i in range(qjogos):
    jogo = random.sample(range(1, 61), 6)
    mega.append(jogo)
    
print(f'a quantidade de jogos foi: {qjogos}')
    
for i in range(qjogos):
    print(sorted(mega[i]))