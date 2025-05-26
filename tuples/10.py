num = [[], []]

for i in range (0,7):
    n = int(input(f'Informe o {i+1} valor: '))
    
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

print(f'Valores Pares : {sorted(num[0])}')
print(f'Valores Impares: {sorted(num[1])}')