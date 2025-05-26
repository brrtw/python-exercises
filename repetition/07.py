maiores=0
menores=0

for c in range(0,7):
    idade=int(input("Informe a idade da {} pessoa: ".format(c+1)))
    if idade >= 18:
        maiores+=1
    else:
        menores+=1
print('A quantidade de maiores de idade é: {}\nA quantidade de menores de idade é: {}'.format(maiores,menores))