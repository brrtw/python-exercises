temp = []
alunos = []

while True:
    aluno = input('infome o nome do aluno: ')
    n1 = float(input('informe sua primeira nota: '))
    n2 = float(input('informe sua segunda nota: '))
    
    temp.append(aluno)
    temp.append(n1)
    temp.append(n2)
    alunos.append(temp[:])
    
    continuar = input('deseja adicionar mais alunos ? [S/N] ').strip().upper()
    if continuar != 'S':
        break
    
for i in range(len(alunos)):
    nome = alunos[i][0]
    media = (alunos[i][1] + alunos[i][2]) / 2
    print(f'Aluno: {nome:} Media: {media}')
    