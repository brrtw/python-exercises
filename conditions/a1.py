v=float(input("informe a velocidade do carro: "))
if v >= 80:
    multa = v*7
    print("voce foi multado!    ")
    print("multa no valor de {:.2f} reais".format(multa))
else:
    print("velocidade dentro do limite permitido")
    