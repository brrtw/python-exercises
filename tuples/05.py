num = []

while True:
    n = int(input('digite um numero: '))
    
    if n not in num:
        num.append(n)
        print('numero adicionado com sucesso!')
    else:
        print('numero ja adicionado')
    
    continuar = input('deseja continuar ? S/N  ').strip().upper()
    if continuar != 'S':
        break

print(f'valores digitados foram {sorted(num)}')