v = float(input("informe a distancia da viagem: "))
if v <= 200:
    print("valor da passagem {:.2f} reais".format(v*0.50))
elif v > 200:
    print("valor da passagem {:.2f} reais".format(v*0.45))