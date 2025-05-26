pessoas = []
temp = []
maispesadas = []
maisleves = []

while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))

    temp.append(nome)
    temp.append(peso)
    pessoas.append(temp[:])
    temp.clear()
    
    if len(pessoas) == 1:
        maispesadas = maisleves = peso
    else:
        if peso > maispesadas:
            maispesadas = peso
        if peso < maisleves:
            maisleves = peso
    
    cont = input('Deseja continuar ? [S/N] ').strip().upper()
    if cont != 'S':
        break
    
print(f'O total de pessoas cadastradas foi: {len(pessoas)}')

print(f'O maior peso cadastrado foi {maispesadas}Kg, peso de ', end='')
for i in pessoas:
    if i[1] == maispesadas:
        print(f'{i[0]}, ', end='')
        
print(f'O menor peso cadastrado foi {maisleves}Kg, peso de ', end='')
for i in pessoas:
    if i[1] == maisleves:
        print(f'{i[0]}, ', end='')