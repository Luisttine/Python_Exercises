#LISTA 2
#Atividade 1

la = float(input("Digite o lado A: ")) 
lb = float(input("Digite o lado B: ")) 
lc = float(input("Digite o lado C: ")) 

if la+lb>lc and la+lc>lb and lc+lb>la: 
  print("Seu triângulo realmente existe!!") 
  if la==lb==lc: 
    print("Seu triângulo é Equilátero.") 
elif la==lb or la==lc or lb==lc : 
  print("Seu triângulo é Isósceles.") 
elif la!=lb and la!=lc and lb!=lc: 
  print("Seu triângulo realmente existe!!")
  print("Seu triângulo é Escaleno.")

else:
  print("Isso não é um triângulo!!")

#Atividade 2

import calendar
ano = int(input("Digite o ano que deseja: "))

if calendar.isleap(ano) == True:
  print("O ano digitado é bissexto!")
else:
  print("O ano digitado não é bissexto!")

#Atividade 3

peso = int(input("Digite os kg resultantes da pesca: "))
multa = 4.00

if peso > 50:
  excesso = peso - 50
  multa = excesso * multa
  print(f"Você recebeu uma multa por excesso de peso de $ {multa}")
else:
  print("Multa 0 \nExcesso 0")

#Atividade 4

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
  print(f"O maior dos três números é {n1}")
if n2 > n1 and n2 > n3:
  print(f"O maior dos três números é {n2}")
if n3 > n1 and n3 > n2:
  print(f"O maior dos três números é {n3}")

#Atividade 5

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
  print(f"O maior dos três números é {n1}")
elif n2 > n1 and n2 > n3:
  print(f"O maior dos três números é {n2}")
elif n3 > n1 and n3 > n2:
  print(f"O maior dos três números é {n3}")

elif n1 < n2 and n1 < n3:
  print(f"O menor dos três números é {n1}")
elif n2 < n1 and n2 < n3:
  print(f"O menor dos três números é {n2}")
elif n3 < n1 and n3 < n2:
  print(f"O menor dos três números é {n3}")

#Atividade 6

h = float(input("Quanto você ganha por hora? R$"))
hmes = int(input("Quantas horas por mês você trabalha? "))

slBruto = h * hmes
IR = slBruto * 0.11
INSS = slBruto * 0.08
Sindicato = slBruto * 0.05
slLiquido = slBruto - IR - INSS - Sindicato

print(f"Seu salário bruto é R${slBruto:.2f}")
print(f"O tanto pago de IR é R${IR:.2f}")
print(f"O tanto pago de INSS é R${INSS:2f}")
print(f"O tanto pago para o Sindicato é R${Sindicato:.2f}")
print(f"Seu salário líquido é R${slLiquido:.2f}")

#Atividade 7

local = int(input("Informe os m² a ser pintado: "))
latas = 0 

if (local % 54) <= 1 or (local % 54) >= 54:
  latas = int(latas +1)
else:
  latas = local / 18
  if (local % 54) <= 1 or (local % 54) >= 54:
    latas = int(latas +1)

preço = latas * 80.00

print(f"Você precisará de {latas:.0f} latas e gastará R${preço:.2f}")



