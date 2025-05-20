numero = int(input("Digite um número inteiro: "))

print("\nEscolha a base de conversão:")
print("[1] Binário")
print("[2] Octal")
print("[3] Hexadecimal")

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"O número {numero} em binário é {bin(numero)[2:]}")
elif opcao == 2:
    print(f"O número {numero} em octal é {oct(numero)[2:]}")
elif opcao == 3:
    print(f"O número {numero} em hexadecimal é {hex(numero)[2:].upper()}")
else:
    print("Opção inválida. Tente novamente.")
