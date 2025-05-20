from random import randint
itens =("Pedra" , "Papel" , "Tesoura")
comp =  randint(0,2)
print('''Opções
[0] Pedra 
[1] Papel
[2] Tesoura''')
jogador = int(input("qual é sua jogada? "))
print("computador jogou {}".format(itens[comp]))
print("jogador jogou {}".format(itens[jogador])) 