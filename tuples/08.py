list = []
pares = []
impares = []

#recebe os numeros
while True:
    n = int(input('digite um numero: '))
    if n not in list:
        list.append(n)
    continuar = str(input('deseja continuar ? S/N  ').strip().upper())
    if continuar != 'S':
        break

#verifica se os numeros sao pares ou impares e realocam eles em outra lista de forma ordenada
for i in list:
    if i % 2 ==0:
        pares.append(i)
    else:
        impares.append(i)
        
print(f'Numeros digitados {list}')
print(f'Numeros pares digitados {sorted(pares)}')
print(f'Numeros impares digitados {sorted(impares)}')