idade=int(input("informe sua idade: "))
if idade == 18:
    print("hora de se alistar")
elif idade < 18:
    print("ainda vai se alistar, falta {:.2f} anos".format(18-idade))
elif idade > 18:
    print("passou o tempo de se alistar, voce esta atrasado em {:.2f} anos".format(idade-18))