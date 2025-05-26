pessoas = []
mulheres = []
lista = []
cadastrados = 0
mediaidade = 0
midade = 0

while True:
    dados = {}
    while True:
        sex = input(f'Informe o sexo[M/F]: ').strip().upper()
        if sex in ['M', 'F']:
            break
        print('Erro no sistema, digite apenas M ou F')
            
    dados['sexo'] = sex
    dados['nome'] = input('informe o nome: ')
    dados['idade'] = int(input('informe a idade: '))
    
    cadastrados += 1
    midade += dados['idade']
    
    pessoas.append(dados.copy())
    
    if dados['sexo'] == 'F':
        mulheres.append(dados.copy())

    continuar = input(f'Deseja continuar ? S/N ').strip().upper()
    if continuar !='S':
        break

mediaidade = midade/cadastrados
    
for i in pessoas:
    if i['idade'] > mediaidade:
        lista.append(i)
    
print(f'A quantidade de pessoas cadastradas foram: {cadastrados}')
print(f'A media de idade dos cadastrados foi: {midade:.2f}')

print('\nLista de mulheres:')
for i in mulheres:
    print(f"- {i['nome']} ({i['idade']} anos)")

print('\nPessoas com idade acima da média:')
for i in lista:
    print(f"- {i['nome']} ({i['idade']} anos)")