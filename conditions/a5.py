n1 = float(input("informe o primeiro numero: "))
n2 = float(input("informe o segundo numero: "))
n3 = float(input("informe o terceiro numero: "))
if n1>n2 and n1>n3:
    print("{:.2f} e o maior numero".format(n1))
elif n2>n1 and n2>n3:
    print("{:.2f} e o maior numero".format(n2))
elif n3>n1 and n3>n2:
    print("{:.2f} e o maior numero".format(n3))