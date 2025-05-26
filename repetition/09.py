media=0
nome=str
menos20=0
maiori=0

for c in range(0, 4):
    nome2 = str(input('informe o nome da {} pessoa: '.format(c+1)))
    sexo = str(input('informe o sexo a {} pessoa [M] para masculino ou [F] para feminino: '.format(c+1)))
    idade = int(input('informe da idade da {} pessoa: '.format(c+1)))
    media += idade
    if sexo == 'm' or 'M':
        if idade>maiori:
            nome = nome2
    if sexo == 'f' or 'F':
        if idade<20:
            menos20+=1
print('a media de idade do grupo foi: {}\no nome do homem mais velho é: {}\nnumero de mulheres maiores de 20 anos foi: {}'.format(media/4,nome,menos20))