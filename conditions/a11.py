n=float(input("informe sua primeira nota: "))
n1=float(input("informe sua segunda nota "))
m=(n+n1)/2
if m > 7:
    print("aprovado!")
elif m < 5:
    print("reprovado!")
else:
    print("recuperação")