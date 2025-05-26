matriz = [[0,0,0], [0,0,0], [0,0,0]]
spares = sterceira = 0
maiorsegundal = 0

for linha in range(3):
    for coluna in range(3):
        num = int(input('Informe os valores: '))
        matriz[linha][coluna] = num
        
        if matriz[linha][coluna] % 2 == 0:
            spares += num
        if coluna == 2:
            sterceira += num
        if linha == 1:
            if coluna == 0:
                maiorsegundal = num
   
print('A matriz foi')             
for linha in range(3):
    for coluna in range(3):
        print(f'{matriz[linha][coluna]:^2}', end='')
    print()

print(f'A soma dos valores pares digitados foi: {spares}')
print(f'A soma dos valores da terceira coluna foi: {sterceira}')
print(f'O maior valor da segunda linha foi: {maiorsegundal}')