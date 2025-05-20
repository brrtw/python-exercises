s = float(input("informe seu salario: "))
if s > 1250:
    s1 = (s*110)/100
    print("seu novo salario e: {:.2f}".format(s1))
elif s <= 1250:
    s2 = (s*115)/100
    print("seu novo salario e: {:.2f}".format (s2))
