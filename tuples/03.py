lista = ('carro', 30000,
      'moto', 10000,
      'caminhao', 50000,
      'aviao', 99999)

print(f'{'LISTA DE PREÇOS':^40}')

for c in range (0, len(lista)):
    if c %2==0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R${lista[c]:>7.2f}')
