matriz = [[0,0,0], [0,0,0], [0,0,0]]

for i in range (0, 3):
   for j in range(0, 3):
       matriz[i][j] = int(input('digite um numero: '))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]:^2}', end='')
    print()