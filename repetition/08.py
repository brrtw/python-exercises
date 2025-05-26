maiorp=0
menorp=300

for c in range(0, 5):
    peso = int(input('informe o peso da {} pessoa: '.format(c+1)))
    if peso>maiorp:
        maiorp=peso
    elif menorp>peso:
        menorp=peso
print('menor peso digitado foi {}\nmaior peso digitado foi {}'.format(menorp,maiorp))