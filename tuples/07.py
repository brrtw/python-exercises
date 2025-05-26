numeros = []

while True:
    n = input('digite um numero: ')
    if n not in numeros:
        numeros.append(n)
    conti= input('deseja continuar ? [S/N]  ').strip().upper()
    if conti != 'S':
        break

print(f'quantidade de numeros digitados foi {len(numeros)}')
print(f'lista ordenada de forma decrescente{sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('5 esta presente na lista')
else:
    print('nao esta presente na lista')