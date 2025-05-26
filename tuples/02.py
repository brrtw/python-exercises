pares = 0
numero = (int(input('informe o primeiro numero: ')),
          int(input('informe o segundo numero: ')),
          int(input('informe o terceiro numero: ')),
          int(input('informe o quarto numero: ')))

print(f'voce digitou os seguintes numeros {numero}')
print(f'o numero 9 apareceu {numero.count(9)} vezes')
print(f'o numero 3 esta na posicao {numero.index(3)}')
for c in range (0,4):
    if numero[c] %2==0:
        pares += 1
print(f'a quantidade de numeros pares foi: {pares}')