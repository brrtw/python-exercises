lista =[]
for i in range(5):
    num = int(input(f'informe o {i} numero : '))
    lista.append(num)
    
maior = max(lista)
menor = min(lista)

print(f'o maior numero foi {maior} e ficou na posicao: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(i)

print(f'o menor numero foi {menor} e ficou na posição: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(i)