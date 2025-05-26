print("tabuada")
print("[0] soma")
print("[1] subtracao")
print("[2] multiplicacao")
print("[3] divisao")

opcao = int(input("informe qual opcao deseja fazer: "))
n = int(input("infome o numero para a tabuada: "))

for c in range(0,10):
    if opcao == 0:
        print("{} + {} = {}".format(n,c,c+n))
    if opcao == 1:
        print("{} - {} = {}".format(n,c,c-n))
    if opcao == 2:
        print("{} x {} = {}".format(n,c,c*n))
    if opcao == 3:
        print("{} / {} = {}".format(n,c,c/n))