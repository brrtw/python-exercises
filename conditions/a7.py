salary = float(input("informe seu salario: "))
home = float(input("informe o valor da casa: "))
years = int(input("informe a quantidade de anos em que deseja pagar a casa: "))
months= years*12
prest1 = home/months
limit = salary*0.30
prest2 = float(input("informe o valor da prestacao que deseja pagar: "))
if prest1 <= limit:
    print("emprestimo aprovado!")
else:
    print("emprestimo negado!")
