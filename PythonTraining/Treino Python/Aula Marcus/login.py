idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("criança")
elif idade <= 18:
    print("adolescente")
elif idade <= 6:
    print("adulto")
else:
    print("idoso")