import random

n1 = (str(input("informe o nome do primeiro aluno: ")))
n2 = (str(input("informe o nome do segundo aluno: ")))
n3 = (str(input("informe o nome do terceiro aluno: ")))
n4 = (str(input("informe o nome do quarto aluno: ")))
sorteio = [n1, n2, n3, n4]
print("o sorteado foi {}".format(random.choices(sorteio, k=4)))